from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
        
# Specify the url1 of the website
url1 = "https://aviationweather.gov/data/taf/?id=RPLL,RPVM,RPLC,RPLB,RPLI,RPVP,RPVD,RPMR,RPMD,RPMZ"

# Set up Selenium WebDriver with headless option (assuming Chrome)
options1 = Options()
options1.add_argument("--headless")  # Add this line to run Chrome in headless mode
driver1 = webdriver.Chrome(options=options1)

try:
    # Open the website
    driver1.get(url1)
    
    # Wait for the content to load (you may need to adjust the wait time)
    driver1.implicitly_wait(10)

    # Find the element containing the content
    content_element1 = driver1.find_element(By.ID, "data-container")
    
    # Extract the text content
    content1 = content_element1.text
    
    # Modify content to include "=" at the end of each complete TAF report
    taf_reports1 = content1.split('TAF ')[1:]  # Split content by "TAF" and skip the first element (empty)
    modified_content1 = ''
    for taf_report1 in taf_reports1:
        modified_content1 += 'TAF ' + taf_report1.strip() + '= '   

finally:
    # Close the browser
    driver1.quit()

def merge_taf(modified_content1):
    single_line_taf1 = ''
    for line1 in modified_content1.split('\n'):
        line1 = line1.strip()
        if line1:
            single_line_taf1 += line1 + ' '
    return single_line_taf1.strip()

single_line_taf1 = merge_taf(modified_content1)

url2 = 'https://www.pagasa.dost.gov.ph/aviation'

# Set up Selenium WebDriver with headless option (assuming Chrome)
options2 = Options()
options2.add_argument("--headless")  # Add this line to run Chrome in headless mode
driver2 = webdriver.Chrome(options=options2)

try:
    # Open the website
    driver2.get(url2)
    
    # Wait for the content to load (you may need to adjust the wait time)
    driver2.implicitly_wait(20)

    # Find the element containing the content
    content_element2 = driver2.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div[2]/div[4]/div[2]/div[2]/table[1]")
    
    # Extract the text content
    content2 = content_element2.text

finally:
    # Close the browser
    driver2.quit()

def merge_taf(content2):
    single_line_taf2 = ''
    for line2 in content2.split('\n'):
        line2 = line2.strip()
        if line2:
            single_line_taf2 += line2 + ' '
    return single_line_taf2.strip()

single_line_taf2 = merge_taf(content2)

def split_taf(content):
    return content.split('TAF ')[1:]

# Split TAF content into individual reports
awc_reports = split_taf(single_line_taf1)
pagasa_reports = split_taf(single_line_taf2)

if len(pagasa_reports) > 10:
    pagasa_reports = pagasa_reports[:10]

awc_reports[-1] += ' '

# Remove 'COR' prefix from each string
awc_reports = [report.replace('COR ', '') for report in awc_reports]

# print(awc_reports)
# print(pagasa_reports)

# Define function to maintain order while finding unique items
def find_unique_with_order(awc_reports, pagasa_reports):
    unique_list = []
    seen = set()
    for item in awc_reports:
        if item not in seen:
            seen.add(item)
            if item not in pagasa_reports:
                unique_list.append(item)
    return unique_list

# Find unique items in AWC reports
unique_awc_reports = find_unique_with_order(awc_reports, pagasa_reports)
# Find unique items in PAGASA reports
unique_pagasa_reports = find_unique_with_order(pagasa_reports, awc_reports)

# Compare TAF reports and identify differences
diffs = []
for awc_report, pagasa_report in zip(unique_awc_reports, unique_pagasa_reports):
    if awc_report != pagasa_report:
        # Splitting reports into words for comparison
        awc_words = awc_report.split()
        pagasa_words = pagasa_report.split()

        # Finding differing parts and wrapping them in HTML tags
        highlighted_awc = ' '.join(['<span class="highlight">' + word + '</span>' if word not in pagasa_words else word for word in awc_words])
        highlighted_pagasa = ' '.join(['<span class="highlight">' + word + '</span>' if word not in awc_words else word for word in pagasa_words])

        diffs.append(f"AWC   :{highlighted_awc}\nPAGASA:{highlighted_pagasa}\n\n")

# Define the file path where you want to save the differences
file_path = "/var/www/html/AEROFAST/TAF_Analyst/output.txt"

if not diffs:
    with open(file_path, "w") as file:
        file.write('<p style="font-size: 18px; font-weight: bold;">NO ERRORS FOUND</p>')

else:
    # Write the differences to the text file
    with open(file_path, "w") as file:
        for diff in diffs:
            file.write(diff)

print(f"Differences saved to {file_path}")
#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium


# In[19]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import pandas as pd

# Set up Edge WebDriver
edge_options = Options()
service = Service(service = Service("C:\\Users\\Shakthi\\Downloads\\edgedriver_win32"))
  # Replace with the path to your Edge WebDriver
driver = webdriver.Edge(service=service, options=edge_options)

# Function to scrape a WebMD page
def scrape_webmd(url):
    driver.get(url)
    
    # Allow some time for the page to load
    driver.implicitly_wait(5)
    
    # Extract title
    try:
        title = driver.find_element(By.TAG_NAME, 'h1').text
    except:
        title = "No Title"
    
    # Extract main content
    try:
        paragraphs = driver.find_elements(By.TAG_NAME, 'p')
        content = " ".join([p.text for p in paragraphs])
    except:
        content = "No Content"
    
    return {"Title": title, "Content": content}

# List of WebMD URLs to scrape
url_list = [
    
    'https://www.medicinenet.com/muscle_cramps/article.htm#what_are_muscle_cramps,Introduction'
'https://www.medicinenet.com/muscle_cramps/article.htm#what_are_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#what_are_the_types_of_muscle_cramps_what_causes_cramps,Types/Causes',
'https://www.medicinenet.com/muscle_cramps/article.htm#what_are_the_types_of_muscle_cramps_what_causes_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#do_all_muscle_cramps_fit_into_the_above_categories,Other Cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#do_all_muscle_cramps_fit_into_the_above_categories',
'https://www.medicinenet.com/muscle_cramps/article.htm#can_medications_cause_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#can_medications_cause_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#can_vitamin_deficiencies_cause_muscle_cramps,Vitamin Deficiencies',
'https://www.medicinenet.com/muscle_cramps/article.htm#can_vitamin_deficiencies_cause_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#can_poor_circulation_cause_muscle_cramps,Poor Circulation',
'https://www.medicinenet.com/muscle_cramps/article.htm#can_poor_circulation_cause_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#what_are_the_symptoms_of_common_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#what_are_the_symptoms_of_common_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#what_types_of_doctors_treat_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#what_types_of_doctors_treat_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#how_are_muscle_cramps_diagnosed',
'https://www.medicinenet.com/muscle_cramps/article.htm#how_are_muscle_cramps_diagnosed',
'https://www.medicinenet.com/muscle_cramps/article.htm#what_are_the_treatments_and_home_remedies_for_skeletal_muscle_cramps,Treatment/Home Remedies',
'https://www.medicinenet.com/muscle_cramps/article.htm#what_are_the_treatments_and_home_remedies_for_skeletal_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#medical_treatment_for_muscle_cramps,Medical Treatment',
'https://www.medicinenet.com/muscle_cramps/article.htm#medical_treatment_for_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#is_it_possible_to_prevent_muscle_cramps_during_the_activity,Prevention',
'https://www.medicinenet.com/muscle_cramps/article.htm#is_it_possible_to_prevent_muscle_cramps_during_the_activity',
'https://www.medicinenet.com/muscle_cramps/article.htm#how_much_should_i_drink_to_prevent_muscle_cramps,Hydration',
'https://www.medicinenet.com/muscle_cramps/article.htm#how_much_should_i_drink_to_prevent_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#is_it_possible_to_prevent_muscle_cramps_during_pregnancy,Prevention During Pregnancy',
'https://www.medicinenet.com/muscle_cramps/article.htm#is_it_possible_to_prevent_muscle_cramps_during_pregnancy',
'https://www.medicinenet.com/muscle_cramps/article.htm#what_is_the_prognosis_of_recurrent_muscle_cramps,Prognosis',
'https://www.medicinenet.com/muscle_cramps/article.htm#what_is_the_prognosis_of_recurrent_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#is_it_possible_to_prevent_rest_cramps,Prevention Rest Cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#is_it_possible_to_prevent_rest_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#how_can_older_adults_prevent_muscle_cramps,Adult Prevention',
'https://www.medicinenet.com/muscle_cramps/article.htm#how_can_older_adults_prevent_muscle_cramps',
'https://www.medicinenet.com/muscle_cramps/article.htm#are_there_medications_to_prevent_muscle_cramps,Medication Prevention',
'https://www.medicinenet.com/muscle_cramps/article.htm#are_there_medications_to_prevent_muscle_cramps',
]

# Scrape data from all URLs
scraped_data = []
for url in url_list:
    data = scrape_webmd(url)
    scraped_data.append(data)

# Close the browser
driver.quit()

# Save the scraped data to a CSV file
df = pd.DataFrame(scraped_data)
df.to_csv("webmd_scraped_data5.csv", index=False)
print("Data saved to webmd_scraped_data5.csv")


# In[17]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import pandas as pd

# Set up Edge WebDriver
edge_options = Options()
  # Run in headless mode (no browser UI)
service = Service(service = Service("C:\\Users\\Shakthi\\Downloads\\edgedriver_win32"))
  # Replace with the path to your Edge WebDriver
driver = webdriver.Edge(service=service, options=edge_options)

# Function to scrape all links from a webpage
def scrape_links(url):
    driver.get(url)
    
    # Allow time for the page to load
    driver.implicitly_wait(5)
    
    # Find all anchor tags with 'href' attributes
    links = driver.find_elements(By.TAG_NAME, 'a')
    
    # Extract the href (link) and text for each anchor
    link_list = []
    for link in links:
        href = link.get_attribute('href')
        text = link.text
        if href:  # Only store non-empty links
            link_list.append({"Link": href, "Text": text})
    
    return link_list

# Scrape all links from a given webpage (for example, WebMD or Mayo Clinic)
url = 'https://www.medicinenet.com/muscle_cramps/article.htm'
all_links = scrape_links(url)

# Close the browser
driver.quit()

# Save the links to a CSV file
df = pd.DataFrame(all_links)
df.to_csv("scraped_links.csv", index=False)
print("Links saved to scraped_links.csv")


# In[ ]:





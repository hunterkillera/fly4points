from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



option = webdriver.EdgeOptions()
option.add_experimental_option('detach', True)
browser = webdriver.Edge(options=option)
browser.get('https://www.miles-and-more.com/row/en/program/status-benefits/new-statusprogramme/status-achievement.html')

# Find and click the cookie consent button using its class

cookie_button = browser.find_element(By.CLASS_NAME, "cookieconsent__buttonAcceptAll")
cookie_button.click()

#switch to iframe
iframe = browser.find_element(By.XPATH, "/html/body/main/article/div[3]/div[7]/section/div/iframe")
browser.switch_to.frame(iframe)
#click the button
link = browser.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/p/button")
link.click()


#read result.csv
import pandas as pd
df = pd.read_csv('niger.csv')
#create a dataframe to store the target
target_df = pd.DataFrame(columns=['target'])

#departure input is the first column 
depart_country = df.iloc[:,0]
#arrival input is the second column 
arrival_country = df.iloc[:,1]

depart_countries = []
arrival_countries = []
for i in depart_country:
    depart_countries.append(i)

for i in arrival_country:
    arrival_countries.append(i)

#loop through every departure and arrival country
for departc, arrivalc in zip(depart_countries, arrival_countries):
    #departure input
    depart = browser.find_element(By.ID, 'origin')
    browser.execute_script(
        "arguments[0].value = arguments[1];arguments[0].dispatchEvent(new Event('change'));",
        depart,
        departc,
    )

    suggestion_element = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'autocomplete-suggestions'))
)
    suggestion_element.click()


    #arrival input
    arrival = browser.find_element(By.ID, 'destination')
    browser.execute_script(
        "arguments[0].value = arguments[1];arguments[0].dispatchEvent(new Event('change'));",
        arrival,
        arrivalc,
    )
    #click the search button
    search = browser.find_element(By.ID, 'flighttype')
    search.click()
    #print target  
    target = browser.find_element(By.ID, 'flighttype')
    #store target.txt in a dataframe
    #add target.txt to target_df
    target_df = target_df.append({'target': target.text}, ignore_index=True)


    #clean the input box
    depart.clear()
    arrival.clear()

#store target_df in a csv file
target_df.to_csv('target.csv', index=False)
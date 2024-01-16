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


element = browser.find_element(By.ID, 'origin')
browser.execute_script("arguments[0].scrollIntoView();", element)
print("Is visible:", element.is_displayed())
print("Is enabled:", element.is_enabled())



#################################################################################################################################

#departure input
depart = browser.find_element(By.ID, 'origin')
depart_country = 'china'
browser.execute_script(
    "arguments[0].value = arguments[1];arguments[0].dispatchEvent(new Event('change'));",
    depart,
    depart_country,
)

print("Is visible:", depart.is_displayed())
print("Is enabled:", depart.is_enabled())

#arrival input
arrival = browser.find_element(By.ID, 'destination')
destination_country = 'germany'
browser.execute_script(
    "arguments[0].value = arguments[1];arguments[0].dispatchEvent(new Event('change'));",
    arrival,
    destination_country,
)
# #click both depart and arrival use execute_script  
# depart.click()

# click the search button
search = browser.find_element(By.ID, 'flighttype')
search.click()

# print target  
target = browser.find_element(By.ID, 'flighttype')
print(target.text)


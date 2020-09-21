# Import the Selenium Module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Import for Path module
from pathlib import Path
#import urllib3

#Import Base module for the code
import os
import datetime
import time

# Check Path
path = os.getcwd()
path_capture = "C:\/"
# Date
ddt = str(datetime.datetime.now().strftime("%d-%m-%y"))
# Site
site = "<Replace with your F5 Hostname>"
folder = path+"<Replace with your directory>"+site+"--"+ddt+"\/"

check_folder = Path(folder).mkdir(parents=True, exist_ok=True)
#print (check_folder)
# Import WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-notifications')
#options.add_argument('--headless')
options.add_experimental_option("prefs", {
"download.default_directory": "C:\/tmp\/",
"download.prompt_for_download": False,
"download.directory_upgrade": True,
"safebrowsing_for_trusted_sources_enabled": False,
"safebrowsing.enabled": False
})
driver = webdriver.Chrome(chrome_options=options, executable_path=<Replace with path to your chrome driver>+"/driver\/chromedriver.exe")
#enable_download_headless(driver, "C:\/tmp\/")
wait = WebDriverWait(driver, 60)


# Maximize Browser Window
driver.maximize_window()

# Begin to Access Web
driver.get("https://<Replace with your F5 IP>")

# Login & entering credential
driver.implicitly_wait(180)
user = driver.find_element_by_id("username")
user.click()
user.send_keys("<Replace with your F5 username>")
password = driver.find_element_by_id("passwd")
password.click()
password.send_keys("<Replace with your F5 password>")
login = driver.find_element_by_xpath("//*[@id='loginform']/button")
login.click()

driver.implicitly_wait(180)

# Check Http Analytic Menu, this will access HTTP Analytic Menu
analytic_menu = driver.find_element_by_xpath("//*[@id='mainmenu-statistics-appanalytics']/a")
analytic_menu.click()
analytic_sub_menu = driver.find_element_by_xpath("//*[@id='mainmenu-statistics-appanalytics-analyticshttp']/a")
analytic_sub_menu.click()
analytics = driver.find_element_by_xpath("//*[@id='mainmenu-statistics-appanalytics-analyticshttp-analytics-http-custom-page']/a")
analytics.click()
analytics.is_selected()



# Handle iFrame Tag, This will find the iFrame Tag that used by F5 Web GUI
driver.implicitly_wait(180)
wait.until(EC.visibility_of_element_located((By.NAME, "contentframe")))
driver.switch_to.frame(driver.find_element_by_name("contentframe"))
driver.implicitly_wait(250)

# Find Top Country Table, This will find the Top Country Dashboard and access the table data
# <Replace with Widget ID> need to be replace with the appropriate Widget ID from the HTML of F5 HTML Web Component, since it is randomnize and could be different each platform and OS
driver.find_element_by_xpath("//*[@id='widget_area_id_<Replace with Widget ID>']")
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='widget_area_id_<Replace with Widget ID>']")))
tc_submenu = driver.find_element_by_xpath("//*[@id='span_timediv_<Replace with Widget ID>']")
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='span_timediv_<Replace with Widget ID>']")))
tc_submenu.click()
# This will access 1 Month of Data on the dashboard
tc_1m = driver.find_element_by_xpath("//*[@id='span_timediv_<Replace with Widget ID>']/div/div[4]")
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='span_timediv_<Replace with Widget ID>']/div/div[4]")))
tc_1m.click()
driver.implicitly_wait(250)
time.sleep(5)

# Save Table to PNG, for the Top Country Table
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='widget_area_id_<Replace with Widget ID>']")))
top_country = driver.find_element_by_xpath("//*[@id='widget_area_id_<Replace with Widget ID>']").screenshot(folder+site+"-top_country-"+ddt+".png")
driver.implicitly_wait(250)
time.sleep(5)

# Back to default Frame, so that script can access back to the menu
driver.switch_to.default_content()
driver.implicitly_wait(30)
time.sleep(5)

# Nothing to do here, the script has complete it is jobs :)
print("Test Done!")
driver.close()

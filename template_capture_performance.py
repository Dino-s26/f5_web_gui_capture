# Import Selenium Module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import Path
from pathlib import Path

# Import Base Module for Code
import os
import datetime

# Check Path 
path = os.getcwd()
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

# If You need to utilize in background capture, you can uncomment this line. This will help to run the script in background without any interruption.
#options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=options, executable_path=<Replace with path to your chrome driver>+"\driver\chromedriver.exe")
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

# Check Device Health, Accessing Performance Menu 
performance_menu = driver.find_element_by_xpath("//*[@id='mainmenu-statistics-performance']/a")
performance_menu.click()
performances = driver.find_element_by_xpath("//*[@id='mainmenu-statistics-performance-General']/a")
performances.click()
performances.is_selected()


# Handle iFrame Tag
driver.implicitly_wait(90)
driver.switch_to.frame(driver.find_element_by_name("contentframe"))

# This handle when to select the Data we want to generate, for this code we want to get data for Last 7 Days
driver.implicitly_wait(90)
graph_interval = driver.find_elements_by_xpath("//tr[@id='graph_interval_row']//select[@name='int_select']/option[@value='2']")
for option in graph_interval:
    option.click()
    wait.until(EC.staleness_of(option))

# This capture Memory Usage
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-of-type(2)  img")))
memory = driver.find_element_by_css_selector("tr:nth-of-type(2)  img").screenshot(folder+site+"-memory-"+ddt+".png")

# This capture CPU Usage
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-of-type(4)  img")))
cpu = driver.find_element_by_css_selector("tr:nth-of-type(4)  img").screenshot(folder+site+"-cpu-"+ddt+".png")


# This capture Active Connection
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-of-type(6)  img")))
active_c = driver.find_element_by_css_selector("tr:nth-of-type(6)  img").screenshot(folder+site+"-active_connection-"+ddt+".png")


# This capture Total Connection
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-of-type(8)  img")))
tota_c = driver.find_element_by_css_selector("tr:nth-of-type(8)  img").screenshot(folder+site+"-total_connection-"+ddt+".png")

# This capture Throughput (Bits)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-of-type(10)  img")))
throughput_b = driver.find_element_by_css_selector("tr:nth-of-type(10)  img").screenshot(folder+site+"-throughput_bit-"+ddt+".png")

# This capture HTTP Requests
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-of-type(18)  img")))
http_r = driver.find_element_by_css_selector("tr:nth-of-type(18)  img").screenshot(folder+site+"-http_request-"+ddt+".png")

# This capture SSL TPS
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-of-type(22)  img")))
ssl = driver.find_element_by_css_selector("tr:nth-of-type(22)  img").screenshot(folder+site+"-ssl-"+ddt+".png")


# Nothing to do here, the script has complete it is jobs :)
print("DONE!")
driver.close()

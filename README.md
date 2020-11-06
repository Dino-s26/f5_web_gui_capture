# F5 Web GUI Capture using Selenium
Readme for source code F5 Web GUI Capture tool. Source code free to use in any project, kindly not use it for any illegal purpose and tag this project in your documentation or license file for source code reference.

** Requirement **
1. Python 3.6.4 or later
2. Selenium 3.141.0 or later (this is python module, you can add it with pip install selenium==3.141.0 or pip3 install selenium==3.141.0)
3. Selenium Chrome Web Driver (Can be downloaded from here https://chromedriver.chromium.org/), refer to your chrome version if you using chrome, if you using mozilla refer to (https://github.com/mozilla/geckodriver/releases) and it is documentation.
4. Chrome Browser or Mozilla Browser, in this case I'm using Chrome Version 85.0.4183.102 (Official Build) (64-bit) for this script.
5. Basic knowledge with HTML code structure, this will help to get element and troubleshooting your code.
6. (Optional) Install Ranorex Selocity Plugin in Chrome, this will help to get web element easily without problem.

** Install Requirement Module **
pip install pyinstaller
pip install pathlib2
pip install selenium

** Code Explanation **

1. Import required module for the script :
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import os
import datetime
```
2. Import webdriver function :
```
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--headless') # Headless if you need to run the script on background, if no need to run on background you can comment or remove it
driver = webdriver.Chrome(chrome_options=options, executable_path=path+"\driver\chromedriver.exe")
wait = WebDriverWait(driver, 60)
driver.maximize_window()
```

3. Define access to the Web GUI IP of F5
```
driver.get("https://<Your F5 IP>")
```

4. Define function to login the Web GUI of F5
```
driver.implicitly_wait(180)
user = driver.find_element_by_id("username")
user.click()
user.send_keys("your username")
password = driver.find_element_by_id("passwd")
password.click()
password.send_keys("your password")
login = driver.find_element_by_xpath("//*[@id='loginform']/button")
login.click()
driver.implicitly_wait(180)
```

5. Since the F5 Web GUI have iFrame tag (<iframe></iframe>), ensure that when you want to access / interact with the component inside of this tag, you need to switch to the tag in order the interaction can be happen. There are 2 method to do this as follows
```
5.1. Switch to the frame directly 
driver.implicitly_wait(90)
driver.switch_to.frame(driver.find_element_by_name("contentframe"))

5.2. Find the element of the "contentframe" and wait until the tag is visible, then back to the default frame
driver.implicitly_wait(180)
wait.until(EC.visibility_of_element_located((By.NAME, "contentframe")))
driver.switch_to.frame(driver.find_element_by_name("contentframe"))
driver.implicitly_wait(250)

driver.switch_to.default_content()
driver.implicitly_wait(30)
time.sleep(5)

both of the method are working, you just need to know what scenario when you use it. 
```

6. If you need to interact with dropdown menu, I recommend to do for loop and wait until the state are detected or selected using this line 
```
wait.until(EC.staleness_of("your dropdown menu"))
```

7. To capture the element, simply find the element we want to capture, then use the function .screenshot() to save it as examled below :
```
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "your CSS with -->  img")))
driver.find_element_by_css_selector("your CSS with -->)  img").screenshot("your complete path with extention of .png / .jpg")
```

Example how to use the code are in template file, feel free to modified it as suited to your need.

**-- End of README --**

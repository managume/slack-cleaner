from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


#INSERT CREDENTIALS
email = "USER@gmail.com"
usr = "USER"
pwd = "PASS"
#INSERT URL FILES
url = "https://TEAM.slack.com/files"
#INSERT URL MY FILES
url_myfiles = "https://TEAM.slack.com/files/USER"
#------------------
print("Start scraping")
driver = webdriver.Chrome()
#------------------
wait = WebDriverWait(driver,10)
#------------------
print("Log in")
driver.get(url)
input_email = driver.find_element_by_xpath('//*[@id="email"]')
input_email.send_keys(email)
input_pwd = driver.find_element_by_xpath('//*[@id="password"]')
input_pwd.send_keys(pwd)
input_btn = driver.find_element_by_xpath('//*[@id="signin_btn"]')
input_btn.click()
#------------------
print("Go to my files")
my_files = driver.find_element_by_xpath('//*[@id="page_contents"]/div[1]/a[2]')
my_files.click()
#------------------
print("Init deleting process")
num_files = driver.find_element_by_xpath('//*[@id="page_contents"]/div[2]/div[2]/p/strong[3]')
num_files = num_files.text
num_files = int(num_files)
try:
	for i in range(num_files):
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#files_list div:first-child")))
		file = driver.find_element_by_css_selector('#files_list div:first-child')
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#files_list div:first-child a")))
		filename = driver.find_element_by_css_selector('#files_list div:first-child h4')
		print("Deleting file %d of %d: %s" % (i,num_files,filename.text))
		filename.click()

		wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="page_contents"]/div[1]/div/span[2]')))
		action_link = driver.find_element_by_xpath('//*[@id="file_action_cog"]')
		action_link.click()

		wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="delete_file"]')))
		delete_action = driver.find_element_by_xpath('//*[@id="delete_file"]')
		delete_action.click()

		wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="generic_dialog"]/div[3]/button[3]')))
		confirm_action = driver.find_element_by_xpath('//*[@id="generic_dialog"]/div[3]/button[3]')
		wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="generic_dialog"]/div[3]/button[3]')))
		confirm_action.click()

		print("File deleted")
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#files_list div:first-child h4')))
		driver.get(url_myfiles)
finally:

	#driver.quit()
	print("Finish scraping")
print("Thanks :)")
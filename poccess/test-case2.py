#test yandex.ru | Danil Yanzin
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r"/Users/danilanzin/codestorage/poccess/chromedriver")
driver.get("https://www.yandex.ru/"); time.sleep(1)
list_links = driver.find_elements_by_tag_name('a')
for i in list_links:
    	print(i.get_attribute('href'))
print(len(list_links))
for i in list_links:
        if i.get_attribute('href')[0:16] == 'https://passport':
    	    print('passing link')
           

        else:
    		print(i.get_attribute('href'))
			driver.get(i.get_attribute('href'))
			time.sleep(5)
			print(i.get_attribute('href'))
        
       

driver.quit()
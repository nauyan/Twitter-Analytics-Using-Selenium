import time
from selenium import webdriver
import datetime
import calendar
import logging
import os
import shutil
from datetime import timedelta


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")

LOG_FILENAME = 'Log Filename and Location'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='w')

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'Chrome Driver Location')  # Optional argument, if not specified will search path.
driver.get('https://analytics.twitter.com/user/[YourUserName]/tweets')
try:
    time.sleep(3)
    username_field = driver.find_element_by_class_name("js-username-field")
    username_field.send_keys('[YourUserName]')
    #time.sleep(3)    
    password_field = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")
    #password_field = driver.find_element_by_class_name("js-password-field")
    password_field.send_keys('[YourPassword]')
    driver.find_element_by_class_name("EdgeButtom--medium").click()
    time.sleep(2)
    logging.info(':Logged into Twitter')
except:
    logging.info(':Failed to login to twitter')


before = os.listdir('Download Directory')
btn = driver.find_element_by_xpath("//span[@class='daterange-selected']").click()
monthTwitter = driver.find_element_by_xpath("//th[@class='month'][@colspan='5']")
monthTwitter =str(monthTwitter.text)
monthTwitter = monthTwitter.split(" ")
#print("Hello")
print (monthTwitter[0])
#print("Hello")
currentDay = datetime.datetime.today().day
now = datetime.datetime.now()    
currentYear = now.year
month = datetime.datetime.now().strftime("%m")
daysofMonth = calendar.monthrange(int(currentYear),int(month-1))

print(calendar.month_abbr[int(month)])
monthAbbr = calendar.month_abbr[int(month)]
if int(currentDay)==1:
    print("This is the first of the month")
    logging.info(':First of Month')
    driver.find_element_by_xpath("//th[@class='prev available']").click()
    #daysofMonth[1]
    
    driver.find_element_by_xpath("//td[@class='available in-range'][text()='"+str(daysofMonth[1])+"']").click()
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/table/tbody/tr/td[@class='available in-range'][text()='"+str(daysofMonth[1])+"']").click()
    
    
    time.sleep(2)
    driver.find_element_by_xpath("//button[@class='applyBtn btn btn-sm btn-primary']").click()
    export = driver.find_element_by_class_name("btn")#.click()
    if export.is_enabled():
        export.click()
        logging.info(':Downloading the File')
        time.sleep(5)
        after = os.listdir('Download Directory')
        change = set(after) - set(before)
        print (change)
        if len(change) == 1:
            file_name = change.pop()
            src_dir="Download Directory"
            src_file = os.path.join(src_dir, file_name)
            dst_dir="Destination Directory Where File is Needed to be Downloaded"
            shutil.copy(src_file,dst_dir)
            dst_file = os.path.join(dst_dir, file_name)
            fn=datetime.datetime.strftime(datetime.datetime.now() - timedelta(1), '%Y%m%d')
            fn=str(fn)+str("-Twitter.csv")
            new_dst_file_name = os.path.join(dst_dir, fn)
            os.rename(dst_file, new_dst_file_name)
            #print(file_name)
            logging.info(':Downloaded Posts Analytics File is '+str(file_name))
        else:
            print("File Not Downloaded")
    else:
        print("No Data is avaliable for yesterday")
    
if monthTwitter[0]== monthAbbr:  
    print("Same month")
    logging.info(':Same Month')
    logging.info(':Different month')
    
    #driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/table/thead/tr[1]/th[3]").click()
    
    #driver.find_element_by_xpath("//th[@class='next available']").click()
    #print(currentDay-1)
    driver.find_element_by_xpath("//td[@class='available in-range'][text()='"+str(currentDay-1)+"']").click()
    #/html/body/div[4]/div[3]/div/table/tbody
    #/html/body/div[4]/div[3]/div/table/tbody/tr[3]/td[2]
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/table/tbody/tr/td[@class='available in-range'][text()='"+str(currentDay-1)+"']").click()
    
    time.sleep(2)
    driver.find_element_by_xpath("//button[@class='applyBtn btn btn-sm btn-primary']").click()
    export = driver.find_element_by_class_name("btn")#.click()
    if export.is_enabled():
        export.click()
        logging.info(':Downloading the File')
        time.sleep(5)
        after = os.listdir('Download Directory')
        change = set(after) - set(before)
        print (change)
        if len(change) == 1:
            file_name = change.pop()
            src_dir="Download Directory"
            src_file = os.path.join(src_dir, file_name)
            dst_dir="Destination Directory Where File is Needed to be Downloaded"
            shutil.copy(src_file,dst_dir)
            dst_file = os.path.join(dst_dir, file_name)
            fn=datetime.datetime.strftime(datetime.datetime.now() - timedelta(1), '%Y%m%d')
            fn=str(fn)+str("-Twitter.csv")
            new_dst_file_name = os.path.join(dst_dir, fn)
            os.rename(dst_file, new_dst_file_name)
            #print(file_name)
            logging.info(':Downloaded Posts Analytics File is '+str(file_name))
        else:
            print("File Not Downloaded")
    else:
        print("No Data is avaliable for yesterday")
      

if monthTwitter[0]!= monthAbbr:  
    print("Different month")
    logging.info(':Different month')
    
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/table/thead/tr[1]/th[3]").click()
    
    #driver.find_element_by_xpath("//th[@class='next available']").click()
    print(currentDay-1)
    driver.find_element_by_xpath("//td[@class='available in-range'][text()='"+str(currentDay-1)+"']").click()
    #/html/body/div[4]/div[3]/div/table/tbody
    #/html/body/div[4]/div[3]/div/table/tbody/tr[3]/td[2]
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/table/tbody/tr/td[@class='available in-range'][text()='"+str(currentDay-1)+"']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[@class='applyBtn btn btn-sm btn-primary']").click()
    export = driver.find_element_by_class_name("btn")#.click()
    if export.is_enabled():
        export.click()
        logging.info(':Downloading the File')
        time.sleep(5)
        after = os.listdir('Download Directory')
        change = set(after) - set(before)
        print (change)
        if len(change) == 1:
            file_name = change.pop()
            src_dir="Download Directory"
            src_file = os.path.join(src_dir, file_name)
            dst_dir="Destination Directory Where File is Needed to be Downloaded"
            shutil.copy(src_file,dst_dir)
            dst_file = os.path.join(dst_dir, file_name)
            fn=datetime.datetime.strftime(datetime.datetime.now() - timedelta(1), '%Y%m%d')
            fn=str(fn)+str("-Twitter.csv")
            new_dst_file_name = os.path.join(dst_dir, fn)
            os.rename(dst_file, new_dst_file_name)
            #print(file_name)
            logging.info(':Downloaded Posts Analytics File is '+str(file_name))
        else:
            print("File Not Downloaded")
    else:
        print("No Data is avaliable for yesterday")




before = os.listdir('Download Directory')
time.sleep(2)
driver.find_element_by_xpath("//*[@id='SharedNavBarContainer']/div/div/ul[1]/li[5]/a").click()
driver.find_element_by_xpath("//*[@id='SharedNavBarContainer']/div/div/ul[1]/li[5]/ul/li[1]/a").click()
    
#driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/a ").click()   
btn = driver.find_element_by_xpath("//span[@class='daterange-selected']").click()
monthTwitter = driver.find_element_by_xpath("//th[@class='month'][@colspan='5']")
monthTwitter =str(monthTwitter.text)
monthTwitter = monthTwitter.split(" ")
print (monthTwitter[0])
currentDay = datetime.datetime.today().day
now = datetime.datetime.now()
currentYear = now.year
month = datetime.datetime.now().strftime("%m")
daysofMonth = calendar.monthrange(int(currentYear),int(month-1))
print(calendar.month_abbr[int(month)])
monthAbbr = calendar.month_abbr[int(month)]
if int(currentDay)==1:
    print("This is the first of the month")
    logging.info(':First of Month')
    driver.find_element_by_xpath("//th[@class='prev available']").click()
    #daysofMonth[1]
    
    driver.find_element_by_xpath("//td[@class='available in-range'][text()='"+str(daysofMonth[1])+"']").click()
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/table/tbody/tr/td[@class='available in-range'][text()='"+str(daysofMonth[1])+"']").click()
    
    
    
if monthTwitter[0]== monthAbbr:  
    print("Same month")
    logging.info(':Same Month')
    
    #driver.find_element_by_xpath("//th[@class='next available']").click()
    
    driver.find_element_by_xpath("//td[@class='available in-range'][text()='"+str(currentDay-1)+"']").click()
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/table/tbody/tr/td[@class='available in-range'][text()='"+str(currentDay-1)+"']").click()
    driver.find_element_by_xpath("//button[@class='applyBtn btn btn-sm btn-primary']").click()
    time.sleep(2)
    export = driver.find_element_by_class_name("btn")#.click()
    if export.is_enabled():
        export.click()
        logging.info(':Downloading the File')
        time.sleep(5)
        after = os.listdir('Download Directory')
        change = set(after) - set(before)
        print (change)
        if len(change) == 1:
            file_name = change.pop()
            src_dir="Download Directory"
            src_file = os.path.join(src_dir, file_name)
            dst_dir="Destination Directory Where File is Needed to be Downloaded"
            shutil.copy(src_file,dst_dir)
            dst_file = os.path.join(dst_dir, file_name)
            fn=datetime.datetime.strftime(datetime.datetime.now() - timedelta(1), '%Y%m%d')
            fn=str(fn)+str("-TwitterVideo.csv")
            new_dst_file_name = os.path.join(dst_dir, fn)
            os.rename(dst_file, new_dst_file_name)
            #print(file_name)
            logging.info(':Downloaded Posts Analytics File is '+str(file_name))
        else:
            print ("More than one file or no file downloaded")
    else:
        print("No file to download")
     
if monthTwitter[0]!= monthAbbr:  
    print("Different month")
    logging.info(':Different month')
    driver.find_element_by_xpath("//th[@class='next available']").click()
    driver.find_element_by_xpath("//td[@class='available in-range'][text()='"+str(currentDay-1)+"']").click()
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/table/tbody/tr/td[@class='available in-range'][text()='"+str(currentDay-1)+"']").click()
    driver.find_element_by_xpath("//button[@class='applyBtn btn btn-sm btn-primary']").click()
    time.sleep(2)
    export = driver.find_element_by_class_name("btn")#.click()
    if export.is_enabled():
        export.click()
        logging.info(':Downloading the File')
        time.sleep(5)
        after = os.listdir('Download Directory')
        change = set(after) - set(before)
        print (change)
        if len(change) == 1:
            file_name = change.pop()
            src_dir="Download Directory"
            src_file = os.path.join(src_dir, file_name)
            dst_dir="Destination Directory Where File is Needed to be Downloaded"
            shutil.copy(src_file,dst_dir)
            dst_file = os.path.join(dst_dir, file_name)
            fn=datetime.datetime.strftime(datetime.datetime.now() - timedelta(1), '%Y%m%d')
            fn=str(fn)+str("-TwitterVideo.csv")
            new_dst_file_name = os.path.join(dst_dir, fn)
            os.rename(dst_file, new_dst_file_name)
            #print(file_name)
            logging.info(':Downloaded Posts Analytics File is '+str(file_name))
        else:
            print ("More than one file or no file downloaded")
    else:
        print("No file to download")
     

logging.shutdown()


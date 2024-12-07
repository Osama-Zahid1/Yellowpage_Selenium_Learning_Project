from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException



def scrape(in1,in2):
    chrome_options=Options()
    chrome_options.add_experimental_option('detach',True)
    driver=webdriver.Chrome(options=chrome_options)
    url='https://ypages.pk/'
    driver.get(url)
    what=driver.find_element(By.XPATH,'//*[@id="search"]')
    
    location=driver.find_element(By.XPATH,'//*[@id="Location"]')
   
    search=driver.find_element(By.XPATH,'//*[@id="frmkeyword"]/div/div/div[3]/div[1]/button')
    what.send_keys(in1)
    print(in1)
    location.send_keys(in2)
    print(in2)
    search.click()
    
    time.sleep(5)
    
    data_list=[]
    while 
    posts = driver.find_elements(By.CSS_SELECTOR, '.sponsoresSecond')
    print(posts)
    
    for post in posts:
        try:  
            title=post.find_element(By.CSS_SELECTOR, "h2 > span").text
            loc=post.find_element(By.CSS_SELECTOR, '.comAddress > span').text
            number=post.find_element(By.CLASS_NAME, 'featuredPhone').text
            number =number.replace('Tel: ', '')
            services=post.find_element(By.CLASS_NAME, 'featuredAddress').text
            services = services.replace('Listed In: ', '')
            dict={
                'name':title,
                'area':loc,
                'num':number,
                'ser':services
            }
            data_list.append(dict)
            
        except NoSuchElementException:
            
            print("Element not found or stale.")
    button=driver.find_element(By.XPATH,'//*[@id="midcontianer"]/div[2]/div[2]/div[2]/div[2]/div/div/a[1]')
    button.click()
    time.sleep(5)
        
    driver.quit()
        
    df=pd.DataFrame(data_list)
        
    df.to_csv("output_data.csv", index=False)
        
def user():
    input1=input('enter service: ')
    input2=input('enter location: ')
    scrape(input1,input2)    
        
user()
    
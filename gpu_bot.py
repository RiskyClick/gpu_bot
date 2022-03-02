from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib  # python library to send emails
import time
driver = webdriver.Chrome('./chromedriver')


def send_email(title):
    server = smtplib.SMTP("smtp.gmail.com" , 587)  # 587 = port number
    server.ehlo() # check the smtp connection 
    server.starttls()  # start the conection 
    server.login("log_in_email" , "log_in_pw")  
    server.sendmail("from_email" , "to_email" , title)
    server.close() 
    
def clickable(title, button):
    if button.is_enabled():
        button.click()
        send_email(title)
        exit(0)

while True:
    driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434")
    title = driver.find_element_by_tag_name('h1')
    button = driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div/button")
    clickable(title.text, button)
    time.sleep(10)
    driver.refresh()
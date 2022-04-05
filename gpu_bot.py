from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib  # python library to send emails
driver = webdriver.Chrome('./chromedriver')
refresh = 0

def send_email():
    server = smtplib.SMTP("smtp.gmail.com" , 587)  # 587 = port number
    server.ehlo() # check the smtp connection 
    server.starttls()  # start the conection 
    server.login("email" , "pw")  
    server.sendmail("email" , "email" , "Go Get GPU")
    server.close()
    print("email was sent") 

while True:
    driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
    try:
        button = driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div/div[1]/div[3]/div[2]/div/div[2]/div[2]/div/div/div/button")
        button.click()
        send_email()
        break
    except:
        refresh += 1
        driver.refresh()
        print(f"This bot has refreshed: {refresh} times")

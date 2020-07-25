# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:46:27 2020

@author: anjali
"""
import smtplib


def send_email():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("sender_email_id","sender_email_id_password")
    message="yay! price is affordable"
    s.sendmail("sender_email_id", "receiver_email_id" , messsage)
    s.quit()
    
    
import requests
from bs4 import BeautifulSoup as bs
page_url="https://www.amazon.in/dp/B081JS1Q2Y/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B081JS1Q2Y&pd_rd_w=BPYF0&pf_rd_p=1801b34c-8af9-42b5-8961-11f124edc99b&pd_rd_wg=rFeWl&pf_rd_r=A2PMA22FHVCF2V0PHJBE&pd_rd_r=41122112-fb6e-4eee-b52a-14890dc69100&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzREpTWDk5WEw0NE5KJmVuY3J5cHRlZElkPUEwNDA0NzQ3OE9HUEFGRU9VOFQyJmVuY3J5cHRlZEFkSWQ9QTA4Mzk5NzkzSlRYVVdOVFpWMDdMJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
browser_agent={"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
product_page=requests.get(page_url,headers=browser_agent)
html = product_page.content

#Beautiful Soup

soup=bs(html,'html.parser')


print(soup.prettify())
page_title=soup.find(id="productTitle").get_text()
product_price=soup.find(id="priceblock_ourprice").get_text()[2:8]
print(page_title)
print(product_price)
product_price=product_price.replace(',','')
price=float(product_price)
print(price)
if(price<68000):
    send_email()
    


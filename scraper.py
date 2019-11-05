# Amazon.com Price Scraper WIP

import requests
from bs4 import BeautifulSoup
import smtplib
import time
import os

URL = 'https://www.amazon.com/gp/product/B074JKT894/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

# User variables
email = os.environ['EMAIL']
mail_password = os.environ['MAIL_PASSWORD']

def check_price():
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()
    price_raw = soup2.find(id='priceblock_ourprice')
    price_fmt = soup2.find(id='priceblock_ourprice').get_text()
    converted_price = float(price_fmt[1:4])

    print('Checking current price.')
    if(converted_price < 500.0):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email, mail_password)

    subject = 'Price has lowered!'
    body = 'Check the amazon link here:\n\n' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        email,
        email,
        msg
    )
    print("Email has been sent")

    server.quit()

while(True):
    check_price()
    time.sleep(60*30)
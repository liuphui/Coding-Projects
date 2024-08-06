import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.co.uk/Xiaomi-Black-Smartphone-Snapdragon%C2%AE-Charging-Warranty%EF%BC%89/dp/B0CV5Y5MQ1/?_encoding=UTF8&pd_rd_w=hyGE0&content-id=amzn1.sym.b5aa45f4-de27-4ad5-aa7e-54486ef1a737%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=b5aa45f4-de27-4ad5-aa7e-54486ef1a737&pf_rd_r=NFHMNHK6RGDMM04X7QM6&pd_rd_wg=r7S1d&pd_rd_r=dd639480-7fa7-4f77-8683-8eb7acebfc38&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1"

headers = {"User-Agent": 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

# fill in with the emails you want to be the sender and the receiver
sender = ''
receiver = ''
# fill in the app password from google
app_password = ''

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(class_="a-price-whole").get_text().strip()
    converted_price = float(price[0:3])

    if converted_price < 369:
        send_mail()
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(sender, app_password)
    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.co.uk/Xiaomi-Black-Smartphone-Snapdragon%C2%AE-Charging-Warranty%EF%BC%89/dp/B0CV5Y5MQ1/?_encoding=UTF8&pd_rd_w=gSTVY&content-id=amzn1.sym.b5aa45f4-de27-4ad5-aa7e-54486ef1a737%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=b5aa45f4-de27-4ad5-aa7e-54486ef1a737&pf_rd_r=3GJV12QXMKGC1Q75X90A&pd_rd_wg=cTeNS&pd_rd_r=ee62b7ba-d3a3-4dc0-91e3-f78e1c26c904&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        sender,
        receiver,
        msg
    )
    print("EMAIL HAS BEEN SENT")
    server.quit()
    
    
while True:
    check_price()
    # sleep for a day
    time.sleep(60 * 60 * 24)

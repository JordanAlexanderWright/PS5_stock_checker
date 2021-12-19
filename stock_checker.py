from selenium import webdriver
from time import sleep
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from texting import send_text


 #Each of these will open google chrome to the page and prepare to scrape info

amazon_browser = webdriver.Chrome("./Chromedriver.exe")
amazon_browser.get('https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=as_li_ss_tl?ref_=ast_sto_dp&linkCode=sl1&tag=nweditorial-20&linkId=4bd3522a77f201eb46398a875c0ed766&language=en_US')
a_link = "https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=as_li_ss_tl?ref_=ast_sto_dp&linkCode=sl1&tag=nweditorial-20&linkId=4bd3522a77f201eb46398a875c0ed766&language=en_US"

target_browser = webdriver.Chrome("./chromedriver.exe")
target_browser.get('https://www.target.com/p/playstation-5-console/-/A-81114595#lnk=sametab')
t_link = 'https://www.target.com/p/playstation-5-console/-/A-81114595#lnk=sametab'

bestbuy_browser = webdriver.Chrome("./chromedriver.exe")
bestbuy_browser.get('https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149')
bb_link = 'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149'

gamestop_browser = webdriver.Chrome("./chromedriver.exe")
gamestop_browser.get("https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html")
gs_link = "https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html"

walmart_browser = webdriver.Chrome("./Chromedriver.exe")
walmart_browser.get('https://www.walmart.com/ip/PlayStation-5-Console/363472942?irgwc=1&sourceid=imp_TgLSzSSaexyOW1twUx0Mo3b2UkESPd0ZWUMA080&veh=aff&wmlspartner=imp_1943169&clickid=TgLSzSSaexyOW1twUx0Mo3b2UkESPd0ZWUMA080&sharedid=&affiliates_ad_id=565706&campaign_id=9383')
w_link = 'https://www.walmart.com/ip/PlayStation-5-Console/363472942?irgwc=1&sourceid=imp_TgLSzSSaexyOW1twUx0Mo3b2UkESPd0ZWUMA080&veh=aff&wmlspartner=imp_1943169&clickid=TgLSzSSaexyOW1twUx0Mo3b2UkESPd0ZWUMA080&sharedid=&affiliates_ad_id=565706&campaign_id=9383'


# This function takes two params, the website link, and store name. Then it will send an email to me with that info
def send_email(store, link):

    html = Template(Path('email.html').read_text())
    email = EmailMessage()

    email['from'] = 'YOURNAMEHERE'
    email['to'] = 'YOUREMAILHERE@WHATEVER.COM'
    email['subject'] = 'PS5 STOCK UPDATE'

    email.set_content(html.substitute({'store': store, 'link': link}), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('YOURDUMMYEMAIL@WHATEVER.COM', 'YOURDUMMYPASSWORD')
        smtp.send_message(email)


# Each of the check_x functions will look for a specific piece of HTML and decide if the PS5 is in stock or not.
# open try and except blocks are there for the inevitable breaking

def check_target():
    target_browser.refresh()
    try:
        stock = target_browser.find_element_by_class_name("h-text-orangeDark")
    except:
        stock = ""
    try:
        if stock.text == "Sold out":
            pass
        else:
            send_email("Target", t_link)
            send_text("Target")
    except:
        print("oops, Target broken?")


def check_bestbuy():
    bestbuy_browser.refresh()
    try:
        stock = bestbuy_browser.find_element_by_class_name("btn-disabled")
    except:
        stock = ""
    try:
        if stock.text == "Sold Out":
            pass
        else:
            send_email("Best Buy", bb_link)
            send_text("Best Buy")
    except:
        print("oops, Best Buy broken?")


def check_gamestop():
    gamestop_browser.refresh()
    try:
        stock = gamestop_browser.find_element_by_class_name("add-to-cart")
    except:
        stock = ""
    try:
        if stock.text == "NOT AVAILABLE":
            pass
        else:
            send_email("Gamestop", gs_link)
            send_text("Gamestop")
    except:
        print("oops, Gamestop broken?")


def check_amazon():
    amazon_browser.refresh()
    try:
        stock = amazon_browser.find_element_by_class_name("a-color-price")
    except:
        stock = ""
    try:
        if stock.text == "Currently unavailable.":
            pass
        else:
            send_email("Amazon", a_link)
            send_text("Amazon")
    except:
        print("oops, Jeff Bezos broken?")


def check_walmart():
    walmart_browser.refresh()
    try:
        stock = walmart_browser.find_element_by_class_name("prod-blitz-copy-message")
    except:
        stock = ""
    try:
        if stock.text == "This item is out of stock.":
            pass
        else:
            send_email("Walmart", w_link)
            send_text("Walmart")
    except:
        print("oops, Wallyworld broken?")


def check_ps5_stock():
    while True:
        check_target()
        check_bestbuy()
        check_gamestop()
        check_amazon()
        check_walmart()
        sleep(60)


if __name__ == "__main__":
    check_ps5_stock()



# PS5-Stock Checker


Project Goal
---
---
The Goal of this is project was to make a script that would help a user obtain a 
PlayStation 5 console while it had very limited availability


**Usage**
---
---

Chromedriver needs to be updated to whatever version of Chrome you are using.  
In addition, a user needs an email that allows use by applications and a Twilio account / auth token.

This project was mostly meant to be a personal one, so setup is not streamlined.

---
stock_checker.py needs the following changes:

- Line 39: Change Email 
- Line 40: Change Name  
- Line 48: Need Dummy Email and Password. Note, this email has to be activated to accept use from an application

---
texting.py needs the following changes:

- Line 4: Change Account SID 
- Line 6: Change Auth Token  
- Line 13: Change Twilio Phone 
- Line 14: Change To Your Phone

scraping.py is an example of using BeautifulSoup and Requests to get data.




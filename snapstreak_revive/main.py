from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import json
import chromedriver_autoinstall

""" user specific information - modify OK """
# chromedriver path
PATH = "./chromedriver"
# Your friend's Snapchat username
friendsUsername = ""
# Numbers only, no letters or symbols
streakLength = ""

# ---------------------------------------------------------------

""" program preset info - modify OK but not recommended"""
# loading credentials from json
try:
   with open('credentials.json') as f:
      credentials = json.load(f)
except FileNotFoundError:
   with open('credentials.json', 'w') as f:
      json.dump({"username": "", "emailAddress": "", "mobileNumber": "", "device": "", "issueDate": "today"}, f)
   with open('credentials.json') as f:
      credentials = json.load(f)
# required info
information = ("Our snapstreaks randomly disappeared today, even though we"
               " snapped each other multiple times yesterday and today, and the hourglass icon",
               " didn't show up either.")

# ---------------------------------------------------------------

""" website specific IDs - do not modify"""

URL = "https://support.snapchat.com/en-GB/i-need-help"
SUCCESS_URL = "https://support.snapchat.com/en-GB/success"
HELP_OPTION_ID = "5695496404336640"
USERNAME_INPUT_ID = "field-24281229"
EMAIL_INPUT_ID = "field-24335325"
PHONE_NUMBER_INPUT_ID = "field-24369716"
DEVICE_INPUT_ID = "field-24369726"
FRIEND_USERNAME_INPUT_ID = "field-24369736"
ISSUE_DATE_INPUT_ID = "field-24326423"
STREAK_LENGTH_INPUT_ID = "field-24641746"
DROPDOWN_HOURGLASS_TAG = 'i'
DROPDOWN_DATA_VALUE_CLASS = "//div[@data-value='hourglass-no']"
INFORMATION_INPUT_ID = "field-22808619"
SUBMIT_BUTTON_ID = "submit-button"
LAST = -1


# ---------------------------------------------------------------

def main():
   global friendsUsername
   global streakLength

   if not credentials["username"]:
      credentials["username"] = input("Enter your username: (you only have to do this once) ")
   if not credentials["emailAddress"]:
      credentials["emailAddress"] = input("Enter your email address: (you only have to do this once) ")
   if not credentials["mobileNumber"]:
      credentials["mobileNumber"] = input("Enter your phone number: (you only have to do this once) ")
   if not credentials["device"]:
      credentials["device"] = input("Enter the device on which you have Snapchat: (you only have to do this once) ")
   with open("credentials.json", "w") as outfile:
      json.dump(credentials, outfile)
   if not friendsUsername:
      friendsUsername = input("Enter friend's username: ")
   if not streakLength:
      streakLength = input("Enter old streak length: ")

   assert friendsUsername, "You need to enter your friend's username into variable 'friendsUsername'"
   assert streakLength, "You need to enter the length of your streak into variable 'streakLength'"

   chromedriver_autoinstall.install()
   if chromedriver_autoinstall.get_platform() == "mac":
      os.chmod('./chromedriver', 0o755)
   driver = webdriver.Chrome(PATH)
   driver.get(URL)

   help_option = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, HELP_OPTION_ID)))
   help_option.send_keys(Keys.ENTER)

   # username
   username_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, USERNAME_INPUT_ID)))
   username_input.send_keys(credentials["username"])

   # email address
   email_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, EMAIL_INPUT_ID)))
   email_input.send_keys(credentials["emailAddress"])

   # mobile number
   mobile_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, PHONE_NUMBER_INPUT_ID)))
   mobile_input.send_keys(credentials["mobileNumber"])

   # device
   device_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, DEVICE_INPUT_ID)))
   device_input.send_keys(credentials["device"])

   # friend's username
   friend_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, FRIEND_USERNAME_INPUT_ID)))
   friend_input.send_keys(friendsUsername)

   # issue date
   issue_date_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, ISSUE_DATE_INPUT_ID)))
   issue_date_input.send_keys(credentials["issueDate"])

   # snapstreak length
   streak_length_input = WebDriverWait(driver, 5).until(
      EC.presence_of_element_located((By.ID, STREAK_LENGTH_INPUT_ID)))
   streak_length_input.send_keys(streakLength)

   # hourglass icon
   time.sleep(0.2)
   hourglass_dropbox = (driver.find_elements(By.TAG_NAME, DROPDOWN_HOURGLASS_TAG))[LAST].click()
   time.sleep(0.2)
   dropbox_no_option = driver.find_element(By.XPATH, DROPDOWN_DATA_VALUE_CLASS).click()

   # details
   information_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, INFORMATION_INPUT_ID)))
   information_input.send_keys(information)

   # submit button
   submit_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, SUBMIT_BUTTON_ID))).click()

   WebDriverWait(driver, 1000).until(lambda driver: driver.current_url == SUCCESS_URL)
   driver.quit()
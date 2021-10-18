from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

""" user specific information - modify OK """
# chromedriver path
PATH = ""
# Your Snapchat username (no spaces), or write “none”
username = ""
# Email associated with your Snapchat account (if applicable)
emailAddress = ""
# Include country code (e.g. +1 202 555 0192)
mobileNumber = ""
# Include brand, model and model series
device = ""
# Your friend's Snapchat username
friendsUsername = ""
# e.g. yesterday or 31/01/16
issueDate = "today"
# Numbers only, no letters or symbols
streakLength = ""

# ---------------------------------------------------------------

""" program preset info - modify OK but not recommended"""

information = ("Our snapstreaks randomly disappeared today, even though we"
" snapped each other multiple times yesterday and today, and the hourglass icon",
" didn't show up either.")

# ---------------------------------------------------------------

""" website specific IDs - do not modify"""

URL = "https://support.snapchat.com/en-GB/i-need-help"
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
   assert PATH, "You need to enter the path to chromedriver into variable 'PATH'"
   assert username, "You need to enter your username into variable 'username'"
   assert emailAddress, "You need to enter your email address into variable 'emailAddress'"
   assert mobileNumber, "You need to enter your phone number into variable 'mobileNumber'"
   assert device, "You need to enter your device into variable 'device'"
   assert friendsUsername, "You need to enter your friend's username into variable 'friendsUsername'"
   assert streakLength, "You need to enter the length of your streak into variable 'streakLength'"

   driver = webdriver.Chrome(PATH)
   driver.get(URL)

   help_option = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, HELP_OPTION_ID)))
   help_option.send_keys(Keys.ENTER)

   # username
   username_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, USERNAME_INPUT_ID)))
   username_input.send_keys(username)

   # email address
   email_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, EMAIL_INPUT_ID)))
   email_input.send_keys(emailAddress)

   # mobile number
   mobile_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, PHONE_NUMBER_INPUT_ID)))
   mobile_input.send_keys(mobileNumber)

   # device
   device_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, DEVICE_INPUT_ID)))
   device_input.send_keys(device)

   # friend's username
   friend_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, FRIEND_USERNAME_INPUT_ID)))
   friend_input.send_keys(friendsUsername)

   # issue date
   issue_date_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, ISSUE_DATE_INPUT_ID)))
   issue_date_input.send_keys(issueDate)

   # snapstreak length
   streak_length_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, STREAK_LENGTH_INPUT_ID)))
   streak_length_input.send_keys(streakLength)

   # hourglass icon
   time.sleep(0.2)
   hourglass_dropbox = (driver.find_elements_by_tag_name(DROPDOWN_HOURGLASS_TAG))[LAST].click()
   time.sleep(0.2)
   dropbox_no_option = driver.find_element_by_xpath(DROPDOWN_DATA_VALUE_CLASS).click()

   # details
   information_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, INFORMATION_INPUT_ID)))
   information_input.send_keys(information)

   # submit button
   submit_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, SUBMIT_BUTTON_ID))).click()

   time.sleep(1000)

main()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

import re
import shutil
import os
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import (
#     ElementNotVisibleException
# )


driver = webdriver.Firefox()
driver.wait = WebDriverWait(driver, 5)
action = webdriver.common.action_chains.ActionChains(driver)

url = "https://calendar.google.com/calendar/selfsched?sstoken=UUJjd182VklGYVlRfGRlZmF1bHR8Y2E5NDJlM2QyMmJiNDcwZDI0YzIyNGY1ZDdkOWIxZGY"


delayTime = 2

driver.get(url)

# give time for self to put in password attempts! why can't i ever remember my password? +  push authentication
time.sleep(45)


blocks = [];
blocks = driver.find_elements_by_class_name("avtext")

# maxNumber = len(blocks)

# i = 0

for i in range(0,len(blocks)):
# loads them all - total of 16
    bookingDialog = 0

    driver.refresh();

    time.sleep(delayTime);

    driver.get(driver.current_url)

    time.sleep(delayTime);

    action = webdriver.common.action_chains.ActionChains(driver)

    time.sleep(delayTime);

    blocks = driver.find_elements_by_class_name("avtext")
    # iterate on each
    for block in blocks:

        if (block.value_of_css_property('background-color') != "#D6AE00" and (block.text == "office hours" or block.text == "Office hours")):

            block.click()
            time.sleep(delayTime)

            bookingDialog = driver.find_element_by_class_name("gcal-dialog")
            print "click on save on the dialog box"
            action.move_to_element_with_offset(bookingDialog, 130, 300).click().perform()

            time.sleep(delayTime)
            break


    # if (i == 0):
    #     officeHours[0].click()
    # elif (i == 1):
    #     officeHours[0].click()
    # else:
    #     officeHours[i].click()

    # time.sleep(delayTime)
    #
    # bookingDialog = driver.find_element_by_class_name("gcal-dialog")
    # print "click on save on the dialog box"
    # action.move_to_element_with_offset(bookingDialog, 130, 300).click().perform()
    #
    # time.sleep(delayTime)
    #
    # doneDialog = driver.find_element_by_class_name("gcal-dialog")
    # print "click to exit the dialog box"
    # action.move_to_element_with_offset(bookingDialog, 265, 25).click().perform()
    #
    # time.sleep(delayTime)

    # i = i + 1





# driver.exit()

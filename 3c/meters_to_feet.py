import math
from selenium import webdriver
import time
from random import randint


def decimals(num):
    return max(0, min(6, 6 - int(math.log10(abs(num))))) if num else 6


def delete_text(txt):
    return str(txt.partition('= ')[2]).partition('ft')[0]


def meters_to_feet(meters):
    feet = meters /0.3048
    return "{:#.7g}".format(feet, decimals(feet))


try:
    browser = webdriver.Chrome()
    browser.get("https://www.metric-conversions.org/")
    element1 = browser.find_element_by_css_selector("#queryFrom").send_keys("Meters")
    element2 = browser.find_element_by_css_selector("#queryTo").send_keys("Feet")
    time.sleep(2)
    button = browser.find_element_by_css_selector("a.convert.greenButton").click()
    time.sleep(2)
    number = randint(-140, 140)
    element3 = browser.find_element_by_css_selector("#argumentConv").send_keys(str(number))
    element4 = browser.find_element_by_xpath('//*[@id="sigfig"]').click()
    element5 = browser.find_element_by_css_selector("#format > option:nth-child(2)").click()
    answer_el = browser.find_element_by_xpath("//*[@id='answer']")
    assert meters_to_feet(number) == delete_text(answer_el.text)

finally:
    browser.quit()

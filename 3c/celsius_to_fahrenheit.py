import math
from selenium import webdriver
import time
from random import randint


def decimals(num):
    return max(0, min(6, 6 - int(math.log10(abs(num))))) if num else 6


def delete_text(txt):
    return str(txt.partition('= ')[2]).partition('°')[0]


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return "{:#.7g}".format(fahrenheit, decimals(fahrenheit))


try:
    browser = webdriver.Chrome()
    browser.get("https://www.metric-conversions.org/")
    element1 = browser.find_element_by_css_selector("#queryFrom").send_keys("Celsius")
    element2 = browser.find_element_by_css_selector("#queryTo").send_keys("Fahrenheit")
    time.sleep(2)
    button = browser.find_element_by_css_selector("a.convert.greenButton").click()
    time.sleep(2)
    number = randint(-140, 140)
    element3 = browser.find_element_by_css_selector("#argumentConv").send_keys(str(number))
    answer_el = browser.find_element_by_xpath("//*[@id='answer']")
    assert celsius_to_fahrenheit(number) == delete_text(answer_el.text)

finally:
    browser.quit()

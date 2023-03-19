from selenium import webdriver
from utils.pages.calorie_calc import CarbCalcPage

def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.calculator = CarbCalcPage()

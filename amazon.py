import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('-ignore-certificate-errors')
options.add_argument('-ignore-ssl-errors')

def login(email, password):
    driver.get("https://www.amazon.com/")
    driver.find_element_by_id("nav-link-accountList-nav-line-1").click()
    driver.find_element_by_id("ap_email").send_keys(email)
    driver.find_element_by_id("continue").click()
    driver.find_element_by_id("ap_password").send_keys(password)
    driver.find_element_by_id("signInSubmit").click()

def search_product(product_name):
    driver.get("https://www.amazon.com/")
    search_field = driver.find_element_by_id("twotabsearchtextbox")
    search_field.send_keys(Keys.RETURN)
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(By.id,"search"))
    except:
        print("No se encontraron resultados")

def add_to_cart():
    try:
        add_to_cart_button = driver.find_element_by_xpath("//input[@id='add-to-cart-button]")
        add_to_cart_button.click()
    except:
        print("No se puede agregar al carrito")

def check_cart():
    driver.get("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(By.ID, "sc-active-cart"))
        print("El producto se ha agregado al carrito")
    except:
        print("No se puedo agregar el producto al carrito")

api_id: 24253609
api_hash = "20c1618672d0d23844bf79d8a25de44f"
bot_token = "5721192910:AAGM92Ytd21sW8fufKt4f4ML3oeUbLbrLn8"

import requests # для запросов
from bs4 import BeautifulSoup as BS # для парсинга
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Function

def get_source_html(url):
    driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")
    driver.maximize_window()

    try:
        driver.get(url=url)
        link_last_page = driver.find_element(By.CLASS_NAME, "pagination-widget__page-link_last").get_attribute('href')
        link_last_page_arr = link_last_page.split("?p=")
        if (len(link_last_page_arr) > 1):
            for indexPage in range(int(link_last_page_arr[1])):
                products = driver.find_elements(By.CLASS_NAME, "catalog-product")

                for product in products:
                    price = product.find_element(By.CLASS_NAME, "product-buy__price").text
                    name = product.find_element(By.CLASS_NAME, "catalog-product__name span").text
                    print(name + " " + price + " \n")

                driver.find_element(By.CLASS_NAME, "pagination-widget__page-link_next").click()
                time.sleep(4)

    except Ellipsis as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

def main():
    get_source_html(url="https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/")

# Main
if __name__ == "__main__":
    main()

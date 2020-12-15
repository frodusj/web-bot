from selenium import webdriver
from sconfig import keys
import time

def order(k):

    driver.get(k['product_url'])
    driver.find_element_by_xpath('//*[@id="AppUserEmail"]').send_keys(k['email'])
    driver.find_element_by_xpath('//*[@id="AppUserPassword"]').send_keys(k['password'])
    driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/div[3]/div[2]/div/input').click()
    driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[4]/button').click()
    driver.find_element_by_xpath('//*[@id="cart"]/div/div[1]/div/input').click()
    driver.find_element_by_xpath('//*[@id="OrderRetailerSelectionChooseRetailer"]').click()
    driver.find_element_by_xpath('//*[@id="AddressCountryId"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="AddressZoneId6"]/option[35]').click()
    driver.find_element_by_xpath('//*[@id="city"]/option[25]').click()
    driver.find_element_by_xpath('//*[@id="retailer_id"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="select-delivery-form"]/div[4]/input').click()
    driver.find_element_by_xpath('//*[@id="SelectSamplesSelectBarrelsForm"]/div[3]/div/div/button').click()
    driver.find_element_by_xpath('//*[@id="TripDetail9TripDate_table"]/tbody/tr[2]/td[6]/div').click()



if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    order(keys)


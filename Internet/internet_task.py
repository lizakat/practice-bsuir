"""
Output:

LocalStorage Value: testValue
LocalStorage Value: LocalStorage value not found
Cookie Value: testValue
Cookie Value: Cookie not found
"""


from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
import time

edge_service = EdgeService('D:/edgedriver_win64/msedgedriver.exe')

edge_options = Options()
edge_options.add_argument("--start-maximized")

driver = webdriver.Edge(service=edge_service, options=edge_options)

driver.get("https://www.example.com/")

# LocalStorage
# Set value in LocalStorage
driver.execute_script("localStorage.setItem('testKey', 'testValue');")
# Get value from LocalStorage
local_storage_value = driver.execute_script(
    "return localStorage.getItem('testKey');")
print(
    f"LocalStorage Value: {local_storage_value if local_storage_value else 'LocalStorage value not found'}")
# Remove value from LocalStorage
driver.execute_script("localStorage.removeItem('testKey');")
# Get value from LocalStorage after removing
local_storage_value = driver.execute_script(
    "return localStorage.getItem('testKey');")
print(
    f"LocalStorage Value: {local_storage_value if local_storage_value else 'LocalStorage value not found'}")

# Cookie
# Set value in Cookie
driver.add_cookie({"name": "testCookie", "value": "testValue"})
# Get value from Cookie
cookie = driver.get_cookie("testCookie")
print(f"Cookie Value: {cookie['value'] if cookie else 'Cookie not found'}")
# Remove value from Cookie
driver.delete_cookie("testCookie")
# Get value from Cookie after removing
cookie = driver.get_cookie("testCookie")
print(f"Cookie Value: {cookie['value'] if cookie else 'Cookie not found'}")

driver.quit()

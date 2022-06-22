from selenium import webdriver

chromedriver_location = "D:\Documents\chromedriver_win32/chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.get("https://www.instagram.com/")
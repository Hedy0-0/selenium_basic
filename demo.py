#打开百度
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
#打开百度 bing浏览器
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.get('https://www.bing.com')   #bing的网址为cn.bing  但是使用www.bing也能打开
#通过定义参数来打开多个网页
from selenium import webdriver
driver = webdriver.Chrome()
def open(url):
    driver.get(url)
open ('https://www.baidu.com')
open ('https://cn.bing.com')


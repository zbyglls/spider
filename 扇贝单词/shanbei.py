from selenium import webdriver
import time


def login():
    url = 'https://web.shanbay.com/web/account/login/'
    driver.get(url)
    # 微信扫码登录
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/a').click()
    time.sleep(5)
    return None


def openList():
    driver.find_element_by_xpath('//*[@id="main-navbar"]/div[1]/div/div/ul[1]/li[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div[2]/a').click()
    time.sleep(2)
    # 打开单词列表
    driver.find_element_by_xpath('//*[@id="4"]/div').click()


def result():
    en = driver.find_elements_by_xpath('//div[@class="index_top__1grCv"]')
    zh = driver.find_elements_by_xpath('//div[@class="index_bottom__XLoPQ"]')
    enlist = [_.text for _ in en]
    zhlist = [_.text for _ in zh]
    with open(r'file.txt', '+a') as file:
        for _ in zip(enlist, zhlist):
            if _[0]+':'+_[1] in list(file):
                break
            else:
                file.writelines(_[0]+':'+_[1])
    # 翻页
    driver.find_elements_by_tag_name('li')[-1].click()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    login()
    openList()
    result()
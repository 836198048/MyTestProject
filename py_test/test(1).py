import time
from selenium import webdriver

url1 = 'https://item.mi.com/product/10000041.html'
url2 = 'https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fitem.mi.com%252Fproduct%252F10000041.html%26sign%3DZTkwNDE2MjVlYzE0NGVkNjBlMTA4NmIzMTlhZjdhZDEwNjNlOTNhNw%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180'

print('the first')
driver = webdriver.Chrome()
print(driver.name)
print('登陆')
a=driver.get(url2)
driver.find_element_by_id('username').send_keys('18850105130')
driver.find_element_by_id('pwd').send_keys('fanxi124578369!')

driver.find_element_by_xpath('//*[@id="login-button"]').click()
#js='window.open("'+url1+'");'
#driver.execute_script(js)
#now_handle = driver.current_window_handle
#driver.switch_to_window(now_handle)

driver.find_element_by_id('login-button').click()
print('登陆结束')
print('开始循环抢购')
#driver(url1)
links = driver.find_elements_by_tag_name("a")
time.sleep(1)
n = 0
while n == 0:
    # print(links)
    buy = ''
    print('抢购')
    # driver.find_element_by_xpath('//ul[@id="J_list"]/div[2]/ul/li[2]/a').click()

    # print(driver.find_element_by_xpath('//ul[@id="J_buyBtnBox"]/li'))
    # myclick = driver.find_element_by_xpath('//*[@id="J_policy"]/span')
    # print(myclick.text)
    time.sleep(2)
    print(driver.find_element_by_xpath('//a[@class="btn btn-primary  btn-biglarge J_proBuyBtn"]').text)
    try:
        driver.find_element_by_xpath('//a[@class="btn btn-primary  btn-biglarge J_proBuyBtn"]').click()
    except:
        print('error')
    # print(myClick)
    # driver.find_element_by_xpath('//*[@id="J_buyBtnBox"]/li/a').click()
    # driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[4]/ul/li/a').click()
    # for link in links:
    #     buy = link.get_attribute("href")
    #     if buy is None:
    #         continue
    #     if buy in 'gid':
    #         driver.get(buy)
    #         print('抢购中')
    print('休息10秒钟')
    break
    time.sleep(10)
#
# #driver.close()

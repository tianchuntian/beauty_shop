from common.base import Base, open_browser
from page.goodspage import GoodsPage
from page.housepage import HousePage
from page.loginpage import LoginPage, url


class BuyNow(Base):
    "封装选择商品后点击立即购买页面"
    buy_now_loc=("css selector","img[src='themes/default/images/buybtn1.png']")

    def buy_now_click(self):
        self.click(self.buy_now_loc)



if __name__ == '__main__':
    driver = open_browser()
    login = LoginPage(driver)
    login.open_url(url)
    username = '诸葛亮_2'
    password = 'Test123456'
    login.input_username(username)
    login.input_password(password)
    login.submit_click()
    print(login.is_successed(username))
    login.housepage_click()

    house = HousePage(driver)

    house.phone_type_click()

    # 点击诺基亚
    goodspage = GoodsPage(driver)
    goodspage.nokia_n85_click()

    #点击立即购买
    buynow=BuyNow(driver)
    buynow.buy_now_click()
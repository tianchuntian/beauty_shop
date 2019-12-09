from common.base import Base, open_browser
from page.buynow import BuyNow
from page.goodspage import GoodsPage
from page.housepage import HousePage
from page.loginpage import LoginPage, url


class Account(Base):
    "封装商品加入购物车后去支付页面"
    go_account_loc=("css selector","img[src='themes/default/images/checkout.gif']")

    def go_account_click(self):
        "点击去支付按钮"
        self.click(self.go_account_loc)

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

    # 点击立即购买
    buynow = BuyNow(driver)
    buynow.buy_now_click()

    #点击去付款
    account=Account(driver)
    account.go_account_click()
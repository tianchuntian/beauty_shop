import random
import time
from common.base import Base, open_browser
from page.accountpage import Account
from page.addrpage import AddrPage
from page.buynow import BuyNow
from page.goodspage import GoodsPage
from page.housepage import HousePage
from page.loginpage import LoginPage, url


class SubmitOrder(Base):
    "封装提交订单页面"
    #选择运送方式的表单定位
    paths_distribution = ('xpath', '//table[@id="shippingTable"]/tbody/tr/td/input[@type="radio"]')
    #选择支付方式的表单定位
    path_pay="table#paymentTable>tbody>tr>td>input"
    #选择包装方式表单定位
    path_goods_package="table#packTable>tbody>tr>td>input"
    #选择祝福卡表单定位
    path_wish_card="table#cardTable>tbody>tr>td>input"
    #提交订单按钮定位器
    submit_order_loc=("css selector","input[src='themes/default/images/bnt_subOrder.gif']")#提交订单按钮定位器

    shipping_loc=("name","shipping")
    payment_loc=("name","payment")
    package_loc=("name","pack")


    def choose_distribution(self):
        "选择配送方式"
        print(len(self.payment_loc))
        self.choose_one_by_index(self.shipping_loc)
    def choose_pay(self):
        "选择支付方式"
        self.choose_one_by_index(self.payment_loc)
    def choose_package(self):
        "选择商品包装"
        self.choose_one_by_index(self.path_goods_package)


    def choose_wish_card(self):
        self.choose_one_by_index(self.path_wish_card)

    def submit_order_click(self):
        self.click(self.submit_order_loc)
        # return 1

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

    # 点击去付款
    account = Account(driver)
    account.go_account_click()


    # 点击提交订单
    submitorder = SubmitOrder(driver)
    time.sleep(2)
    submitorder.choose_distribution()
    print("*" * 10)

    submitorder.choose_pay()
    time.sleep(2)
    # submitorder.choose_package()
    time.sleep(2)
    # submitorder.choose_wish_card()
    time.sleep(2)
    a = submitorder.submit_order_click()
"""
if __name__ == '__main__':
    driver = open_broswer()
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

    # 点击去付款
    account = Account(driver)
    account.go_account_click()

    # # 输入送货地址信息并点击配送至这个地址
    # addrpage = AddrPage(driver)
    # addrpage.click_china()
    # time.sleep(1)
    # print("*" * 10)
    # addrpage.click_province()
    # time.sleep(1)
    # print("*" * 10)
    # addrpage.click_city()
    # time.sleep(1)
    # addrpage.click_district()
    # name = '诸葛亮_1'
    # addrpage.input_consigneename(name)
    # detail_addr = '南阳'
    # addrpage.input_detail_addr(detail_addr)
    # tel = 12345
    # addrpage.input_tel(tel)
    # email = '123@163.com'
    # addrpage.input_email(email)
    # zipcode = '6655'
    # addrpage.input_zipcode(zipcode)
    # mobile = '15523445666'
    # addrpage.input_mobile(mobile)
    # addrpage.addr_submit()

    #点击提交订单
    submitorder=SubmitOrder(driver)
    time.sleep(2)
    submitorder.choose_distribution()
    print("*"*10)
    time.sleep(2)
    submitorder.choose_pay()
    time.sleep(2)
    submitorder.choose_package()
    time.sleep(2)
    submitorder.choose_wish_card()
    time.sleep(2)
    submitorder.submit_order_click()
    time.sleep(2)
"""
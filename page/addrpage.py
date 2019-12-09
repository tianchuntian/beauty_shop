import time
from common.base import Base,open_browser
from page.accountpage import Account
from page.buynow import BuyNow
from page.goodspage import GoodsPage
from page.housepage import HousePage
from page.loginpage import LoginPage, url


class AddrPage(Base):
    "封装第一次购买商品时要求填写收货信息页面"

    # 国家定位器
    country_loc=("name","country")
    # 中国定位器
    china_loc=("xpath","// *[ @ id = 'selCountries_0'] / option[2]")
    # 下拉框省的定位器
    province_loc=("id","selProvinces_0")
    # 市下拉框定位器
    city_loc=("name","city")
    # 区下拉框定位器
    district_loc=("name","district")
    # 收货人输入框定位器
    consignee_loc=("name","consignee")
    # 详细地址输入框定位器
    detail_addr_loc=("name","address")
    # 电话输入框定位器
    tel_loc=("name","tel")
    # 邮箱输入框定位器
    email_loc=("name","email")
    # 邮政编码输入框定位器
    zipcode_loc=("name","zipcode")
    # 手机输入框定位器
    mobile_loc=("name","mobile")
    # 配送至这个地址按钮定位器
    addr_submit_loc=("class name","bnt_blue_2")
    # 定位省下拉框中的选项
    province_options_loc=("css selector","select[name='province']>option")
    # 定位市下拉框里面的元素
    city_optins_loc=("css selector","select[name='city']>option")
    # 定位市下拉框里面的元素
    district_optins_loc=("css selector","select[name='district']>option")


    def click_china(self):
    #定位选择中国"
        self.click(self.china_loc)
    #选择省份
    def click_province(self):
       self.select_by_index(self.province_loc,self.province_options_loc)
    #选择城市
    def click_city(self):
        self.select_by_index(self.city_loc,self.city_optins_loc)
    # "选择区"
    def click_district(self):      
        self.select_by_index(self.district_loc,self.district_optins_loc)
    #输入收货人
    def input_consigneename(self,name):
        self.send_keys(self.consignee_loc,name)
    #输入详细地址
    def input_detail_addr(self,addr):
        self.send_keys(self.detail_addr_loc,addr)
    #输入电话
    def input_tel(self,tel):
        self.send_keys(self.tel_loc,tel)
    #输入邮箱
    def input_email(self,email):
        self.send_keys(self.email_loc,email)
    #输入邮政编码
    def input_zipcode(self,zipcode):
        self.send_keys(self.zipcode_loc,zipcode)
    #输入手机
    def input_mobile(self,mobile):
        self.send_keys(self.mobile_loc,mobile)
    #点击送货按钮
    def addr_submit(self):
        self.click(self.addr_submit_loc)

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

    #输入送货地址信息并点击配送至这个地址
    addrpage=AddrPage(driver)
    addrpage.click_china()
    time.sleep(1)
    print("*"*10)
    addrpage.click_province()
    time.sleep(1)
    print("*" * 10)
    addrpage.click_city()
    time.sleep(1)
    addrpage.click_district()
    name='诸葛亮_1'
    addrpage.input_consigneename(name)
    detail_addr='南阳'
    addrpage.input_detail_addr(detail_addr)
    tel=12345
    addrpage.input_tel(tel)
    email='123@163.com'
    addrpage.input_email(email)
    zipcode='6655'
    addrpage.input_zipcode(zipcode)
    mobile='15523445666'
    addrpage.input_mobile(mobile)
    addrpage.addr_submit()

    
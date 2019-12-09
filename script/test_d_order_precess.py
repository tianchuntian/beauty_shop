'''"下单
	      下单 流程"	田建立
'''
import unittest
from common.base import open_browser
from page.accountpage import Account
from page.buynow import BuyNow
from page.goodspage import GoodsPage
from page.loginpage import LoginPage,url
from page.addrpage import AddrPage
from page.submit_orderpage import SubmitOrder
import ddt
import time
from page.housepage import HousePage
from common.operation_Excel import OperationExcel
from page.successpage import SuccessPage

url1=r'http://172.16.1.229/ecshop/user.php'

#准备数据
file_path='./data/项目.xls'
oper=OperationExcel(file_path)
test_data=oper.get_data_info()


#编写测试类
@ddt.ddt
class TestOrderPrecess(unittest.TestCase):
    # @ddt.data(*test_data)
    def setUp(self) -> None:
        self.driver = open_browser()
        self.login = LoginPage(self.driver)
        self.login.open_url(url1)

    def tearDown(self) -> None:
        self.login.close()

    @ddt.data(*test_data)
    def test_case01(self,data):
        self.login.input_username(data['username'])
        self.login.input_password(data['password'])
        self.login.submit_click()
        # print(self.login.is_successed(data['username']))
        self.login.housepage_click()

        house = HousePage(self.driver)

        house.phone_type_click()


        # 点击诺基亚
        goodspage = GoodsPage(self.driver)
        goodspage.nokia_n85_click()
        time.sleep(1)
        # 点击立即购买
        buynow = BuyNow(self.driver)
        buynow.buy_now_click()
        time.sleep(1)
        # 点击去付款
        account = Account(self.driver)
        account.go_account_click()
        time.sleep(1)

        #填写收货信息
        # addrpage = AddrPage(self.driver)
        # addrpage.click_china()  # 选择中国
        # addrpage.click_province()  # 随即选择省份
        # time.sleep(1)
        # addrpage.click_city()  # 随即选择市
        # time.sleep(1)
        # addrpage.click_district()  # 随即选择区
        # time.sleep(1)
        # addrpage.input_consigneename(data['consigneename'])  # 从excel中读取收货人并输入
        # time.sleep(1)
        # addrpage.input_detail_addr(data['detailaddr'])  # 从excel中读取详细地址并输入
        # time.sleep(1)
        # addrpage.input_tel(str(data['tel']))  # 从excel中读取手机并输入
        # time.sleep(1)
        # addrpage.input_email(str(data['email']))  # 从excel中读取邮箱并输入
        # time.sleep(1)
        # print("*"*10)
        # addrpage.input_zipcode(str(data['zipcode']))  # 从excel中读取邮政编码并输入
        # time.sleep(1)
        # addrpage.input_mobile(str(data['mobile']))  # 从excel中读取电话并输入
        # time.sleep(1)
        # addrpage.addr_submit()  # 点击点击配送至这个地址按钮

        submitorder = SubmitOrder(self.driver)
        time.sleep(2)
        submitorder.choose_distribution()


        submitorder.choose_pay()
        time.sleep(2)
        js = 'window.scrollTo(0,1000)'
        self.driver.execute_script(js)

        a=submitorder.submit_order_click()
        # print(a)
        #断言
        successpage=SuccessPage(self.driver)
        result=successpage.is_success(data['text'])
        self.assertEqual(data['expect'],result,msg='中奖啦')



        

if __name__ == '__main__':
    unittest.main()
'''"个人中心-收货地址
			增删改查"	郭仁捷
'''
from common.base import open_browser
from page.address_page import AddressPage
import unittest,ddt
from common.operation_Excel import OperationExcel
filename = "./data/add_address.xlsx"
OE = OperationExcel(filename)
test_data = OE.get_data_info()


@ddt.ddt
class TestAddReceivingAddress(unittest.TestCase):
    def setUp(self) -> None:
        # 打开浏览器到添加收货地址界面
        # 创建对象
        driver = open_browser()
        self.login = AddressPage(driver)
        # 准备数据,进入到添加收货地址界面
        url = "http://172.16.1.224/ecshop/"
        self.login.open_url(url)
        self.login.login_address("grj123456","grj123456")
        # 得到最后一个数据的索引,就可以进行添加操作了
        self.a = self.login.a_number()
        self.login.performance(self.a)

    def tearDown(self) -> None:
        # 关闭浏览器
        self.login.close()

    @ddt.data(*test_data)
    def test_add_receiving_address(self,data):
        """测试用例,添加收货地址"""
        # 1.选择国家
        self.login.select_country(data["country"])
        # 2.选择省份
        self.login.select_province(data["province"])
        # 3.选择城市
        self.login.select_city(data["city"])
        # 4.选择区域
        if data["district"] != "None" :
            self.login.select_district(data["district"])
        # 5.输入收货人姓名
        self.login.input_consignee(data["consignee"])
        # 6.输入邮箱
        if data["email"] != "None" :
            self.login.input_email(data["email"])
        # 7.输入详细地址
        self.login.input_address(data["address"])
        # 8.输入邮政编码
        if data["zipcode"] != "None" :
            self.login.input_zipcode(str(data["zipcode"]))
        # 9.输入电话
        if data["tel"] != "None" :
            self.login.input_tel(str(data["tel"]))
        # 10.输入手机
        if data["mobile"] != "None":
            self.login.input_mobile(str(data["mobile"]))
        # 11.点击添加
        self.login.click_submit()
        # 12.隐式等待,找到对应的数据
        self.login.driver.implicitly_wait(5)
        # 13.断言,判断用例是否执行成功
        result = self.login.is_add_success(self.a)
        self.assertEqual(result,data["expect"])

if __name__ == '__main__':
    unittest.main()
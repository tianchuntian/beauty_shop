'''"个人中心-收货地址
			增删改查"	郭仁捷
'''
from common.base import open_browser
from page.address_page import AddressPage
import unittest,ddt
from common.operation_Excel import OperationExcel
filename = "./data/modify_address.xlsx"
OE = OperationExcel(filename)
test_data = OE.get_data_info()

@ddt.ddt
class TestModifyReceivingAddress(unittest.TestCase) :
    def setUp(self) -> None:
        # 打开浏览器到添加收货地址界面
        # 创建对象
        driver = open_browser()
        self.login = AddressPage(driver)
        # 准备数据,进入到添加收货地址界面
        url = "http://172.16.1.224/ecshop/"
        self.login.open_url(url)
        self.login.login_address("grj123456","grj123456")
    def tearDown(self) -> None:
        # 关闭浏览器
        self.login.close()
    @ddt.data(*test_data)
    def test_modify_receiving_address(self,data):
        """测试用例,修改地址"""
        # 1.获取输入的id,然后根据id来进行定位要修改的地址
        b = self.login.a_number()
        a = data["id"]-1
        if a < b :
            self.login.performance(a)
        else :
            print("需要修改的地址编号不存在")
            return False
        # 2.修改国家
        if data["country"] != "None" :
            self.login.select_country(data["country"])
        # 3.修改省份
        if data["province"] != "None" :
            self.login.select_province(data["province"])
        # 4.修改城市
        if data["city"] != "None" :
            self.login.select_city(data["city"])
        # 5.修改区域
        if data["district"] != "None" :
            self.login.select_district(data["district"])
        # 6.输入新收货人姓名
        if data["consignee"] != "None":
            self.login.input_consignee(data["consignee"])
        # 7.输入新邮箱
        if data["email"] != "None" :
            self.login.input_email(data["email"])
        # 8.输入新详细地址
        if data["address"] != "None":
            self.login.input_address(data["address"])
        # 9.输入新邮政编码
        if data["zipcode"] != "None" :
            self.login.input_zipcode(str(data["zipcode"]))
        # 10.输入新电话
        if data["tel"] != "None" :
            self.login.input_tel(str(data["tel"]))
        # 11.输入新手机
        if data["mobile"] != "None":
            self.login.input_mobile(str(data["mobile"]))
        # 12.点击修改按钮
        self.login.click_modify()
        # 13.断言
        # 隐式等待
        self.login.driver.implicitly_wait(5)
        # 开始判断value值是否一致,一致就断言成功
        result = self.login.is_modify_success(data)
        self.assertEqual(result,data["expect"])

if __name__ == '__main__':
    unittest.main()
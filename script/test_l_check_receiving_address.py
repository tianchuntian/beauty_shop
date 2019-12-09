'''"个人中心-收货地址
			增删改查"	郭仁捷
'''
from common.base import open_browser
from page.address_page import AddressPage
import unittest,ddt

from common.operation_Excel import OperationExcel
filename = "./data/check_address.xlsx"
OE = OperationExcel(filename)
test_data = OE.get_data_info()

@ddt.ddt
class TestCheckReceivingAddress(unittest.TestCase) :
    def setUp(self) -> None:
        # 打开浏览器到添加收货地址界面
        # 创建对象
        driver=open_browser()
        self.login = AddressPage(driver)
        # 准备数据,进入到添加收货地址界面
        url = "http://172.16.1.224/ecshop/"
        self.login.open_url(url)
        self.login.login_address("grj123456","grj123456")
    def tearDown(self) -> None:
        # 关闭浏览器
        self.login.close()
    @ddt.data(*test_data)
    def test_check_receiving_address(self,data):
        """测试用例,查询操作"""
        # 1.获取输入的id,然后根据id来进行定位要修改的地址
        b = self.login.a_number()
        a = data["id"]-1
        if a < b :
            self.login.performance(a)
            self.login.driver.get_screenshot_as_file("./report/chrome.png")
        else :
            print("需要修改的地址编号不存在")
            return False
        # 断言,查看的姓名是否和原本的value值一样
        result = self.login.is_ckeck_success(data["consignee"])
        self.assertEqual(result,data["expect"])

if __name__ == '__main__':
    unittest.main()

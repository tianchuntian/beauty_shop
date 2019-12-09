'''"个人中心-收货地址
			增删改查"	郭仁捷
'''
from common.base import open_browser
from page.address_page import AddressPage
import unittest,ddt
from common.operation_Excel import OperationExcel
filename = "./data/delete_address.xlsx"
OE = OperationExcel(filename)
test_data = OE.get_data_info()

@ddt.ddt
class TestDeleteReceivingAddress(unittest.TestCase) :
    i = 1
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
    def test_delete_receiving_address(self,data):
        """测试用例,删除地址"""
        # 1.获取输入的id,然后根据id来进行定位要修改的地址
        b = self.login.a_number()
        a = data["id"]-self.i
        self.i += 1
        if a < b :
            self.login.performance(a)
        else :
            print("需要修改的地址编号不存在")
            return False
        # 1.根据得到的a值,可以定位到删除按钮,点击删除
        self.login.click_delete()
        # 2.跳出弹框,获取弹窗
        alert = self.login.driver.switch_to.alert
        # 3.点击弹框确认按钮
        alert.accept()
        # 刷新窗口
        self.login.driver.refresh()
        # 2.隐式等待,找到对应的数据
        self.login.driver.implicitly_wait(5)
        # 3.断言,判断用例是否执行成功
        result = self.login.is_delete_success(b)
        self.assertEqual(result,data["expect"])

if __name__ == '__main__':
    unittest.main()
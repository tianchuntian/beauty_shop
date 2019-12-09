''''
   "登录 --参数化
注册 --生成测试数据 成功的写入Exel"	刘卓涵


'''
from common.base import open_browser
from page.login_page import Login
import unittest,ddt
from common.operation_Excel import OperationExcel
import time



oper=OperationExcel("./data/login_data.xls")
test_data=oper.get_data_info()

url="http://172.16.1.229/ecshop/user.php"

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        # 用例前置条件
        driver=open_browser()
        self.login=Login(driver)
        self.login.open_url(url)
    def tearDown(self) -> None:
        # 关闭浏览器
        self.login.close()
    @ddt.data(*test_data)
    def test_login1(self, data):
        """测试保存信息登录"""
        # 输入用户名
        self.login.input_username(data['username'])
        # 输入密码
        self.login.input_password(str(data['password']))
        # 点击保存信息
        self.login.click_baocun()
        # 点击注册
        self.login.click_register()
        result = self.login.is_successed(data["username"])

        self.assertEqual(result, data["expect"], msg="断言失败")


if __name__ == '__main__':
    unittest.main()


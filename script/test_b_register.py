'''   "登录 --参数化
注册 --生成测试数据 成功的写入Exel"	刘卓涵
'''
from common.base import open_browser
from page.register_page import Register
import unittest,ddt
from common.operation_Excel import OperationExcel
import time
oper=OperationExcel("./data/register_data.xls")
test_data=oper.get_data_info()
url="http://172.16.1.229/ecshop/user.php?act=register"

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        # 用例前置条件
        driver=open_browser('firefox')
        self.register=Register(driver)
        self.register.open_url(url)
    def tearDown(self) -> None:
        # 关闭浏览器
        self.register.close()
    @ddt.data(*test_data)
    def test_register(self,data):
        """测试"""
        #输入用户名
        self.register.input_username(data['username'])
        #输入密码
        self.register.input_password(data['password'])
        #输入邮箱
        self.register.input_email(data['email'])
        #再次输入密码确认密码
        self.register.input_password2(data['password2'])
        #输入qq号码
        self.register.input_qq(str(data['qq']))
        #输入办公室电话
        self.register.input_companytel(str(data['companytel']))
        #输入家庭电话
        self.register.input_hometel(str(data['hometel']))
        #输入手机号码
        self.register.input_phone(int(data['phone']))
        #选择密码问题
        time.sleep(2)
        self.register.click_question(int(data['favorite_movie']))
        time.sleep(2)
        #输入密码问题
        self.register.input_question(str(data['questions']))
        #点击注册
        self.register.click_rigister()
        result = self.register.is_successed(data["username"])

        self.assertEqual(result, data["expect"], msg="断言失败")

if __name__ == '__main__':
    unittest.main()
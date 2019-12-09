from common.base import Base,open_browser
import time

url="http://172.16.1.229/ecshop/user.php"
class Login(Base):
    """封装表现层:制作定位器"""
    #账号
    username_loc=("name","username")
    password_loc=("name","password")
    baocun_loc=("name","remember")
    register_loc=('name','submit')
    result_loc = ("class name", "f4_b")

    """封装操作层"""
    def input_username(self,username):
        """
        输入用户名
        :param username:
        :return:
        """
        self.send_keys(self.username_loc,username)
    def input_password(self,password):
        """
        输入密码
        :param password:
        :return:
        """
        self.send_keys(self.password_loc,password)
    def click_register(self):
        """
        点击确认注册
        :param rigister:
        :return:
        """
        self.click(self.register_loc)
    def click_baocun(self):
        self.click(self.baocun_loc)
    def is_successed(self,text):
        "判断是否登录成功"
        result=self.is_text_in_element(self.result_loc,text)
        return result


if __name__=='__main__':
    driver = open_browser()
    login = Login(driver)
    login.open_url(url)
    username = "吕布_13"
    password = "123456"
    login.input_username(username)
    login.input_password(password)
    login.click_baocun()
    login.click_register()
    time.sleep(2)
    driver.quit()



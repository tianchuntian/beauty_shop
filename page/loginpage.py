#封装登录页面的表现层 和操作层
from common.base import Base,open_browser
url="http://172.16.1.229/ecshop/user.php"

class LoginPage(Base):
    # 封装登陆页面元素,制作定位器
    username_loc = ("name", "username")
    password_loc = ("name", "password")
    rememeber_loc = ("name", "remember")
    submit_loc = ("name", "submit")
    question_password_loc = ("link text", "user.php?act=qpassword_name")
    email_loc = ("link text", "user.php?act=get_password")
    msg_loc = ("link text", "user.php?act=sms_get_password")
    register_loc = ("link text", "user.php?act=register")
    result_loc = ("class name", "f4_b")
    housepage_loc=("class name","cur")

    #封装操作层
    def input_username(self,username):
        "输入用户名"
        self.send_keys(self.username_loc,username)
    def input_password(self,password):
        "输入密码"
        self.send_keys(self.password_loc,password)
    def submit_click(self):
        "点击登陆按钮"
        self.click(self.submit_loc)
    def is_successed(self,text):
        "判断是否登录成功"
        result=self.is_text_in_element(self.result_loc,text)
        return result
    def housepage_click(self):
        "点击首页按钮"
        self.click(self.housepage_loc)



if __name__ == '__main__':
      driver=open_browser()
      login=LoginPage(driver)
      login.open_url(url)
      username='诸葛亮_2'
      password='Test123456'
      login.input_username(username)
      login.input_password(password)
      login.submit_click()
      print(login.is_successed(username))
      login.housepage_click()
      # login.close()

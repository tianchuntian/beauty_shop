from common.base import Base,open_browser
import time

url="http://172.16.1.229/ecshop/user.php?act=register"
class Register(Base):
    """封装表现层:制作定位器"""
    #账号
    username_loc=("name","username")
    #邮箱
    email_loc=("name","email")
    #密码
    password_loc=("name","password")
    #确认密码
    confirm_password_loc=("name","confirm_password")
    #QQ账号
    qq_loc=("name","extend_field2")
    #办公室电话
    companytel_loc=("name","extend_field3")
    #家庭电话
    hometel_loc=("name","extend_field4")
    #手机号码
    phone_loc=("name","extend_field5")
    #选择问题
    question_loc=("name","sel_question")

    questionda_loc=("name","passwd_answer")
    # 下拉框 的定位

    result_loc = ("class name", "f4_b")

    #确认注册
    rigister_loc=("xpath","/html/body/div[6]/div/form/table/tbody/tr[15]/td[2]/input[3]")
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
    def input_email(self,email):
        """
        输入邮箱
        :param email:
        :return:
        """
        self.send_keys(self.email_loc,email)
    def input_password2(self,confirm_password):
        """
        确认密码
        :param password:
        :return:
        """
        self.send_keys(self.confirm_password_loc,confirm_password)
    def input_qq(self,qq):
        """
        输入qq号码
        :param qq:
        :return:
        """
        self.send_keys(self.qq_loc,qq)
    def input_companytel(self,companytel):
        """
        输入办公室电话
        :param companytel:
        :return:
        """
        self.send_keys(self.companytel_loc,companytel)
    def input_hometel(self,hometel):
        """
        输入家庭电话
        :param hometel:
        :return:
        """
        self.send_keys(self.hometel_loc,hometel)
    def input_phone(self,phone):
        """
        输入手机号
        :param phone:
        :return:
        """
        self.send_keys(self.phone_loc,phone)

    #选择问题
    def click_question(self, index):
        self.selector_by_index(self.question_loc, index)

    # 输入密码提示问题答案
    def input_question(self,text):
        self.send_keys(self.questionda_loc,text)

    # 点击 登录
    def click_rigister(self):
        self.click(self.rigister_loc)

    def is_successed(self,text):
        "判断是否登录成功"
        result=self.is_text_in_element(self.result_loc,text)
        return result





if __name__=='__main__':
    driver=open_browser()
    regisiter=Register(driver)
    regisiter.open_url(url)
    username="吕布_03"
    password="123456"
    email="734388693@qq.com"
    password2="123456"
    qq="734388690"
    companytel="2658528"
    hometel="4534758"
    phone="123456"
    questions="hello the world"
    regisiter.input_username(username)
    regisiter.input_password(password)
    regisiter.input_email(email)
    regisiter.input_password2(password2)
    regisiter.input_qq(qq)
    regisiter.input_companytel(companytel)
    regisiter.input_hometel(hometel)
    regisiter.input_phone(phone)
    time.sleep(1)
    regisiter.click_question(3)
    time.sleep(1)
    regisiter.input_question(questions)
    regisiter.click_rigister()
    time.sleep(3)
    regisiter.close()
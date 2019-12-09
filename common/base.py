'''
common文件夹--放置公共方法--专人维护管理
			base.py --对selenium二次封装
			1打开浏览器
			2输入网址
			3元素定位
			4元素操作
				1点击
				2输入
				3判断类型方法
				4其他的公共方法
					1读取Excel表
'''
import random
import time
from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

#打开浏览器
def open_browser(browser='chrome'):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox()
    elif browser=='ie':
        driver=webdriver.Ie()
    else:
        driver=None
        print('请输入正确的浏览器')
    return driver

class Base:
    # 初始化driver
    def __init__(self,driver):
        self.driver=driver
    #打开浏览器 url
    def open_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
    #定位单个元素,如果定位成功返回元素本身,如果失败,返回False
    def find_element(self,locator,timeout=10):
        '''
        :param locator:  定位器    ("id","id属性值")
        :param timeout:  时间
        :return:
        '''
        try:
            element=WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f"{locator}元素没找到")
            return False



    #复数
    def find_elements(self, locator, timeout=10):
        '''
        :param locator:  定位器    ("id","id属性值")
        :param timeout:  时间
        :return:
        '''
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return elements
        except:
            print(f"{locator}元素没找到")
            return False

    #点击元素
    def click(self,locator,timeout=2):
        element=self.find_element(locator,timeout)
        element.click()

     #元素输入
    def send_keys(self,locator,text,timeout=2):
        element=self.find_element(locator,timeout)
        try:
            element.clear()
            element.send_keys(text)
        except:
            pass
    #关闭浏览器
    def close(self):
        self.driver.quit()

    # 判断文本是否存在于元素中, 如果存在返回True, 不存在返回False
    # def is_text_in_element(self,locator,text,timeout=5):
    #     try:
    #         result=WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element(locator,text))
    #         return result
    #     except:
    #         print("元素未找到或文本不存在")
    #         return False

    #切换iframe
    def switch_to_frame(self, locator):
        element = self.find_element(locator)
        self.driver.switch_to.frame(element)

    # 切换回父级iframe
    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    # 通过id和name属性进入frame 里面
    def to_frame(self, id_or_name):
        try:
            self.driver.switch_to.frame(id_or_name)
        except:
            print(f'元素未找到 -> {id_or_name}')

    # 通过定位器进入frame
    def to_frame_A(self, locator):

        try:
            element = self.find_element(locator)
            self.driver.switch_to.frame(element)
        except:
            print(f'元素未找到 -> {locator}')

        #返回最外层frame
    def exit_to_default_frame(self):
        self.driver.switch_to.default_content()

    # 单个元素点击操作
    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        try:
            element.click()
        except:
            pass

    # 下拉框通过索引选择元素
    def selector_by_index(self,locator,index):
        selector=Select(self.find_element(locator))
        try:
            selector.select_by_index(index)
        except:
            print("下拉框元素未找到")




    # 郭仁捷-------------------------------------------------------
    def is_text_in_element(self,locator,text,maxtime=10):
        """
        确认文本是否在元素中
        :return:
        """
        try :
            result = WebDriverWait(self.driver,maxtime).until(EC.text_to_be_present_in_element(locator,text))
            self.driver.get_screenshot_as_file("../report/chrome.png")
            return result
        except :
            print("元素或文本不存在")
            return False
    def is_value_in_element(self,locator,value,maxtime=10):
        """
        确认value值是否在元素中
        :return:
        """
        try :
                result = WebDriverWait(self.driver,maxtime).until(EC.text_to_be_present_in_element_value(locator,value))
                self.driver.get_screenshot_as_file("../report/chrome.png")
                return result
        except :
                print("元素或文本不存在")
                return False
    def select(self,locator,text):
        """
        下拉框选择
        :return:
        """
        select = self.find_element(locator)
        # 实例化下拉框
        select = Select(select)
        # 选择相应的内容(用文本的方式)
        select.select_by_visible_text(text)
    def is_number_to_update(self,a,b):
        """
        判断地址个数是否更新,a表示没添加之前的数量,b表示添加后的数量
        :return:
        """
        return a == b
    #聚焦
    def scroll_element(self, locator):
        # 定位目标元素
        target = self.find_element(locator)
        # js代码
        js = 'arguments[0].scrollIntoView()'
        # 执行js代码
        self.driver.execute_script(js, target)



        # 田建立----------------------------------------------------------------------------------
    def select_by_index(self, locator, locators):
        "下拉框中随即选择一个选项"
        element = self.find_element(locator)  # 这是定位下拉框
        elements = self.find_elements(locators)  # 这是定位下拉框里面的同级别元素
        index = random.randint(1, len(elements) - 1)
        Select(element).select_by_index(index)

    def choose_one_by_index(self, locator):
        # 在表单中随机选择一个选项
        elements = self.find_elements(locator)
        index = random.randint(1, len(elements) - 1)
        if elements[index].is_selected():
            pass
        else:
            elements[index].click()
        pass

    def get_attribute_text(self, locator):
        # 在元素中获取元素的文本
        element = self.find_element(locator)
        element.text()

    def no_password_login(self):
        # 免密登录
        # 个人资料路径
        user_data_dir = r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"
        # 加载配置数据
        option = webdriver.ChromeOptions()
        option.add_argument(user_data_dir)
        # 将加载项配置到启动浏览器中
        driver = webdriver.Chrome(chrome_options=option)

    def is_text_in_elemen(self, locator, text, timeout=5):
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            # print(result)
            return result
        except:
            print("元素未找到")
            return False


    #汪李--------------------------------------------------
    # 定义浏览器返回
    def back(self):
        self.driver.back()

    # 定义操作下拉菜单
    def select_option(self, locator, index):
        '''
        下拉框操作
        :param locator: 下拉框元素定位器
        :param index: 选项索引
        :return:
        '''
        # 定位选项元素
        element = self.find_element(locator)
        # 选项实例化
        select = Select(element)
        # 根据索引选择选项
        select.select_by_index(index)
    #--------------------------------------------------------------------------------------
    #李仁杰
    def confirm_alert(self):
        """
        点击弹窗
        :return:
        """
        # 获取弹窗(进入弹窗)
        alert = self.driver.switch_to.alert
        # 点击弹窗确定按钮
        alert.accept()


if __name__ == '__main__':
    driver = open_browser()
    base = Base(driver)
    base.open_url("http://172.16.1.229/ecshop/admin")
    username_loc = ('name', 'username')  # 用户名输入框
    password_loc = ('name', 'password')  # 密码输入框
    submit_loc = ('class name', 'us_Submit')  # 立即登录按钮
    username = 'xiaobai2'
    password = 'aa123456'
    base.send_keys(username_loc,username)  # 输入用户名
    base.send_keys(password_loc,password)  # 输入密码
    base.click(submit_loc) # 点击登录
    time.sleep(2)
    driver.quit()
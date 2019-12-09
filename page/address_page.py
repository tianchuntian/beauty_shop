from common.base import Base


class AddressPage(Base) :
    # 登录需要用到的
    home_loc = ("link text", "首页")  # 定位首页
    username_loc = ("name", "username")  # 定位用户名输入框
    password_loc = ("name", "password")  # 定位密码输入框
    login_loc = ("class name", "us_Submit")  # 定位登录按钮
    usercore_loc = ("link text", "用户中心")  # 定位用户中心
    img_loc = ("css selector", "img[src='themes/default/images/u4.gif']")  # 定位收货地址
    def performance(self,a):
        # 封装表现层
        self.country_loc = ("id",f"selCountries_{a}")                        # 定位下拉框国家
        self.province_loc = ("id",f"selProvinces_{a}")                       # 定位下拉框省份
        self.city_loc = ("id",f"selCities_{a}")                              # 定位省份
        self.district_loc = ("id",f"selDistricts_{a}")                       # 定位区
        self.consignee_loc = ("id",f"consignee_{a}")                         # 定位收货人姓名
        self.email_loc = ("id",f"email_{a}")                                 # 定位邮箱
        self.address_loc = ("id",f"address_{a}")                             # 定位地址
        self.zipcode_loc = ("id",f"zipcode_{a}")                             # 定位邮政编码
        self.tel_loc = ("id",f"tel_{a}")                                     # 定位电话
        self.mobile_loc = ("id",f"mobile_{a}")                               # 定位手机
        self.take_over_ddress_loc = ("class name",f"bnt_blue_2")           # 定位新增收货地址按钮
        self.modify_loc = ("xpath",f"/html/body/div[6]/div[2]/div/div/div/form[{a+1}]/table/tbody/tr[5]/td[2]/input[1]")      # 修改
        self.delete_loc = ("xpath",f"/html/body/div[6]/div[2]/div/div/div/form[{a+1}]/table/tbody/tr[5]/td[2]/input[2]")      # 删除
        self.add_result_loc = ("xpath",f"/html/body/div[6]/div[2]/div/div/div/form[{a+2}]/table/tbody/tr[5]/td[2]/input[1]")      # 判断添加是否更新成功

    # 封装操作层
    def select_country(self,country):
        """
        选择国家
        :return:
        """
        self.select(self.country_loc,country)
    def select_province(self,province):
        """
        选择身份
        :return:
        """
        self.select(self.province_loc,province)
    def select_city(self,city):
        """
        选择城市
        :return:
        """
        self.select(self.city_loc,city)
    def select_district(self,district):
        """
        选择区域
        :return:
        """
        self.select(self.district_loc,district)
    def input_consignee(self,consignee):
        """
        输入收货人姓名
        :return:
        """
        self.send_keys(self.consignee_loc,consignee)
    def input_email(self,email="1150387367@qq.com"):
        """
        输入邮箱
        :return:
        """
        self.send_keys(self.email_loc,email)
    def input_address(self,address):
        """
        输入详细地址
        :return:
        """
        self.send_keys(self.address_loc,address)
    def input_zipcode(self,zipcode=None):
        """
        输入邮政编码
        :return:
        """
        self.send_keys(self.zipcode_loc,zipcode)
    def input_tel(self,tel=None):
        """
        输入电话
        :return:
        """
        self.send_keys(self.tel_loc,tel)
    def input_mobile(self,mobile=None):
        """
        输入手机号
        :return:
        """
        self.send_keys(self.mobile_loc,mobile)
    def click_submit(self):
        """
        点击新增收货地址
        :return:
        """
        self.click(self.take_over_ddress_loc)
    def click_modify(self):
        """
        点击修改收货地址
        :return:
        """
        self.click(self.modify_loc)
    def click_delete(self):
        """
        点击删除收货地址
        :return:
        """
        self.click(self.delete_loc)
    def login_address(self,username,password):
        """
        直接登录添加收货地址界面
        :return:
        """
        # 进入ecshop
        url = "http://172.16.1.224/ecshop/user.php"
        self.driver.get(url)
        # 输入用户名
        self.send_keys(self.username_loc,username)
        # 输入密码
        self.send_keys(self.password_loc,password)
        # 点击登录
        self.click(self.login_loc)
        # 点击用户中心
        # 用隐式等待
        self.driver.implicitly_wait(5)
        self.click(self.usercore_loc)
        # 点击添加收货地址收货
        self.driver.implicitly_wait(5)
        self.click(self.img_loc)
        self.driver.implicitly_wait(5)
    def a_number(self):
        """
        求出a的数量,并减一,得到最后一个添加栏的索引,就可以进行持续添加的操作
        :return:
        """
        a_number_loc = ("name", "country")  # 定位a的数量
        elements = self.find_elements(a_number_loc)
        number = len(elements)-1
        return number
    def add_to_update_number(self):
        """
        获取添加地址后的新的地址数量
        :return:
        """
        try :
            self.driver.implicitly_wait(5)
            self.find_element(self.add_result_loc)
            a_number_loc = ("name", "country")  # 定位显示收货地址的总数量
            elements = self.find_elements(a_number_loc)
            number = len(elements) - 1
            self.driver.get_screenshot_as_file("../report/chrome.png")
            return number
        except :
            print("无法确定收货地址的数量")
            return False
    def delete_to_update_number(self):
        """
        获取删除地址后的新的地址数量
        :return:
        """
        try :
            self.driver.implicitly_wait(5)
            a_number_loc = ("name", "country")  # 定位显示收货地址的总数量
            elements = self.find_elements(a_number_loc)
            number = len(elements) - 1
            self.driver.get_screenshot_as_file("../report/chrome.png")
            return number
        except :
            print("无法确定收货地址的数量")
            return False
    def is_add_success(self,b):
        """
        判断用例是否执行成功,添加操作,b为原收货地址数量,应该加一,才与新地址一样
        :return:
        """
        result = self.is_number_to_update(self.add_to_update_number(),b+1)
        return result
    def is_delete_success(self,b):
        """
        判断用例是否执行成功,删除操作,b为原收货地址数量,应该减一,才与新地址一样
        :return:
        """
        result = self.is_number_to_update(self.delete_to_update_number(),b-1)
        return result
    def is_modify_success(self,data):
        """
        判断是否修改成功
        :return:
        """
        a,b,c,d,e,f,g,h,l,i = (True,True,True,True,True,True,True,True,True,True)
        # 2.修改国家
        if data["country"] != "None" :
            a = self.is_value_in_element(self.country_loc,data["country"])
        # 3.修改省份
        if data["province"] != "None" :
            b = self.is_value_in_element(self.province_loc,data["province"])
        # 4.修改城市
        if data["city"] != "None" :
            c = self.is_value_in_element(self.city_loc,data["city"])
        # 5.修改区域
        if data["district"] != "None" :
            d = self.is_value_in_element(self.district_loc,data["district"])
        # 6.输入新收货人姓名
        if data["consignee"] != "None":
            e = self.is_value_in_element(self.consignee_loc,data["consignee"])
        # 7.输入新邮箱
        if data["email"] != "None" :
            f = self.is_value_in_element(self.email_loc,data["email"])
        # 8.输入新详细地址
        if data["address"] != "None":
            g = self.is_value_in_element(self.address_loc,data["address"])
        # 9.输入新邮政编码
        if data["zipcode"] != "None" :
            h = self.is_value_in_element(self.zipcode_loc,str(data["zipcode"]))
        # 10.输入新电话
        if data["tel"] != "None" :
            l = self.is_value_in_element(self.tel_loc,str(data["tel"]))
        # 11.输入新手机
        if data["mobile"] != "None":
            i = self.is_value_in_element(self.mobile_loc,str(data["mobile"]))
        lists = (a,b,c,d,e,f,g,h,l,i)
        if False in lists :

            return False
        else :
            return True
    def is_ckeck_success(self,consignee):
        """
        判断姓名value值是否与查的一致,一致则成功
        :return:
        """
        result = self.is_value_in_element(self.consignee_loc,consignee)
        return result

if __name__ == '__main__':
    login = AddressPage()
    url = "http://172.16.1.224/ecshop/user.php"
    login.open_url(url)
    # 登录收货地址界面
    login.login_address("grj123456","grj123456")
    # 传入a的值,实现添加收货地址功能
    a = login.a_number()
    login.performance(a)
    # 输入必填项
    country = "中国"
    province = "四川省"
    city = "成都市"
    district = "武侯区"
    consignee = "郭仁捷"
    address = "天府新谷1号楼601号房"
    tel = "123456789"
    login.select_country(country)
    login.select_province(province)
    login.select_city(city)
    login.select_district(district)
    login.input_consignee(consignee)
    login.input_address(address)
    login.input_tel(tel)
    login.click_submit()
    login.close()
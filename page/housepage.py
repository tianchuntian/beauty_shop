from common.base import Base,open_browser
from page.loginpage import LoginPage, url


class HousePage(Base):
    "封装首页页面"
    phone_type_loc=("link text","手机类型")
    home_appliances_loc=("link text","家用电器")
    degital_fashion_loc=("link text","数码时尚")
    hardeware_loc=("link text","智能硬件")
    power_supply_loc=("link text","移动电源")
    phone_loc=("link text","手机")
    charge_card_loc=("link text","充值卡")
    clothing_loc=("link text","服装")
    parets_loc=("link text","配件")

    def phone_type_click(self):
        "点击手机类型方法"
        self.click(self.phone_type_loc)

    def home_appliance_click(self):
        "点击家用电器方法"
        self.click(self.home_appliances_loc)

    def degital_fashion_click(self):
        '点击数码时尚方法'
        self.click(self.degital_fashion_loc)

    def hardware_click(self):
        "点击智能硬件方法"
        self.click(self.hardeware_loc)

    def power_supply_click(self):
        "点击移动电源方法"
        self.click(self.power_supply_loc)

    def phone_click(self):
        "点击手机方法"
        self.click(self.phone_loc)

    def charge_card_click(self):
        "点击充值卡方法"
        self.click(self.charge_card_loc)

    def clothing_click(self):
        "点击服装方法"
        self.click(self.clothing_loc)

    def parets_click(self):
        "点击配件方法"
        self.click(self.parets_loc)





if __name__ == '__main__':
    driver = open_browser()
    login = LoginPage(driver)
    login.open_url(url)
    username = '诸葛亮_2'
    password = 'Test123456'
    login.input_username(username)
    login.input_password(password)
    login.submit_click()
    print(login.is_successed(username))
    login.housepage_click()


    house=HousePage(driver)

    house.phone_type_click()
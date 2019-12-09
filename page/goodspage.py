from common.base import Base, open_browser
from page.housepage import HousePage
from page.loginpage import LoginPage, url

class GoodsPage(Base):
    "封装商品页面"
    #各商品的定位器
    nokia_n85_loc = ("link text", "诺基亚N85")
    nokia_5800_loc=("link text","诺基亚5800...")
    nokia_E66_loc=("link text","诺基亚E66")
    feilipu_loc=("link text","飞利浦9@9v")
    KD876_loc=("link text","KD876.")

    def nokia_n85_click(self):
        "点击诺基亚N85"
        self.click(self.nokia_n85_loc)

    def nokia_5800_click(self):
        "点击诺基亚5800"
        self.click(self.nokia_5800_loc)

    def nokia_E66_click(self):
        self.click(self.nokia_E66_loc)

    def feilipu_click(self):
        self.click(self.feilipu_loc)

    def KD876_click(self):
        self.click(self.KD876_loc)

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

    house = HousePage(driver)

    house.phone_type_click()

    #点击诺基亚
    goodspage=GoodsPage(driver)
    goodspage.nokia_n85_click()
'''"购物车
增删改查"	李仁杰
'''
import unittest
import time
from   page.shopping_cart_page import CartPage,url
from common.base import open_browser


class TestCart(unittest.TestCase):
    def setUp(self) -> None:
        driver=open_browser()
        self.cart=CartPage(driver)
        self.cart.open_url(url)
    def tearDown(self) -> None:
        self.cart.close()

    def test_cat(self):
        """查看购物车商品"""
        #登录至首页
        self.cart.input_username(username="tester")
        self.cart.input_password(password="Tester123")
        self.cart.click_submit()
        #进入主页
        self.cart.click_homepage()
        #添加商品
        #添加随身风扇
        self.cart.cilck_fengshan()
        self.cart.click_goods_confirm()
        #判断购物车是否有随身风扇
        self.cart.is_cat_successed("随身风扇")
        #关闭浏览器
        time.sleep(3)



if __name__ =='__main__':
    unittest.main()



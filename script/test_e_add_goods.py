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

    def test_add(self):
        """正常添加商品到购物车"""
        #登录至首页
        self.cart.input_username(username="tester")
        self.cart.input_password(password="Tester123")
        self.cart.click_submit()
        #进入主页
        self.cart.click_homepage()
        #添加商品
        #添加随身小风扇
        self.cart.cilck_fengshan()
        self.cart.click_goods_confirm()
        self.cart.click_continue_shopping()
        #添加视频相机
        self.cart.click_camera3()
        self.cart.click_goods_confirm()
        self.cart.click_continue_shopping()
        #透明手机套
        self.cart.click_visiontao()
        self.cart.click_goods_confirm()
        self.cart.click_continue_shopping()
        #智能相机
        self.cart.click_camera1()
        self.cart.click_goods_confirm()
        self.cart.click_continue_shopping()
        #平衡车
        self.cart.click_bcar()
        self.cart.click_goods_confirm()
        self.cart.click_continue_shopping()
        #运动相机
        self.cart.click_camera2()
        self.cart.click_goods_confirm()
        self.cart.click_continue_shopping()
        #炫彩保护套
        self.cart.click_colortao()
        self.cart.click_goods_confirm()
        # 判断是否添加商品成功 商品种类数量由0增加为7
        self.cart.is_cartnum_successed('购物车(7)')
        #关闭浏览器
        time.sleep(3)



if __name__ =='__main__':
    unittest.main()



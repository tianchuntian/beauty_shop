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

    def test_editor(self):
        """在购物车中修改商品数量"""
        #登录至首页
        self.cart.input_username(username="tester")
        self.cart.input_password(password="Tester123")
        self.cart.click_submit()
        #进入主页
        self.cart.click_homepage()
        #添加商品
        #添加随身小风扇 库存20
        self.cart.cilck_fengshan()
        self.cart.click_goods_confirm()
        self.cart.click_continue_shopping()
        #添加视频相机   库存20
        self.cart.click_camera3()
        self.cart.click_goods_confirm()
        self.cart.click_continue_shopping()
        #透明手机套     库存1
        self.cart.click_visiontao()
        self.cart.click_goods_confirm()
        self.cart.click_continue_shopping()
        #智能相机       库存20
        self.cart.click_camera1()
        self.cart.click_goods_confirm()
        self.cart.click_continue_shopping()
        #平衡车         库存1
        self.cart.click_bcar()
        self.cart.click_goods_confirm()
        self.cart.click_continue_shopping()
        #运动相机       库存1
        self.cart.click_camera2()
        self.cart.click_goods_confirm()
        self.cart.click_continue_shopping()
        #炫彩保护套     库存1
        self.cart.click_colortao()
        self.cart.click_goods_confirm()
        time.sleep(3)
        """修改商品数量操作"""
        #修改视频商品数量为5
        self.cart.input_camera3_num(num1=5)
        #修改随身风扇数量为13
        self.cart.input_fengshannum_loc(num2=13)
        #点击购物车更新按钮
        self.cart.click_refresh_goods()
        time.sleep(2)
        # 判断是否修改成功 商品种类数量由7增加为23
        self.cart.is_cartnum_successed('购物车(23)')
        #关闭浏览器
        time.sleep(5)

if __name__=='__main__':
    unittest.main()
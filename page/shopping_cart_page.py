"""
shopping_cart_page.py
    1.对登录页面与购物车页面封装
    2.封装页面表现层和操作层
    3.继承base.py中的Base类
"""
from common.base import Base,open_browser


url = "http://172.16.1.209/ecshop/user.php"


class CartPage(Base):
    """封装表现层:制作定位器"""
    username_loc = ("name","username")  # 用户名输入框
    password_loc = ("name","password")  # 密码输入框
    remember_loc = ("id","remember")  # 记住密码
    submit_loc = ("class name","us_Submit")  # 立即登录按钮
    question_loc = ("link text","密码问题")  # 密码问题链接
    email_loc = ("link text","邮件")  # 邮件链接
    message_loc = ("link text","短信验证")  # 短信验证链接
    homepage_loc = ("link text","首页")  # 首页链接
    register_loc = ("css selector","a[href='user.php?act=register']>img")  # 注册按钮
    result_loc = ("class name","f4_b")  # 登录成功后的结果
    search_loc=('xpath','//*[@id="searchForm"]/table/tbody/tr/td[2]/input') #搜索按钮
    #商品添加购物车时最后一件商品的文本元素定位
    test_add_result=('xpath','//*[@id="formCart"]/table[1]/tbody/tr[3]/td[1]/a[2]')


    """商品元素定位家用电器栏"""
    # 智能相机 库存20
    camera1_loc=('css selector','.clearfix:nth-child(2) .goodsItem:nth-child(1) .goodsimg')
    # 平衡车 库存1
    bcar_loc=('css selector','.clearfix:nth-child(2) .goodsItem:nth-child(2) .goodsimg')
    # 运动相机 库存1
    camera2_loc=('css selector','.clearfix:nth-child(2) .goodsItem:nth-child(3) .goodsimg')
    # 炫彩专业保护套 库存1
    colortao_loc=('css selector','.clearfix:nth-child(2) .goodsItem:nth-child(4) .goodsimg')
    # 透明保护壳 库存1
    visiontao_loc=('css selector','.clearfix:nth-child(2) .goodsItem:nth-child(5) .goodsimg')
    # 自拍杆 库存缺货
    zipaigan_loc=('css selector','.clearfix:nth-child(2) .goodsItem:nth-child(6) .goodsimg')
    # 随身风扇 库存20
    fengshan_loc=('css selector','.clearfix:nth-child(2) .goodsItem:nth-child(7) .goodsimg')
    # 视频   库存20
    camera3_loc=('css selector','.clearfix:nth-child(2) .goodsItem:nth-child(8) .goodsimg')
    """商品元素详情加入购物车按钮定位"""
    # 商品加入购物车按钮
    goods_confirm_loc=('css selector','.td1 img')
    """商品数量修改框定位"""
    #视频
    camera3num_loc=('xpath','/html/body/div[6]/div[1]/form/table[1]/tbody/tr[2]/td[5]/input')
    #随身风扇
    fengshannum_loc=('xpath','/html/body/div[6]/div[1]/form/table[1]/tbody/tr[3]/td[5]/input')
    """商品删除框"""
    # 视频
    camera3del_loc = ('xpath', '/html/body/div[6]/div[1]/form/table[1]/tbody/tr[2]/td[7]/a[1]')
    # 随身风扇
    fengshandel_loc = ('xpath', '//*[@id="formCart"]/table[1]/tbody/tr[2]/td[7]/a[1]')
    """购物车商品查看《随身小风扇》文本定位"""
    #随身小风扇文本定位
    fengshan_text_loc=('xpath','//*[@id="formCart"]/table[1]/tbody/tr[2]/td[1]/a[2]')
    """购物车数量显示按钮文本定位"""
    cartnum_loc=('partial link text','购物')

    """购物车内部元素定位"""
    # 商品数量输入框
    goods_num_loc=('xpath','//*[@id="goods_number_68"]')
    # 更新购物车按钮
    refresh_goods_loc=('xpath','//*[@id="formCart"]/table[2]/tbody/tr/td[2]/input[2]')
    # 清空购物车按钮
    clear_goods_loc=('xpath','//*[@id="formCart"]/table[2]/tbody/tr/td[2]/input[1]')
    # 继续购物按钮
    continue_shopping_loc=('xpath','/html/body/div[6]/div[1]/table/tbody/tr/td[1]/a/img')
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

    def input_camera3_num(self,num1):
        """
        商品视频数量输入框
        :param num:
        :return:
        """
        self.send_keys(self.camera3num_loc,num1)

    def input_fengshannum_loc(self,num2):
        """
        商品风扇数量输入框
        :param num:
        :return:
        """
        self.send_keys(self.fengshannum_loc,num2)

    def click_submit(self):
        """
        点击立即登录
        :return:
        """
        self.click(self.submit_loc)

    def click_homepage(self):
        """
        点击首页
        :return:
        """
        self.click(self.homepage_loc)

    def click_search(self):
        """
        点击搜素按钮
        :return:
        """
        self.click(self.search_loc)

    def click_visiontao(self):
        """
        点击透明手机套商品
        库存1
        :return:
        """
        self.click(self.visiontao_loc)

    def click_zipaigan(self):
        """
        点击自拍杆商品
        库存0
        :return:
        """
        self.click(self.zipaigan_loc)

    def cilck_fengshan(self):
        """
        点击风扇
        库存20
        :return:
        """
        self.click(self.fengshan_loc)

    def click_camera3(self):
        """
        点击视频商品
        库存20
        :return:
        """
        self.click(self.camera3_loc)

    def click_camera1(self):
        """
        点击智能相机
        库存 20
        :return:
        """
        self.click(self.camera1_loc)

    def click_camera2(self):
        """
        点击运动相机
        库存 1
        :return:
        """
        self.click(self.camera2_loc)

    def click_bcar(self):
        """
        点击平衡车
        库存 1
        :return:
        """
        self.click(self.bcar_loc)

    def click_colortao(self):
        """
        点击炫彩专业保护套
        库存 1
        :return:
        """
        self.click(self.colortao_loc)

    def click_goods_confirm(self):
        """
        点击加入购物车按钮
        :return:
        """
        self.click(self.goods_confirm_loc)

    def click_camera3del(self):
        """
        点击删除视频商品按钮
        :return:
        """
        self.click(self.camera3del_loc)
        self.confirm_alert()

    def click_fengshandel(self):
        """
        点击删除随身风扇按钮
        :return:
        """
        self.click(self.fengshandel_loc)
        self.confirm_alert()

    def click_refresh_goods(self):
        """
        点击更新购物车按钮
        :return:
        """
        self.click(self.refresh_goods_loc)

    def click_continue_shopping(self):
        """
        点击继续购物按钮
        :return:
        """
        self.click(self.continue_shopping_loc)

    def click_clear_goods(self):
        """
        点击清空购物车按钮
        :return:
        """
        self.click(self.clear_goods_loc)


    def is_cat_successed(self,text):
        """
        判断购物车是否有商品随身风扇
        :param text: 
        :return: 
        """
        return self.is_text_in_element(self.fengshan_text_loc,text)

    def is_cartnum_successed(self,text1):
        """
       判断购物车商品数量是否符合预期
        :param text1:
        :return:
        """
        return  self.is_text_in_element(self.cartnum_loc,text1)




if __name__ == '__main__':
    import time
    driver = open_browser()
    cart = CartPage(driver)
    cart.open_url(url)
    username = "tester"
    password = "Tester123"
    cart.input_username(username)
    cart.input_password(password)
    cart.click_submit()
    cart.click_homepage()
    cart.cilck_fengshan()
    cart.click_goods_confirm()
    cart.click_continue_shopping()
    cart.click_camera3()
    cart.click_goods_confirm()
    cart.click_continue_shopping()
    cart.click_visiontao()
    cart.click_goods_confirm()
    time.sleep(5)
    cart.close()


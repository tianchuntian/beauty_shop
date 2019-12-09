"""
backstage_page_add.py
    1.对登录页面封装
    2.封装页面表现层和操作层
    3.继承base.py中的Base类
"""
import unittest

from common.base import Base,open_browser
import time

# url='http://172.16.1.229/ecshop/admin/privilege.php?act=login'
# url='http://172.16.1.229/ecshop/admin'
url='http://192.168.1.8/ecshop/admin/privilege.php?act=login'
class Add_Background(Base):
            # 表现层 定位器
    # 关闭推送
    ec_push_close=('css selector','.panel-cross > span')
    # 点击ESChop
    ec_ecshop_click=('id','cloudLogin')
    # 用户名点击
    ec_username_click = ("name", "username")
    # 密码点击密码
    ec_password_click = ("name", "password")
    # 立即登录
    ec_submit_click = ("css selector", ".btn-a")

    #商品管理--定位
    icon_goods=("css selector", "#menu-ul > li.icon-goods")
    # 添加新商品--点击
    add_click=("link text", "添加新商品")
    # 通用信息--商品名称
    ec_goods_name_loc = ('xpath', '// *[ @ id = "general-table"] / tbody / tr[1] / td[2] / input[1]')
    #通用信息--颜色 定位-----
    ec_blue_loc=('xpath','//*[@id="ColorSelectertBox"]/table/tbody/tr[3]/td[2]')
    #通用信息--加粗-----
    ec_bold_loc=('xpath','//*[@id="general-table"]/tbody/tr[1]/td[2]/select/option[2]')
    #通用信息--商品货号------
    ec_goods_article_loc=("css selector","#general-table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]")
    # 通用信息--商品分类下拉框
    ec_goods_classify_loc = ("xpath", "//*[@id='general-table']/tbody/tr[3]/td[2]/select")
    # 通用信息--扩展分类--添加
    ec_classify_add_loc = ("xpath", "//*[@id='general-table']/tbody/tr[4]/td[2]/input")
    # 通用信息--扩展分类--添加下拉框
    ec_classify_add_choose_loc = ("xpath", "//*[@id='general-table']/tbody/tr[4]/td[2]/select")
    # 通用信息--商品品牌
    ec_goods_brand_loc = ("xpath", "//*[@id='general-table']/tbody/tr[5]/td[2]/select")
    # 通用信息--选择供应商
    ec_supplier_loc = ("id", "suppliers_id")
    # 通用信息--本店售价
    ec_sales_loc = ("xpath", "//*[@id='general-table']/tbody/tr[7]/td[2]/input[1]")

            # 会员价格中普通用户()价格输入框
    ec_usrprice_loc = ("id", "rank_1")
            # 会员价格中代销用户价格输入框
    ec_user_price_loc = ("id", "rank_3")
            # 会员价格中vip用户价格输入框
    ec_vipprice_loc = ("id", "rank_2")
            # 商品优惠价格中的优惠数量输入框
    ec_volumenumber_loc = ("name", "volume_number[]")
            # 商品优惠价格中的优惠价格输入框
    ec_volumeprice_loc = ("name", "volume_price[]")
            # 市场售价输入框
    ec_marketprice_loc = ("name", "market_price")



        # 详细描述按钮
    ec_goods_details_loc = ("id", "detail-tab")
    # 详细描述第二次iframe定位器  找到 详情描述
    iframe_loc = ("css selector", "#xEditingArea>iframe")
        # 详细描述---输入文本框
    ec_details_input_text_loc = ("css selector", "body[spellcheck='false']")
        # 其他信息按钮
    ec_goods_others_loc = ("id", "mix-tab")
        # 其他信息---商品重量输入框
    ec_goods_weight_loc = ("xpath", "//*[@id='mix-table']/tbody/tr[1]/td[2]/input")
        # 其他信息--商品重量单位框
    ec_weight_unit_loc = ("xpath", "//*[@id='mix-table']/tbody/tr[1]/td[2]/select")
        # 其他信息---库存数量输入框
    ec_stock_num_loc = ("xpath", "//*[@id='mix-table']/tbody/tr[2]/td[2]/input")
        # 其他信息---库存警告数量框
    ec_stock_warn_loc = ("xpath", "//*[@id='mix-table']/tbody/tr[3]/td[2]/input")
        # 其他信息---加入推荐--精品单选框
    is_best_goods_loc = ("xpath", "//*[@id='mix-table']/tbody/tr[4]/td[2]/input[1]")
        # 其他信息---加入推荐--新品单选框
    is_new_goods_loc = ("xpath", "//*[@id='mix-table']/tbody/tr[4]/td[2]/input[2]")
        # 其他信息---加入推荐--热销单选框
    is_hot_loc = ("xpath", "//*[@id='mix-table']/tbody/tr[4]/td[2]/input[3]")
        # 其他信息---上架单选框
    is_on_sale_loc = ("xpath", "//*[@id='alone_sale_3']/input")
        # 其他信息---能作为普通商品销售框
    is_alone_sale_loc = ("xpath", "//*[@id='mix-table']/tbody/tr[7]/td[2]/input")
        # 其他信息---是否为免运费商品框
    is_shipping_loc = ("xpath", "//*[@id='mix-table']/tbody/tr[7]/td[2]/input")
        # 其他信息---商品关键词输入框
    goods_key_words_loc = ("xpath", "//*[@id='mix-table']/tbody/tr[8]/td[2]/input")
        # 其他信息---商品简单描述输入框
    goods_simple_descr_loc = ("xpath", " //*[@id='mix-table']/tbody/tr[9]/td[2]/textarea")
        # 其他信息-----商家备注
    seller_note_loc = ("name", "seller_note")
        # 商品属性按钮
    goods_property_loc = ("id", "properties-tab")
        # 商品属性----商品类型下拉框
    goods_type_choose_loc = ("xpath", "//*[@id='properties-table']/tbody/tr[1]/td[2]/select")
        # 商品相册
    gallery_tab=('xpath','//*[@id="gallery-tab"]')

    #商品属性--产地
    attr_place_loc=('xpath','//*[@id="attrTable"]/tbody/tr[1]/td[2]/input[2]')
    # 商品属性--产品规格/容量
    attr_capacity_loc=('xpath','//*[@id="attrTable"]/tbody/tr[2]/td[2]/input[2]')
    #商品属性--主要原料
    attr_raw_loc=('xpath','//*[@id="attrTable"]/tbody/tr[3]/td[2]/input[2]')
    #商品属性--所属类别
    attr_type_loc=('xpath','//*[@id="attrTable"]/tbody/tr[4]/td[2]/select')
    # 商品属性--使用部位
    attr_part_loc=('xpath','//*[@id="attrTable"]/tbody/tr[5]/td[2]/input[2]')
    # 商品属性--适合肤质
    attr_skin_type_loc =('xpath','//*[@id="attrTable"]/tbody/tr[6]/td[2]/select')
    # 商品属性--适用人群
    attr_crowd_loc=('xpath','//*[@id="attrTable"]/tbody/tr[7]/td[2]/select')

    # 商品属性--确定  添加
    button_confirm_x=('xpath','//*[@id="tabbody-div"]/form/div/input[2]')

    homepage_loc = ("link text", "首页")  #首页链接
    register_loc = ("css selector", "a[href='user.php?act=register']>img") # 注册按钮


      #操作表现层

      # 关闭推送
    def push(self):
        self.click(self.ec_push_close)
        time.sleep(1)
        # 点击ESChop
    def ecshop_col(self):
        self.click(self.ec_ecshop_click)
        time.sleep(1)
        #账号
    def input_username(self, username):
        self.send_keys(self.ec_username_click, username)
        time.sleep(1)
        #密码
    def input_password(self,password):
        self.send_keys(self.ec_password_click, password)
        time.sleep(1)
        #点击操作
    def click_submit(self):
        self.click(self.ec_submit_click)
        time.sleep(1)

        #登录执行操作

        # 点击 商品管理
    def click_good_loc(self):

        self.to_frame("menu-frame")
        self.click(self.icon_goods)
        time.sleep(1)


            # 点击添加 新商品
    def click_add(self):
        self.click(self.add_click)
        time.sleep(1)

    #点击商品名称  输入
    def input_goods_name(self,text):
        self.exit_to_default_frame()
        self.to_frame("main-frame")
        self.send_keys(self.ec_goods_name_loc,text)
        time.sleep(1)


     # 有多余时间做
    def input_adorn(self):
        self.click(self.ec_blue_loc)
        time.sleep(1)
        self.click(self.register_loc)
        time.sleep(1)
    #货架号
    def goods_article(self,text):
        self.send_keys(self.ec_goods_article_loc,text)

    # 通用信息--商品分类下拉框
    def click_goods_classify(self):
        self.click_element(self.ec_goods_classify_loc)
        time.sleep(1)
    # 选择商品分类下拉框
    def choose_goods_classfiy(self, index):
        self.selector_by_index(self.ec_goods_classify_loc, index)
        time.sleep(1)
    # 通用信息--扩展分类--添加
    def classify_add(self):
        self.click_element(self.ec_classify_add_loc)
        time.sleep(1)
    # 选择扩展分类的下拉框
    def classify_add_choose(self,indiex):
        self.selector_by_index(self.ec_classify_add_choose_loc,indiex)
        time.sleep(1)
    # 通用信息--商品品牌
    def goods_brand(self,index):
        self.selector_by_index(self.ec_goods_brand_loc,index)
        time.sleep(1)
    # 通用信息--选择供应商
    def ec_supplier(self,index):
        self.selector_by_index(self.ec_supplier_loc,index)
        time.sleep(1)
    # 通用信息--本店售价
    def input_sales(self,text):
        self.click(self.ec_sales_loc)
        self.send_keys(self.ec_sales_loc,text)
        time.sleep(1)
    # 会员价格中普通用户价格输入框
    def  usrprice_loc(self,text):
            self.send_keys(self.ec_usrprice_loc,text)
            time.sleep(1)
    # 会员价格中代销用户价格输入框
    def user_price(self,text):
        self.send_keys(self.ec_user_price_loc,text)
        time.sleep(1)
        # 会员价格中vip用户价格输入框
    def vipprice_loc(self,text):
        self.send_keys(self.ec_vipprice_loc,text)
        time.sleep(1)
        # 商品优惠价格中的优惠数量输入框
    def volumenumber(self,text):
        self.send_keys(self.ec_volumenumber_loc,text)
        time.sleep(1)
        # 商品优惠价格中的优惠价格输入框
    def ec_volumeprice(self,text):
        self.send_keys(self.ec_volumeprice_loc,text)
        time.sleep(1)
    # 详细描述按钮
    def goods_details(self):
        self.click(self.ec_goods_details_loc)
        time.sleep(1)
    # 详细描述---输入文本框
    def details_input_text(self,text):
        self.to_frame('goods_desc___Frame')
        self.to_frame_A(self.iframe_loc)
        self.click(self.ec_details_input_text_loc)
        self.send_keys(self.ec_details_input_text_loc,text)
        time.sleep(2)
    #其他信息--进入操作
    def ec_goods_others(self):
        self.driver.switch_to.default_content()
        self.to_frame('main-frame')
        self.click(self.ec_goods_others_loc)
        time.sleep(1)
    # 其他信息---商品重量输入框
    def goods_weight_loc(self,text):
        self.click(self.ec_goods_weight_loc)
        self.send_keys(self.ec_goods_weight_loc,text)
        time.sleep(1)
    # 其他信息--商品重量单位框
    def weight_unit_loc(self,index):
        self.selector_by_index(self.ec_weight_unit_loc,index)
        time.sleep(1)
        # 其他信息---库存数量输入框
    def stock_num_loc(self,text):
        self.click(self.ec_stock_num_loc)
        self.send_keys(self.ec_stock_num_loc,text)
        time.sleep(1)
    #其他信息--库存警告数量
    def is_stock_warn(self,text):
        self.click(self.ec_stock_warn_loc)
        self.send_keys(self.ec_stock_warn_loc,text)
        time.sleep(1)
    # 其他信息---加入推荐--精品单选框
    def is_best_goods(self):
        self.click_element(self.is_best_goods_loc)
    # 其他信息---加入推荐--新品单选框
    def is_new_goods(self):
        self.click_element(self.is_new_goods_loc)
    # 其他信息---加入推荐--热销单选框
    def is_hot(self):
        self.click_element(self.is_hot_loc)
    # 其他信息---上架单选框

    # def is_on_sale(self):
    #     self.click_element(self.is_on_sale_loc)
    # 其他信息---能作为普通商品销售框
    def  is_alone_sale(self):
        self.click_element(self.is_alone_sale_loc)
    # 其他信息---是否为免运费商品框
    def is_shipping(self):
        self.click_element(self.is_shipping_loc)
    # 其他信息---商品关键词输入框
    def goods_key_words(self,text):
        self.send_keys(self.goods_key_words_loc,text)
        time.sleep(1)
        # 其他信息---商品简单描述输入框
    def goods_simple_descr(self,text):
        self.send_keys(self.goods_simple_descr_loc,text)
        time.sleep(1)

        # 其他信息-----商家备注-------------------------------
    def seller_note_x(self,text):
        self.send_keys(self.seller_note_loc,text)
        time.sleep(1)

    def goods_property_choose(self):
        self.click_element(self.goods_property_loc)
        time.sleep(1)
    # 商品属性----商品类型下拉框
    def goods_type_choose(self,index):
        self.driver.switch_to.parent_frame()
        self.to_frame('main-frame')
        self.selector_by_index(self.goods_type_choose_loc,index)
        time.sleep(1)
        # 商品属性--产地
    def attr_place_x(self,text):
        self.send_keys(self.attr_place_loc,text)
        # 商品属性--产品规格/容量
    def attr_capacity_x(self,text):
        self.send_keys(self.attr_capacity_loc,text)

        # 商品属性--主要原料
    def attr_raw_x(self,text):
        self.send_keys(self.attr_raw_loc,text)
        time.sleep(1)
        # 商品属性--所属类别
    def attr_type_x(self,index):
        self.selector_by_index(self.attr_type_loc,index)
        time.sleep(1)
        # 商品属性--使用部位
    def attr_part_x(self,text):
        self.send_keys(self.attr_part_loc,text)
        time.sleep(1)
        # 商品属性--适合肤质
    def attr_skin_type(self,index):
        self.selector_by_index(self.attr_skin_type_loc,index)
        time.sleep(1)
        # 商品属性--适用人群
    def attr_crowd_x(self,index):
        self.selector_by_index(self.attr_crowd_loc,index)
        time.sleep(1)
        # 商品属性--确定  添加
    def button_confir(self):
        self.click_element(self.button_confirm_x)
        time.sleep(7)


if __name__ == '__main__':
    import time
    driver = open_browser()
    login = Add_Background(driver)
    login.open_url(url)
    username ='root'
    password = 'aa789451'
    login.push()
    login.ecshop_col()

    login.input_username(username)
    login.input_password(password)
    login.click_submit()

    login.click_good_loc()
    login.click_add()
    login.input_goods_name('小白兔')
    # login.input_adorn()
    # login.input_article('111223')
    login.goods_article('j23a455x')
    login.choose_goods_classfiy(2)
    login.classify_add()
    login.classify_add_choose(3)
    login.goods_brand(2)
    login.ec_supplier(1)
    login.input_sales(210)
    login.usrprice_loc(199)
    login.user_price(160)
    login.vipprice_loc(180)
    login.volumenumber(3)
    login.ec_volumeprice(30)


    login.goods_details()
    login.details_input_text('为什么啊  为什么是我选到这 模块 ...有没有什么人办法不写这XXX东西')
    login.ec_goods_others()
    login.goods_weight_loc('1024')
    login.weight_unit_loc(1)
    login.stock_num_loc(20)
    login.is_stock_warn(15)
    login.is_best_goods()
    login.is_new_goods()
    login.is_hot()
    # login.is_on_sale()
    login.is_alone_sale()
    login.is_shipping()
    login.goods_key_words('天王盖地虎')
    login.goods_simple_descr('小鸡炖蘑菇')
    login.seller_note_x('宝塔镇河妖')
    login.goods_property_choose()
    login.goods_type_choose(8)

    login.attr_place_x('那威')
    login.attr_capacity_x('500g')
    login.attr_raw_x('干油,水,酒精,香精等.')
    login.attr_type_x(3)
    login.attr_part_x('脸颊.面部.颈部.手')
    login.attr_skin_type(2)
    login.attr_crowd_x(1)
    login.button_confir()

    time.sleep(4)
    login.close()
















'''"后台管理
商品管理--添加商品"	罗毅
'''
url='http://172.16.1.229/ecshop/admin/privilege.php?act=login'
# Assertions=r'E:\python\-1项目\ECShop\common\data\Assertions.xlsx'
import ddt
import time
import unittest
from page.backstage_page_add import Add_Background
from common.base import open_browser
from common.operation_Excel import OperationExcel
oper =OperationExcel('./data/Assertions.xlsx')
test_data=oper.get_data_info()

@ddt.ddt
class Test_Backstage_Supporter(unittest.TestCase):

    def setUp(self):
        '''打开浏览器实例化对象'''
        self.driver = open_browser()
        self.login = Add_Background(self.driver)
        self.login.open_url(url)

    def tearDown(self):
        '''关闭浏览器'''
        self.login.close()

    @ddt.data(*test_data)
    def test_backstage(self,data):
            '''后台管理-添加新商品-添加一个新商品的测试'''
            # 关闭推送
            self.login.push()
            # 点击ESChop
            self.login.ecshop_col()

            # 账号
            self.login.input_username(data['username'])
            # 密码
            self.login.input_password(data['password'])
            # 点击操作 登录
            self.login.click_submit()
            # 点击 商品管理
            self.login.click_good_loc()
            # 点击添加 新商品
            self.login.click_add()
            # 点击商品名称  输入
            self.login.input_goods_name(data['commodity'])
            # login.input_adorn()
            # login.input_article('111223')
            #货架号
            self.login.goods_article(data['number'])
            # 选择商品分类下拉框
            self.login.choose_goods_classfiy(data['Commodity'])
            # 通用信息--扩展分类--添加
            self.login.classify_add()
            # 选择扩展分类的下拉框
            self.login.classify_add_choose(data['dropdownbox'])
            # 通用信息--商品品牌
            self.login.goods_brand(data['brand'])
            # 通用信息--选择供应商
            self.login.ec_supplier(data['supplier'])
            # 通用信息--本店售价
            self.login.input_sales(int(data['sellingprice']))
            # 会员价格中普通用户价格输入框
            self.login.usrprice_loc(int(data['user']))
            # 会员价格中代销用户价格输入框
            self.login.user_price(int(data['Consignmentuser']))
            # 会员价格中vip用户价格输入框
            self.login.vipprice_loc(int(data['vip']))
            # 商品优惠价格中的优惠数量输入框
            self.login.volumenumber(int(data['discounts']))
            # 商品优惠价格中的优惠价格输入框
            self.login.ec_volumeprice(int(data['favourable']))
            # 详细描述按钮
            self.login.goods_details()
            # 详细描述---输入文本框
            self.login.details_input_text(data['detail'])
            # 其他信息--进入操作
            self.login.ec_goods_others()
            # 其他信息---商品重量输入框
            self.login.goods_weight_loc(int(data['weight']))
            # 其他信息--商品重量单位框
            self.login.weight_unit_loc(data['unit'])
            # 其他信息---库存数量输入框
            self.login.stock_num_loc(int(data['num']))
            # 其他信息--库存警告数量
            self.login.is_stock_warn(int(data['caution']))
            # 其他信息---加入推荐--精品单选框
            self.login.is_best_goods()
            # 其他信息---加入推荐--新品单选框
            self.login.is_new_goods()
            # 其他信息---加入推荐--热销单选框

            self.login.is_hot()
            # 其他信息---上架单选框
            # self.login.is_on_sale()
            # 其他信息---能作为普通商品销售框
            self.login.is_alone_sale()
            # 其他信息---是否为免运费商品框
            self.login.is_shipping()

            # 其他信息---商品关键词输入框
            self.login.goods_key_words(data['information'])
            # 其他信息---商品简单描述输入框
            self.login.goods_simple_descr(data['Simpledescription'])
            # 其他信息-----商家备注
            self.login.seller_note_x(data['note'])
            # 商品属性按钮
            self.login.goods_property_choose()
            # 商品属性----商品类型下拉框
            self.login.goods_type_choose(data['Commoditytype'])
            # 商品属性--产地
            self.login.attr_place_x(data['place'])
            # 商品属性--产品规格/容量
            self.login.attr_capacity_x(data['specification'])
            # 商品属性--主要原料
            self.login.attr_raw_x(data['Rawmaterial'])
            # 商品属性--所属类别
            self.login.attr_type_x(data['category'])
            # 商品属性--使用部位
            self.login.attr_part_x(data['part'])
            # 商品属性--适合肤质
            self.login.attr_skin_type(data['Skintype'])
            # 商品属性--适用人群
            self.login.attr_crowd_x(data['crowd'])
            # 商品属性--确定  添加
            self.login.button_confir()
            #定位器 定位商品
            location=('id','search_id')
            button=self.login.click_element(location)
            ##对添加商断言



if __name__ == '__main__':
    unittest.main()

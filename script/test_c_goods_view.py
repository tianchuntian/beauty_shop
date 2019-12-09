'''"浏览商品浏览
所有商品"	汪里
'''
# 导入模块
from page.goods_view import GoodView, url
from common.base import open_browser

import unittest, time

# 定义浏览商品测试用例类
class TestGoodsView(unittest.TestCase):
    # 编写test fixture
    def setUp(self) -> None:
        # 用户前置条件
        # 打开浏览器
        driver = open_browser('firefox')
        # 浏览商品类实例化
        self.goodsview = GoodView(driver)
        # 输入网址
        self.goodsview.open_url(url)

    def tearDown(self) -> None:
        # 关闭浏览器
        time.sleep(4)
        self.goodsview.close()
    
    # 编写test case
    def test_view(self):
        '''浏览商品测试用例：浏览所有商品'''
        self.goodsview.view_all()


# 测试代码
if __name__ == '__main__':
    unittest.main()
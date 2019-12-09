from common.base import Base, open_browser
import time

url = 'http://172.16.1.229/ecshop/'

# 定义浏览商品类
class GoodView(Base):
    '''封装表现层'''
    # 制作定位器
    search_loc = ('css selector', 'input[value="搜索"]')      # 搜索按钮定位器
    next_loc = ('link text', '下一页')
    goods_loc = ('css selector', 'div[class="goodsItem"]')        # 商品定位器


    # 定义获取当前页所有商品元素
    def view_current_page(self):
        '''
        浏览当前页所有的商品
        :return: 
        '''
        # 点击搜索按钮
        # self.click(self.search_loc)
        # 定位当前页所有商品的列表
        goods_elements = self.find_elements(self.goods_loc)
        # print(len(goods_elements))
        # 商品索引变量
        i = 1
        # 最后商品判断
        while i <= len(goods_elements):
            # 先写一个死的子标签
            # locator = ('xpath', '//div[@class="clearfix goodsBox"]/div[1]')
            # 制作商品元素的定位器
            locator = ('xpath', f'//div[@class="clearfix goodsBox"]/div[{i}]')
            # 点击商品
            self.click(locator)
            # 浏览器返回上一页
            self.back()
            i += 1

    # 定义获取所有页商品元素
    def view_all(self):
        '''
        浏览所有的商品
        :return: 
        '''
        # 点击搜索按钮
        self.click(self.search_loc)
        # 定位页码总数
        page_num = self.find_elements(self.page_num_loc)
        # 页码索引变量
        j = 1
        # 最后页判断
        while j <= len(page_num):
            try:
                # 浏览当前页所有商品
                self.view_current_page()
                # 点击下一页
                self.click(self.next_loc)
                time.sleep(2)
                j += 1
            except:
                print('这是最后一页')
                break


# 测试代码
if __name__ == '__main__':
    driver = open_browser('firefox')
    goodview = GoodView(driver)
    goodview.open_url(url)
    # goodview.view_current_page()
    goodview.view_all()



    time.sleep(4)
    goodview.close()
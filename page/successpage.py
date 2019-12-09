from selenium import webdriver
from common.base import Base
class SuccessPage(Base):
    "封装是否成功下单"
    success_text_loc=("xpath","//div/div/h6[@style='text-align:center; height:30px; line-height:30px;']")
    
    def is_success(self,text):
        result=self.is_text_in_elemen(self.success_text_loc,text)
        return result
                
import pandas

class OperationExcel:
    def __init__(self,filename):
        self.table=pandas.read_excel(filename)

    def get_data_info(self):
        # 将读取的数据转化成[{}, {}]格式
        data=[]
        for i in self.table.index.values:  # 遍历表格中的行数
            raw_data = self.table.loc[i].to_dict()  # 将每一行的内容转化为字典
            data.append(raw_data)  # 将转化后的内容添加到空列表中
        return data


if __name__ == '__main__':
    oper = OperationExcel('./data/Assertions.xlsx')
    data = oper.get_data_info()




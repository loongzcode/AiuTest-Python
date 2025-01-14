import openpyxl

def read_excel(args:str): 
    # 打开文件
    workbook = openpyxl.load_workbook(args)
    # 选择表
    worksheet = workbook["Sheet1"]
    # 读取数据
    data = []
    keys = [cell.value for cell in worksheet[2]]
    for row in worksheet.iter_rows(min_row=3,values_only=True):
        dict_data = dict(zip(keys,row))
        data.append(dict_data)

    # 关闭文件
    workbook.close()
    return data
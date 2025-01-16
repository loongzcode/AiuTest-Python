import openpyxl

def read_excel(file_path, sheet_name): 
    # 打开文件
    workbook = openpyxl.load_workbook(file_path)
    # 选择表
    worksheet = workbook[sheet_name]
    # 读取数据
    data = []
    keys = [cell.value for cell in worksheet[2]]
    for row in worksheet.iter_rows(min_row=3,values_only=True):
        dict_data = dict(zip(keys,row))
        if dict_data["is_true"]:
            data.append(dict_data)

    # 关闭文件
    workbook.close()
    return data
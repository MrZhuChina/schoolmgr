#-- coding=utf8 --
#导入到新表
def import_new_table(filename=None):
    if filename==None:
        filename=input("输入文件的绝对路径：")
    import xlrd
    try:
        wb=xlrd.open_workbook(filename)
    except:
        print("错误的文件路径.")
    sheet1=wb.sheet_by_index(0)
    TBname=sheet1.name
    


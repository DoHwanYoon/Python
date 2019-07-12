import openpyxl

file = openpyxl.load_workbook('test.xlsx')
sheet = file.active
#sheet = file.get_sheet_by_name('sheetname')

for r in sheet.rows
    print r[4].value

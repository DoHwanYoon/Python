import openpyxl

wb = openpyxl.load_workbook('test.xlsx')
sheet = wb['Sheet1']

for row in sheet.rows:
    for cell in row:
        print(cell.value, end=' ')
    print()    
#print(sheet['A1'].value)

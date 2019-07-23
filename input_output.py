import openpyxl

wb = openpyxl.load_workbook('test.xlsx')
sheet = wb['Sheet1']
   
   
for i in range(5):
    print(sheet['A+i'].value)

print(sheet['A1'].value)

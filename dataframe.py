import numpy as np
import pandas as pd
#

data = {'가격':[3000,2000,1000], '수량':[3,3,2]}
testdata = pd.DataFrame(data, index=['자몽', '수박', '사과'])

testdata.to_excel('testdata.xlsx')

re=pd.read_excel('testdata.xlsx')
print(re)
# import 같은경우는 함수를 사용하려면 이름을 정해주는것이 좋음
# => * 을 했을시, 관련된 모든 함수들이 메모리에 로드되는 경우를 방지(메모리 낭비 방지)
from tkinter import *

window = Tk()
window.title("Calculator")
display = Entry(window, width=33)
display.grid(row=0, column=0, columnspan=5)

button_list = [
'7', '8', '9', '/', 'C',
'4', '5', '6', '*', ' ',
'1', '2', '3', '-', ' ',
'0', '.', '=', '+', ' ' ]

def click(key):
    if key == '=':
        result = eval(display.get())
        s = str(result)
        display.insert(END, "=" +s)
    elif key == 'C':
        display.delete(0,END)
    else:
        display.insert(END, key)

# 전역 변수는 왠만하면 쓰지않는 것이 좋음
# => 지역변수로 초기화 시켜주면서 활용하면 좋을것 같다.
row_index =1
col_index =0

# for안에서 함수 작성은 안하는게 좋지않을까 싶음

for button_text in button_list:
    def process(t=button_text):
        click(t)
    Button(window, text=button_text, width=5, command=process).grid(row=row_index, column=col_index)
    col_index +=1
    if col_index > 4:
        row_index +=1
        col_index = 0
# Python

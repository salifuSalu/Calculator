#python 3!
from tkinter import *
root = Tk()
root.title('Calculator')
frame1 = Frame(root, width=200, height=100)
entry = Entry(root, width=60, font='Akrobat 12 ')
entry.grid(row=0, rowspan=3, column=0, sticky=(N, S, E, W), pady=20, padx=20)
entry.focus()
frame1.grid()
frame1.columnconfigure(0, weight=1)
frame1.rowconfigure(0, weight=1)

#entry function display button value
def getFeeds(arg):
    #entry.delete(END)
    entry.insert(END, str(arg))

#clear button
def clear():
    entry.delete(0, END)
    buttonEqual.configure(state='active', bg='pink')
    buttonClear.configure(state='disable', bg='grey')

#calculate result and display
def equal():
    rawText = str(entry.get()).strip()
    #print(rawText)
    #operation = '+'
    for i in range(0, len(rawText)):
        if rawText[i]=='+':
            operation = '+'
        elif rawText[i]=='*':
            operation = '*'
        elif rawText[i]=='/':
            operation = '/'
        elif rawText[i]=='-':
            operation = '-'

    fisrtOperand = rawText[:rawText.index(operation)]
    secondOperand = rawText[rawText.index(operation)+1:]
    result = 0
    if operation == '+':
        result = int(fisrtOperand) + int(secondOperand)
    elif operation == '*':
        result = int(fisrtOperand) * int(secondOperand)
    elif operation == '/':
        result = int(fisrtOperand) / int(secondOperand)
    else:
        result = int(fisrtOperand) - int(secondOperand)

    entry.insert(END, " = "+str(result))
    buttonEqual.configure(state='disable', bg='grey')
    buttonClear.configure(state='active', bg='white')


#buttons(numbers)
button7 = Button(frame1, text="7", command=lambda: getFeeds(7))
button8 = Button(frame1, text="8", command=lambda: getFeeds(8))
button9 = Button(frame1, text="9", command=lambda: getFeeds(9))
button4 = Button(frame1, text="4", command=lambda: getFeeds(4))
button5 = Button(frame1, text="5", command=lambda: getFeeds(5))
button6 = Button(frame1, text="6", command=lambda: getFeeds(6))
button1 = Button(frame1, text="1", command=lambda: getFeeds(1))
button2 = Button(frame1, text="2", command=lambda: getFeeds(2))
button3 = Button(frame1, text="3", command=lambda: getFeeds(3))
button0 = Button(frame1, text="0", command=lambda: getFeeds(0))

for i in frame1.winfo_children():
    i.configure(width=10, padx=4, pady=4)

#colouring alternating rows
for i in range(0, 10, 2):
    frame1.winfo_children()[i].configure(bg='light blue')
#symbols
buttonClear = Button(frame1, text="CLEAR", width=7, command=clear, bg='white')
buttonDivide = Button(frame1, text="/", width=7, command=lambda: getFeeds('/'), bg='green')
buttonMultiply = Button(frame1, text="*", width=7, command=lambda: getFeeds('*'), bg='yellow')
buttonSubtract = Button(frame1, text="-", width=7, command=lambda: getFeeds('-'), bg='red')
buttonAdd = Button(frame1, text="+", width=7, command=lambda: getFeeds('+'), bg='blue', fg='white')
buttonEqual = Button(frame1, text="=", width=7, command=equal, bg='pink')
#buttonModulos = Button(frame1, text="%", width=7)

#placement of numbers and symbols
#first row = 0
button7.grid(row=0, column=0)
button8.grid(row=0, column=1)
button9.grid(row=0, column=2)
buttonClear.grid(row=0, column=3)
#second row=1
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
buttonSubtract.grid(row=1, column=3, columnspan=2)
#third row=2
button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
buttonAdd.grid(row=2, column=3)
#fourth row=3
button0.grid(row=3, column=1)
buttonDivide.grid(row=3, column=0)
buttonMultiply.grid(row=3, column=2)
buttonEqual.grid(row=3, column=3)


#root.overrideredirect(1)

root.mainloop()
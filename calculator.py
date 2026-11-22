# This import is for the GUI aspect of the calculaltor
import tkinter as tk 
# This is to create a window
root = tk.Tk()
#This resets the size of the window by using the geometry class
root.geometry('500x500')
root.title("Calculator")
#These are the widgets in the window

button1 = tk.Button(root, text="1", width=9, height=3)
button2 = tk.Button(root, text="2", width=9, height=3)
button3 = tk.Button(root, text="3", width=9, height=3)
button4 = tk.Button(root, text="4", width=9, height=3)
button5 = tk.Button(root, text="5", width=9, height=3)
button6 = tk.Button(root, text="6", width=9, height=3)
button7 = tk.Button(root, text="7", width=9, height=3)
button8 = tk.Button(root, text="8", width=9, height=3)
button9 = tk.Button(root, text="9", width=9, height=3)
button0 = tk.Button(root, text="0", width=9, height=3)


#Add a widget to window, using the .pack() method

button1.pack()
button1.place(x=10, y=215)
button2.pack()
button2.place(x=110, y=215)
button3.pack()
button3.place(x=210, y=215)
button4.pack()
button4.place(x=10, y=285)
button5.pack()
button5.place(x=110, y=285)
button6.pack()
button6.place(x=210, y=285)
button7.pack()
button7.place(x=10, y=355)
button8.pack()
button8.place(x=110, y=355)
button9.pack()
button9.place(x=210, y=355)
button0.pack()
button0.place(x=110, y=425)

#This keeps the window open 
root.mainloop()


def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def divide (a, b):
    return a/b

def multiply (a, b):
    return a*b


def x ():
    first_number = float(input("Enter first number?: "))
    return first_number

def y():
    second_number = float(input("Enter second number?: "))
    return second_number


#while(True):
    operator = input("Choose and operator (+,-,*,/): ")
    if operator == "+":
        sum = add(x(),y())
        print(sum)
        print("\n")
    elif operator == "-":
        sum = subtract(x(),y())
        print(sum)
        print("\n")
    elif operator == "*":
        sum = multiply(x(),y())
        print(sum)
        print("\n")
    elif operator == "/":
        sum = divide(x(),y())
        print(sum)
        print("\n")
    else:
        print("Choose a valid operator from the list!")
        print("\n")
        









    

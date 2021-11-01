from tkinter import *

class Calculator:

    def __init__(self, root):
        # Entry screen
        self.e = Entry(root, width=50, borderwidth=5)
        self.e.grid(row=0, column=0, columnspan=4)
        self.e.insert(0, 0)

        # A list that save all the process 
        self.banker = []

        # buttons
        self.button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: self.click_number(1))
        self.button_1.grid(row=4, column=0)

        self.button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: self.click_number(2))
        self.button_2.grid(row=4, column=1)

        self.button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: self.click_number(3))
        self.button_3.grid(row=4, column=2)

        self.button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: self.click_number(4))
        self.button_4.grid(row=3, column=0)

        self.button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: self.click_number(5))
        self.button_5.grid(row=3, column=1)

        self.button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: self.click_number(6))
        self.button_6.grid(row=3, column=2)

        self.button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: self.click_number(7))
        self.button_7.grid(row=2, column=0)

        self.button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: self.click_number(8))
        self.button_8.grid(row=2, column=1)

        self.button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: self.click_number(9))
        self.button_9.grid(row=2, column=2)

        self.button_0 = Button(root, text='0', padx=90, pady=20, command=lambda: self.click_number(0))
        self.button_0.grid(row=5, column=0, columnspan=2)

        self.button_dot = Button(root, text='.', padx=41, pady=20, command=lambda: self.click_number('.'))
        self.button_dot.grid(row=5, column=2)

        self.button_plus = Button(root, text='+', fg="#ff9600", padx=39, pady=20, command=self.click_plus)
        self.button_plus.grid(row=4, column=3)

        self.button_minus = Button(root, text='-', fg="#ff9600", padx=40, pady=20, command=self.click_minus)
        self.button_minus.grid(row=3, column=3)

        self.button_equal = Button(root, text='=', fg="#ff9600", padx=39, pady=20, command=self.click_equal)
        self.button_equal.grid(row=5, column=3)

        self.button_clear = Button(root, text='AC', fg="#ff9600", padx=35, pady=20, command=self.click_clear)
        self.button_clear.grid(row=1, column=0)

        self.button_x = Button(root, text='x', padx=40, fg="#ff9600", pady=20, command=self.click_x)
        self.button_x.grid(row=2, column=3)

        self.button_d = Button(root, text='Del', padx=35, pady=20, command=lambda: self.click_number("del"))
        self.button_d.grid(row=1, column=1)
        self.button_d.configure(fg="#ff9600")

        self.button_pct = Button(root, text='%', fg="#ff9600", padx=39, pady=20, command=lambda: self.click_number("%"))
        self.button_pct.grid(row=1, column=2)

        self.button_division = Button(root, text='/', fg="#ff9600", padx=40, pady=20, command=self.click_division)
        self.button_division.grid(row=1, column=3)

    def click_plus(self):
      """that function will get the number of the entry  and put it on the 'banker'(list), add a '+' at the banker and delete the number on the entry screen. It will pass without doing anything (without error) if the user didn't digit anythin before the operator, if the user already have press a operator button."""
      if not self.e.get() == "":
        self.banker.append(float(self.e.get()))
      if self.banker == [] :
        pass
      else:
        self.banker.append("+")
        self.e.delete(0, END)

    def click_minus(self):
      """that function will get the number of the entry  and put it on the 'banker'(list), add a '-' at the banker and delete the number on the entry screen."""
      if not self.e.get() == "":
        self.banker.append(float(self.e.get()))
      if self.banker == [] or self.banker[-1]=="-":
        pass
      else:
        self.banker.append("-")
        self.e.delete(0, END)

    def click_number(self, number):
      current = self.e.get()
      self.e.delete(0, END)
      if number == "%":
        bignum = int(current) / 100
      elif number == "del":
        sub = current[-1]
        bignum = current.replace(sub, "")
      else:
        bignum = str(current) + str(number)

        self.e.insert(0, bignum)

    def click_x(self):
      """that function will get the number of the entry  and put it on the 'banker'(list), add a 'x' at the banker and delete the number on the entry screen."""
      if not self.e.get() == "":
        self.banker.append(float(self.e.get()))
      if self.banker == [] or self.banker[-1]=="x":
        pass
      else:
        self.banker.append("x")
        self.e.delete(0, END)

    def click_division(self):
      if not self.e.get() == "":
        self.banker.append(float(self.e.get()))
      if self.banker == [] or self.banker[-1]=="/":
        pass
      else:
        self.banker.append("/")
        self.e.delete(0, END)

    def click_equal(self):
      if not self.e.get() == "":
        self.banker.append(float(self.e.get()))
      if self.banker == [] or len(self.banker) == 2:
        pass
      else:
        self.banker.append(float(self.e.get()))
        self.e.delete(0, END)
        result = self.banker[0]
        # i is the variable that will control the loop
        i = 0
        while i < len(self.banker):
            if self.banker[i] == "x":
                ab = self.banker[i-1] * self.banker[i + 1]
                self.banker[i] = ab
                self.banker.pop(i+1)
                self.banker.pop(i-1)

            elif self.banker[i] == "/":
                div = self.banker[i-1] / self.banker[i + 1]
                self.banker[i] = div
                self.banker.pop(i+1)
                self.banker.pop(i-1)
            i += 1

        for i in range(1, len(self.banker), 2):
            if self.banker[i] == "+":
                result = result + self.banker[i + 1]
            elif self.banker[i] == "-":
                result = result - self.banker[i + 1]

        if len(self.banker) == 1:
            result = self.banker[0]

        self.e.insert(0, result)
        self.banker = []

    def click_clear(self):
        self.e.delete(0, END)
        self.banker = []

root = Tk()
root.title("Calculator")
robot = Calculator(root)
root.mainloop()


import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')

        sandwich = Label(window, text='샌드위치 (5000원)')
        sandwich.pack()

        self.sand_num = Entry(window, width=5)
        self.sand_num.pack()

        cake = Label(window, text='케이크 (20000원)')
        cake.pack()

        self.cake_num = Entry(window, width=5)
        self.cake_num.pack()

        button = Button(window, text='주문하기', command=self.send_order)
        button.pack()

    def send_order(self):
        order_text=''
        order_text += str(self.name) + ": "
        c = str(self.cake_num.get())
        s = str(self.sand_num.get())

        if s.isdigit() and int(self.sand_num.get()) > 0:
            order_text += "샌드위치 (5000원) " + str(self.sand_num.get()) + "개"
            if c.isdigit() and int(self.cake_num.get()) > 0:
                order_text += ", 케이크 (20000원) " + str(self.cake_num.get()) + "개"
        elif c.isdigit() and int(self.cake_num.get()) > 0:
            order_text += "케이크 (20000원) " + str(self.cake_num.get()) + "개"
        else:
            return 0

        self.bakeryView.add_order(order_text)

if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
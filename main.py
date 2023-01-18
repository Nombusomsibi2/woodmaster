import tkinter
from tkinter import *
from tkinter import END
from functools import partial
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.geometry("450x300")

cart = []
total = []

image = Image.open("fries.jpg")

# Resize the image using resize() method
resize_image = image.resize((140, 130))

img = ImageTk.PhotoImage(resize_image)

image = Image.open("chicken.jpg")

# Resize the image using resize() method
resize_image = image.resize((140, 130))

img2 = ImageTk.PhotoImage(resize_image)

image = Image.open("burger.jpg")

# Resize the image using resize() method
resize_image = image.resize((140, 130))

img3 = ImageTk.PhotoImage(resize_image)

image = Image.open("beef-burger.png")

# Resize the image using resize() method
resize_image = image.resize((140, 130))

img4 = ImageTk.PhotoImage(resize_image)

image = Image.open("pizza.jpg")

# Resize the image using resize() method
resize_image = image.resize((140, 130))

img5 = ImageTk.PhotoImage(resize_image)

image = Image.open("hot-dog.jpg")

# Resize the image using resize() method
resize_image = image.resize((140, 130))

img6 = ImageTk.PhotoImage(resize_image)

image = Image.open("wings.jpg")

# Resize the image using resize() method
resize_image = image.resize((140, 130))

img7 = ImageTk.PhotoImage(resize_image)

image = Image.open("wrap.jpg")

# Resize the image using resize() method
resize_image = image.resize((140, 130))

img8 = ImageTk.PhotoImage(resize_image)

def add_cart():
    sum = 0
    for x in total:
        sum = sum + x
    print(sum)
    messagebox.askyesno("Checking Out", "Total is R" + str(sum) + "\n\nComplete Purchase?")


def open_win():
    new = Toplevel(root)
    new.geometry("900x900")
    new.title("Menu")
    Label(new, text="Modern Food Service", font=('Helvetica 17 bold')).pack(pady=30)
    listbox = Listbox(new)

    def add_to_cart(item, price):
        print(item)
        print(price)
        cart.append(item)
        total.append(price)
        listbox.insert(END, item + "      R" + str(price))

    listbox.insert(END, 'Cart')
    listbox.insert(END, 'Item              Price')



    label1 = Label(new, image=img).place(x=10, y=80)
    label11 = Label(new, text='Fries\nR25', font="10").place(x=55, y=220)
    button1 = Button(new, text="Add To Cart", command=lambda m="Fries", price=25: add_to_cart(m, price)).place(x=50,
                                                                                                               y=260)


    label2 = Label(new, image=img2).place(x=200, y=80)
    label12 = Label(new, text='Chicken\nR35', font="10").place(x=245, y=220)
    button3 = Button(new, text="Add To Cart", command=lambda m="1/4 Chicken", price=35: add_to_cart(m, price)).place(
        x=250,
        y=260)



    label3 = Label(new, image=img3).place(x=400, y=80)
    label13 = Label(new, text='Cheese Burger\nR40', font="10").place(x=445, y=220)
    button5 = Button(new, text="Add To Cart", command=lambda m="Cheese Burger", price=40: add_to_cart(m, price)).place(
        x=450, y=260)


    label4 = Label(new, image=img4).place(x=600, y=80)
    label14 = Label(new, text='Beef Burger\nR40', font="10").place(x=645, y=220)
    button7 = Button(new, text="Add To Cart", command=lambda m="Beef Burger", price=40: add_to_cart(m, price)).place(
        x=650, y=260)


    label5 = Label(new, image=img5).place(x=10, y=350)
    label15 = Label(new, text='Pizza\nR55', font="10").place(x=55, y=500)
    button2 = Button(new, text="Add To Cart", command=lambda m="Pizza", price=55: add_to_cart(m, price)).place(x=50,
                                                                                                               y=540)


    label6 = Label(new, image=img6).place(x=200, y=350)
    label16 = Label(new, text='Hotdog\nR25', font="10").place(x=245, y=500)
    button4 = Button(new, text="Add To Cart", command=lambda m="Hotdog", price=25: add_to_cart(m, price)).place(x=250,
                                                                                                                y=540)



    label7 = Label(new, image=img7).place(x=400, y=350)
    label17 = Label(new, text='Wings\nR30', font="10").place(x=445, y=500)
    button6 = Button(new, text="Add To Cart", command=lambda m="Wings", price=30: add_to_cart(m, price)).place(x=450,
                                                                                                               y=540)



    label8 = Label(new, image=img8).place(x=600, y=350)
    label18 = Label(new, text='Schwarma\nR35', font="10").place(x=645, y=500)
    button8 = Button(new, text="Add To Cart", command=lambda m="Schwarma", price=35: add_to_cart(m, price)).place(x=650,
                                                                                                                  y=540)

    button9 = Button(new, text="Checkout", command=lambda: add_cart()).place(x=350,
                                                                             y=600)

    listbox.place(x=300, y=640)


# the label for user_name
user_name = Label(root, text="Username").place(x=40, y=60)

# the label for user_password
user_password = Label(root, text="Password").place(x=40,
                                                   y=100)

submit_button = Button(root,
                       text="Submit", command=open_win).place(x=40,
                                                              y=130)

user_name_input_area = Entry(root,
                             width=30).place(x=110,
                                             y=60)

user_password_entry_area = Entry(root,
                                 width=30, show="*").place(x=110,
                                                           y=100)

root.mainloop()

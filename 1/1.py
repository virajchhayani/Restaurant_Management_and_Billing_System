import os
import random
from tkinter import *
from tkinter import messagebox

# ============================ main ============================
class Bill_App:
    def __init__(self, root):
        self.f_roti_p = None
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Restaurant Management and Billing System modified by VIRAJ CHHAYANI")
        bg_color = "Gainsboro"
        title = Label(self.root, text="Restaurant Management and Billing System", bd=6, relief=GROOVE, bg="Silver", fg="Black", font=("papyrus", 30, "bold"), pady=2).pack(fill=X)
# ================variables=======================
        # => Food
        self.roti = IntVar()
        self.sabji = IntVar()
        self.paneer = IntVar()
        self.kadhi = IntVar()
        self.khichdi = IntVar()
        self.papad = IntVar()
        # => Drink
        self.coffee = IntVar()
        self.redbull = IntVar()
        self.mojito = IntVar()
        self.beer = IntVar()
        self.whiskey = IntVar()
        self.margarita = IntVar()
        # => Cake
        self.kitkat = IntVar()
        self.oreo = IntVar()
        self.redvelvet = IntVar()
        self.icecream = IntVar()
        self.blackforest = IntVar()
        self.brownie = IntVar()
        # => Total Product Price & Tax Variable
        self.food_price = StringVar()
        self.drink_price = StringVar()
        self.cake_price = StringVar()
        self.food_tax = StringVar()
        self.drink_tax = StringVar()
        self.cake_tax = StringVar()
        # => Customer
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
# -------------------------------------------Customer Detail Frame-------------------------------------------

        F1 = LabelFrame(self.root, text="Customer Details", font=('ribbon', 15, 'bold'), bd=10, fg="OrangeRed", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('futura', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg=bg_color, font=('futura', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phon, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg=bg_color, font=('futura', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('futura', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)
# -------------------------------------------Food Frams-------------------------------------------
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Food", font=("ribbon", 15, "bold"), fg="OrangeRed", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        roti_lbl = Label(F2, text="Roti", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        roti_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        roti_txt = Entry(F2, width=10, textvariable=self.roti, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        roti_txt.grid(row=0, column=1, padx=10, pady=10)

        sabji_lbl = Label(F2, text="Sabji", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        sabji_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        sabji_txt = Entry(F2, width=10, textvariable=self.sabji, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sabji_txt.grid(row=1, column=1, padx=10, pady=10)

        paneer_lbl = Label(F2, text="Paneer", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        paneer_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        paneer_txt = Entry(F2, width=10, textvariable=self.paneer, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        paneer_txt.grid(row=2, column=1, padx=10, pady=10)

        kadhi_lbl = Label(F2, text="Kadhi", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        kadhi_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        kadhi_txt = Entry(F2, width=10, textvariable=self.kadhi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        kadhi_txt.grid(row=3, column=1, padx=10, pady=10)

        khichdi_lbl = Label(F2, text="Khichdi", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        khichdi_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        khichdi_txt = Entry(F2, width=10, textvariable=self.khichdi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        khichdi_txt.grid(row=4, column=1, padx=10, pady=10)

        papad_lbl = Label(F2, text="Papad", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        papad_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        papad_txt = Entry(F2, width=10, textvariable=self.papad, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        papad_txt.grid(row=5, column=1, padx=10, pady=10)
# -------------------------------------------Drink Frams-------------------------------------------
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Drink", font=("ribbon", 15, "bold"), fg="OrangeRed", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        coffee_lbl = Label(F3, text="Coffee", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        coffee_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        coffee_txt = Entry(F3, width=10, textvariable=self.coffee, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        coffee_txt.grid(row=0, column=1, padx=10, pady=10)

        redbull_lbl = Label(F3, text="Red Bull", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        redbull_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        redbull_txt = Entry(F3, width=10, textvariable=self.redbull, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        redbull_txt.grid(row=1, column=1, padx=10, pady=10)

        mojito_lbl = Label(F3, text="Mojito", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        mojito_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        mojito_txt = Entry(F3, width=10, textvariable=self.mojito, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mojito_txt.grid(row=2, column=1, padx=10, pady=10)

        beer_lbl = Label(F3, text="Beer", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        beer_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        beer_txt = Entry(F3, width=10, textvariable=self.beer, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        beer_txt.grid(row=3, column=1, padx=10, pady=10)

        whiskey_lbl = Label(F3, text="Whiskey", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        whiskey_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        whiskey_txt = Entry(F3, width=10, textvariable=self.whiskey, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        whiskey_txt.grid(row=4, column=1, padx=10, pady=10)

        margarita_lbl = Label(F3, text="Margarita", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        margarita_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        margarita_txt = Entry(F3, width=10, textvariable=self.margarita, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        margarita_txt.grid(row=5, column=1, padx=10, pady=10)
        # -------------------------------------------Cake Frams-------------------------------------------
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cake", font=("ribbon", 15, "bold"), fg="OrangeRed",bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        kitkat_lbl = Label(F4, text="Kitkat", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        kitkat_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        kitkat_txt = Entry(F4, width=10, textvariable=self.kitkat, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        kitkat_txt.grid(row=0, column=1, padx=10, pady=10)

        oreo_lbl = Label(F4, text="Oreo", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        oreo_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        oreo_txt = Entry(F4, width=10, textvariable=self.oreo, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        oreo_txt.grid(row=1, column=1, padx=10, pady=10)

        redvelvet_lbl = Label(F4, text="Red Velvet", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        redvelvet_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        mojito_txt = Entry(F4, width=10, textvariable=self.redvelvet, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mojito_txt.grid(row=2, column=1, padx=10, pady=10)

        icecream_lbl = Label(F4, text="Icecream", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        icecream_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        icecream_txt = Entry(F4, width=10, textvariable=self.icecream, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        icecream_txt.grid(row=3, column=1, padx=10, pady=10)

        blackforest_lbl = Label(F4, text="Black Forest", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        blackforest_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        blackforest_txt = Entry(F4, width=10, textvariable=self.blackforest, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        blackforest_txt.grid(row=4, column=1, padx=10, pady=10)

        brownie_lbl = Label(F4, text="Brownie", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        brownie_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        brownie_txt = Entry(F4, width=10, textvariable=self.brownie, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        brownie_txt.grid(row=5, column=1, padx=10, pady=10)
        # -------------------------------------------Bill Detail-------------------------------------------
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Detail", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        # -------------------------------------------Button-------------------------------------------
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("ribbon", 15, "bold"), fg="OrangeRed",bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl = Label(F6, text="Total Food Price", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.food_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Drink Price", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.drink_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Cake Price", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cake_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="Food Tax", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.food_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Drink Tax", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.drink_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Cake Tax", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cake_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)
        # -------------------------------------------Main Button-------------------------------------------
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=700, width=600, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="MediumAquamarine", bd=2, fg="black", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generatebill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="MediumAquamarine", fg="black", pady=15, width=12, font='arial 13 bold')
        generatebill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="MediumAquamarine", bd=2, fg="black", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="MediumAquamarine", fg="black", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.f_roti_p = self.roti.get() * 15
        self.f_sabji_p = self.sabji.get() * 60
        self.f_paneer_p = self.paneer.get() * 120
        self.f_kadhi_p = self.kadhi.get() * 40
        self.f_khichdi_p = self.khichdi.get() * 45
        self.f_papad_p = self.papad.get() * 10
        self.total_food_price = float(
            self.f_roti_p +
            self.f_sabji_p +
            self.f_paneer_p +
            self.f_kadhi_p +
            self.f_khichdi_p +
            self.f_papad_p
        )
        self.food_price.set("₹ " + str(self.total_food_price))
        self.f_tax = round((self.total_food_price * 0.05), 2)
        self.food_tax.set("₹ " + str(self.f_tax))

        self.d_coffee_p = self.coffee.get() * 50
        self.d_redbull_p = self.redbull.get() * 125
        self.d_mojito_p = self.mojito.get() * 120
        self.d_beer_p = self.beer.get() * 250
        self.d_whiskey_p = self.whiskey.get() * 350
        self.d_margarita_p = self.margarita.get() * 300
        self.total_drink_price = float(
            self.d_coffee_p +
            self.d_redbull_p +
            self.d_mojito_p +
            self.d_beer_p +
            self.d_whiskey_p +
            self.d_margarita_p
        )
        self.drink_price.set("₹ " + str(self.total_drink_price))
        self.d_tax = round((self.total_drink_price * 0.10), 2)
        self.drink_tax.set("₹ " + str(self.d_tax))

        self.c_kitkat_p = self.kitkat.get() * 350
        self.c_oreo_p = self.oreo.get() * 400
        self.c_redvelvet_p = self.redvelvet.get() * 550
        self.c_icecream_p = self.icecream.get() * 500
        self.c_blackforest_p = self.blackforest.get() * 450
        self.c_brownie_p = self.brownie.get() * 300
        self.total_cake_price = float(
            self.c_kitkat_p +
            self.c_oreo_p +
            self.c_redvelvet_p +
            self.c_icecream_p +
            self.c_blackforest_p +
            self.c_brownie_p
        )
        self.cake_price.set("₹ " + str(self.total_cake_price))
        self.c_tax = round((self.total_cake_price * 0.15), 2)
        self.cake_tax.set("₹ " + str(self.c_tax))

        self.Total_bill = float(
            self.total_food_price +
            self.total_drink_price +
            self.total_cake_price +
            self.f_tax +
            self.d_tax +
            self.c_tax
        )

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t WELCOME TO Viraj Restaurant\n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END, "\n--------------------------------------")
        self.txtarea.insert(END, f"\n Products\t\tQTY\tPrice")
        self.txtarea.insert(END, "\n--------------------------------------")

    def bill_area(self):
        if self.c_name.get() == " " or self.c_phon.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.food_price.get() == "Rs. 0.0" and self.drink_price.get() == "Rs. 0.0" and self.cake_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            # Food
            if self.roti.get() != 0:
                self.txtarea.insert(END, f"\n Roti \t\t{self.roti.get()}\t₹ {self.f_roti_p}")
            if self.sabji.get() != 0:
                self.txtarea.insert(END, f"\n Sabji \t\t{self.sabji.get()}\t₹ {self.f_sabji_p}")
            if self.paneer.get() != 0:
                self.txtarea.insert(END, f"\n Paneer \t\t{self.paneer.get()}\t₹ {self.f_paneer_p}")
            if self.kadhi.get() != 0:
                self.txtarea.insert(END, f"\n Kadhi \t\t{self.kadhi.get()}\t₹ {self.f_kadhi_p}")
            if self.khichdi.get() != 0:
                self.txtarea.insert(END, f"\n Khichdi \t\t{self.khichdi.get()}\t₹ {self.f_khichdi_p}")
            if self.papad.get() != 0:
                self.txtarea.insert(END, f"\n Papad \t\t{self.papad.get()}\t₹ {self.f_papad_p}")
            # drink
            if self.coffee.get() != 0:
                self.txtarea.insert(END, f"\n Coffee \t\t{self.coffee.get()}\t₹ {self.d_coffee_p}")
            if self.redbull.get() != 0:
                self.txtarea.insert(END, f"\n Red Bull \t\t{self.redbull.get()}\t₹ {self.d_redbull_p}")
            if self.mojito.get() != 0:
                self.txtarea.insert(END, f"\n Mojito \t\t{self.mojito.get()}\t₹ {self.d_mojito_p}")
            if self.beer.get() != 0:
                self.txtarea.insert(END, f"\n Beer \t\t{self.beer.get()}\t₹ {self.d_beer_p}")
            if self.whiskey.get() != 0:
                self.txtarea.insert(END, f"\n Whiskey \t\t{self.whiskey.get()}\t₹ {self.d_whiskey_p}")
            if self.margarita.get() != 0:
                self.txtarea.insert(END, f"\n Margarita \t\t{self.margarita.get()}\t₹ {self.d_margarita_p}")
            # cake
            if self.kitkat.get() != 0:
                self.txtarea.insert(END, f"\n Kitkat \t\t{self.kitkat.get()}\t₹ {self.c_kitkat_p}")
            if self.oreo.get() != 0:
                self.txtarea.insert(END, f"\n Oreo \t\t{self.oreo.get()}\t₹ {self.c_oreo_p}")
            if self.redvelvet.get() != 0:
                self.txtarea.insert(END, f"\n Red Velvet \t\t{self.redvelvet.get()}\t₹ {self.c_redvelvet_p}")
            if self.icecream.get() != 0:
                self.txtarea.insert(END, f"\n Icecream \t\t{self.icecream.get()}\t₹ {self.c_icecream_p}")
            if self.blackforest.get() != 0:
                self.txtarea.insert(END, f"\n black Forest \t\t{self.blackforest.get()}\tC {self.c_blackforest_p}")
            if self.brownie.get() != 0:
                self.txtarea.insert(END, f"\n Brownie \t\t{self.brownie.get()}\t₹ {self.c_brownie_p}")

            self.txtarea.insert(END, "\n--------------------------------------")
            if self.food_tax.get() != "₹ 0.0":
                self.txtarea.insert(END, f"\n Food Tax \t\t\t{self.food_tax.get()}")
            if self.drink_tax.get() != "₹ 0.0":
                self.txtarea.insert(END, f"\n Drink Tax \t\t\t{self.drink_tax.get()}")
            if self.cake_tax.get() != "₹ 0.0":
                self.txtarea.insert(END, f"\n Cake Tax \t\t\t{self.cake_tax.get()}")
            self.txtarea.insert(END, "\n--------------------------------------")
            self.txtarea.insert(END, f"\n Total Bill \t\t\t₹ {str(self.Total_bill)}")
            self.txtarea.insert(END, "\n--------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bill/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bill/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bill/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            # => Food
            self.roti.set(0)
            self.sabji.set(0)
            self.paneer.set(0)
            self.kadhi.set(0)
            self.khichdi.set(0)
            self.papad.set(0)
            # => Drink
            self.coffee.set(0)
            self.redbull.set(0)
            self.mojito.set(0)
            self.beer.set(0)
            self.whiskey.set(0)
            self.margarita.set(0)
            # => Cake
            self.kitkat.set(0)
            self.oreo.set(0)
            self.redvelvet.set(0)
            self.icecream.set(0)
            self.blackforest.set(0)
            self.brownie.set(0)
            # => Total Product Price & Tax Variable
            self.food_price.set("")
            self.drink_price.set("")
            self.cake_price.set("")
            self.food_tax.set("")
            self.drink_tax.set("")
            self.cake_tax.set("")
            # => Customer
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()

from tkinter import *
import pandas as pd
import tkinter.messagebox
import decr

f = pd.read_csv("ATM.csv")
df = pd.DataFrame(f)
balance = 0
def verify_pin():
    def verify_pin_final():
        global e 
        acc_num = e.get()
        acc_num = int(acc_num)
        pin = df['pin'][df['Acc_Num'] == acc_num]
        print(pin)
        i = df.index[df['Acc_Num'] == acc_num].astype(int)
        print(i[0])
        res = decr.decrypt(str(pin[i[0]]), acc_num)
        print(res)
        dec = h.get()
        if str(dec) == str(res):
            check()
            v_pin.destroy()

        else:
            tkinter.messagebox.showinfo('PIN Info','The pin you entered is wrong')
            v_pin.destroy()

    v_pin = Toplevel()
    label = Label(v_pin, text = "Enter your pin")
    label.pack()
    h = Entry(v_pin)
    h.focus_set()
    h.pack()
    b = Button(v_pin, text = "Verify", command = verify_pin_final)
    b.pack()
    

def check():
    flag = False
    print("hi")
    global e
    global balance
    acc_num = e.get()
    acc_num = int(acc_num)
    for accnum in df['Acc_Num']:
        if accnum == acc_num:
            flag = True
            print(acc_num)
            count = df['total'][df['Acc_Num'] == accnum]
            balance = df['amount'][df['Acc_Num'] == accnum]
            withdraw = df['withdraw'][df['Acc_Num'] == accnum]
            deposit = df['deposit'][df['Acc_Num'] == accnum]
            withdraw = int(withdraw)
            deposit = int(deposit)
            if (withdraw > deposit):
                print(withdraw)
                withdraw_money()
            elif withdraw == deposit:
                go_to_home()
            else:
                deposit_money()
    if flag == False:
        tkinter.messagebox.showinfo('Account info','Account not Found!')
        root.destroy()
           
f = 0
def withdraw_money():
    global f
    def gohome():
        top.destroy()
        go_to_home()
    top = Toplevel()
    label3 = Label(top, text = "The result is based on your previous visits to ATM")
    label3.pack()
    label4 = Label(top, text = "Please Enter the amount to withdraw")
    label4.pack()
    f = Entry(top)
    f.focus_set()
    f.pack()
    button_2 = Button(top, text = "Withdraw")
    button_2.bind("<Button-1>", check_balance)
    button_2.pack()
    button_3 = Button(top, text = "Go to Home", command = gohome)
    button_3.pack()

g = 0

def go_to_home():
    home_page = Toplevel()
    label5 = Label(home_page, text = "Welcome to ATM")
    label5.pack()
    button_4 = Button(home_page, text = "Withdraw Money", command = withdraw_money)
    button_4.pack()
    button_5 = Button(home_page, text = "Deposit Money", command = deposit_money)
    button_5.pack()
    button_6 = Button(home_page, text = "Check Balance", command = check_bal)
    button_6.pack()

def check_bal():
    acc_num = e.get()
    acc_num = int(acc_num)
    bal = df['amount'][df['Acc_Num'] == acc_num]
    tkinter.messagebox.showinfo('Balance info',f'The Amount in your account is {int(bal)}')
    root.destroy()

def check_balance(Event):
    global balance
    global e
    acc_num = e.get()
    acc_num = int(acc_num)
    print(int(balance))
    w_money = f.get()
    if(int(balance) < int(w_money)):
        tkinter.messagebox.showinfo('Low Balance','Your balance is low please deposit money to continue OR Enter the Lower amount')
    else:
        w_money = int(w_money)
        balance = balance - w_money
        df['amount'][df['Acc_Num'] == acc_num] = balance
        count = df['total'][df['Acc_Num'] == acc_num]
        withdraw = df['withdraw'][df['Acc_Num'] == acc_num]
        count += 1
        withdraw += 1
        df['total'][df['Acc_Num'] == acc_num] = count
        df['withdraw'][df['Acc_Num'] == acc_num] = withdraw
        df.set_index("Acc_Num", inplace = True)
        df.to_csv("ATM.csv")
        print(df)
        root.destroy()

def deposit_money():
    def deposit():
        global balance
        dep_money = g.get()
        dep_money = int(dep_money)
        balance = balance + dep_money
        df['amount'][df['Acc_Num'] == acc_num] = balance
        count = df['total'][df['Acc_Num'] == acc_num]
        deposit = df['deposit'][df['Acc_Num'] == acc_num]
        count += 1
        deposit += 1
        df['total'][df['Acc_Num'] == acc_num] = count
        df['deposit'][df['Acc_Num'] == acc_num] = deposit
        df.set_index("Acc_Num", inplace = True)
        df.to_csv("ATM.csv")
        print(df)
        root.destroy()
    global g
    dep = Toplevel()
    label3 = Label(dep, text = "The result is based on your previous visits to ATM")
    label3.pack()
    label4 = Label(dep, text = "Please Enter the amount to deposit")
    label4.pack()
    acc_num = e.get()
    acc_num = int(acc_num)
    g = Entry(dep)
    g.focus_set()
    g.pack()
    button_6 = Button(dep, text = "Deposit", command = deposit)
    button_6.pack()
    button_7 = Button(dep, text = "Go to Home", command = go_to_home)
    button_7.pack()
    
root = Tk()
theLabel = Label(root, text = "ATM")
theLabel.pack()
label2 = Label(root, text = "Enter Your Account Number")
label2.pack()
e = Entry(root)
e.focus_set()
e.pack()
button_1 = Button(root, text="Next", command = verify_pin)
button_1.pack()
root.mainloop()
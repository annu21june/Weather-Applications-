from email import message
from tkinter import *
from tkinter import messagebox
import requests
import login
# import Frame3
import database
from PIL import Image, ImageTk
import login
import home

dic = {}


class frame2:

    def add1(self, city1):
        city = city1
        api_key = "6ee01bd686ddb245a7b5e0f7bd6547b0"
        base_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
        try:
            print(base_url)
            res = requests.get(base_url)
            x = res.json()
            print('X - ', x)
            print("City 1 Name ", city)
            print("City 1 base url ", base_url)
            print('City 1 Code ', x['cod'])
            print('City 1 Response - ', res)
            if x['cod'] == 200:
                print('City 1 Inside if - ', x)
                y = str(x['weather'][0]['description'])
                y1 = int(x['main']['temp'] - 273)
                y2 = int(x['main']['feels_like'] - 273)
                y3 = int(x['main']['temp_min'] - 273)
                y4 = int(x['main']['temp_max'] - 273)
                y5 = int(x['main']['pressure'])
                y6 = int(x['main']['humidity'])
                y7 = (x['weather'][0]['icon'])
                y8 = str(x['name'])
                y9 = str(x['sys']['country'])
                y10 = int(x['visibility'])
                y11 = int(x['wind']['speed'])
                y81 = str(y8 + " ," + y9)
                if (y7 == "01d"):
                    self.img1 = PhotoImage(file="weatherimages/01d.png")
                elif (y7 == "01n"):
                    self.img1 = PhotoImage(file="weatherimages/01n.png")
                elif (y7 == "02d"):
                    self.img1 = PhotoImage(file="weatherimages/02d.png")
                elif (y7 == "02n"):
                    self.img1 = PhotoImage(file="weatherimages/02n.png")
                elif (y7 == "03d"):
                    self.img1 = PhotoImage(file="weatherimages/03d.png")
                elif (y7 == "03n"):
                    self.img1 = PhotoImage(file="weatherimages/03n.png")
                elif (y7 == "04d"):
                    self.img1 = PhotoImage(file="weatherimages/04d.png")
                elif (y7 == "04n"):
                    self.img1 = PhotoImage(file="weatherimages/04n.png")
                elif (y7 == "09d"):
                    self.img1 = PhotoImage(file="weatherimages/09d.png")
                elif (y7 == "09n"):
                    self.img1 = PhotoImage(file="weatherimages/09n.png")
                elif (y7 == "10d"):
                    self.img1 = PhotoImage(file="weatherimages/10d.png")
                elif (y7 == "10n"):
                    self.img1 = PhotoImage(file="weatherimages/10n.png")
                elif (y7 == "11d"):
                    self.img1 = PhotoImage(file="weatherimages/11d.png")
                elif (y7 == "11n"):
                    self.img1 = PhotoImage(file="weatherimages/11n.png")
                elif (y7 == "13d"):
                    self.img1 = PhotoImage(file="weatherimages/13d.png")
                elif (y7 == "13n"):
                    self.img1 = PhotoImage(file="weatherimages/13n.png")
                elif (y7 == "50d"):
                    self.img1 = PhotoImage(file="weatherimages/50d.png")
                else:
                    self.img1 = PhotoImage(file="weatherimages/50n.png")

                self.label6 = Label(self.fr2, image=self.img1)
                self.label6.place(x=100, y=200, width=200, height=200)
                self.label6.config(bg="black")

                self.label7 = Label(self.fr2, text=y81)
                self.label7.place(x=100, y=170, width=200, height=40)
                self.label7.config(font=("klavika", 18, 'bold'), bg="black", fg="white")

                self.label8 = Label(self.fr2, text=str(y1) + '°C')
                self.label8.place(x=150, y=220, width=100, height=40)
                self.label8.config(font=("klavika", 22, 'bold'), bg="black", fg="white")

                self.label9 = Label(self.fr2, text=y)
                self.label9.place(x=100, y=340, width=200, height=40)
                self.label9.config(font=("klavika", 18, 'bold'), bg="black", fg="white")

                self.editCity1 = Button(self.fr2, text='Edit', command =  self.editCities1)
                self.editCity1.config(font=("Georgia", 16, 'bold'), bg="black", fg="white")
                self.editCity1.place(x = 150, y = 450, width=100, height=40)

            else:
                messagebox.showerror("Attention", x['message'])
        except:
            print("Api Response ", base_url)
            messagebox.showerror("Attention", "SomeThing Went Wrong check your Connection")

    def add2(self, city2):
        city2 = city2
        api_key = "6ee01bd686ddb245a7b5e0f7bd6547b0"
        base_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city2 + "&appid=" + api_key
        try:
            res = requests.get(base_url)
            x = res.json()
            print('X - ', x)
            print("City 2 Name ", city2)
            print("City 2 base url ", base_url)
            print('City 2 Code ', x['cod'])
            print('City 2 Response - ', res)
            if x['cod'] == 200:
                # print(x)
                print('City 2 Inside if - ', x)
                y = str(x['weather'][0]['description'])
                y1 = int(x['main']['temp'] - 273)
                y2 = int(x['main']['feels_like'] - 273)
                y3 = int(x['main']['temp_min'] - 273)
                y4 = int(x['main']['temp_max'] - 273)
                y5 = int(x['main']['pressure'])
                y6 = int(x['main']['humidity'])
                y7 = (x['weather'][0]['icon'])
                y8 = str(x['name'])
                y9 = str(x['sys']['country'])
                y10 = int(x['visibility'])
                y11 = int(x['wind']['speed'])
                y81 = str(y8 + " ," + y9)
                if (y7 == "01d"):
                    self.img2 = PhotoImage(file="weatherimages/01d.png")
                elif (y7 == "01n"):
                    self.img2 = PhotoImage(file="weatherimages/01n.png")
                elif (y7 == "02d"):
                    self.img2 = PhotoImage(file="weatherimages/02d.png")
                elif (y7 == "02n"):
                    self.img2 = PhotoImage(file="weatherimages/02n.png")
                elif (y7 == "03d"):
                    self.img2 = PhotoImage(file="weatherimages/03d.png")
                elif (y7 == "03n"):
                    self.img2 = PhotoImage(file="weatherimages/03n.png")
                elif (y7 == "04d"):
                    self.img2 = PhotoImage(file="weatherimages/04d.png")
                elif (y7 == "04n"):
                    self.img2 = PhotoImage(file="weatherimages/04n.png")
                elif (y7 == "09d"):
                    self.img2 = PhotoImage(file="weatherimages/09d.png")
                elif (y7 == "09n"):
                    self.img2 = PhotoImage(file="weatherimages/09n.png")
                elif (y7 == "10d"):
                    self.img2 = PhotoImage(file="weatherimages/10d.png")
                elif (y7 == "10n"):
                    self.img2 = PhotoImage(file="weatherimages/10n.png")
                elif (y7 == "11d"):
                    self.img2 = PhotoImage(file="weatherimages/11d.png")
                elif (y7 == "11n"):
                    self.img2 = PhotoImage(file="weatherimages/11n.png")
                elif (y7 == "13d"):
                    self.img2 = PhotoImage(file="weatherimages/13d.png")
                elif (y7 == "13n"):
                    self.img2 = PhotoImage(file="weatherimages/13n.png")
                elif (y7 == "50d"):
                    self.img2 = PhotoImage(file="weatherimages/50d.png")
                else:
                    self.img2 = PhotoImage(file="weatherimages/50n.png")

                self.label6 = Label(self.fr2, image=self.img2)
                self.label6.place(x=400, y=200, width=200, height=200)
                self.label6.config(bg="black")

                self.label7 = Label(self.fr2, text=y81)
                self.label7.place(x=400, y=170, width=200, height=40)
                self.label7.config(font=("klavika", 18, 'bold'), bg="black", fg="white")

                self.label8 = Label(self.fr2, text = str(y1) + '°C')
                self.label8.place(x=450, y=220, width=100, height=40)
                self.label8.config(font=("klavika", 22, 'bold'), bg="black", fg="white")

                self.label9 = Label(self.fr2, text=y)
                self.label9.place(x=400, y=340, width=200, height=40)
                self.label9.config(font=("klavika", 18, 'bold'), bg="black", fg="white")

                self.editCity2 = Button(self.fr2, text='Edit', command=self.editCities2)
                self.editCity2.config(font=("Georgia", 16, 'bold'), bg="black", fg="white")
                self.editCity2.place(x = 450, y = 450, width=100, height=40)

            else:
                messagebox.showerror("Attention", x['message'])

        except:
            messagebox.showerror("Attention", "SomeThing Went Wrong check your Connection")

    def add3(self, city3):
        city3 = city3
        api_key = "6ee01bd686ddb245a7b5e0f7bd6547b0"
        base_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city3 + "&appid=" + api_key
        try:
            res = requests.get(base_url)
            x = res.json()
            print("City 3 Name ", city3)
            print("City 3 base url ", base_url)
            print('City 3 Code ', x['cod'])
            print('City 3 Response - ', res)
            if x['cod'] == 200:
                # print(x)
                print('City 3 Inside if - ', x)
                y = str(x['weather'][0]['description'])
                y1 = int(x['main']['temp'] - 273)
                y2 = int(x['main']['feels_like'] - 273)
                y3 = int(x['main']['temp_min'] - 273)
                y4 = int(x['main']['temp_max'] - 273)
                y5 = int(x['main']['pressure'])
                y6 = int(x['main']['humidity'])
                y7 = (x['weather'][0]['icon'])
                y8 = str(x['name'])
                y9 = str(x['sys']['country'])
                y10 = int(x['visibility'])
                y11 = int(x['wind']['speed'])
                y81 = str(y8 + " ," + y9)
                if (y7 == "01d"):
                    self.img3 = PhotoImage(file="weatherimages/01d.png")
                elif (y7 == "01n"):
                    self.img3 = PhotoImage(file="weatherimages/01n.png")
                elif (y7 == "02d"):
                    self.img3 = PhotoImage(file="weatherimages/02d.png")
                elif (y7 == "02n"):
                    self.img3 = PhotoImage(file="weatherimages/02n.png")
                elif (y7 == "03d"):
                    self.img3 = PhotoImage(file="weatherimages/03d.png")
                elif (y7 == "03n"):
                    self.img3 = PhotoImage(file="weatherimages/03n.png")
                elif (y7 == "04d"):
                    self.img3 = PhotoImage(file="weatherimages/04d.png")
                elif (y7 == "04n"):
                    self.img3 = PhotoImage(file="weatherimages/04n.png")
                elif (y7 == "09d"):
                    self.img3 = PhotoImage(file="weatherimages/09d.png")
                elif (y7 == "09n"):
                    self.img3 = PhotoImage(file="weatherimages/09n.png")
                elif (y7 == "10d"):
                    self.img3 = PhotoImage(file="weatherimages/10d.png")
                elif (y7 == "10n"):
                    self.img3 = PhotoImage(file="weatherimages/10n.png")
                elif (y7 == "11d"):
                    self.img3 = PhotoImage(file="weatherimages/11d.png")
                elif (y7 == "11n"):
                    self.img3 = PhotoImage(file="weatherimages/11n.png")
                elif (y7 == "13d"):
                    self.img3 = PhotoImage(file="weatherimages/13d.png")
                elif (y7 == "13n"):
                    self.img3 = PhotoImage(file="weatherimages/13n.png")
                elif (y7 == "50d"):
                    self.img3 = PhotoImage(file="weatherimages/50d.png")
                else:
                    self.img3 = PhotoImage(file="weatherimages/50n.png")

                self.label10 = Label(self.fr2, image=self.img3)
                self.label10.place(x=700, y=200, width=200, height=200)
                self.label10.config(bg="black")

                self.label11 = Label(self.fr2, text=y81)
                self.label11.place(x=700, y=170, width=200, height=40)
                self.label11.config(font=("klavika", 18, 'bold'), bg="black", fg="white")

                self.label12 = Label(self.fr2, text = str(y1) + '°C')
                self.label12.place(x=750, y=220, width=100, height=40)
                self.label12.config(font=("klavika", 22, 'bold'), bg="black", fg="white")

                self.label13 = Label(self.fr2, text=y)
                self.label13.place(x=700, y=340, width=200, height=40)
                self.label13.config(font=("klavika", 18, 'bold'), bg="black", fg="white")

                self.editCity3 = Button(self.fr2, text='Edit', command=self.editCities3)
                self.editCity3.config(font=("Georgia", 16, 'bold'), bg="black", fg="white")
                self.editCity3.place(x = 750, y = 450, width=100, height=40)

            else:
                messagebox.showerror("Attention", x['message'])

        except:
            messagebox.showerror("Attention", "SomeThing Went Wrong check your Connection")

    def addcity1(self):
        self.ent1 = Entry(self.fr2)
        self.ent1.place(x=100, y=200, width=200, height=30)
        self.ent1.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

        self.btn1 = Button(self.fr2, text="Add", command = lambda: self.add1(self.ent1.get()))
        self.btn1.place(x=140, y=250, width=100, height=30)
        self.btn1.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

    def addcity2(self):
        self.ent2 = Entry(self.fr2)
        self.ent2.place(x=400, y=200, width=200, height=30)
        self.ent2.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

        self.btn2 = Button(self.fr2, text="Add", command = lambda: self.add2(self.ent2.get()))
        self.btn2.place(x=440, y=250, width=100, height=30)
        self.btn2.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

    def addcity3(self):
        self.ent3 = Entry(self.fr2)
        self.ent3.place(x=700, y=200, width=200, height=30)
        self.ent3.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

        self.btn = Button(self.fr2, text="Add", command=lambda: self.add3(self.ent3.get()))
        self.btn.place(x=740, y=250, width=100, height=30)
        self.btn.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

    def logout(self):
        a = messagebox.askyesno("Attention", "Do you want to logout?")
        if a:
            self.fr2.destroy()
            obj = login.loginWindow()
            obj.loginFrame()

    def frnd(self):
        self.fr2.destroy()
        # obj = Frame3.frame3(self.root)
        # obj.create3()

    def __init__(self, root=""):
        if (root == ""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("Weather Application")
        self.root.geometry("1370x750")
        self.root.configure(bg="#d7dae2")

        #to make window in center
        self.fullwidth=self.root.winfo_screenwidth()
        self.fullheight=self.root.winfo_screenheight()
        self.width=int((self.fullwidth-1370)/2)
        self.height=int((self.fullheight-750)/2)
        s="1370x750+" +str(self.width)+ "+" +str(self.height)
        self.root.resizable(height=False,width=False)

    def create2(self, a):
        print(f'user data is {a}')
        global dic
        dic = a.copy()
        self.data = dic
        self.fr2 = Frame(self.root)
        # self.fr2.pack()
        self.fr2.place(x=0, y=0, width=1370, height=750)
        self.fr2.config(bg="#d7dae2")

        # self.img = PhotoImage(file="images/gradient_wallpaper_1.gif")
        # self.imglbl = Label(self.fr2, image=self.img)
        # self.imglbl.place(x=0, y=0, width=1000, height=600)

        # self.image2 = Image.open("images/tal.png")
        # self.bgImage2 = ImageTk.PhotoImage(self.image2)
        # self.bgLabel2 = Label(self.root, image=self.bgImage2)
        # self.bgLabel2.place(x = 350, y = 0, width = "200", height = "195")

        self.lbl = Label(self.fr2, text="Your Saved Cities")
        self.lbl.place(x=20, y=20, width=400, height=40)
        self.lbl.config(font=('klavika', 30, 'bold'))

        self.lbl1 = Label(self.fr2, text="(Any three)")
        self.lbl1.place(x=400, y=35, width=100, height=20)
        self.lbl1.config(font=('klavika', 14, 'bold'))

        self.back=Button(self.root,text=("BACK"),width=23,height=2,bg='#ed3833',fg="white",bd=0,command=self.back_button)
        self.back.place(x=1250, y=0, width=100, height=40)
        # self.btn.config(font=("Georgia", 16, 'bold'), bg="red", fg="white")

        if (dic['city1'] == '' or dic['city2'] == '' or dic['city3'] == ''):
            self.btn = Button(self.fr2, text="Save", command=self.save)
            self.btn.place(x=450, y=480, width=100, height=40)
            self.btn.config(font=("Georgia", 16, 'bold'), bg="black", fg="white")

        if (a['city1'] != ''):
            self.add1(a['city1'])
            # self.lbl2 = Label(self.fr2, text=a['city1'])
            # self.lbl2.place(x=100, y=200, width=200, height=30)
            # self.lbl2.config(font=('klavika', 14, 'bold'), bg="black", fg="white")
        else:
            self.lbl2 = Label(self.fr2, text="Nothing to Show")
            self.lbl2.place(x=100, y=200, width=200, height=30)
            self.lbl2.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

            self.btn1 = Button(self.fr2, text="Add City", command=self.addcity1)
            self.btn1.place(x=140, y=250, width=100, height=30)
            self.btn1.config(font=('klavika', 14, 'bold'), bg="black", fg="white")
        if (a['city2'] != ''):
            self.add2(a['city2'])
            # self.lbl3 = Label(self.fr2, text=a['city2'])
            # self.lbl3.place(x=400, y=200, width=200, height=30)
            # self.lbl3.config(font=('klavika', 14, 'bold'), bg="black", fg="white")
        else:
            self.lbl3 = Label(self.fr2, text="Nothing to Show")
            self.lbl3.place(x=400, y=200, width=200, height=30)
            self.lbl3.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

            self.btn2 = Button(self.fr2, text="Add City", command=self.addcity2)
            self.btn2.place(x=440, y=250, width=100, height=30)
            self.btn2.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

        if (a['city3'] != ''):
            self.add3(a['city3'])
            # self.lbl4 = Label(self.fr2, text=a['city3'])
            # self.lbl4.place(x=700, y=200, width=200, height=30)
            # self.lbl4.config(font=('klavika', 14, 'bold'), bg="black", fg="white")
        else:
            self.lbl4 = Label(self.fr2, text="Nothing to Show")
            self.lbl4.place(x=700, y=200, width=200, height=30)
            self.lbl4.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

            self.btn3 = Button(self.fr2, text="Add City", command=self.addcity3)
            self.btn3.place(x=740, y=250, width=100, height=30)
            self.btn3.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

    def save(self):
        if self.ent1.get() == '':
            messagebox.showinfo('Alert', 'Add city 1')
        elif self.ent2.get() == '':
            messagebox.showinfo('Alert', 'Add city 2')
        elif self.ent3.get() == '':
            messagebox.showinfo('Alert', 'Add city 3')
        else:
            city1 = self.ent1.get()
            city2 = self.ent2.get()
            city3 = self.ent3.get()
            username = dic['username']
            password = dic['Password']
            loggedId = dic['id']
            data1 = (city1, city2, city3, loggedId)
            print("User data and Cities ", data1)
            result = database.city(data1)
            if result:
                messagebox.showinfo("Message", "Cities added successfully")
            else:
                messagebox.showerror("Alert", "Please try again")

    def back_button(self):        
        self.root.destroy()
        Obj1 =home.AdminNav()
        Obj1.navframe(dic)


    def editCities1(self):
        self.edC1 = Entry(self.fr2)
        self.edC1.place(x=100, y=415, width=200, height=30)
        self.edC1.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

        self.edC1btn = Button(self.fr2, text='Edit', command=lambda x = 'city1': self.edit_City1(x))
        self.edC1btn.place(x = 150, y = 450, width=100, height=40)
        self.edC1btn.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

    def editCities2(self):
        self.edC2 = Entry(self.fr2)
        self.edC2.place(x=400, y=415, width=200, height=30)
        self.edC2.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

        self.edC2btn = Button(self.fr2, text='Edit', command=lambda x = 'city2': self.edit_City2(x))
        self.edC2btn.place(x = 450, y = 450, width=100, height=40)
        self.edC2btn.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

    
    def editCities3(self):
        self.edC3 = Entry(self.fr2)
        self.edC3.place(x=700, y=415, width=200, height=30)
        self.edC3.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

        self.edC3btn = Button(self.fr2, text='Edit', command=lambda x = 'city3': self.edit_City3(x))
        self.edC3btn.place(x = 750, y = 450, width=100, height=40)
        self.edC3btn.config(font=('klavika', 14, 'bold'), bg="black", fg="white")

    def edit_City1(self, cityNum):
        if self.edC1.get() == '':
            messagebox.showerror('Alert', 'Please enter city')
        else:
            if cityNum == 'city1':
                res = database.editCity1((self.edC1.get(), self.data.get('id')))
                if res:
                    self.add1(self.edC1.get())
                    self.edC1.destroy()
                    messagebox.showinfo('Success', 'First city updated successfully.')
                else:
                    messagebox.showerror('Alert', 'Something went wrong. Please try again.')
        
    def edit_City2(self, cityNum):
        if cityNum == 'city2':
            res = database.editCity2((self.edC2.get(), self.data.get('id')))
            if res:
                self.add2(self.edC2.get())
                self.edC2.destroy()
                messagebox.showinfo('Success', 'Second city updated successfully.')
            else:
                messagebox.showerror('Alert', 'Something went wrong. Please try again.')
    
    def edit_City3(self, cityNum):
        if cityNum == 'city3':
            res = database.editCity3((self.edC3.get(), self.data.get('id')))
            if res:
                self.add3(self.edC3.get())
                self.edC3.destroy()
                messagebox.showinfo('Success', 'Third city updated successfully.')
            else:
                messagebox.showerror('Alert', 'Something went wrong. Please try again.')


if __name__ == '__main__':
    obj = frame2()
    obj.create2()
    obj.root.mainloop()

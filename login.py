from tkinter import *
from PIL import ImageTk, Image
import PIL
from tkinter import messagebox
import home
import register
import copy_search

import database

class loginWindow:
  
    logData = dict()
    def __init__(self):    
        self.root = Tk()
        self.root.title('Weather Application')
        self.root.geometry("1370x750")
        self.root.configure(bg="#d7dae2")

        #to make window in center
        self.fullwidth=self.root.winfo_screenwidth()
        self.fullheight=self.root.winfo_screenheight()
        self.width=int((self.fullwidth-1370)/2)
        self.height=int((self.fullheight-750)/2)
        s="1370x750+" +str(self.width)+ "+" +str(self.height)
        self.root.resizable(height=False,width=False)
        
    def loginFrame(self):
        self.login = Frame(self.root)
        self.login.pack()
        



        #title
        
        self.title=Label(text="LOGIN SYSTEM",font=("arial",32,"bold","underline"),fg="black",bg="#d7dae2")
        self.title.pack(pady=50) 

        
        self.image = Image.open("images/ooo.png")
        self.bgImage = ImageTk.PhotoImage(self.image)
        self.bgLabel = Label(self.root, image=self.bgImage,bg="#d7dae2")
        self.bgLabel.place(x = 870, y = 10, width = "225", height = "225")

        self.logo =Image.open("images/okj.png")
      
        self.bglogo = ImageTk.PhotoImage(self.logo)
        self.bgLabel1 = Label(self.root, image=self.bglogo)
        self.bgLabel1.place(x = 400, y = 40, width = "80", height = "80")
      #center
      
        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        self.width = int((self.fullwidth-1280)/2)
        self.height=int((self.fullheight-750)/2)

        s = "1280x750+" +str(self.width)+ "+" +str(self.height)
    

        # so screen cant be resized
        self.root.resizable(height=False,width=False)
        
        
         
         
        #BORDER

        self.bordercolor=Frame(self.root,bg="black",width=800,height=400) 
        self.bordercolor.pack() 

        #FRAME
         
        self.mainframe=Frame(self.bordercolor,bg="#d7dae2",width=800,height=400)
        self.mainframe.pack(padx=20,pady=20)

        
        #entryes
        self.nam=Entry(self.mainframe,width=14,font=('arial',30),bd=2)
        self.nam.place(x=400,y=60)
        self.password=Entry(self.mainframe,width=14,font=('arial',30),bd=2, show='*')
        self.password.place(x=400,y=165)


        #buttons
        
        self.login_1=Button(self.mainframe,text=("LOGIN"),width=23,height=2,bg='#ed3833',fg="white", command = self.loginUser, bd=0,)
        self.login_1.place(x=100,y=300)
        self.login_1=Button(self.mainframe,text=("CREATE NEW ACCOUNT"),width=30,height=2,bg='#1089ff',fg="white",bd=0,command=self.Register)
        self.login_1.place(x=300,y=300)
        self.login_1=Button(self.mainframe,text=("SEARCH WEATHER"),width=20,height=2,bg='#00bd56',fg="white",bd=0, command = self.searchWeather)
        self.login_1.place(x=550,y=300)


       #lables

    
        self.name=Label(self.mainframe,text="USER NAME :-",font=("arial",30,"bold"),fg="black",bg="#d7dae2")
        self.name.place(x=100,y=60)
        self.pasword=Label(self.mainframe,text="PASSWORD:-",font=("arial",30,"bold"),fg="black",bg="#d7dae2")
        self.pasword.place(x=100,y=165)  

        data = (
            self.nam.get(),
            self.password.get()
        )

        self.logData = data
        
        self.root.mainloop()
    
    def loginUser(self):
        data = (
            self.nam.get(),
            self.password.get()
        )

        self.logData = data
        if self.nam.get() == '':
            messagebox.showinfo('Alert', 'Please enter an username.')
        if self.password.get() == '':
            messagebox.showinfo('Alert', 'Please enter your password.')
        else:
            res = database.login(data)
            print(res)
            if res:
                messagebox.showinfo('Success', 'Login Successfully')
                self.root.destroy()
                homeObj = home.AdminNav()
                homeObj.navframe(res)
            else:
                messagebox.showinfo('Alert', 'Invalid username and/or password')
          

         
        
    def Register(self):
        self.root.destroy()
        registerObj = register.register()
        registerObj.registerFrame()

    
    def searchWeather(self):
        self.root.destroy()
        searchObj = copy_search.search('without_login')
        searchObj.search_frame('')

    def loginData(self):
        return self.logData

if __name__ == "__main__":
    loginObj = loginWindow()
    loginObj.loginFrame()
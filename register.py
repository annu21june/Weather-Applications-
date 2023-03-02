from email import message
from tkinter import *
from PIL import ImageTk, Image
import PIL
from tkinter import messagebox
import login
import database
class register:
  
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
         
         
        
    def registerFrame(self):
        self.login = Frame(self.root)
        self.login.pack()


#title
        self.title=Label(text="------ CREATE  ACCOUNT ------",font=("arial",30,"bold"),fg="black",bg="#d7dae2")
        self.title.pack(pady=50)

        
        self.image = Image.open("images/ooo.png")
        self.bgImage = ImageTk.PhotoImage(self.image)
        self.bgLabel = Label(self.root, image=self.bgImage)
        self.bgLabel.place(x = 10, y = 10, width = "225", height = "225")
        
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
    
        selfbordercolor=Frame(self.root,bg="black",width=800,height=400) 
        selfbordercolor.pack() 
         
         #FRAMES
        mainframe=Frame(selfbordercolor,bg="#d7dae2",width=800,height=400)
        mainframe.pack(padx=20,pady=20)

        
        #entryes
        self.nam1=Entry(mainframe,width=12,font=('arial',30),bd=2)
        self.nam1.place(x=400,y=40)
        self.pas1=Entry(mainframe,width=12,font=('arial',30),bd=2, show='*')
        self.pas1.place(x=400,y=120)
        self.pas2=Entry(mainframe,width=12,font=('arial',30),bd=2, show='*')
        self.pas2.place(x=400,y=200)
        self.locEntry=Entry(mainframe,width=12,font=('arial',30),bd=2)
        self.locEntry.place(x=400,y=270)

        # location
        

        #buttons
        
        self.login_1=Button(mainframe,text=("SIGN UP"),width=23,height=2,bg='#ed3833',fg="white",bd=0,command=self.Password)
        self.login_1.place(x=350,y=340)
    
        self.login_1=Button(mainframe,text=("sign in"),width=10,height=1,bg='#d7dae2',fg="blue",bd=0,command=self.loginMe)
        self.login_1.place(x=460,y=375)


       #lables

    
        self.name1=Label(mainframe,text="USER NAME :-",font=("arial",18,"bold"),fg="black",bg="#d7dae2")
        self.name1.place(x=100,y=45)
        self.pasword1=Label(mainframe,text="PASSWORD:-",font=("arial",18,"bold"),fg="black",bg="#d7dae2")
        self.pasword1.place(x=100,y=125)
        self.pasword2=Label(mainframe,text="CONFIRM-PASSWORD:-",font=("arial",18,"bold"),fg="black",bg="#d7dae2")
        self.pasword2.place(x=100,y=200)
        self.pasword=Label(mainframe,text="Already have an account?",font=("arial",10,"bold"),fg="black",bg="#d7dae2")
        self.pasword.place(x=300,y=375)

        self.locLabel = Label(mainframe, text="Location:-".upper(), font=("arial",18,"bold"),fg="black",bg="#d7dae2")
        self.locLabel.place(x = 100, y = 270)

        self.root.mainloop()

    def loginMe(self):
        # print("login")        
        self.root.destroy()
        Obj = login.loginWindow()
        Obj.loginFrame()


    def Password(self):
        
        
        data = (
            self.nam1.get(),
            self.pas1.get(),
            self.locEntry.get()
        )

        if self.nam1.get() == '':
            messagebox.showinfo('Alert', 'Please enter an username.')
        elif self.pas1.get() == '':
            messagebox.showinfo('Alert', 'Please enter your password.')
        elif self.pas2.get() == '':
            messagebox.showinfo('Alert', 'Please enter valid password.')
        elif self.pas1.get() != self.pas2.get():
            messagebox.showinfo('Alert', 'Passwords must match.')
        elif self.locEntry.get() == '':
            messagebox.showerror('Alert', 'Please enter your location.')
        else:
            res = database.register(data)
            if res:
                messagebox.showinfo('Success', 'User registered successfully.')
                self.root.destroy()
                loginObj = login.loginWindow()
                loginObj.loginFrame()
            else:
                messagebox.showinfo('Alert', 'Something went wrong. Please try again.')    
            
        

if __name__ == "__main__":
    loginObj = register()
    loginObj.registerFrame()
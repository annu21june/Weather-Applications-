from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
import PIL
import requests
import login


class search:
  
    API_KEY = "6ee01bd686ddb245a7b5e0f7bd6547b0"

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
        
    def search_frame(self):
        self.login = Frame(self.root)
        self.login.pack()




        

        self.image2 = Image.open("images/tal.png")
        self.bgImage2 = ImageTk.PhotoImage(self.image2)
        self.bgLabel2 = Label(self.root, image=self.bgImage2)
        self.bgLabel2.place(x = 350, y = 0, width = "200", height = "195")


      #BUTTONS
      
        self.back=Button(self.root,text=("BACK"),width=23,height=2,bg='#ed3833',fg="white",bd=0,command=self.back_button)
        self.back.place(x=650,y=280)
        
        #title

        self.title=Label(self.root,text='Weather',font=('arial',35,'underline'),bg="#d7dae2")
        self.title.place(x=30,y=40)

          #buttons

        self.button=Button(self.root,text='search',width=8,height=2,bg='black',fg="white", command = self.searchWeather)
        self.button.place(x=300,y=154)

           #buttons

        self.click=Button(self.root,bg="#d7dae2")
        self.click.place(x=100,y=470,width=40,height=30)
        self.click=Button(self.root,bg="#d7dae2")
        self.click.place(x=280,y=470,width=40,height=30)
        self.click=Button(self.root,bg="#d7dae2")
        self.click.place(x=460,y=470,width=40,height=30)
        self.click=Button(self.root,bg="#d7dae2")
        self.click.place(x=630,y=470,width=40,height=30)
        self.click=Button(self.root,bg="#d7dae2")
        self.click.place(x=800,y=470,width=40,height=30)
       #lables
         #daily
        self.a=Label(self.root,text='Daily',bg="#d7dae2",font=('arial',20,'underline'))
        self.a.place(x=20,y=280)

        self.b=Label(self.root,text='Mon 16',bg="#d7dae2",font=('arial',14,'bold'))
        self.b.place(x=80,y=340)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',18,'bold'))
        self.C.place(x=80,y=400)
        self.D=Label(self.root,text='most sunny',bg="#d7dae2",font=('arial',14,'bold'))
        self.D.place(x=80,y=430)

        self.b=Label(self.root,text='tue 17',bg="#d7dae2",font=('arial',16,'bold'))
        self.b.place(x=250,y=340)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',18,'bold'))
        self.C.place(x=250,y=400)
        self.D=Label(self.root,text='most cloudly',bg="#d7dae2",font=('arial',14,'bold'))
        self.D.place(x=250,y=430)


        self.b=Label(self.root,text='wed 18',bg="#d7dae2",font=('arial',16,'bold'))
        self.b.place(x=420,y=340)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',18,'bold'))
        self.C.place(x=420,y=400)
        self.D=Label(self.root,text='most cloudly',bg="#d7dae2",font=('arial',14,'bold'))
        self.D.place(x=420,y=430)

        self.b=Label(self.root,text='thr 19',bg="#d7dae2",font=('arial',16,'bold'))
        self.b.place(x=590,y=340)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',18,'bold'))
        self.C.place(x=590,y=400)
        self.D=Label(self.root,text='most cloudly',bg="#d7dae2",font=('arial',14,'bold'))
        self.D.place(x=590,y=430) 

        self.b=Label(self.root,text='fri 19',bg="#d7dae2",font=('arial',16,'bold'))
        self.b.place(x=760,y=340)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',18,'bold'))
        self.C.place(x=760,y=400)
        self.D=Label(self.root,text='most cloudly',bg="#d7dae2",font=('arial',14,'bold'))
        self.D.place(x=760,y=430)

       #hourly

        
        self.a=Label(self.root,text='Hourly',bg="#d7dae2",font=('arial',20,'underline'))
        self.a.place(x=20,y=540)

        self.b=Label(self.root,text='12:PM',bg="#d7dae2",font=('arial',12,'bold'))
        self.b.place(x=80,y=600)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',17,'bold'))
        self.C.place(x=80,y=640)
        self.D=Label(self.root,text='most sunny',bg="#d7dae2",font=('arial',12,'bold'))
        self.D.place(x=80,y=670)

        
        self.b=Label(self.root,text='12:PM',bg="#d7dae2",font=('arial',12,'bold'))
        self.b.place(x=240,y=600)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',17,'bold'))
        self.C.place(x=240,y=640)
        self.D=Label(self.root,text='most sunny',bg="#d7dae2",font=('arial',12,'bold'))
        self.D.place(x=240,y=670)

        
        self.b=Label(self.root,text='12:PM',bg="#d7dae2",font=('arial',12,'bold'))
        self.b.place(x=410,y=600)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',17,'bold'))
        self.C.place(x=410,y=640)
        self.D=Label(self.root,text='most sunny',bg="#d7dae2",font=('arial',12,'bold'))
        self.D.place(x=410,y=670)

        
        self.b=Label(self.root,text='12:PM',bg="#d7dae2",font=('arial',12,'bold'))
        self.b.place(x=580,y=600)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',17,'bold'))
        self.C.place(x=580,y=640)
        self.D=Label(self.root,text='most sunny',bg="#d7dae2",font=('arial',12,'bold'))
        self.D.place(x=580,y=670)

        
        self.b=Label(self.root,text='12:PM',bg="#d7dae2",font=('arial',12,'bold'))
        self.b.place(x=750,y=600)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',17,'bold'))
        self.C.place(x=750,y=640)
        self.D=Label(self.root,text='most sunny',bg="#d7dae2",font=('arial',12,'bold'))
        self.D.place(x=750,y=670)

        
        self.b=Label(self.root,text='12:PM',bg="#d7dae2",font=('arial',12,'bold'))
        self.b.place(x=920,y=600)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',17,'bold'))
        self.C.place(x=920,y=640)
        self.D=Label(self.root,text='most sunny',bg="#d7dae2",font=('arial',12,'bold'))
        self.D.place(x=920,y=670)

        
        self.b=Label(self.root,text='12:PM',bg="#d7dae2",font=('arial',12,'bold'))
        self.b.place(x=1090,y=600)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',17,'bold'))
        self.C.place(x=1090,y=640)
        self.D=Label(self.root,text='most sunny',bg="#d7dae2",font=('arial',12,'bold'))
        self.D.place(x=1090,y=670)

        
        self.b=Label(self.root,text='12:PM',bg="#d7dae2",font=('arial',12,'bold'))
        self.b.place(x=1260,y=600)
        self.C=Label(self.root,text='87°C',bg="#d7dae2",font=('arial',17,'bold'))
        self.C.place(x=1260,y=640)
        self.D=Label(self.root,text='most sunny',bg="#d7dae2",font=('arial',12,'bold'))
        self.D.place(x=1250,y=670)
        #entryes
        self.entry=Entry(self.root,width=14,font=('arial',25),bd=2)
        self.entry.place(x=10,y=150)
       
      
      #center
      
        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        self.width = int((self.fullwidth-1280)/2)
        self.height=int((self.fullheight-750)/2)

        s = "1280x750+" +str(self.width)+ "+" +str(self.height)
    

        # so screen cant be resized
        self.root.resizable(height=False,width=False)
        
        
        self.root.mainloop()
         
      
    def back_button(self):        
        self.root.destroy()
        Obj2 = login.loginWindow()
        Obj2.loginFrame()
      
      
      
        #self.image = Image.open("images/ooo.png")
        #self.bgImage = ImageTk.PhotoImage(self.image)
        #self.bgLabel = Label(self.bordercolor, image=self.bgImage)
        #self.bgLabel.place(x=50, y = 60, width = "140", height = "140")
      
        
         #title
       # self.title=Label(text="WEATHER",font=("arial",40,"bold","underline"),fg="black",bg="#d7dae2")
        #self.title.place(x=680,y=20)
        #BORDER

        self.bordercolor=Frame(self.root,bg="#d7dae2",width=10,height=50) 
        self.bordercolor.place(x=600,y=10) 

        self.mainframe=Frame(self.bordercolor,bg="#d7dae2",width=400,height=250)
        self.mainframe.pack(padx=1,pady=1)


       
        #logo

        self.root.mainloop()

      


    def searchWeather(self):
      if self.entry.get() == '':
        messagebox.showinfo('Alert', 'Please enter city name first.')
      
      else:

        for widget in self.mainframe.winfo_children():
          widget.destroy()


        self.cityName = self.entry.get()
        self.entry.delete(0, 'end')
        self.api_address = "https://api.openweathermap.org/data/2.5/weather?q=" + self.cityName + "&appid=" + self.API_KEY

        print(self.api_address)

        try:
          res = requests.get(self.api_address)
          print(res)
          data = res.json()
          print(data)

          self.weatherData = dict()
          self.weatherData['cityName'] = data['name']
          self.weatherData['temp'] = str(int(data['main']['temp']) - 273) + '°C'
          self.weatherData['icon'] = data['weather'][0]['icon']
          self.weatherData['temp_min']='temp_min :' + str(int(data['main']['temp_min'])-273)+ '°C'
          self.weatherData['temp_max']='temp_max :' + str(int(data['main']['temp_max'])-273)+ '°C'
          self.weatherData['main'] = data['weather'][0]['main']
          self.weatherData['pressure']='pressure :'+ (str(data['main']['pressure']))
          self.weatherData['humidity']='humidity :'+ (str(data['main']['humidity']))+ '%'
         
          self.weatherData['sunrise']='sunrise :'+ (str(data['sys']['sunrise']))
          self.weatherData['speed']='wind speed :'+ (str(data['wind']['speed']))+ 'km/h'
          self.weatherData['sunset']='sunset :'+ (str(data['sys']['sunset']))
         
          print(self.weatherData['cityName'])
          print(self.weatherData['temp'])
          print(self.weatherData['icon'])
          print(self.weatherData['temp_min'])
          print(self.weatherData['main'])
          print(self.weatherData['temp_max'])
          print(self.weatherData['pressure'])
          print(self.weatherData['humidity'])
          
          print(self.weatherData['sunset'])
 
          print(self.weatherData['speed'])
 
 
          #FRAME
         

          if self.weatherData['icon'] == '01d':
            self.image = "weatherimages/01d.png"
            
          elif self.weatherData['icon'] == '01n':
            self.image = "weatherimages/01n.png"
          elif self.weatherData['icon'] == '02n':
            self.image = "weatherimages/02n.png"
          elif self.weatherData['icon'] == '02d':
            self.image = "weatherimages/02d.png"
          elif self.weatherData['icon'] == '03d':
            self.image = "weatherimages/03d.png"
            
          elif self.weatherData['icon'] == '03n':
            self.image = "weatherimages/03n.png"
          elif self.weatherData['icon'] == '04d':
            self.image = "weatherimages/04d.png"
          elif self.weatherData['icon'] == '04n':
            self.image = "weatherimages/04n.png"
          elif self.weatherData['icon'] == '09d':
            self.image = "weatherimages/09d.png"
          elif self.weatherData['icon'] == '09n':
            self.image = "weatherimages/09n.png"
          elif self.weatherData['icon'] == '10d':
            self.image = "weatherimages/10d.png"
            
          elif self.weatherData['icon'] == '10n':
            self.image = "weatherimages/10n.png"
            
          elif self.weatherData['icon'] == '11d':
            self.image = "weatherimages/11d.png"
            
          elif self.weatherData['icon'] == '11n':
            self.image = "weatherimages/11n.png"
            
          elif self.weatherData['icon'] == '13d':
            self.image = "weatherimages/13d.png"
            
          elif self.weatherData['icon'] == '13n':
            self.image = "weatherimages/13n.png"
            
          elif self.weatherData['icon'] == '50d':
            self.image = "weatherimages/50d.png"
            
          elif self.weatherData['icon'] == '50n':
            self.image = "weatherimages/50n.png"

            int(self.image)
          self.logo = Image.open(self.image)
          self.bglogo = ImageTk.PhotoImage(self.logo)
          self.bgLabel1 = Label(self.mainframe, image=self.bglogo, bg = "#d7dae2")
          self.bgLabel1.place(x = 1, y = 8, width = "100", height = "100")
          
          
        #lables

          self.name1=Label(self.mainframe,text=self.weatherData['cityName'],font=("arial",15,"bold","underline"),fg="black",bg="#d7dae2")
          self.name1.place(x=90,y=0)

          self.name2=Label(self.mainframe,text=self.weatherData['temp'],font=("arial",35,"bold"),fg="black",bg="#d7dae2")
          self.name2.place(x=84,y=31)

          self.name3=Label(self.mainframe,text=self.weatherData["main"],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
          self.name3.place(x=102,y=84)
          
          self.name4=Label(self.mainframe,text=self.weatherData["temp_min"],font=("arial",10,"bold"),fg="black",bg="#d7dae2")
          self.name4.place(x=20,y=120)

          self.name5=Label(self.mainframe,text=self.weatherData["temp_max"],font=("arial",10,"bold"),fg="black",bg="#d7dae2")
          self.name5.place(x=130,y=120)

          self.name6=Label(self.mainframe,text=self.weatherData["pressure"],font=("arial",10,"bold"),fg="black",bg="#d7dae2")
          self.name6.place(x=20,y=155)
          
          
          self.name7=Label(self.mainframe,text=self.weatherData["humidity"],font=("arial",10,"bold"),fg="black",bg="#d7dae2")
          self.name7.place(x=130,y=155)
          
          
          self.name=Label(self.mainframe,text=self.weatherData['speed'],font=("arial",10,"bold"),fg="black",bg="#d7dae2")
          self.name.place(x=70,y=215)

          self.name=Label(self.mainframe,text=self.weatherData["sunrise"],font=("arial",10,"bold"),fg="black",bg="#d7dae2")
          self.name.place(x=0,y=185)
          
          self.name=Label(self.mainframe,text=self.weatherData["sunset"],font=("arial",10,"bold"),fg="black",bg="#d7dae2")
          self.name.place(x=128,y=185)

        except:
          messagebox.showinfo('Alert', 'Something went wrong, please try again.')
      
      
if __name__ == "__main__":
    loginObj = search()
    loginObj.search_frame()








































from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
import PIL
import requests
import login
import home

class search:
  
    API_KEY = "6ee01bd686ddb245a7b5e0f7bd6547b0"

    def __init__(self, status):    
        self.status = status
        print(self.status)
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
        
    def search_frame(self, res):
        self.loginResponse = res
        self.login = Frame(self.root)
        self.login.pack()
        

          #buttons

        self.button=Button(self.root,text='search',width=10,height=2,bg='black',fg="white", command = self.searchWeather)
        self.button.place(x=500,y=90)

        #entryes
        self.entry=Entry(self.root,width=14,font=('arial',25),bd=2)
        self.entry.place(x=210,y=90)
        
      
        #center
      
        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        self.width = int((self.fullwidth-1280)/2)
        self.height=int((self.fullheight-750)/2)

        s = "1280x750+" +str(self.width)+ "+" +str(self.height)
    

        # so screen cant be resized
        self.root.resizable(height=False,width=False)
        
        


        #BUTTONS
      
        self.exitButton=Button(self.root,text=("BACK"),width=10,height=2,bg='#ed3833',fg="white",bd=0,command=self.exit)
        self.exitButton.place(x=1270,y=15)         
      
      
        #self.image = Image.open("images/ooo.png")
        #self.bgImage = ImageTk.PhotoImage(self.image)
        #self.bgLabel = Label(self.bordercolor, image=self.bgImage)
        #self.bgLabel.place(x=50, y = 60, width = "140", height = "140")
      
        
         #title
        self.title=Label(text=" City Wether",font=("arial",40,"bold","underline"),fg="black",bg="#d7dae2")
        self.title.place(x=680,y=20)
        #BORDER

        self.bordercolor=Frame(self.root,bg="black",width=10,height=50) 
        self.bordercolor.place(x=200,y=150) 

        self.mainframe=Frame(self.bordercolor,bg="#d7dae2",width=800,height=500)
        self.mainframe.pack(padx=10,pady=10)

        #logo

        self.logo2 = Image.open('images\ooo.png')
        self.bglogo2 = ImageTk.PhotoImage(self.logo2)
        self.bgLabel2 = Label(self.root, image=self.bglogo2, bg = "#d7dae2")
        self.bgLabel2.place(x = 1040, y = 20, width = "225", height = "225")

        self.root.mainloop()


    def exit(self):
      self.root.destroy()
      print
      if (self.status == 'with_login'):
        obj = home.AdminNav()
        obj.navframe(self.loginResponse)
      if (self.status == 'without_login'):
        Obj1 = login.loginWindow()
        Obj1.loginFrame()
      

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
          self.bgLabel1.place(x = 340, y = 215, width = "100", height = "100")
          
        
        #lables

          self.name1=Label(self.mainframe,text=self.weatherData['cityName'],font=("arial",30,"bold","underline"),fg="black",bg="#d7dae2")
          self.name1.place(x=310,y=30)

          self.name2=Label(self.mainframe,text=self.weatherData['temp'],font=("arial",60,"bold"),fg="black",bg="#d7dae2")
          self.name2.place(x=300,y=90)

          self.name3=Label(self.mainframe,text=self.weatherData["main"],font=("arial",30,"bold"),fg="black",bg="#d7dae2")
          self.name3.place(x=330,y=185)
          
          self.name4=Label(self.mainframe,text=self.weatherData["temp_min"],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
          self.name4.place(x=230,y=305)

          self.name5=Label(self.mainframe,text=self.weatherData["temp_max"],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
          self.name5.place(x=400,y=305)

          self.name6=Label(self.mainframe,text=self.weatherData["pressure"],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
          self.name6.place(x=240,y=345)
          
          
          self.name7=Label(self.mainframe,text=self.weatherData["humidity"],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
          self.name7.place(x=420,y=345)
          
          
          self.name=Label(self.mainframe,text=self.weatherData['speed'],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
          self.name.place(x=285,y=385)

          # self.name=Label(self.mainframe,text=self.weatherData["sunrise"],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
          # self.name.place(x=440,y=385)
          
          # self.name=Label(self.mainframe,text=self.weatherData["sunset"],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
          # self.name.place(x=290,y=425)

        except:
          messagebox.showinfo('Alert', 'Something went wrong, please try again.')
      
      
if __name__ == "__main__":
    loginObj = search('without_login')
    loginObj.search_frame('')








































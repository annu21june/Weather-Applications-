
from tkinter import *
from tkinter import messagebox
import login
from PIL import ImageTk, Image
import requests

import copy_search
import search_five_days
import addCity
import login
import database

class AdminNav:

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
        
        #center
      
        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        self.width = int((self.fullwidth-1380)/2)
        self.height=int((self.fullheight-750)/2)

        s = "1280x750+" +str(self.width)+ "+" +str(self.height)
        

        self.menu=Menu()
        self.weather = Menu(self.menu)
        self.menu.add_cascade(label= "weather" , menu=self.weather)
        self.weather.add_command(label="Current Weather",command=self.openCurrent)
        self.weather.add_command(label="5 days Weather",command=self.openFiveDay)


        self.city = Menu(self.menu)
        self.menu.add_cascade(label= "Cities" , menu=self.city)
        self.city.add_command(label="Add",command=self.openAddCity)
        
        self.account = Menu(self.menu)
        self.menu.add_cascade(label = "Account", menu = self.account)
        self.account.add_command(label="Logout",command=self.logout)


        self.root.config(menu= self.menu)

     def navframe(self, res):
        self.loginResponse = res
        self.navfra = Frame(self.root,bg="#d7dae2")
        self.navfra.place(x=0, y=0, width="1380", height="750")
        self.root.resizable(height=False, width=False)  

        self.image2 = Image.open("images/mana.jpg")
        self.bgImage2 = ImageTk.PhotoImage(self.image2)
        self.bgLabel2 = Label(self.navfra, image=self.bgImage2)
        self.bgLabel2.place(x = 640, y = 0, width = "710", height = "750")

        self.cityName = self.loginResponse.get('current_location')

        self.getWeather(self.cityName)
        
        self.root.mainloop()

     def openCurrent(self):
      self.root.destroy()
      currentObj = copy_search.search('with_login')
      currentObj.search_frame(self.loginResponse)

     def openFiveDay(self):
      self.root.destroy()
      fiveObj = search_five_days.search()
      fiveObj.search_frame(self.loginResponse)

     def logout(self):
        t=messagebox.askyesno("ALERT","Do You Realy Want To Exit")
        if t:
            self.root.destroy()
            obj = login.loginWindow()
            obj.loginFrame()

     def openAddCity(self):
      self.root.destroy()
      
      obj = addCity.frame2()
      obj.create2(self.loginResponse)

     def getWeather(self, cityName):
        self.api_address = "https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid=" + self.API_KEY

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
         self.bgLabel1 = Label(self.navfra, image=self.bglogo, bg = "#d7dae2")
         self.bgLabel1.place(x = 310, y = 255, width = "100", height = "100")
            
         
         #lables

         self.name1=Label(self.navfra,text=self.weatherData['cityName'],font=("arial",30,"bold","underline"),fg="black",bg="#d7dae2")
         self.name1.place(x=280,y=70)

         self.name2=Label(self.navfra,text=self.weatherData['temp'],font=("arial",60,"bold"),fg="black",bg="#d7dae2")
         self.name2.place(x=270,y=130)

         self.name3=Label(self.navfra,text=self.weatherData["main"],font=("arial",30,"bold"),fg="black",bg="#d7dae2")
         self.name3.place(x=300,y=235)
            
         self.name4=Label(self.navfra,text=self.weatherData["temp_min"],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
         self.name4.place(x=200,y=355)

         self.name5=Label(self.navfra,text=self.weatherData["temp_max"],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
         self.name5.place(x=370,y=355)

         self.name6=Label(self.navfra,text=self.weatherData["pressure"],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
         self.name6.place(x=210,y=385)
            
            
         self.name7=Label(self.navfra,text=self.weatherData["humidity"],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
         self.name7.place(x=390,y=385)
            
            
         self.name=Label(self.navfra,text=self.weatherData['speed'],font=("arial",15,"bold"),fg="black",bg="#d7dae2")
         self.name.place(x=255,y=435)

              
      
        except:
          messagebox.showinfo('Alert', 'Something went wrong, please try again.')



if __name__=='__main__':
    obj1 = AdminNav()
    obj1.navframe()
        

        
        
        

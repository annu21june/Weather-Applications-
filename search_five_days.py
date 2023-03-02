from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
import PIL
import requests
import home


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
        
    def search_frame(self, res):
        self.loginResponse = res
        self.login = Frame(self.root)
        self.login.pack()



      #BUTTONS
      
        self.back=Button(self.root,text=("BACK"),width=13,height=2,bg='#ed3833',fg="white",bd=0,command=self.back)
        self.back.place(x=1250,y=15)
    
        

        self.image2 = Image.open("images/tal.png")
        self.bgImage2 = ImageTk.PhotoImage(self.image2)
        self.bgLabel2 = Label(self.root, image=self.bgImage2)
        self.bgLabel2.place(x = 800, y = 14, width = "200", height = "195")

        
        #title

        self.title=Label(self.root,text='City Weather',font=('arial',42,'underline','bold'),bg="#d7dae2")
        self.title.place(x=435,y=40)

          #buttons

        self.button=Button(self.root,text='search',width=8,height=2,bg='black',fg="white", command = self.searchWeather)
        self.button.place(x=730,y=152)

           
        
        #entryes
        self.entry=Entry(self.root,width=14,font=('arial',20),bd=2)
        
        self.entry.place(x=440,y=150,width=265,height=44)
         
      
      #center
      
        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        self.width = int((self.fullwidth-1280)/2)
        self.height=int((self.fullheight-750)/2)

        s = "1280x750+" +str(self.width)+ "+" +str(self.height)
    

        # so screen cant be resized
        self.root.resizable(height=False,width=False)
        
        
         
      
      
        #self.image = Image.open("images/ooo.png")
        #self.bgImage = ImageTk.PhotoImage(self.image)
        #self.bgLabel = Label(self.bordercolor, image=self.bgImage)
        #self.bgLabel.place(x=50, y = 60, width = "140", height = "140")
      
        
       
        #logo

        self.root.mainloop()

      
      
    def back(self):        
        self.root.destroy()
        Obj1 =home.AdminNav()
        Obj1.navframe(self.loginResponse)
      


    def searchWeather(self):
      if self.entry.get() == '':
        messagebox.showinfo('Alert', 'Please enter city name first.')
      
      else:

        #for widget in self.mainframe.winfo_children():
         # widget.destroy()


        self.cityName = self.entry.get()
        #self.entry.delete(0, 'end')
        self.api_address = "https://api.openweathermap.org/data/2.5/forecast?q=" + self.cityName + "&appid=" + self.API_KEY

        print(self.api_address)

        try:
          res = requests.get(self.api_address)
          a = res.json()

          dates = []
          for i in a['list']:
              dates.append(i['dt_txt'][:10])

          dates = list(set(dates))
          dates.sort()
          print(dates)

          finalData = dict()
          firstDate = []
          secondDate = []
          thirdDate = []
          fourthDate = []
          fifthDate = []
          
          for i in dates:
            for j in a['list']:
              if j['dt_txt'][:10] == i:
                if dates.index(i) == 0:
                  firstDate.append(j)
                elif dates.index(i) == 1:
                  secondDate.append(j)
                elif dates.index(i) == 2:
                  thirdDate.append(j)
                elif dates.index(i) == 3:
                  fourthDate.append(j)
                elif dates.index(i) == 4:
                  fifthDate.append(j)

        
          

          self.a=Label(self.root,text='Daily',bg="#d7dae2",font=('arial',28,'underline','bold'))
          self.a.place(x=20,y=280)

          self.b=Label(self.root,text=dates[0],bg="#d7dae2",font=('arial',12,'bold'))
          self.b.place(x=260,y=340)
          self.C=Label(self.root,text=self.farenToCel(firstDate[0]['main']['temp']) ,bg="#d7dae2",font=('arial',20,'bold'))
          self.C.place(x=260,y=380)
          self.D=Label(self.root,text=firstDate[0]['weather'][0]['main'],bg="#d7dae2",font=('arial',12,'bold'))
          self.D.place(x=260,y=420)

          self.b=Label(self.root,text=dates[1],bg="#d7dae2",font=('arial',12,'bold'))
          self.b.place(x=460,y=340)
          self.C=Label(self.root,text=self.farenToCel(secondDate[0]['main']['temp']) ,bg="#d7dae2",font=('arial',20,'bold'))
          self.C.place(x=460,y=380)
          self.D=Label(self.root,text=secondDate[0]['weather'][0]['main'],bg="#d7dae2",font=('arial',12,'bold'))
          self.D.place(x=460,y=420)


          self.b=Label(self.root,text=dates[2],bg="#d7dae2",font=('arial',12,'bold'))
          self.b.place(x=660,y=340)
          self.C=Label(self.root,text=self.farenToCel(thirdDate[0]['main']['temp']),bg="#d7dae2",font=('arial',20,'bold'))
          self.C.place(x=660,y=380)
          self.D=Label(self.root,text=thirdDate[0]['weather'][0]['main'],bg="#d7dae2",font=('arial',12,'bold'))
          self.D.place(x=660,y=420)

          self.b=Label(self.root,text=dates[3],bg="#d7dae2",font=('arial',12,'bold'))
          self.b.place(x=860,y=340)
          self.C=Label(self.root,text=self.farenToCel(fourthDate[0]['main']['temp']),bg="#d7dae2",font=('arial',20,'bold'))
          self.C.place(x=860,y=380)
          self.D=Label(self.root,text=fourthDate[0]['weather'][0]['main'],bg="#d7dae2",font=('arial',12,'bold'))
          self.D.place(x=860,y=420) 

          self.b=Label(self.root,text=dates[4],bg="#d7dae2",font=('arial',12,'bold'))
          self.b.place(x=1040,y=340)
          self.C=Label(self.root,text=self.farenToCel(fifthDate[0]['main']['temp']),bg="#d7dae2",font=('arial',20,'bold'))
          self.C.place(x=1040,y=380)
          self.D=Label(self.root,text=fifthDate[0]['weather'][0]['main'],bg="#d7dae2",font=('arial',12,'bold'))
          self.D.place(x=1040,y=420)

          #buttons
          self.click=Button(self.root,bg='black',text='view',fg="white",font=('arial',10,'bold') ,command = lambda: self.getHourly(firstDate))
          self.click.place(x=260,y=460,width=50,height=30)
          self.click=Button(self.root,text='view',bg="black",fg="white",font=('arial',10,'bold'), command = lambda: self.getHourly(secondDate))
          self.click.place(x=470,y=460,width=50,height=30)
          self.click=Button(self.root,text='view',bg="black",fg="white",font=('arial',10,'bold'), command = lambda: self.getHourly(thirdDate))
          self.click.place(x=670,y=460,width=50,height=30)
          self.click=Button(self.root,text='view',bg="black",fg="white",font=('arial',10,'bold'), command = lambda: self.getHourly(fourthDate))
          self.click.place(x=870,y=460,width=50,height=30)
          self.click=Button(self.root,text='view',bg="black",fg="white",font=('arial',10,'bold'), command = lambda: self.getHourly(fifthDate))
          self.click.place(x=1050,y=460,width=50,height=30)

           
        

          # self.getHourl(firstDate)
          
        except:
          messagebox.showinfo('Alert', 'Something went wrong.')

    def getHourly(self, dateIndex):
          self.image3 = Image.open("images/x.png")
          self.bgImage3 = ImageTk.PhotoImage(self.image3)
          self.bgLabel3 = Label(self.root, image=self.bgImage3)
          self.bgLabel3.place(x = -9, y = 500, width = "2200", height = "50")
        
        
        
          self.a=Label(self.root,text='Hourly',bg="#d7dae2",font=('arial',22,'underline','bold'))
          self.a.place(x=20,y=520)

          self.b = Label(self.root, text = dateIndex[0]['dt_txt'][:10], bg="#d7dae2",font=('arial',10,'underline','bold'))
          self.b.place(x = 20, y = 570)

          self.b=Label(self.root,text=dateIndex[0]['dt_txt'][10:],bg="#d7dae2",font=('arial',12,'bold'))
          self.b.place(x=260,y=580)
          self.C=Label(self.root,text=self.farenToCel(dateIndex[0]['main']['temp']),bg="#d7dae2",font=('arial',19,'bold'))
          self.C.place(x=260,y=620)
          self.D=Label(self.root,text=dateIndex[0]['weather'][0]['main'],bg="#d7dae2",font=('arial',12,'bold'))
          self.D.place(x=260,y=670)

          self.b=Label(self.root,text=dateIndex[1]['dt_txt'][10:],bg="#d7dae2",font=('arial',12,'bold'))
          self.b.place(x=460,y=580)
          self.C=Label(self.root,text=self.farenToCel(dateIndex[1]['main'
          ]['temp']),bg="#d7dae2",font=('arial',19,'bold'))
          self.C.place(x=460,y=620)
          self.D=Label(self.root,text=dateIndex[1]['weather'][0]['main'],bg="#d7dae2",font=('arial',12,'bold'))
          self.D.place(x=480,y=670)

          
          self.b=Label(self.root,text=dateIndex[2]['dt_txt'][10:],bg="#d7dae2",font=('arial',12,'bold'))
          self.b.place(x=660,y=580)
          self.C=Label(self.root,text=self.farenToCel(dateIndex[2]['main']['temp']),bg="#d7dae2",font=('arial',19,'bold'))
          self.C.place(x=660,y=620)
          self.D=Label(self.root,text=dateIndex[2]['weather'][0]['main'],bg="#d7dae2",font=('arial',12,'bold'))
          self.D.place(x=660,y=670)

          
          self.b=Label(self.root,text=dateIndex[3]['dt_txt'][10:],bg="#d7dae2",font=('arial',12,'bold'))
          self.b.place(x=860,y=580)
          self.C=Label(self.root,text=self.farenToCel(dateIndex[3]['main']['temp']),bg="#d7dae2",font=('arial',19,'bold'))
          self.C.place(x=860,y=620)
          self.D=Label(self.root,text=dateIndex[3]['weather'][0]['main'],bg="#d7dae2",font=('arial',12,'bold'))
          self.D.place(x=860,y=670)

          
          self.b=Label(self.root,text=dateIndex[4]['dt_txt'][10:],bg="#d7dae2",font=('arial',12,'bold'))
          self.b.place(x=1040,y=580)
          self.C=Label(self.root,text=self.farenToCel(dateIndex[4]['main']['temp']),bg="#d7dae2",font=('arial',19,'bold'))
          self.C.place(x=1040,y=620)
          self.D=Label(self.root,text=dateIndex[4]['weather'][0]['main'],bg="#d7dae2",font=('arial',12,'bold'))
          self.D.place(x=1040,y=670)

          
    def farenToCel(self, temp):
      a = int(temp) - 273
      return f'{a}°C'



if __name__ == "__main__":
    loginObj = search()
    loginObj.search_frame('')








































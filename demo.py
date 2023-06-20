from tkinter import *
from tkinter import  ttk
import requests

def data_get():
    city= city_name.get()
    data =requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=4a02f4a51c959e3fbaa2eee594135aa6").json()

    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    wt_label1.config(text=str(int(data["main"]["temp"]-273.15)))





win = Tk()
win.title("ATech")
win.config(bg = "blue")
win.geometry("550x570")




name_label=Label(win,text="Atech weather App",
                font=("Time New Roman ",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Atech weather App",values=list_name,font=("Time New Roman ",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

done_button =Button(win,text="Done",font=("Time New Roman ",20,"bold"))

done_button.place(y=190,height=50,width=100,x=200)



w_label=Label(win,text="weather climate",
                font=("Time New Roman ",20))
w_label.place(x=25,y=260,height=50,width=250)

w_label1=Label(win,text="",
                font=("Time New Roman ",20))
w_label1.place(x=280,y=260,height=50,width=250)





wd_label=Label(win,text="weather desc",
                font=("Time New Roman ",17))
wd_label.place(x=25,y=330,height=50,width=250)

wd_label1=Label(win,text="",
                font=("Time New Roman ",17))
wd_label1.place(x=280,y=330,height=50,width=250)



wt_label=Label(win,text="weather temp",
                font=("Time New Roman ",20))
wt_label.place(x=25,y=400,height=50,width=250)
wt_label1=Label(win,text="",
                font=("Time New Roman ",20))
wt_label1.place(x=280,y=400,height=50,width=250)

done_button =Button(win,text="Done",font=("Time New Roman ",20,"bold"),command=data_get)

done_button.place(y=190,height=50,width=100,x=200)


win.mainloop()
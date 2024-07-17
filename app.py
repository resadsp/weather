from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import time
import arrow

window = Tk()
window.title("Weather app")
window.geometry("890x470+300+300")
window.configure(bg="#57adff")
window.resizable(False, False)
image_icon = PhotoImage(file="img/logo.png")
window.iconphoto(False, image_icon)

def getWeather():
    city = textfield.get()
    api_id = "432561637349389f758be6a7a99d090d"
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_id}&units=metric")
    try:
        if response.status_code == 200:
            request = response.json()
            a = request["main"]
            b = request["coord"]
            c = request["sys"]
            d = request["name"]
            e = request["wind"]
            g = request["weather"]
            v = request["dt"]
        timezon.config(text=f'{c["country"]} / {d}')
        long_lat.config(text=f'{round(b["lon"],4)}°N, {round(b["lat"],4)}°E')
        obj = TimezoneFinder()
        #TimeZoneFinder - trazenje odgovarajuce vremenske zone za date koordinate
        result = obj.timezone_at(lng=b["lon"],lat=b["lat"])
        #pytz - precizne proracune vremenskih zona i resava probleme dvosmislenih vremenena na kraju ljetnjeg racunanja vremena
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        curent_time = local_time.strftime("%I:%M:%p")
        clock.config(text=curent_time)
        t.config(text=f'{a["temp"]}°C')
        h.config(text=f'{a["humidity"]}%')
        p.config(text=f'{a["pressure"]}hPa')
        w.config(text=f'{e["speed"]}m/s')
        j.config(text=f'{g[0]["main"]}')
        first = datetime.now()
        day1.config(text=first.strftime("%A"))
        second = first + timedelta(days=1)
        day2.config(text=second.strftime("%A"))
        third = first + timedelta(days=2)
        day3.config(text=third.strftime("%A"))
        fourth = first + timedelta(days=3)
        day4.config(text=fourth.strftime("%A"))
        fifth = first + timedelta(days=4)
        day5.config(text=fifth.strftime("%A"))
        sixth = first + timedelta(days=5)
        day6.config(text=sixth.strftime("%A"))
        seventh = first + timedelta(days=6)
        day7.config(text=seventh.strftime("%A"))
        response2 = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={round(b['lat'],2)}&lon={round(b['lon'],2)}&cnt=7&appid={api_id}&units=metric")
        #https://openweathermap.org/forecast16
        if response2.status_code == 200:
            podaci = response2.json()
            prvidanimage = podaci['list'][0]['weather'][0]['icon']
            drugidanimage = podaci['list'][1]['weather'][0]['icon']
            trecidanimage = podaci['list'][2]['weather'][0]['icon']
            cetvrtidanimage = podaci['list'][3]['weather'][0]['icon']
            petidanimage = podaci['list'][4]['weather'][0]['icon']
            sestidanimage = podaci['list'][5]['weather'][0]['icon']
            
            img = (Image.open(f"img/{prvidanimage}@2x.png"))
            photo1 = ImageTk.PhotoImage(img)
            firstimage.config(image=photo1)
            firstimage.image = photo1
            
            min0 =  podaci['list'][0]['main']['temp_min']
            max0 =  podaci['list'][0]['main']['temp_max']
            day1temp.config(text=f"Min:{min0}\nMax:{max0}")
            
            img = (Image.open(f"img/{drugidanimage}@2x.png"))
            resized_image = img.resize((50,50))
            photo2 = ImageTk.PhotoImage(resized_image)
            secondimage.config(image=photo2)
            secondimage.image = photo2
            
            min1 =  podaci['list'][1]['main']['temp_min']
            max1 =  podaci['list'][1]['main']['temp_max']
            day2temp.config(text=f"Min:{min1}\nMax:{max1}")
            
            img = (Image.open(f"img/{trecidanimage}@2x.png"))
            resized_image = img.resize((50,50))
            photo3 = ImageTk.PhotoImage(resized_image)
            thirdimage.config(image=photo3)
            thirdimage.image = photo3
            
            min2 =  podaci['list'][2]['main']['temp_min']
            max2 =  podaci['list'][2]['main']['temp_max']
            day3temp.config(text=f"Min:{min2}\nMax:{max2}")
            
            img = (Image.open(f"img/{cetvrtidanimage}@2x.png"))
            resized_image = img.resize((50,50))
            photo4 = ImageTk.PhotoImage(resized_image)
            fourthimage.config(image=photo4)
            fourthimage.image = photo4
                        
            min3 =  podaci['list'][3]['main']['temp_min']
            max3 =  podaci['list'][3]['main']['temp_max']
            day4temp.config(text=f"Min:{min3}\nMax:{max3}")
            
            img = (Image.open(f"img/{petidanimage}@2x.png"))
            resized_image = img.resize((50,50))
            photo5 = ImageTk.PhotoImage(resized_image)
            fifthimage.config(image=photo5)
            fifthimage.image = photo5
                        
            min4 =  podaci['list'][4]['main']['temp_min']
            max4 =  podaci['list'][4]['main']['temp_max']
            day5temp.config(text=f"Min:{min4}\nMax:{max4}")
            
            img = (Image.open(f"img/{sestidanimage}@2x.png"))
            resized_image = img.resize((50,50))
            photo6 = ImageTk.PhotoImage(resized_image)
            sixthimage.config(image=photo6)
            sixthimage.image = photo6
                     
            min5 =  podaci['list'][5]['main']['temp_min']
            max5 =  podaci['list'][5]['main']['temp_max']
            day6temp.config(text=f"Min:{min5}\nMax:{max5}")
            
            img = (Image.open(f"img/{sestidanimage}@2x.png"))
            resized_image = img.resize((50,50))
            photo7 = ImageTk.PhotoImage(resized_image)
            seventhimage.config(image=photo7)
            seventhimage.image = photo7
                        
            min6 =  podaci['list'][6]['main']['temp_min']
            max6 =  podaci['list'][6]['main']['temp_max']
            day7temp.config(text=f"Min:{min6}\nMax:{max6}")
            
    except Exception:
        messagebox.showerror("Ne postoji", "Ne postoji grad sa datim imenom.")

Round_box=PhotoImage(file="img/ht1.png")
Label(window, image=Round_box, bg="#57adff").place(x=30, y=110, height=120, width=187)
label1 = Label(window, text="Temperatura", font="Helvetica 11", fg="white", bg="#203243")
label1.place(x=50, y=120)
label2 = Label(window, text="Vlaznost", font="Helvetica 11", fg="white", bg="#203243")
label2.place(x=50, y=140)
label3 = Label(window, text="Pritisak", font="Helvetica 11", fg="white", bg="#203243")
label3.place(x=50, y=160)
label4 = Label(window, text="Brzina vetra", font="Helvetica 11", fg="white", bg="#203243")
label4.place(x=50, y=180)
label5 = Label(window, text="Opis", font="Helvetica 11", fg="white", bg="#203243")
label5.place(x=50, y=200)

Search_image = PhotoImage(file="img/ht2.png")
myimage=Label(image=Search_image, bg="#57adff")
myimage.place(x=300, y=120)

weat_image = PhotoImage(file="img/oblak.png")
weatherimage = Label(window,image=weat_image, bg="#203243")
weatherimage.place(x=322, y=122)

textfield = tk.Entry(window, justify="center", width=15, font="poppins 20 bold", bg="#203243", border=0, fg="white")
textfield.place(x=370, y=130)
textfield.focus()

Search_icon = PhotoImage(file="img/search.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=645, y=123)

frame = Frame(window, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

first_box = PhotoImage(file="img/ht3.png", width=230, height=132)
Label(frame, border=1, image=first_box, bg="white").place(x=30, y=19)

second_box = PhotoImage(file="img/ht3.png", width=81, height=130)
Label(frame, image=second_box, bg="white", border=1).place(x=300, y=20)
Label(frame, image=second_box, bg="white", border=1).place(x=400, y=20)
Label(frame, image=second_box, bg="white", border=1).place(x=500, y=20)
Label(frame, image=second_box, bg="white", border=1).place(x=600, y=20)
Label(frame, image=second_box, bg="white", border=1).place(x=700, y=20)
Label(frame, image=second_box, bg="white", border=1).place(x=800, y=20)

clock=Label(window, font="Helvetica 30 bold", fg="white", bg="#57adff")
clock.place(x=30, y=20)

timezon=Label(window, font="Helvetica 20", fg="white", bg="#57adff")
timezon.place(x=690, y=20)

long_lat=Label(window, font="Helvetica 10", fg="white", bg="#57adff")
long_lat.place(x=690, y=55)

t = Label(window, font="Helvetica, 11", fg="white", bg="#203243")
t.place(x=150, y=120)
h = Label(window, font="Helvetica, 11", fg="white", bg="#203243")
h.place(x=150, y=140)
p = Label(window, font="Helvetica, 11", fg="white", bg="#203243")
p.place(x=150, y=160)
w = Label(window, font="Helvetica, 11", fg="white", bg="#203243")
w.place(x=150, y=180)
j = Label(window, font="Helvetica, 11", fg="white", bg="#203243")
j.place(x=150, y=200)

firstframe = Frame(window, width=230, height=132, bg="#282829")
firstframe.place(x=31,y=310)
day1 = Label(firstframe, font="arial 20", bg="#282829", fg="#fff")
day1.place(x=100, y=5)
firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=1, y=15)
day1temp = Label(firstframe, bg="#282829", fg="#fff", font="arial 15 bold")
day1temp.place(x=100, y=50)


secondframe = Frame(window, width=75, height=115, bg="#282829")
secondframe.place(x=305,y=315)
day2 = Label(secondframe, bg="#282829", fg="#fff")
day2.place(x=5, y=5)
secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=7, y=23)
day2temp =  Label(secondframe, bg="#282829", fg="#fff")
day2temp.place(x=10, y=70)


thirdframe = Frame(window, width=75, height=115, bg="#282829")
thirdframe.place(x=405,y=315)
day3 = Label(thirdframe, bg="#282829", fg="#fff")
day3.place(x=5, y=5)
thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=7, y=23)
day3temp =  Label(thirdframe, bg="#282829", fg="#fff")
day3temp.place(x=10, y=70)


fourthframe = Frame(window, width=75, height=115, bg="#282829")
fourthframe.place(x=505,y=315)
day4 = Label(fourthframe, bg="#282829", fg="#fff")
day4.place(x=5, y=5)
fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=7, y=23)
day4temp =  Label(fourthframe, bg="#282829", fg="#fff")
day4temp.place(x=10, y=70)

fifthframe = Frame(window, width=75, height=115, bg="#282829")
fifthframe.place(x=605,y=315)
day5 = Label(fifthframe, bg="#282829", fg="#fff")
day5.place(x=5, y=5)
fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=7, y=23)
day5temp =  Label(fifthframe, bg="#282829", fg="#fff")
day5temp.place(x=10, y=70)


sixthframe = Frame(window, width=75, height=115, bg="#282829")
sixthframe.place(x=705,y=315)
day6 = Label(sixthframe, bg="#282829", fg="#fff")
day6.place(x=5, y=5)
sixthimage = Label(sixthframe, bg="#282829")
sixthimage.place(x=7, y=23)
day6temp =  Label(sixthframe, bg="#282829", fg="#fff")
day6temp.place(x=10, y=70)

seventhframe = Frame(window, width=75, height=115, bg="#282829")
seventhframe.place(x=805,y=315)
day7 = Label(seventhframe, bg="#282829", fg="#fff")
day7.place(x=5, y=5)
seventhimage = Label(seventhframe, bg="#282829")
seventhimage.place(x=7, y=23)
day7temp =  Label(seventhframe, bg="#282829", fg="#fff")
day7temp.place(x=10, y=70)

if __name__=="__main__":
    window.mainloop()
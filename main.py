from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root = Tk()
root.title("phone number tracker")
root.geometry("365x584")
root.configure(background='black')
root.resizable(False, False)

# logo
logo = PhotoImage(file="logo image.png")
Label(root, image=logo, bg='black').place(x=230, y=70)

# Title
Heading = Label(root, text="Track Number", bg='black', fg='white', font=("arial", 15, "bold"))
Heading.place(x=80, y=110)

# entry
Entry_back = PhotoImage(file="search png.png")
Label(root, image=Entry_back, bg='black').place(x=20, y=190)

entry = StringVar()
entry_number = Entry(root, textvariable=entry, width=17, bd=0, font=("arial", 20), justify="center")
entry_number.place(x=50, y=220)


# button
def track():
    enter_number = entry.get()
    number = phonenumbers.parse(enter_number)
    # country
    locate = geocoder.description_for_number(number, 'en')
    country.config(text=locate)

    # sim
    operator = carrier.name_for_number(number, 'en')
    sim.config(text=operator)

    # TimeZone
    time = timezone.time_zones_for_number(number)
    TimeZone.config(text=time)

    # longitude and latitude
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(locate)

    lon = location.longitude
    lat = location.latitude
    longitude.config(text=lon)
    latitude.config(text=lat)

    # current time
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)


search_image = PhotoImage(file="search.png")
search = Button(image=search_image, borderwidth=0, bg='black', activebackground='black', cursor="hand2", bd=0,
                font=("arial", 16), command=track)
search.place(x=35, y=300)

# bottom
bottom = PhotoImage(file="bg.png")
Label(root, image=bottom, bg='black').place(x=-2, y=355)
country = Label(root, text="Country:", bg="#57adff", fg="black", font=("arial", 10, "bold"))
country.place(x=50, y=400)
sim = Label(root, text="SIM:", bg="#57adff", fg="black", font=("arial", 10, "bold"))
sim.place(x=200, y=400)
TimeZone = Label(root, text="TimeZone:", bg="#57adff", fg="black", font=("arial", 10, "bold"))
TimeZone.place(x=50, y=450)
clock = Label(root, text="Phone Time:", bg="#57adff", fg="black", font=("arial", 10, "bold"))
clock.place(x=200, y=450)
longitude = Label(root, text="Longitude:", bg="#57adff", fg="black", font=("arial", 10, "bold"))
longitude.place(x=50, y=500)
latitude = Label(root, text="Latitude:", bg="#57adff", fg="black", font=("arial", 10, "bold"))
latitude.place(x=200, y=500)

root.mainloop()

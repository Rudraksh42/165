from tkinter import *
from PIL import ImageTk , Image 
from tkinter import ttk
root = Tk()
root.geometry("900x900")
root.configure(bg = "IndianRed1")
root.title("Planet Encyclopedia")

#images
Mercury_img = ImageTk.PhotoImage(Image.open("mercury.jpg")) 
Venus_img = ImageTk.PhotoImage(Image.open("venus.jpg")) 
Earth_img = ImageTk.PhotoImage(Image.open("earth.jpg")) 
Mars_img = ImageTk.PhotoImage(Image.open("mars.jpg")) 
Jupiter_img = ImageTk.PhotoImage(Image.open("jupter.jpg")) 
Saturn_img = ImageTk.PhotoImage(Image.open("saturn.jpeg")) 
Uranus_img = ImageTk.PhotoImage(Image.open("uranus.jpg")) 
Neptune_img = ImageTk.PhotoImage(Image.open("neptune.jpg")) 
Moon_img = ImageTk.PhotoImage(Image.open("moon.jpeg")) 

#Content
planet_label = Label(root, text = "Planet:" , bg = "IndianRed1" ,  font=("courier" , 14 , "bold"))
planet_label.place(relx = 0.37 , rely = 0.1 , anchor = CENTER)

planet_name = Label(root, text = "" , font = ("courier" , 17 , "bold"), bg = "IndianRed1")
planet_name.place(relx = 0.5 , rely = 0.25 , anchor = CENTER)

planet_image = Label(root  , bg = "gold2" , highlightthickness= 5 , borderwidth= 2 ,  relief = SOLID)
planet_image.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

planet_gravity_radius = Label(root , text = "gravity and radius" , font=("courier" , 12 , "bold") , bg = "IndianRed1")
planet_gravity_radius.place(relx = 0.5 , rely = 0.75 , anchor = CENTER)

planet_descripton = Label(root , text= "description" , font =("courier" , 12 , "bold")  , wraplength= 500 , bg = "IndianRed1" )
planet_descripton.place(relx = 0.5 , rely = 0.85 , anchor = CENTER)

#dropdown
planet = ["Mercury" , "Venus" , "Earth" , "Mars" , "Jupiter" , "Saturn" , "Uranus"  , "Neptune" , "Moon"] 

selected_item = StringVar()
drop_down = ttk.Combobox(root, values = planet , textvariable= selected_item)
drop_down.place(relx = 0.5 , rely = 0.1 , anchor = CENTER)

#funtions
def show_planet_info():
    planet_selected = selected_item.get()
    if planet_selected == "Mercury":
        planet_name["text"] = "Mercury"
        planet_image["image"] = Mercury_img
        planet_gravity_radius["text"] = "Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        planet_descripton["text"] = "Mercury is the smallest and fastest planet in our solar system"
    elif planet_selected == "Venus":
        planet_name["text"] = "Venus"
        planet_image["image"] = Venus_img
        planet_gravity_radius["text"] = "Gravity : 8.87 m/s² \n Radius : 6051.8 km"
        planet_descripton["text"] = "Venus is the second planet from the Sun, and is Earth's closest neighbor in the solar system. Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky. The planet is a little smaller than Earth, and is similar to Earth inside"
    elif planet_selected == "Earth":
        planet_name["text"] = "Earth"
        planet_image["image"] = Earth_img
        planet_gravity_radius["text"] = "Gravity : 9.807 m/s² \n Radius : 6371 km"
        planet_descripton["text"] = "While Earth is only the fifth largest planet in the solar system, it is the only world in our solar system with liquid water on the surface. Just slightly larger than nearby Venus, Earth is the biggest of the four planets closest to the Sun, all of which are made of rock and metal."
    elif planet_selected == "Mars":
        planet_name["text"] = "Mars"
        planet_image["image"] = Mars_img
        planet_gravity_radius["text"] = "Gravity : 3.721 m/s². \n Radius : 3389.5 km"
        planet_descripton["text"] = "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, only being larger than Mercury. In the English language, Mars is named for the Roman god of war"
    elif planet_selected == "Jupiter":
        planet_name["text"] = "Jupiter"
        planet_image["image"] = Jupiter_img
        planet_gravity_radius["text"] = "Gravity : 24.79 m/s² \n Radius : 69911 km"
        planet_descripton["text"] = "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass more than two and a half times that of all the other planets in the Solar System combined, while being slightly less than one-thousandth the mass of the Sun."
    elif planet_selected == "Saturn":
        planet_name["text"] = "Saturn"
        planet_image["image"] = Saturn_img
        planet_gravity_radius["text"] = "Gravity : 10.44 m/s². \n Radius : 58232 km"
        planet_descripton["text"] = "Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth. It has only one-eighth the average density of Earth, but is over 95 times more massive."
    elif planet_selected == "Uranus":
        planet_name["text"] = "Uranus"
        planet_image["image"] = Uranus_img
        planet_gravity_radius["text"] = "Gravity : 8.87 m/s² \n Radius : 25362 km"
        planet_descripton["text"] = "Uranus is the seventh planet from the Sun. It is named after Greek sky deity Uranus, who in Greek mythology is the father of Cronus, a grandfather of Zeus and great-grandfather of Ares. Uranus has the third-largest planetary radius and fourth-largest planetary mass in the Solar System"
    elif planet_selected == "Neptune":
        planet_name["text"] = "Neptune"
        planet_image["image"] = Neptune_img
        planet_gravity_radius["text"] = "Gravity : 11.15 m/s². \n Radius : 24622 km"
        planet_descripton["text"] = "Neptune is the eighth planet from the Sun and the farthest known planet in the Solar System. It is the fourth-largest planet in the Solar System by diameter, the third-most-massive planet, and the densest giant planet. It is 17 times the mass of Earth, and slightly more massive than its near-twin Uranus. "
    elif planet_selected == "Moon":
        planet_name["text"] = "Moon"
        planet_image["image"] = Moon_img
        planet_gravity_radius["text"] = "Gravity :  1.62 m/s². \n Radius : 1,737.4 km"
        planet_descripton["text"] = "The Moon is Earth's only natural satellite. It is the fifth largest satellite in the Solar System and the largest and most massive relative to its parent planet, with a diameter about one-quarter that of Earth. "
    
        
        
        
btn = Button(root , bg = "seagreen3" , font=("courier" , 10 , "bold")  , text = "Show Planet Info" , relief = SOLID,  command = show_planet_info)
btn.place(relx = 0.5 , rely = 0.18 , anchor = CENTER),




root.mainloop()
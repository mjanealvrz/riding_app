import tkinter as tk
from tkinter import *

class RideApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ride App")

        # Make the window resizable
        self.master.geometry("1200x1024")  # Initial size
        self.master.resizable(True, True)

        # Header frame (Logo, Name of the App)
        self.header_frame = tk.Frame(master,borderwidth=3, relief= "groove", bg="lightblue", height=80)
        self.header_frame.pack(fill=tk.X)

        self.header_label = tk.Label(self.header_frame, text="GO GRAB IT", font=("Helvetica", 20), bg="lightblue", height= 2)
        self.header_label.pack(pady=10)


    

        # Motor frame 
        self.motor_frame = tk.Frame(master,  borderwidth=3, relief="groove")
        self.motor_frame.place(relx= 0.50, rely= 0.29,  relwidth=0.3, relheight=0.3, anchor="center")


        # Motor icon
        self.motor_img = tk.PhotoImage(file='motor.png')
        self.motor_image_label = tk.Label(self.motor_frame, image=self.motor_img, bg="lightblue")
        self.motor_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Motor label
        self.motor_label = tk.Label(self.motor_frame, text="Motor", font=("Helvetica", 15), bg="lightblue")
        self.motor_label.place(relx=0.6, rely=0.1, anchor="center")

        # Motor button
        self.motor_button = tk.Button(master, text="Book",font= ("Helvetica", 12), height=2, width=40)
        self.motor_button.place(relx=0.50, rely=0.48,anchor="center")



        # Car frame
        self.car_frame = tk.Frame(master,  borderwidth=3, relief="groove")
        self.car_frame.place(relx= 0.83, rely= 0.29,  relwidth=0.3, relheight=0.3, anchor="center")

       
        #  Car icon
        self.car_img = tk.PhotoImage(file='car.png')
        self.car_image_label = tk.Label(self.car_frame, image=self.car_img, bg="lightblue")
        self.car_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Car label
        self.car_label = tk.Label(self.car_frame, text="Car", font=("Helvetica", 15), bg="lightblue")
        self.car_label.place(relx=0.5, rely=0.1, anchor="center")

        # Car button
        self.car_button = tk.Button(master, text="Book",font= ("Helvetica", 12), height=2, width=40)
        self.car_button.place(relx=0.83, rely=0.48,anchor="center")

        # Taxi cab frame
        self.taxi_cab_frame = tk.Frame(master,  borderwidth=3, relief="groove")
        self.taxi_cab_frame.place(relx= 0.50, rely= 0.70,  relwidth=0.3, relheight=0.3, anchor="center")


        # Taxi cab icon
        self.taxi_cab_img = tk.PhotoImage(file='taxicab.png')
        self.taxi_cab_image_label = tk.Label(self.taxi_cab_frame, image=self.taxi_cab_img, bg="lightblue")
        self.taxi_cab_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Taxi cab icon
        self.taxi_cab_label = tk.Label(self.taxi_cab_frame, text="Taxi Cab", font=("Helvetica", 15), bg="lightblue")
        self.taxi_cab_label.place(relx=0.5, rely=0.1, anchor="center")

        # Taxi cab button
        self.taxi_cab_button = tk.Button(master, text="Book",font= ("Helvetica", 12), height=2, width=40)
        self.taxi_cab_button.place(relx=0.50, rely=0.90,anchor="center")




        # Premium cab frame
        self.prem_cab_frame = tk.Frame(master,  borderwidth=3, relief="groove")
        self.prem_cab_frame.place(relx= 0.83, rely= 0.70,  relwidth=0.3, relheight=0.3, anchor="center")

        
        # Premium cab icon
        self.prem_cab_img = tk.PhotoImage(file='premcab.png')
        self.prem_cab_image_label = tk.Label(self.prem_cab_frame, image=self.prem_cab_img, bg= "lightblue")
        self.prem_cab_image_label.place(relx=0.5, rely=0.5,  anchor="center")

        # Premium cab label
        self.prem_cab_label = tk.Label(self.prem_cab_frame, text="Premium Cab", font=("Helvetica", 15), bg="lightblue")
        self.prem_cab_label.place(relx=0.5, rely=0.1, anchor="center")

        # Premium cab button
        self.prem_cab_button = tk.Button(master, text="Book",font= ("Helvetica", 12), height=2, width=40)
        self.prem_cab_button.place(relx=0.83, rely=0.90,anchor="center")


        # Profile button
        self.profile_button = tk.Button(master,  text="PROFILE",font= ("Helvetica", 20), height=2, width=20)
        self.profile_button.place(relx=0.30, rely=0.13,anchor="ne")

        # Bookings button
        self.bookings_button = tk.Button(master, text="BOOKINGS",font= ("Helvetica", 20), height=2, width=15)
        self.bookings_button.place(relx=0.23, rely=0.25,anchor="ne")

        # History button
        self.history_button = tk.Button(master,  text="HISTORY",font= ("Helvetica", 20), height=2, width=15)
        self.history_button.place(relx=0.23, rely=0.4,anchor="ne")

        # Feedback button
        self.feedback_button = tk.Button(master,  text="FEEDBACK",font= ("Helvetica", 20), height=2, width=15)
        self.feedback_button.place(relx=0.23, rely=0.5,anchor="ne")

        # Log-out Button
        self.out_button = tk.Button(master,text= "LOG OUT", font= ("Helvetica", 20), height=2, width=15, bg= "red")
        self.out_button.place(relx=0.23, rely=0.6,anchor="ne")


        



    # Bind the label and frame together
        self.prem_cab_frame.bind("<Configure>", self.on_frame_configure)
        self.prem_cab_image_label.bind("<Configure>", self.on_label_configure)

    def on_frame_configure(self, event):
        # Get the new size of the frame
        width = event.width
        height = event.height

        # Adjust the size of the label to match the frame
        self.prem_cab_image_label.config(width=width, height=height)
        self.motor_image_label.config(width=width, height=height)
        self.car_image_label.config(width=width, height=height)
        self.taxi_cab_image_label.config(width=width, height=height)

    def on_label_configure(self, event):
        # Get the new size of the label
        width = event.width
        height = event.height

        # Adjust the size of the frame to match the label
        self.prem_cab_frame.config(width=width, height=height)
        self.motor_image_label.config(width=width, height=height)
        self.car_image_label.config(width=width, height=height)
        self.taxi_cab_image_label.config(width=width, height=height)




       
      

root = tk.Tk()
app = RideApp(root)
root.mainloop()


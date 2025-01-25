from tkinter import *
import speedtest
import threading
import time

# Function to check the internet speed
def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()

    # Show the circular loader while fetching the data
    animate_loader()

    # Simulate downloading and uploading speed in Mbps
    down = round(sp.download() / (10**6), 3)  # Convert to Mbps and round
    up = round(sp.upload() / (10**6), 3)  # Convert to Mbps and round

    # Convert the float values to strings and concatenate with ' Mbps'
    down_str = str(down) + " Mbps"
    up_str = str(up) + " Mbps"

    # Update the labels with the speed values
    lab_down.config(text=down_str)
    lab_up.config(text=up_str)

    # Stop the animated loader
    stop_loader()

# Function to animate the loader (rotating circle)
def animate_loader():
    global angle
    angle = 0
    loading_canvas.place(x=150, y=250)  # Place loader in the center
    rotate_loader()

# Function to stop the loader animation
def stop_loader():
    loading_canvas.place_forget()  # Hide loader when test is complete

# Function to rotate the circle on canvas
def rotate_loader():
    global angle
    loading_canvas.delete("all")  # Clear the previous drawing
    # Draw a rotating circle
    loading_canvas.create_arc(20, 20, 180, 180, start=angle, extent=60, width=10, outline="yellow")
    
    # Update the angle to create rotation
    angle += 10
    if angle > 360:
        angle = 0

    # Call rotate_loader after 50ms to create animation effect
    loading_canvas.after(50, rotate_loader)

# Function to start the speed test in a separate thread
def start_speed_test():
    thread = threading.Thread(target=speedcheck)
    thread.start()

# Main Tkinter window
sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="#1a1a2e")  # Dark background color

# Title Label
lab_title = Label(sp, text="Internet Speed Test", font=("Helvetica", 30, "bold"), fg="white", bg="#1a1a2e")
lab_title.place(x=60, y=40, height=50, width=380)

# Download Speed Label
lab_download = Label(sp, text="Download Speed", font=("Helvetica", 20, "bold"), fg="white", bg="#1a1a2e")
lab_download.place(x=60, y=130, height=50, width=380)

# Download Speed Value
lab_down = Label(sp, text="00 Mbps", font=("Helvetica", 25, "bold"), fg="white", bg="#1a1a2e")
lab_down.place(x=60, y=200, height=50, width=380)

# Upload Speed Label
lab_upload = Label(sp, text="Upload Speed", font=("Helvetica", 20, "bold"), fg="white", bg="#1a1a2e")
lab_upload.place(x=60, y=290, height=50, width=380)

# Upload Speed Value
lab_up = Label(sp, text="00 Mbps", font=("Helvetica", 25, "bold"), fg="white", bg="#1a1a2e")
lab_up.place(x=60, y=360, height=50, width=380)

# Speed Check Button
button = Button(sp, text="Check Speed", font=("Helvetica", 20, "bold"), relief=RAISED, bg="#e94560", fg="white", command=start_speed_test)
button.place(x=60, y=460, height=50, width=380)

# Canvas for the rotating loader
loading_canvas = Canvas(sp, width=200, height=200, bg="#1a1a2e", bd=0, highlightthickness=0)

sp.mainloop()


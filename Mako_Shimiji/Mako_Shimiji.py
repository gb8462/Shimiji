import tkinter as tk
import random

window = tk.Tk()

# Window properties
window.geometry('200x200+500+600')  # Adjusted Y-coordinate to start lower
window.overrideredirect(True)  # Remove window decorations like title bar
window.wm_attributes('-topmost', True)  # Keep the window on top of others
window.wm_attributes('-transparentcolor', 'white')  # Set white as transparent

# Load your pet's images
idle_image = tk.PhotoImage(file='Mako_Shimiji/Idle_mako.png')  # Idle image
# For walking Left and right
left_walk_frames = [tk.PhotoImage(file='Mako_Shimiji/Left_walk_Gif.gif', format=f'gif -index {i}') for i in range(2)]  # 2 frames
right_walk_frames = [tk.PhotoImage(file='Mako_Shimiji/Right_walk_Gif.gif', format=f'gif -index {i}') for i in range(2)]  # 2 frames

# Initially set to the idle image
current_image = idle_image

# Create a label to hold the image
label = tk.Label(window, image=current_image, bg='white')
label.pack()

# Movement and animation variables
x = 500
direction = 1  # 1 for moving right, -1 for moving left
speed = 5      # Speed of movement
is_moving = False  # Determines if the pet is moving or stopped
frame_index = 0    # To keep track of the GIF frames

# Function to randomly choose a new direction
def choose_new_direction():
    return random.choice([-1, 1])  # -1 for left, 1 for right

# Function to decide if the pet should stop or resume walking
def decide_action():
    global is_moving, direction
    if random.random() < 0.2:  # 20% chance of stopping
        is_moving = False
        label.config(image=idle_image)  # Set to idle when stopped
    else:
        is_moving = True
        direction = choose_new_direction()  # Randomly choose a new direction when moving

    # Schedule the next action decision after a random interval (between 2 to 5 seconds)
    window.after(random.randint(2000, 5000), decide_action)

# Function to animate the walking GIF
def animate_walk():
    global frame_index
    if is_moving:
        # Choose the correct frame for the current direction
        if direction == 1:
            current_frame = right_walk_frames[frame_index]
        else:
            current_frame = left_walk_frames[frame_index]

        # Update the label with the current frame
        label.config(image=current_frame)

        # Update frame index for the next cycle
        frame_index = (frame_index + 1) % len(right_walk_frames)
        
    # Repeat animation at 100 ms intervals
    window.after(100, animate_walk)

# Function to move the pet
def move_pet():
    global x, direction  # Declare direction as global
    if is_moving:
        x += speed * direction
        if x > 1000:  # Right boundary
            direction = -1
        elif x < 0:  # Left boundary
            direction = 1

        # Update the window position and repeat
        window.geometry(f'200x200+{x}+600')  # Adjust Y-coordinate here
    
    window.after(50, move_pet)  # Keep the loop going

# Start the movement loop
move_pet()

# Start the action decision loop
decide_action()

# Start the animation loop for walking
animate_walk()

# Start the Tkinter main loop
window.mainloop()

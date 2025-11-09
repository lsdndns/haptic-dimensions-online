import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv

# -------------------------------
# Triple trials
# -------------------------------
triple_trials = [
    ['img/img1.png', 'img/img2.png', 'img/img3.png'],
    ['img/img4.png', 'img/img5.png', 'img/img6.png'],
    ['img/img7.png', 'img/img8.png', 'img/img9.png'],
    ['img/img10.png', 'img/img11.png', 'img/img12.png'],
    ['img/img1.png', 'img/img12.png', 'img/img13.png']
]

# -------------------------------
# Data storage
# -------------------------------
data_list = []

# -------------------------------
# Tkinter setup
# -------------------------------
root = tk.Tk()
root.title("Triple Odd-One-Out Experiment")
canvas = tk.Canvas(root, width=900, height=400)
canvas.pack()

current_trial = 0
images = []

# -------------------------------
# Functions
# -------------------------------
def show_trial(trial_index):
    global images
    canvas.delete("all")
    images = []  # reset references
    trial = triple_trials[trial_index]
    positions = [100, 350, 600]  # x positions
    y_pos = 200

    print(f"Showing trial {trial_index + 1}: {trial}")  # debug

    for i, img_path in enumerate(trial):
        try:
            img = Image.open(img_path)
            img = img.resize((150, 150))
            photo = ImageTk.PhotoImage(img)
            images.append(photo)
            canvas.create_image(positions[i], y_pos, image=photo, tags=("img"+str(i)))
            canvas.tag_bind("img"+str(i), "<Button-1>", lambda e, idx=i: record_response(idx))
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")

def record_response(choice_index):
    global current_trial
    trial = triple_trials[current_trial]
    response_img = trial[choice_index]

    # Save trial data
    data_list.append({
        'item1': trial[0],
        'item2': trial[1],
        'item3': trial[2],
        'response_img': response_img
    })

    print(f"Trial {current_trial + 1} response: {response_img}")  # debug

    current_trial += 1
    if current_trial < len(triple_trials):
        show_trial(current_trial)
    else:
        end_experiment()

def end_experiment():
    # Save CSV
    with open('experiment_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['item1', 'item2', 'item3', 'response_img']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data_list:
            writer.writerow(row)
    
    messagebox.showinfo("Done", "Thank you for participating!\nData saved to experiment_data.csv")
    root.destroy()

def start_experiment():
    messagebox.showinfo(
        "Welcome",
        "Welcome to the Triple Odd-One-Out Experiment!\n\n"
        "You will see sets of three images.\n"
        "Click the image that does not fit with the other two.\n\n"
        "Press OK to start."
    )
    show_trial(0)

# -------------------------------
# Start experiment
# -------------------------------
root.after(100, start_experiment)
root.mainloop()


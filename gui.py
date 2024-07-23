import tkinter as tk
from tkinter import messagebox
import json
from spotify_service_and_mood_selector import get_filtered_songs, select_song, read_track_ids_from_json, add_random_songs_to_queue
from get_analysis import get_audio_features, write_audio_features_to_json
from get_stuff import get_all_saved_track_ids, write_track_ids_to_json


def set_mood_happy():
    mood_var.set("Happy")
    label.config(text="You are ... Happy! :)")

def set_mood_sad():
    mood_var.set("Sad")
    label.config(text="You are ... Sad :(")

recommendation_count = 0

def select_song_action():
    global recommendation_count
    mood = mood_var.get()

    filtered_songs = get_filtered_songs(mood)

    if select_song(filtered_songs, mood):
        recommendation_count += 1
        label_recommendation.config(text=f"Recommended you a {mood} song ({recommendation_count})")
    else:
        messagebox.showinfo("No songs found", "No songs found for the given mood.")

def get_and_write_track_ids():
    track_ids = get_all_saved_track_ids()
    write_track_ids_to_json(track_ids)
    messagebox.showinfo("Success", "Saved track IDs written to file!")

def get_and_write_audio_features():
    track_ids = read_track_ids_from_json()
    audio_features = get_audio_features(track_ids)
    write_audio_features_to_json(audio_features)
    messagebox.showinfo("Success", "Audio features retrieved and written to file!")

def calculate_song_mood_percentage():
    try:
        with open("audio_features.json", "r") as file:
            json_data = json.load(file)

        total_songs = len(json_data)
        sad_songs = 0
        happy_songs = 0

        for song in json_data:
            valence = song["valence"]
            if valence < 0.5:
                sad_songs += 1
            else:
                happy_songs += 1

        percentage_sad = round((sad_songs / total_songs) * 100, 2)
        percentage_happy = round((happy_songs / total_songs) * 100, 2)

        messagebox.showinfo("Song Mood Percentage",
                            f"Percentage of sad songs: {percentage_sad}%\n"
                            f"Percentage of happy songs: {percentage_happy}%")
    except FileNotFoundError:
        messagebox.showerror("Error", "Failed to calculate song mood percentage.")

def add_to_queue_action():
    num_songs = int(entry.get())
    mood = mood_var.get()
    if 1 <= num_songs <= 10:
        if add_random_songs_to_queue(mood, num_songs):
            messagebox.showinfo("Success", f"{num_songs} random {mood} song(s) added to the queue.")
        else:
            messagebox.showinfo("No songs found", f"No {mood} songs found.")
    else:
        messagebox.showerror("Invalid input", "Please enter a number between 1 and 10.")

def on_entry_click(event):
    if entry.get() == 'Enter number of songs (1-10)':
        entry.delete(0, "end") 
        entry.insert(0, '') 
        entry.config(fg='black') 

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Enter number of songs (1-10)')
        entry.config(fg='grey', width=27) 

root = tk.Tk()
root.geometry("400x400")  
root.resizable(False, False) 
root.title("Mood Master")

mood_var = tk.StringVar()
mood_var.set("")

label = tk.Label(root, text="You are ... waiting for selection")
label.pack()

button_frame = tk.Frame(root)
button_frame.pack()

button_happy = tk.Button(button_frame, text="Happy", command=set_mood_happy)
button_happy.pack(side=tk.LEFT)

button_sad = tk.Button(button_frame, text="Sad", command=set_mood_sad)
button_sad.pack(side=tk.LEFT)

button_recommend = tk.Button(root, text="Recommend me a song!", command=select_song_action)
button_recommend.pack()

button_getinfo = tk.Button(root, text="Get Track IDs and Audio Features", command=lambda: [get_and_write_track_ids(), get_and_write_audio_features()])
button_getinfo.pack()

button_analysis = tk.Button(root, text="Calculate Song Mood Percentage", command=calculate_song_mood_percentage)
button_analysis.pack()

addsongslabel = tk.Label(root, text="Add songs to your queue!")
addsongslabel.pack()

entry = tk.Entry(root, fg='grey', width=27)
entry.insert(0, 'Enter number of songs (1-10)')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.pack()

button_add_to_queue = tk.Button(root, text="Add to Queue", command=add_to_queue_action)
button_add_to_queue.pack()

label_recommendation = tk.Label(root, text="")
label_recommendation.pack()

root.mainloop()
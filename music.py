import tkinter as tk
from tkinter import filedialog
import pygame
import os
# Initialize pygame
pygame.init()
# Create the main window
window = tk.Tk()
os.environ['DISPLAY'] = ':0'
window.title("Music Player")
# Initialize variables
playlist = []
current_track = 0
is_playing = False
# Functions for controlling the player
def add_to_playlist():
    file_path = filedialog.askopenfilename()
    if file_path:
        playlist.append(file_path)
        playlist_box.insert(tk.END, os.path.basename(file_path))
def play_music():
    global is_playing
    if not is_playing:
        file_path = playlist[current_track]
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        is_playing = True
def stop_music():
    pygame.mixer.music.stop()
    global is_playing
    is_playing = False
def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    stop_music()
    play_music()
def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    stop_music()
    play_music()
def delete_track():
    selected_index = playlist_box.curselection()
    if selected_index:
        index = selected_index[0]
        playlist.pop(index)
        playlist_box.delete(index)
# Create GUI components
add_button = tk.Button(window, text="Add to Playlist", command=add_to_playlist)
add_button.pack()
playlist_box = tk.Listbox(window)
playlist_box.pack()
play_button = tk.Button(window, text="Play", command=play_music)
play_button.pack()
stop_button = tk.Button(window, text="Stop", command=stop_music)
stop_button.pack()
next_button = tk.Button(window, text="Next", command=next_track)
next_button.pack()
prev_button = tk.Button(window, text="Previous", command=previous_track)
prev_button.pack()
delete_button = tk.Button(window, text="Delete", command=delete_track)
delete_button.pack()
# Start the Tkinter main loop
window.mainloop()

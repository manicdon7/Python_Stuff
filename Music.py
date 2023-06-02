import tkinter as tk
import pygame
from tkinter import filedialog

class Musicplayer:
        def __init__(self, root):
                self.root = root
                self.root.title("Music Player")
                self.current_track = None
                self.paused = False

                # Create UI elements
                self.track_label = tk.Label(root, text="No track selected")
                self.track_label.pack(pady=10)

                self.open_button = tk.Button(root, text="Open Track", command=self.open_track, bg="orange")
                self.open_button.pack(pady=5)

                self.play_button = tk.Button(root, text="Play", command=self.play_track, state=tk.DISABLED, bg="green")
                self.play_button.pack(pady=5)

                self.pause_button = tk.Button(root, text="Pause", command=self.pause_track, state=tk.DISABLED, bg="yellow")
                self.pause_button.pack(pady=5)

                self.stop_button = tk.Button(root, text="Stop", command=self.stop_track, state=tk.DISABLED, bg="red")
                self.stop_button.pack(pady=5)

        def open_track(self):
                file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
                if file_path:
                        self.current_track = file_path
                        self.track_label.config(text=file_path)
                        self.play_button.config(state=tk.NORMAL)
                        self.stop_button.config(state=tk.NORMAL)
        def play_track(self):
                if not self.paused:
                        pygame.mixer.init()
                        pygame.mixer.music.load(self.current_track)
                        pygame.mixer.music.play()
                else:
                        pygame.mixer.music.unpause()

                self.paused = False
                self.play_button.config(state=tk.DISABLED)
                self.pause_button.config(state=tk.NORMAL)

        def pause_track(self):
                pygame.mixer.music.pause()
                self.paused = True
                self.pause_button.config(state=tk.DISABLED)
                self.play_button.config(state=tk.NORMAL)

        def stop_track(self):
                pygame.mixer.music.stop()
                self.play_button.config(state=tk.NORMAL)
                self.pause_button.config(state=tk.DISABLED)
                
root = tk.Tk()
music_player = Musicplayer(root)
root.geometry("400x400")
root.resizable(True,True)
root.configure(bg="sky blue")
# Run the application
root.mainloop()


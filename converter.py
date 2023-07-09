import tkinter as tk
from gtts import gTTS

# 1sec audio = ~ 0.4KB
# 7min audio = ~ 1.7MB

# creating text and saving as .mp3
def convert_to_voice():
    text = text_edit.get("1.0", tk.END).strip() # retrieving text
    if not text:
        raise ValueError("No text is present") # exception if no text
    file_name = file_name_edit.get().strip()  # retrieving file name
    tts = gTTS(text)
    file = file_name + ".mp3"
    tts.save(file)

# creating window
window = tk.Tk()
window.title("Converting Text to Speech")

# window size
window.geometry("400x250") # width x height

# frame for file name input
file_name_frame = tk.Frame(window)
file_name_frame.pack(pady=10)

# file name label
file_name_label = tk.Label(file_name_frame, text="File Name:")
file_name_label.pack(side="left")

# file name entry
file_name_edit = tk.Entry(file_name_frame)
file_name_edit.pack(side="left")

# labels
label = tk.Label(window, text="Text:")
label.pack()

# entry
text_edit = tk.Text(window, height=10)
text_edit.pack()

# processing button
press = tk.Button(window, text="Convert", command=convert_to_voice)
press.pack()

# GUI loop
window.mainloop()
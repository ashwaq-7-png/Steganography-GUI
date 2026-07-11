import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from steganography import embed_data, extract_data
import gui

def embed_data_gui():
    image_path = image_path_entry.get()
    data_to_hide = data_to_hide_entry.get()
    output_path = output_path_entry.get()
    alpha = alpha_entry.get() if alpha_entry.get() else None
    embed_data(image_path, data_to_hide, output_path, alpha)
    messagebox.showinfo("Success", "Data embedded successfully!")

def extract_data_gui():
    stego_image_path = stego_image_path_entry.get()
    extracted_data = extract_data(stego_image_path)
    extracted_data_text.delete(1.0, tk.END)
    extracted_data_text.insert(tk.END, extracted_data)

app = tk.Tk()
app.title("Steganography Tool")

# Label and Entry for cover image
image_path_label = tk.Label(app, text="Cover Image:")
image_path_label.pack()
image_path_entry = tk.Entry(app)
image_path_entry.pack()
image_path_button = tk.Button(app, text="Browse", command=lambda: browse_file(image_path_entry))
image_path_button.pack()

# Label and Entry for data to hide
data_to_hide_label = tk.Label(app, text="Data to Hide:")
data_to_hide_label.pack()
data_to_hide_entry = tk.Entry(app)
data_to_hide_entry.pack()

# Label and Entry for stego image
output_path_label = tk.Label(app, text="Stego Image:")
output_path_label.pack()
output_path_entry = tk.Entry(app)
output_path_entry.pack()
output_path_button = tk.Button(app, text="Save As", command=lambda: save_file(output_path_entry))
output_path_button.pack()

# Label and Entry for alpha (transparency)
alpha_label = tk.Label(app, text="Alpha (Transparency):")
alpha_label.pack()
alpha_entry = tk.Entry(app)
alpha_entry.pack()

# Embed Data Button
embed_button = tk.Button(app, text="Embed Data", command=embed_data_gui)
embed_button.pack()

# Label and Entry for stego image (extraction)
stego_image_path_label = tk.Label(app, text="Stego Image:")
stego_image_path_label.pack()
stego_image_path_entry = tk.Entry(app)
stego_image_path_entry.pack()
stego_image_path_button = tk.Button(app, text="Browse", command=lambda: browse_file(stego_image_path_entry))
stego_image_path_button.pack()

# Extract Data Button
extract_button = tk.Button(app, text="Extract Data", command=extract_data_gui)
extract_button.pack()

# Text widget to display extracted data
extracted_data_text = tk.Text(app, height=10, width=40)
extracted_data_text.pack()

# Function to browse for a file and update the entry field
def browse_file(entry_field):
    file_path = filedialog.askopenfilename()
    entry_field.delete(0, tk.END)
    entry_field.insert(0, file_path)

# Function to save a file and update the entry field
def save_file(entry_field):
    file_path = filedialog.asksaveasfilename()
    entry_field.delete(0, tk.END)
    entry_field.insert(0, file_path)

app.geometry("500x500")
app.mainloop()
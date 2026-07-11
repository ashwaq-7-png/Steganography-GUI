from tkinter import filedialog
import tkinter as tk
from gui import embed_data_gui , extract_data_gui
 
def main():
    app = tk.Tk()
    app.title("MEC Steganography GUI")

    # Create and configure widgets
    cover_image_label = tk.Label(app, text="Cover Image:")
    cover_image_entry = tk.Entry(app)
    cover_image_button = tk.Button(app, text="Browse", command=lambda: cover_image_entry.insert(0, filedialog.askopenfilename()))

    data_to_hide_label = tk.Label(app, text="Data to Hide:")
    data_to_hide_entry = tk.Entry(app)

    embedding_rate_label = tk.Label(app, text="Embedding Rate (0.0 to 1.0):")
    embedding_rate_entry = tk.Entry(app)

    embed_button = tk.Button(app, text="Embed Data", command=embed_data_gui)

    stego_image_label = tk.Label(app, text="Stego Image:")
    stego_image_entry = tk.Entry(app)
    stego_image_button = tk.Button(app, text="Browse", command=lambda: stego_image_entry.insert(0, filedialog.askopenfilename()))

    extracting_rate_label = tk.Label(app, text="Extracting Rate (0.0 to 1.0):")
    extracting_rate_entry = tk.Entry(app)

    extract_button = tk.Button(app, text="Extract Data", command=extract_data_gui)

    # Place widgets in the window using grid
    cover_image_label.grid(row=0, column=0, padx=10, pady=5)
    cover_image_entry.grid(row=0, column=1, padx=10, pady=5)
    cover_image_button.grid(row=0, column=2, padx=10, pady=5)

    data_to_hide_label.grid(row=1, column=0, padx=10, pady=5)
    data_to_hide_entry.grid(row=1, column=1, padx=10, pady=5)

    embedding_rate_label.grid(row=2, column=0, padx=10, pady=5)
    embedding_rate_entry.grid(row=2, column=1, padx=10, pady=5)

    embed_button.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    stego_image_label.grid(row=4, column=0, padx=10, pady=5)
    stego_image_entry.grid(row=4, column=1, padx=10, pady=5)
    stego_image_button.grid(row=4, column=2, padx=10, pady=5)

    extracting_rate_label.grid(row=5, column=0, padx=10, pady=5)
    extracting_rate_entry.grid(row=5, column=1, padx=10, pady=5)

    extract_button.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

    app.mainloop()

if __name__ == "_main_":
    main()
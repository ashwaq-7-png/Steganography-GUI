from PIL import Image
import numpy as np

def embed_data(image_path, data_to_hide, output_path, alpha=None):
    # Open the cover image
    cover_image = Image.open(image_path)

    # Create a NumPy array from the cover image
    cover_array = np.array(cover_image)

    # Get the shape of the cover array
    rows, cols, _ = cover_array.shape

    # Ensure data to hide is not longer than available space
    max_data_length = rows * cols
    data_to_hide = data_to_hide[:max_data_length]

    # Convert the data to a binary string
    binary_data = ''.join(format(ord(char), '08b') for char in data_to_hide)

    # Embed the binary data into the cover image
    binary_data_index = 0

    for row in range(rows):
        for col in range(cols):
            if binary_data_index < len(binary_data):
                pixel = cover_array[row][col]
                pixel[-1] = (pixel[-1] & 254) | int(binary_data[binary_data_index])
                binary_data_index += 1

    # Create an image from the modified NumPy array
    stego_image = Image.fromarray(cover_array)

    # Optionally, adjust the alpha value of the stego image
    if alpha is not None:
        stego_image.putalpha(alpha)

    # Save the stego image to the output path
    stego_image.save(output_path)

def extract_data(stego_image_path):
    # Open the stego image
    stego_image = Image.open(stego_image_path)

    # Get the NumPy array from the stego image
    stego_array = np.array(stego_image)

    # Extract the binary data from the stego image
    binary_data = ''
    for row in stego_array:
        for pixel in row:
            binary_data += str(pixel[-1] & 1)

    # Convert the binary data to a string
    extracted_data = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))

    return extracted_data
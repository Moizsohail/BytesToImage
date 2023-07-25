import glob
from PIL import Image
def extract_bits_from_images(sequence, tile_size):
    bytes = bytearray()
    for image in sequence:
        pixels = list(image.getdata())
        for i in range(0, len(pixels), 8):
            byte = 0
            for j in range(8):
                pixel = pixels[i + j]
                bit = pixel & 1
                byte |= bit << j
            bytes.append(byte)
    return bytes

def remove_padding(bits, padding_size):
    return bits[:len(bits) - padding_size]

# Define image dimensions and tile size
image_width = 1024
image_height = 1024
tile_size = image_width * image_height // 8

# Load the sequence of images
sequence = []
num_tiles = len(glob.glob('output/*'))  # Replace with the actual number of tiles

for i in range(num_tiles):
    image = Image.open(f'output/tile_{i}.png')
    sequence.append(image)

# Extract the bits from the images
bits = extract_bits_from_images(sequence, tile_size)

# Remove padding
bits = bits[:66537080]
# Save the reconstructed file
with open('decoded.mp4', 'wb') as file:
    file.write(bits)
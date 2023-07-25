import math
from PIL import Image

def arrange_bits_into_tiles(bytes, tile_size):
    total_size = len(bytes)
    num_tiles = math.ceil(total_size / tile_size * 8)
    # padding_size = (num_tiles * tile_size) - total_size

    # # Calculate the number of bytes required for padding
    # padding_bytes = padding_size // 8
    # padding_bits = padding_size % 8

    # # Add padding bytes
    # bits += b'\x00' * padding_bytes

    # Add padding bits
    # if padding_bits > 0:
    # last_byte = bits[-1]
    # last_byte |= (1 << (8 - padding_bits)) - 1
    # bits = bits[:-1] + bytes([last_byte])
    return bytes, num_tiles

def convert_bits_to_images(bytes, num_tiles, image_width, image_height):
    for i in range(num_tiles):
        start_index = i * image_width * image_height // 8 
        end_index = (i + 1) * image_width * image_height // 8
        tile_bytes = bytes[start_index:end_index]
        image_data = [(byte & (1 << j)) >> j for byte in tile_bytes for j in range(8)]
        image = Image.new('1', (image_width, image_height))
        image.putdata(image_data)
        image.save(f'output/tile_{i}.png')
    

# Read the file and obtain the bits
filename = 'src.mp4'
with open(filename, 'rb') as file:
    bytes = file.read()

# Arrange bits into tiles
tile_size = 1920 * 1080
bytes, num_tiles = arrange_bits_into_tiles(bytes, tile_size)
# Define image dimensions
image_width = 1920
image_height = 1080

# Convert bits to a sequence of images
sequence = convert_bits_to_images(bytes, num_tiles, image_width, image_height)


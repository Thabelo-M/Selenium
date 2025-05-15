# Python code to convert an image into a binary string

def image_to_binary_string(image_path):
    with open(image_path, "rb") as image_file:
        binary_string = image_file.read()
    return binary_string

# Example usage
image_path = "buggy.jpg"  # Path to your image file
binary_string = image_to_binary_string(image_path)

# To print the binary string (optional and may be large)
# print(binary_string)

# Save the binary string into a file (optional)
with open("binary_image.bin", "wb") as binary_file:
    binary_file.write(binary_string)

print(f"Binary string created from image: {image_path}")

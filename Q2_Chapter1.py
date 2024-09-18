from PIL import Image
import random
import os

def generate_n():
    return random.randint(1, 50)

def process_image(input_path, output_path, n):
    # Open the image
    with Image.open(input_path) as img:
        # Convert image to RGB mode if it's not already
        img = img.convert('RGB')
        
        # Get the dimensions of the image
        width, height = img.size
        
        # Create a new image with the same size
        new_img = Image.new('RGB', (width, height))
        
        # Process each pixel
        sum_red = 0
        for x in range(width):
            for y in range(height):
                # Get the RGB values of the current pixel
                r, g, b = img.getpixel((x, y))
                
                # Add n to each channel, ensuring values stay within 0-255
                new_r = min(r + n, 255)
                new_g = min(g + n, 255)
                new_b = min(b + n, 255)
                
                # Set the new pixel in the new image
                new_img.putpixel((x, y), (new_r, new_g, new_b))
                
                # Add the new red value to the sum
                sum_red += new_r
        
        # Save the new image
        new_img.save(output_path)
        
        return sum_red

# Main execution
if __name__ == "__main__":
    n = generate_n()
    
    # Use absolute paths with .jpg extension
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_image = os.path.join(current_dir, "Chapter1.jpg")
    output_image = os.path.join(current_dir, "chapter1out.png")
    
    if not os.path.exists(input_image):
        print(f"Error: Input image not found at {input_image}")
        print("Please make sure the file exists and the name is correct (including case).")
    else:
        sum_of_red = process_image(input_image, output_image, n)
        print(f"The sum of all red pixel values in the new image is: {sum_of_red}")
        print(f"The generated number n was: {n}")
        print(f"Output image saved as: {output_image}")

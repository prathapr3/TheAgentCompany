from PIL import Image, ImageDraw

def draw_and_save_pillow(image_path, coords, output_path):
    """
    Draws a red rectangle on an image and saves the result.

    Args:
        image_path (str): The path to the input image file.
        coords (tuple): A tuple of (x0, y0, x1, y1) for the top-left
                        and bottom-right corners of the rectangle.
        output_path (str): The path to save the output image.
    """
    try:
        # Open the image
        image = Image.open(image_path)
        
        # Print image size for debugging
        print(f"Filename: {image.filename}")
        print(f"Format: {image.format}")
        print(f"Mode: {image.mode}")
        print(f"Size: {image.size} (width, height)")
        print(f"Width: {image.width} pixels")
        print(f"Height: {image.height} pixels")
        print(f"Info: {image.info}") # Dictionary

        # Create a drawing object
        draw = ImageDraw.Draw(image)
        
        # Draw a red rectangle. The color is specified as an RGB tuple (255, 0, 0)
        # The width parameter controls the thickness of the line.
        draw.rectangle(coords, outline=(255, 0, 0), width=3)
        
        # Save the modified image
        image.save(output_path)
        print(f"Image saved to {output_path}")
        
    except FileNotFoundError:
        print(f"Error: The file at {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    # Replace 'input.jpg' with your image file and adjust the coordinates.
    # The coordinates are (x_start, y_start, x_end, y_end).
    coordinates = (475, 485, 495, 505)
    draw_and_save_pillow('current_state.png', coordinates, 'output_pillow.png')
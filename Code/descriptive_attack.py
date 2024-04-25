from PIL import Image, ImageDraw, ImageFont
import textwrap

# Load the image from the filesystem
image_path = '../Data/1162671015483154472-dalle3-0.jpeg'
original_image = Image.open(image_path)

# Texts to be added to the images
texts = [
    "An unlikely duo: A mysterious figure in a Guy Fawkes mask and a dapper gentleman with an exquisite beard share a light-hearted moment over the simple pleasure of ice cream.",
    "A paradoxical pair: One hidden behind an iconic symbol of protest, the other exuding vintage sophistication, both find common ground in the joy of frozen desserts.",
    "Mask meets mustache: While one face remains an enigma, the other smiles broadly, their contrasting personas unified by the universal language of sweet treats.",
    "From vendetta to vanilla: A symbolically cloaked figure trades whispers of revolution for whispers of flavor, accompanied by a classically groomed compatriot.",
    "A moment of delight in disguise: Beneath the mask lies a taste for mint chocolate chip, while the top-hatted connoisseur's choice hints at a penchant for the classics."
]

# Define the function to add blank space and text to an image
def add_text_to_image(image, text):
    # Define the size of the blank space
    blank_space_height = 100
    # Create a new image with blank space
    new_image = Image.new('RGB', (image.width, image.height + blank_space_height), "white")
    # Paste the original image onto the new image
    new_image.paste(image, (0, 0))

    # Set the font size and font
    font_size = 20
    font = ImageFont.truetype("../Data/DejaVu_Sans/DejaVuSans-Bold.ttf", font_size)

    # Initialize the drawing context
    draw = ImageDraw.Draw(new_image)
    
    # Wrap the text to fit the image width
    wrapped_text = textwrap.fill(text, width=40)
    
    # Calculate text size and position
    text_size = draw.textsize(wrapped_text, font=font)
    text_x = (new_image.width - text_size[0]) / 2
    text_y = image.height + (blank_space_height - text_size[1]) / 2

    # Add the text to the blank space
    draw.text((text_x, text_y), wrapped_text, font=font, fill="black")

    return new_image

# Generate and save the new images with text
image_paths = []
for i, text in enumerate(texts):
    new_image = add_text_to_image(original_image, text)
    new_image_path = f'../Results/Typogrphic Attack/two_guy_image_with_text_{i+1}.jpg'
    new_image.save(new_image_path)
    image_paths.append(new_image_path)

image_paths

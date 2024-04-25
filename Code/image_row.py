from PIL import Image
import numpy as np

# Define a function to square an image and add spacing
def square_image_and_add_spacing(img, side_length, spacing, background_color=(255, 255, 255)):
    # Create a new image with the desired background color and size plus spacing
    squared_img = Image.new("RGB", (side_length + 2*spacing, side_length + 2*spacing), background_color)
    
    # Calculate the position to paste the input image so it's centered
    img.thumbnail((side_length, side_length))
    paste_position = (spacing + (side_length - img.width) // 2, spacing + (side_length - img.height) // 2)
    
    # Paste the input image onto the squared image
    squared_img.paste(img, paste_position)
    
    return squared_img

# Load the images from the files
file_paths = [
    '1162218741245935670-dalle3-0.jpg',  # The first image is a .jpg
    '1162218741245935670-dalle3-1.png',
    '1162218741245935670-dalle3-2.png',
    '1162218741245935670-FusionBrain-1.png',
    '1162218741245935670-FusionBrain-2.png'
]

# Ensure all images are the same height for the final merging
side_length = max(Image.open(fp).height for fp in file_paths)
spacing = 10  # spacing between images

# Process and square each image, then add spacing
processed_images = [square_image_and_add_spacing(Image.open(fp), side_length, spacing) for fp in file_paths]

# Calculate the total width for the final image (including spacing between images)
total_width = sum(img.width for img in processed_images)

# Create a new image with the calculated total width and the height of the squared images
final_image = Image.new('RGB', (total_width, side_length + 2*spacing), (255, 255, 255))

# Paste each image onto the final image, one after another
current_x = 0
for img in processed_images:
    final_image.paste(img, (current_x, 0))
    current_x += img.width

# Save the final image
output_path = 'merged_row_image.png'
final_image.save(output_path)

# Return the path to the saved image
output_path


# # Define the file paths for the newly uploaded images
# new_file_paths = [
#     '1162217595026554880-dalle3-0.jpg',  # The first image is a .jpg
#     '1162217595026554880-dalle3-1.png',
#     '1162217595026554880-dalle3-2.png',
#     '1162217595026554880-FusionBrain-1.png',
#     '1162217595026554880-FusionBrain-2.png'
# ]

# # Determine the side length for squaring the images based on the largest image height
# new_side_length = max(Image.open(fp).height for fp in new_file_paths)

# # Process and square each new image, then add spacing
# new_processed_images = [square_image_and_add_spacing(Image.open(fp), new_side_length, spacing) for fp in new_file_paths]

# # Calculate the total width for the new final image (including spacing between images)
# new_total_width = sum(img.width for img in new_processed_images)

# # Create a new image with the calculated total width and the height of the squared images
# new_final_image = Image.new('RGB', (new_total_width, new_side_length + 2*spacing), (255, 255, 255))

# # Paste each new image onto the final image, one after another
# current_x = 0
# for img in new_processed_images:
#     new_final_image.paste(img, (current_x, 0))
#     current_x += img.width

# # Save the new final image
# new_output_path = 'new_merged_row_image.png'
# new_final_image.save(new_output_path)

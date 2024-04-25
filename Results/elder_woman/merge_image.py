from PIL import Image
import os

def merge_images_centered(image_files, output_file):
    images = [Image.open(img) for img in image_files]

    # Assuming all images are the same size, get dimensions of first image
    width, height = images[0].size

    # Create a new image with a white background
    new_im = Image.new('RGB', (width * 3, height * 3), (255, 255, 255))

    # Iterate over the images and paste them into the new image, centered in each grid cell
    for i, img in enumerate(images):
        # Calculate the offsets to center each image in its grid cell
        x_offset = (i % 3) * width + (width - img.width) // 2
        y_offset = (i // 3) * height + (height - img.height) // 2

        new_im.paste(img, (x_offset, y_offset))

    new_im.save(output_file)

# Define the image files to be merged
image_files1 = [
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence1_img1.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence2_img1.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence3_img1.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence4_img1.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence5_img1.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence6_img1.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence7_img1.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence8_img1.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence9_img1.png'
]

image_files2 = [
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence1_img2.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence2_img2.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence3_img2.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence4_img2.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence5_img2.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence6_img2.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence7_img2.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence8_img2.png', 
    '/Users/maomao/Documents/GitHub/CS523Project/Results/elder_woman/DALLE_sentence9_img2.png'
]


# Define the output file name
output_file1 = 'merged_image1.png'
output_file2 = 'merged_image2.png'
merge_images_centered(image_files1, output_file1)
merge_images_centered(image_files2, output_file2)

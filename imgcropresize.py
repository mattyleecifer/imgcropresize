from PIL import Image, ImageOps
import re

imgPath = input("Enter image path:\n")
img = Image.open(imgPath, 'r')

# Crop to content
img = img.convert('RGB')
bbox = ImageOps.invert(img).getbbox()
cropped = img.crop(bbox)

# Creates white bg
img_w, img_h = cropped.size
background = Image.new('RGBA', (img_w, img_h), (255, 255, 255, 255))
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
background.paste(cropped, offset)
# background.save('out.png')

# Resize image
width, height = background.size
new_width = int(width * (20/height))
resized_image = background.resize((new_width, 20))

# Save the resized image as original name + 20.png
outputName = re.findall("(\w+)\.[^\.]+$", imgPath)
outputName = outputName[0] + "20.png"
resized_image.save(outputName)

print("Image output to " + outputName + ("\n"))


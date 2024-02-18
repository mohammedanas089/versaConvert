'''from PIL import Image, ImageDraw, ImageFont

# Take text input from the user
text = "the still smell of old beer drinkers it takes hi to bring out the order I called it yourself invest a salt a kotess find the M tacos Al pastor my favourite is just for food is Bihar cross bun"
# Create an Image object
img = Image.new('RGB', (500, 200), color = (73, 109, 137))

# Create a Draw object
d = ImageDraw.Draw(img)

# Specify the font to be used
font = ImageFont.truetype('arial.ttf', size=50)

# Get the size of the text
text_size = d.textsize(text, font)

# Calculate the position of the text
x = (4000 - text_size[0]) 
y = (100 - text_size[1])
print(x,img.height,text_size[1])
# Draw the text on the image
d.text((x, y), text, fill=(255, 255, 0), font=font)

# Save the image
img.save('text_image.png')

# Show the image
img.show()
'''
from PIL import Image, ImageDraw, ImageFont
def txt_img():
    # set the text to be added to the image
    text=input("Enter the text to convert to image:")
    print("check")
    # set the font size and font type
    font_size = 50
    font_type = "arial.ttf"

    # create the font object
    font = ImageFont.truetype(font_type, size=font_size)

    # calculate the required width and height of the image
    text_width, text_height = font.getsize(text)
    image_width = text_width + 20  # add padding to the width
    image_height = text_height + 20  # add padding to the height

    # create a new image with the calculated dimensions
    image = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))

    # create a draw object
    draw = ImageDraw.Draw(image)

    # set the position for the text
    text_x = 10
    text_y = 10

    # add the text to the image
    draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

    # save the image
    image.save('text_image.png')
    image.show()
    image.close()
    image.__exit__()


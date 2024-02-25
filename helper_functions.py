from PIL import Image
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
import requests
from io import BytesIO


def text_to_image(text, output_image_path, font_size=72, max_width=1272, font_path="Hind-Light.ttf"):
    # Initialize image with a white background
    # Initial height is 0, will be updated dynamically
    image_size = (max_width, 0)
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(
        font_path, font_size) if font_path else ImageFont.load_default()

    # Split the text into lines based on max_width
    lines = []
    words = text.split()
    current_line = words[0]

    for word in words[1:]:
        test_line = current_line + " " + word
        text_width, _ = draw.textsize(test_line, font)

        if text_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)

    # Calculate the total text height and update image size
    total_text_height = sum(font.getsize(line)[1] for line in lines)
    image_size = (max_width, total_text_height)
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    # Draw the lines on the image
    y_position = 0
    for line in lines:
        text_width, text_height = draw.textsize(line, font)
        x_position = (max_width - text_width) // 2
        draw.text((x_position, y_position), line, fill="black", font=font)
        y_position += text_height

    image.save(output_image_path)


def resize_image(width, filename):
    base_width = width
    img = Image.open(filename)

    w_percent = (base_width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))

    # Use Image.LANCZOS for resampling
    img = img.resize((base_width, h_size), Image.LANCZOS)
    img.save(filename)


def save_image_from_url(url, path):
    max_width = 1272
    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.save(path)
        resize_image(max_width, path)
        print('Image saved successfully.')
    else:
        print('Failed to download image. Status code:', response.status_code)

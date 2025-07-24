from PIL import Image, ImageDraw, ImageFont

def get_empty():
    return Image.new("RGB", (1,1), color=(0,)*4)

def draw_card(text:str, author:str):
    img = Image.open("base.png").convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font.ttf", 48)
    attrib_font = ImageFont.truetype("font.ttf", 24)
    
    max_width = img.width - 40
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + " " + word if current_line else word
        w = draw.textlength(test_line, font=font)
        if w <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
        if len(lines) == 4:
            break

    if len(lines) < 4 and current_line:
        lines.append(current_line)

    if len(lines) == 4 and (len(words) > sum(len(line.split()) for line in lines)):
        while True:
            if not lines[-1]:
                break
            test_line = lines[-1] + "..."
            w = draw.textlength(test_line, font=font)
            if w <= max_width:
                lines[-1] = lines[-1] + "..."
                break
            else:
                # Remove last word
                lines[-1] = " ".join(lines[-1].split()[:-1])

    # Draw lines
    y = 20
    for line in lines:
        draw.text((24, y), line, font=font, fill=(255,)*4)
        y += 48 + 8

    author_w = draw.textlength(author, font=attrib_font)
    draw.text((img.width-author_w-20, img.height-60), author, font=attrib_font)

    return img

if __name__ == "__main__":
    img = draw_card(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sodales, lectus a gravida posuere, erat justo vestibulum nisl, non venenatis orci turpis ac nulla. Cras dictum et felis feugiat rutrum. Integer a odio tempus, luctus nisl ut, ultricies lacus. Nunc in nibh felis. Nulla mollis tincidunt mauris. Pellentesque pellentesque auctor laoreet. Maecenas finibus accumsan lobortis. Praesent vel ornare magna. In suscipit pharetra ipsum pellentesque sagittis.",
        "@author"
    )
    img.show()

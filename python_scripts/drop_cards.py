from PIL import ImageFile, ImageDraw, ImageFont
from io import BytesIO
import mysql.connector, textwrap, PIL, random, string, os

""" def get_custom_image_drop(card_id):
    def text_edition(img, font, text, color=(0, 0, 0)):
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(text, font)
        position = ((strip_width-text_width+200)/2,765)
        draw.text(position, text, color, font=font)
        return img

    mycursor.execute("SELECT * FROM card_info WHERE card_id = " + str(card_id))
    res = mycursor.fetchone()   

    strip_width, strip_height = 500, 810

    file_like= BytesIO(res["card_img"])
    background = PIL.Image.open(file_like)
    background = background.resize((500, 810))
    foreground = ""
    if res["card_edition"] == 1:
        foreground = PIL.Image.open("./borders/level1.png")
        background.paste(foreground, (0, 0), foreground)
    elif res["card_edition"] == 2:
        foreground = PIL.Image.open("./borders/level2.png")
        background.paste(foreground, (0, 0), foreground)
    elif res["card_edition"] == 3:
        foreground = PIL.Image.open("./borders/level3.png")
        background.paste(foreground, (0, 0), foreground)
    else:
        foreground = PIL.Image.open("./borders/level1.png")
        background.paste(foreground, (0, 0), foreground)

    #image_width
    font = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 40)
    small_font = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 28)

    text_start_height = 75
    draw_multiple_line_text(background, res["char_name"], font, "#000", text_start_height)
    draw_multiple_line_text(background, res["anime_origin"], font, "#000", 685)

    background = text_edition(background, small_font, str(res["card_edition"]) + " · #" + str(res["card_total_count"] + 1))
    
    buffer = BytesIO()     
    background.save(buffer, 'jpeg')
    buffer.seek(0)        
    bg_image = buffer         

    return bg_image

def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=25)
    if len(lines) > 1:
        y_text -= 20
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height

def byte_img(img, i, location):
    img.save("./" + str(location) + "/" + str(i) + ".png", format='PNG') """

def main():
    mycursor.execute("SELECT * FROM card_amount")
    cardamount = mycursor.fetchone()["amount"]

    cards = []

    for i in range(3):
        n = random.randint(0, cardamount - 1)
        mycursor.execute("SELECT * from card_info LIMIT 1 OFFSET " + str(n))
        cards.append(mycursor.fetchone())

    """ _location = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    os.mkdir("./drops/" + str(_location))

    test = [get_custom_image_drop(m["card_id"]) for m in cards]
    images = [PIL.Image.open(x).save("./drops/" + str(_location) + "/" + str(i + 1) + ".png", format='PNG') for i, x in enumerate(test)] """
    output = {'card1': cards[0]["card_id"], 'card2': cards[1]["card_id"], 'card3': cards[2]["card_id"]}
    print(output)

if __name__ == "__main__":
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="oni-cards",
        use_unicode=True,
        charset="utf8mb4",
        collation='utf8mb4_general_ci',)
    mydb.set_charset_collation('utf8mb4', 'utf8mb4_general_ci')
    mycursor = mydb.cursor(dictionary=True, buffered=True)
    main = main()
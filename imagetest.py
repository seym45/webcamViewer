from PIL import Image, ImageDraw

im = Image.open('test.jpg')

picture = im.convert('RGBA')
frame = Image.open('frame_2.png')
background = Image.new('RGBA', frame.size, (255, 255, 255, 0))
background.paste(picture, (10,9))
background.paste(frame, (0,0), frame)
background.save('logocopy.png', 'PNG')

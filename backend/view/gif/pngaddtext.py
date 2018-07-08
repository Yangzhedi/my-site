# -*- coding: utf-8 -*-
from PIL import Image,ImageFont,ImageDraw
import imageio
def processImage(path,text):
    # ttfont = ImageFont.truetype("/Library/Fonts/华文细黑.ttf",20)
    # im = Image.open(path)
    # draw = ImageDraw.Draw(im)
    # draw.text((10,10),u'韩寒', fill=(0,0,0),font=ttfont)
    # draw.text((40,40),unicode('杨利伟','utf-8'), fill=(0,0,0),font=ttfont)
    # im.show()
    im = Image.open(path)
    draw = ImageDraw.Draw(im)
    newfont = ImageFont.truetype('/usr/share/fonts/msyh.ttc', 20, encoding="unic")
    # text1 = '1234567890123456789012345678'
    text = text
    # text = 'abcdefghijk'
    # print(text.__len__())
    left = 160 - (text.__len__() * 20) / 2
    draw.text((left, 170), text, (255, 255, 255),font=newfont)
    # im.show()
    im.save('gif/target/'+ path[:-4][15:]+'.png')
    print('gif/target/'+ path[:-4][15:]+'.png')



def create_gif(image_list, gif_name):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
        # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.1)
    return


def main(list):
    # 第一句话
    for i in range(14):
        processImage("gif/wangjingze/wangjingze-"+str(i)+".png", list[0])
    for i in range(14,16):
        processImage("gif/wangjingze/wangjingze-"+str(i)+".png", '')
    for i in range(16, 28):
        processImage("gif/wangjingze/wangjingze-" + str(i) + ".png", list[1])
    for i in range(28, 30):
        processImage("gif/wangjingze/wangjingze-" + str(i) + ".png", '')
    for i in range(30, 43):
        processImage("gif/wangjingze/wangjingze-" + str(i) + ".png", list[2])
    for i in range(43, 46):
        processImage("gif/wangjingze/wangjingze-" + str(i) + ".png", '')
    for i in range(46, 56):
        processImage("gif/wangjingze/wangjingze-" + str(i) + ".png", list[3])
    for i in range(56, 64):
        processImage("gif/wangjingze/wangjingze-" + str(i) + ".png", '')
        # print(i)
    image_list = []
    for i in range(55):
        # if i % 2 == 0:
        image_list.append('gif/target/wangjingze-' + str(i) + '.png')
        print(i)
    # image_list = ['wangjingze/wangjingze-0.png', 'test_gif-2.png', 'test_gif-4.png', 'test_gif-6.png', 'test_gif-8.png', 'test_gif-10.png']
    gif_name = 'created_test.gif'
    print(image_list)
    create_gif(image_list, gif_name)


if __name__ == "__main__":
    main()
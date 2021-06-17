from PIL import Image
import os


for file in os.listdir('orig'): # . 代表現在位置
    if file.endswith('.jpg'): # 檢查字串結尾
        #image_file = Image.open('orig/' + file) # open colour image
        image_file = Image.open(os.path.join('orig', file)) # open colour image
        #print(type(image_file)) #find image_file class
        image_file = image_file.convert('L') # convert image to black and white
        #image_file.save('result/' + file[:-4] + '_grey.png')  # [:-4] 零到倒數第四個位置
        image_file.save(os.path.join('result', file[:-4] + '_grey.png'))  # [:-4] 零到倒數第四個位置


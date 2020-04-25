from grid_captcha import CaptchaBuilder
from tqdm import tqdm
import os
os.system('mkdir grid_captcha_data')

for i in tqdm(range(1000000)):
    builder = CaptchaBuilder()  # Create builder
    builder.build()  # Generate new image
    #print(''.join(builder.ret_name()))
    word = builder.word
    #builder.show()
    builder.save(str(''.join(builder.ret_name())+".png"))
    image_jpeg = builder.base64()
    image_png = builder.base64(image_format='PNG')
    os.system('mv *.png grid_captcha_data')
    
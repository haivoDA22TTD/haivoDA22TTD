import os
import random
from PIL import Image, ImageDraw

if not os.path.exists('dist'):
    os.makedirs('dist')

frames = []
width, height = 500, 500

# Tạo khung hình giả lập mưa sao băng
for i in range(30):  # Tạo 30 khung hình
    img = Image.new('RGB', (width, height), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Vẽ sao băng ngẫu nhiên
    for _ in range(5):  # 5 sao băng trong mỗi khung hình
        x_start = random.randint(0, width)
        y_start = random.randint(0, height // 2)
        length = random.randint(50, 150)
        draw.line([x_start, y_start, x_start + length, y_start + length], fill="white", width=2)
    
    frames.append(img)

# Lưu file GIF
frames[0].save('dist/meteor_shower.gif', save_all=True, append_images=frames[1:], duration=100, loop=0)

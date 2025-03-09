from PIL import Image, ImageDraw
import random

# Kích thước của ảnh (tương tự kích thước biểu đồ đóng góp)
width, height = 400, 400
background_color = (0, 0, 0)  # Màu nền là đen
meteor_color = (255, 255, 255)  # Màu của sao băng là trắng

# Số lượng sao băng sẽ xuất hiện
num_meteors = 30

# Tạo các frame cho GIF
frames = []

for i in range(20):  # Tạo 20 frame GIF
    frame = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(frame)

    # Vẽ sao băng ngẫu nhiên
    for _ in range(num_meteors):
        # Vị trí ngẫu nhiên của sao băng
        x = random.randint(0, width)
        y = random.randint(0, height)
        length = random.randint(10, 30)  # Độ dài sao băng
        speed = random.randint(1, 5)  # Tốc độ sao băng
        # Vẽ sao băng
        for j in range(length):
            draw.line([(x + j * speed, y - j * speed), (x + (j + 1) * speed, y - (j + 1) * speed)], fill=meteor_color, width=2)

    frames.append(frame)

# Lưu các frame dưới dạng GIF động
frames[0].save('dist/meteor_shower.gif', save_all=True, append_images=frames[1:], duration=100, loop=0)

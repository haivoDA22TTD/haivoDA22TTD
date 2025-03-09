import os
from PIL import Image, ImageDraw, ImageFont

# Đảm bảo thư mục dist/ tồn tại
if not os.path.exists('dist'):
    os.makedirs('dist')

# Tạo một số khung hình giả sử (chỉ là ví dụ)
frames = []  # Đây sẽ là danh sách chứa các khung hình của mưa sao băng

# Giả sử bạn đang tạo ảnh từ các khung hình đơn giản
for i in range(10):
    img = Image.new('RGB', (500, 500), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((10, 10), f"Frame {i}", fill=(0, 0, 0))
    frames.append(img)

# Lưu file GIF vào thư mục dist/
frames[0].save('dist/meteor_shower.gif', save_all=True, append_images=frames[1:], duration=100, loop=0)

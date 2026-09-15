with open("lab1.bmp", "rb") as f:
    data = bytearray(f.read())

#размеры и смещение пикселей
offset = int.from_bytes(data[10:14], "little")
width  = int.from_bytes(data[18:22], "little")
height = int.from_bytes(data[22:26], "little")

row_size = (width * 3 + 3) & ~3   # строки выровнены до 4 байт

def dot(x, y, color, size=2):
    r, g, b = color
    for dy in range(-size, size + 1):
        for dx in range(-size, size + 1):
            px, py = x + dx, y + dy
            if 0 <= px < width and 0 <= py < height:
                #снизу вверх, порядок байт B, G, R
                i = offset + (height - 1 - py) * row_size + px * 3
                data[i], data[i+1], data[i+2] = b, g, r

dot(3, 3, (0, 127, 127))         # верхний левый угол
dot(width - 3, 3, (127, 0, 127))    # правый верхний угол
dot(0, height // 2, (127, 127, 0))  # центр левого столбца
with open("output.bmp", "wb") as f:
    f.write(data)

import os
os.startfile("output.bmp")
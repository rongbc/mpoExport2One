#!/usr/bin/env python3
import sys
import os
from PIL import Image
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="PIL")


if len(sys.argv) == 2:
    inputFile = sys.argv[1]
    if os.path.isfile(inputFile):
        with open(inputFile, 'rb') as ff:
            ff.seek(6)
            data = ff.read()
            # find the marker for the second image
            offset = data.find(b'\xFF\xD8\xFF\xE1') # 在二进制数据中查找字节序列，需要加上b前缀
            dataLeft = data[offset:]
            # print(f"size of left: {len(dataLeft)}")
            ff.seek(0)
            data = ff.read()
        dataRight = data[:offset+6]
        filePair = os.path.splitext(inputFile)
        fileName = filePair[0]
        # write output
        with open(fileName+'-L.jpg', 'wb') as left:
            left.write(dataLeft)
        with open(fileName+'-R.jpg', 'wb') as right:
            right.write(dataRight)
        # 读取左右两张图片
        imgLeft = Image.open(fileName+'-L.jpg')
        imgRight = Image.open(fileName+'-R.jpg')
        # 获取图片的宽度和高度
        widthLeft, heightLeft = imgLeft.size
        widthRight, heightRight = imgRight.size
        # 创建一个新的图片，宽度为两张图片的宽度之和，高度为两张图片的最大高度
        imgCombined = Image.new('RGB', (widthLeft + widthRight, max(heightLeft, heightRight)))
        # 将左右两张图片粘贴到新的图片上，左边的图片在左上角，右边的图片在右上角
        imgCombined.paste(imgRight, (0, 0))
        imgCombined.paste(imgLeft, (widthRight, 0))
        # 保存拼接后的图片
        imgCombined.save(fileName+'-Combined.jpg')
        print(f"Processing is complete: {inputFile[-13:]}")
    else:
        print(f"No such file, {inputFile}")
else:
    print(f"{sys.argv[0]} takes only one argument, a single file ending with .mpo")

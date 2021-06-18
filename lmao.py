import os
import urllib.request
from pygame import mixer

run = True
'''opener = urllib.request.FancyURLopener({})
urllib.request.urlretrieve('http://www.ptnk.edu.vn/index.php?option=com_content&task=blogcategory&id=42&Itemid=224', filename= os.getcwd()+ '/lmao.txt')
previous = open(os.getcwd()+ '/lmao.txt', 'r', encoding="utf-8").read()'''
while run:
    file = open(os.getcwd()+ '/lmao.txt', "r", encoding="utf-8")
    for line in file:
        print(line)
        if 'KẾT QUẢ TUYỂN SINH NĂM HỌC 2020-2021' in line or 'KẾT QUẢ TUYỂN SINH NĂM HỌC 2021-2022' in line: #or 'KẾT QUẢ TUYỂN SINH NĂM HỌC 2019-2020' in line
            run = False
            mixer.init()
            urllib.request.urlretrieve("https://github.com/nVietUK/FakeModernUIApplication/blob/main/Rick%20Astley%20-%20Never%20Gonna%20Give%20You%20Up%20(Video).mp3?raw=true", filename= os.getcwd()+ '/lmao.mp3')
            mixer.music.load(os.getcwd()+ '/lmao.mp3')
            mixer.music.play()
    urllib.request.urlretrieve('http://www.ptnk.edu.vn/index.php?option=com_content&task=blogcategory&id=42&Itemid=224', filename= os.getcwd()+ '/lmao.txt')
input()
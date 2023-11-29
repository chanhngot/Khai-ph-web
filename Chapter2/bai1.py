import requests
from bs4 import BeautifulSoup
import os

#####CHỈ CẦN XÂY DỰNG TẬP HYPERLINK THÔI

url="http://baovanhoa.vn/kinh-te/doanh-nghiep"

#Cách 2: Dựa trên quy tắc cấu trúc url để tạo link
Links_ToDo=[url]
for i in range(2,93):
    Link="http://baovanhoa.vn/kinh-te/doanh-nghiep/pgrid/591/pageid/" + str(i)
    Links_ToDo += [Link]
str=""
for url in Links_ToDo:
    print(url)
    html = requests.get(url).text
print(str)
# # Bóc tách các nội dung, gồm: Tiêu đề bài báo, Tóm tin, Ngày giờ đăng bài, Nguồn tin.
#Installing emot library
#### LẤY HYPERLINK MÀ LƯU VÔ FILE TEXT THÌ : 
import requests
from bs4 import BeautifulSoup
import os


url="http://baovanhoa.vn/kinh-te/doanh-nghiep"

#Cách 2: Dựa trên quy tắc cấu trúc url để tạo link
Links_ToDo=[url]
for i in range(2,5):
    Link="http://baovanhoa.vn/kinh-te/doanh-nghiep/pgrid/591/pageid/" + str(i)
    Links_ToDo += [Link]
for url in Links_ToDo:
    html = requests.get(url).text
    with open('vidu.txt','a',encoding='utf-8') as f:
        f.writelines(url+"\n")
# Bóc tách các nội dung, gồm: Tiêu đề bài báo, Tóm tin, Ngày giờ đăng bài, Nguồn tin.


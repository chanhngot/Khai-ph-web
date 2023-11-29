from bs4 import BeautifulSoup
import requests
import os


url="https://tapchinganhang.gov.vn/chinh-sach.htm"


#Cách 2: Dựa trên quy tắc cấu trúc url để tạo link
Links_ToDo=[url]
for i in range(2,19):
    Link="https://tapchinganhang.gov.vn/chinh-sach/p-" + str(i) + ".htm"
    Links_ToDo += [Link]


str=""
for url in Links_ToDo:
    print(url)
    html = requests.get(url).text


    #Tối ưu hóa code HTML bằng thư viện html5lib
    soup = BeautifulSoup(html, 'html5lib')


    #Sử dụng thư viện BeautifulSoup để bóc tách dữ liệu
    TieuDe = soup.find_all("a",class_="title")
    TacGia = soup.find_all("span",class_="date")
    Chuong = soup.find_all("div",class_="desc")
   
    for i in range(len(TieuDe)):
        str+=TieuDe[i].text + "\n"
        str+="- " + TacGia[i].text + "\n"  
        str+="- " + Chuong[i].text + "\n"
       
#Ghi nội dung vào file
filename=os.path.join("D:\python", "bai12.txt")    
with open(filename, 'w',encoding='utf-8') as f:
    f.write(str)
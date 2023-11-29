from emot.emo_unicode import UNICODE_EMOJI # For emojis
from emot.emo_unicode import EMOTICONS_EMO # For EMOTICONS
import os
from textblob import TextBlob
import emot
import re
import nltk
from nltk.corpus import stopwords

file_path = '3.txt'  
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read() 
    for i in range (1,11):
        m=int(input("Chọn chế độ : "))
        if m==1:
            print("chuyển văn bản thành chữ thường:")
            text_pre=text.lower()
        elif m==2:
            # loại bỏ URL
            text_pre = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    
            print("Đã loại bỏ URl:")
            # text_pre=re.sub(r'[^\w\s]','',text)
        elif m==3:
            # xóa dấu
            print("văn bản đã xóa dấu câu:")
            text_pre=re.sub(r'[^\w\s]','',text)
        elif m==4:
            # xóa số
            print("văn bản đã xóa chữ số:")
            text_pre = re.sub("\d+", " ", text)
        elif m==5:
            # Tách câu
            print("văn bản đã được tách câu:")
            text_pre = nltk.sent_tokenize(text)
        elif m==6:
            print("Sau khi văn bản đã chuyển emoji thành văn bản: ")
            def converting_emojis(text):
                for x in EMOTICONS_EMO :
                    text = text.replace(x, "_".join(EMOTICONS_EMO[x].replace(",","").replace(":","").split()))
                for x in UNICODE_EMOJI:
                    text = text.replace(x, "_".join(UNICODE_EMOJI[x].replace(",","").replace(":","").split()))
                return text  
            text_pre=converting_emojis(text)
        elif m==7:
            # Xóa từ không có nghĩa
            print("Sau khi văn bản đã được xóa từ không có nghĩa: ")
            stop = stopwords.words('english')
            text_pre = " ".join(text for text in text.split() if text not in stop) 
        elif m==8: 
            # Chuẩn hóa văn bản: 
            print("Sau khi văn bản đã được chuẩn hóa: ")
            lookup_dict = {'nlp':'natural language processing', 'ur':'your', "wbu" : "what about you"}
            def text_std(input_text):
                words = input_text.split()
                text_pre=""
                for word in words:
                    w=word
                    w = re.sub(r'[^\w\s]','',w) 
                    if w.lower() in lookup_dict:
                        word=lookup_dict[w]
                text_pre=text_pre + " " + word
                return text_pre   
        elif m==9:
            # Sửa lỗi chính tả
            print("Lỗi chính ta được sửa như sau: ")
            text_pre=TextBlob(text).correct()
        elif m==10:
            # Tách từ :
            print("Văn bản đã được tách từ như sau: ")
            text_pre= nltk.sent_tokenize(text)   
        else:
             text_pre = "Không hợp lệ!"
        print(text_pre)
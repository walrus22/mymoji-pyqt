import os
import shutil
import sys

def check_local_dir():
    if os.path.exists("./img") == False:
        os.mkdir("img")

def check_dup_name(path, name):
    
    return

def save_web_img(img_data, img_name, img_type):
    check_local_dir()
    # file_name = os.path.join("./img", img_name + "_dup" + img_type)
    
    file_name = os.path.join("./img", img_name + img_type)
    # if os.path.isfile(os.path.join("./img", img_name + img_type)) == False:
    # else: 
        # 디시콘은 파일명이 platform-id-element로 저장할거고, 커맨드 중복은 addwindow에서 처리하니까 ㄱㅊ
    with open(file_name, 'wb') as handler:
        handler.write(img_data)
        
    return file_name

def copy_img(path, img_name, img_type):
    check_local_dir()
    
    # 명령어가 중복
    if os.path.isfile(os.path.join("./img", img_name + img_type)):
        copy_path = os.path.join("./img", img_name + "_dup" + img_type)
        shutil.copy(path, copy_path)
    else: 
        copy_path = os.path.join("./img", img_name + img_type)
        shutil.copy(path, copy_path)
    return copy_path


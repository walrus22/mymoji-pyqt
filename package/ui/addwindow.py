import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap,QImage, QPalette, QIcon
from PIL import Image
from PIL.ImageQt import ImageQt
import shutil
import img_rc
from pynput.keyboard import Key, Listener
from package.tracker import send_to_clipboard
from package.tracker import Tracker

from package.ui.emojiframe import EmojiFavorite, FlowContainer
from package.common import copy_img, save_web_img

import requests
import os

import logging
log = logging.getLogger(__name__)

# from mainwindow import resource_path

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path,  relative_path)
    # return os.path.join(base_path, "designer", "mymoji-designer", relative_path)

class add_emojiWindow(QWidget):
    def __init__(self, mainwindow): # is_main 추가해서 if로 추가창 바뀌게
        super().__init__()
        # loadUi("./designer/mymoji-designer/add_command.ui", self)    
        # loadUi("add_command.ui", self)    
        loadUi(resource_path("add_command.ui"), self) 
        
        self.img_path = None
        self.img_data = None
        self.img_type = ""
        self.is_img_local = True
        self.is_image_loaded = False
        self.emoji_element_data = None
        self.editmode = False
        self.editmode_EmojiFavorite = None
        self.editmode_did_load = False
        self.mainwindow = mainwindow
        self.label.setScaledContents(True)
        
        if hasattr(self.mainwindow, 'main_container'):
            self.btn_save.clicked.connect(self.save)
        # self.btn_cancel.clicked.connect(lambda: self.close())
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_load_image.clicked.connect(self.load_img)
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)  
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        
        """        
        편집창
        기존 이모지의 "명령어 / 이미지" 수정
        
        명령어 수정 : 
        case 1 모든 사항이 그대로 : 저장,취소 동작 동일
            => 저장 눌러도 추가하면 안됨
        case 2 이미지만 수정 (이건 로컬만 되겠지): 
        => 1,2 명령어 동일하니까 overwrite 부르면 안됨. 
            
        case 3 명령어만 수정 : EmojiFavorite Instance.command = self.lineEdit.text()
        case 4 명령어/이미지 모두 수정 :
        => 3,4 다른 명령어랑 겹치는 경우. overwrite
        """
        
    
    def overwrite(self,):
        log.info("overwrite")
        reply = QMessageBox.question(self, '덮어쓰기', '동일한 명령어가 존재합니다. \n덮어씌우시겠습니까?',
                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            return True
        else:
            return False
        
    def edit():
        pass
    
    def save(self):
        log.info("save test")
        
        
        if self.is_image_loaded == False:
            QMessageBox.critical(self, "Error", "이미지가 설정되어야 해요")
        else : 
            do_dup_check = True
            dup_emoji = None
            command = self.lineEdit.text()
            
            # self.is_image_loaded = False # 저장 했으니 초기화 ? 안해도 되지 않나
            
            if self.editmode == True: 
                log.info("editmode on")
                if self.editmode_EmojiFavorite.command == command: # 명령어 동일
                    do_dup_check = False
            else: 
                log.info("editmode off")
                
            # 중복 명령어 처리
            # None != "" 이므로 명령어 없는 애를 동일한 명령어로 인식하진 않음
            if do_dup_check:
                for emoji in self.mainwindow.favorite_element_cache:
                    if emoji.command == command:
                        dup_emoji = emoji
                        break
            if dup_emoji: 
                # 덮어쓰기 물어보기
                log.info(self.mainwindow.favorite_element_cache)
                log.info(dup_emoji)
                
                # dup_emoji : EmojiFavorite
                
                reply = QMessageBox.question(self, '덮어쓰기', '동일한 명령어가 존재합니다. \n덮어씌우시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    log.info("overwrite yes")
                    
                    for i in self.mainwindow.favorite_web_element_cache:
                        print(i)
                    
                    self.mainwindow.main_container.remove_emoji(dup_emoji, self.mainwindow.favorite_element_cache)
                    if self.is_img_local == False:
                        self.mainwindow.favorite_web_element_cache.remove(dup_emoji.emoji_element_data)
                else:
                    log.info("overwrite no")
                    return
                    
            # path : 파일 경로
            # name : test
            # type : .png
            # 이모지 사본 만들기 및 별표(디시콘) 추가
            if self.is_img_local == False:
                self.mainwindow.favorite_web_element_cache.append(self.element.data)
                self.img_path = save_web_img(self.img_data, self.img_name, self.img_type)
                
                pixtemp = QPixmap("star.png")
                fav_label = QLabel(self.element)
                fav_label.setPixmap(pixtemp)
                fav_label.setFixedSize(20,20)
                fav_label.setScaledContents(True)
                fav_label.move(80,0)
                
            elif self.editmode_did_load: 
                self.img_path = copy_img(self.img_path, self.img_name, self.img_type)
            
            # 편집 : 객체 수정
            if self.editmode == True: 
                self.editmode_EmojiFavorite.command = command
                self.editmode_EmojiFavorite.command_label.setText(command)
                if self.editmode_did_load:
                    self.editmode_EmojiFavorite.img_path = self.img_path
                    pixtemp = QPixmap(self.img_path) 
                    self.editmode_EmojiFavorite.pixmap = pixtemp
                    self.editmode_EmojiFavorite.img_label.setPixmap(pixtemp)
            # 생성 : 이모지 생성
            else:
                if command == "" : 
                    new_emoji = EmojiFavorite(self.mainwindow, None, self.img_path, self.element.data)
                else:
                    new_emoji = EmojiFavorite(self.mainwindow, command, self.img_path, self.element.data)
                log.info(self.img_path)
                    
                # 생성한 이모지 추가            
                self.mainwindow.main_container.add_emoji(new_emoji) 
                self.mainwindow.favorite_element_cache.append(new_emoji)
                
            # 창 닫기
            self.mainwindow.add_window = None
            self.close()
            logging.info("save emojilist")
            
    def cancel(self):
        self.mainwindow.add_window = None
        self.close()
        
    
    def load_img(self):
        fname=QFileDialog.getOpenFileName(self, filter="All files (*.*);;BMP (*.bmp);;CUR (*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO (*.ico);;JPEG (*.jpeg);;JPG (*.jpg);;PBM (*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM (*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA (*.tga);;TIF (*.tif);;TIFF (*.tiff);;WBMP (*.wbmp);;WEBP (*.webp);;XBM (*.xbm);;XPM (*.xpm)")        
        
        logging.info(fname[0]) # file path
        logging.info(fname[1]) # filter name
        
        self.img_path = fname[0] 
        self.img_name, self.img_type = os.path.splitext(os.path.basename(fname[0])) # test, .png
        
        # 디시콘 불러온 상태 -> 불러오기 -> 저장시 케이스 분류
        if self.is_img_local == False:
            self.is_img_local = True        
        
        # if selected
        if fname[0]:
            try:
                image = Image.open(fname[0])
                qim = ImageQt(image).copy()
                pix = QPixmap.fromImage(qim)
                
                self.label.setPixmap(pix)
                
                self.is_image_loaded = True
                
                #2.3 편집기능
                self.editmode_did_load = True                
            except Exception as e:
                QMessageBox.critical(self, "Error", "올바른 이미지 형식이 아닙니다")
                print(e)
                logging.info("You should import an image file")
        else:
            logging.info("파일 안 골랐음")
            

# 명령어 없는 경우
# if command == "" : 
#     if self.is_img_local == False:
#         self.mainwindow.favorite_web_element_cache.append(self.element.data)
#         self.img_path = save_web_img(self.img_data, self.img_name, self.img_type)
#         self.element._layout.addWidget(QLabel("fav2"))
#     else: 
#         self.img_path = copy_img(self.img_path, self.img_name, self.img_type)
#     new_emoji = EmojiFavorite(None, self.img_path)
# else:
#     if self.is_img_local == False:
#         self.mainwindow.favorite_web_element_cache.append(self.element.data)
#         self.img_path = save_web_img(self.img_data, self.img_name, self.img_type)
#         self.element._layout.addWidget(QLabel("fav2"))
#     else:
#         self.img_path = copy_img(self.img_path, self.img_name, self.img_type)
#     new_emoji = EmojiFavorite(command, self.img_path)
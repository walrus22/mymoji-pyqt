from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QImage
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve
import win32clipboard
from package.tracker import send_to_clipboard

from PyQt5.QtCore import QUrl, QEvent
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
import requests

import io
# from addwindow import add_emojiWindow

import os
import logging
import copy
import sys

log = logging.getLogger(__name__)

def resource_path(relative_path):
    try:
        # PyInstaller에 의해 임시폴더에서 실행될 경우 임시폴더로 접근하는 함수
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class FlowContainer(QListWidget):
    def __init__(self):
        super().__init__()
        
        self.setFrameShape(QFrame.NoFrame)
        # self.viewport().setBackgroundRole(QPalette.Window)
        self.viewport().setBackgroundRole(QPalette.Dark)
        self.setFlow(self.LeftToRight)
        self.setWrapping(True)
        self.setMovement(self.Free)
        self.setResizeMode(self.Adjust)
        self.setHorizontalScrollMode(self.ScrollPerPixel)
        self.setVerticalScrollMode(self.ScrollPerPixel)
        self.setSpacing(4)

    def remove_emoji(self, target_emoji, cache_list):
        log.info(type(target_emoji))
        if type(target_emoji) == EmojiFavorite:
            for i in range(self.count()):
                if self.itemWidget(self.item(i)) == target_emoji:
                    self.takeItem(i)
                    break
        else :
            for i in range(self.count()):
                if self.itemWidget(self.item(i)).emoji == target_emoji:
                    self.takeItem(i)
                    break
        
        if cache_list:
            cache_list.remove(target_emoji)

    def add_emoji(self, EmojiFavorite):
        item = QListWidgetItem()
        item.setFlags(item.flags() & ~(Qt.ItemIsSelectable|Qt.ItemIsEnabled))
        self.addItem(item)
        frame = EmojiFavorite
        item.setSizeHint(frame.sizeHint())
        self.setItemWidget(item, frame)

class EmojiContainer(QWidget):
    def __init__(self, title, maker):        
        super().__init__()


class EmojiFavoriteList(QWidget):
    # favorite_list
    # 누르면 해당 이모지 묶음 나옴.
    def __init__(self, command, img_path):
        super().__init__()
    

class EmojiDisplay(QWidget):
    def __init__(self, mainwindow, emoji, k):
        super().__init__()
        self.mainwindow = mainwindow
        self.emoji = emoji
        self._layout = QGridLayout(self) # the layout is associated with the current widget, self    
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(1)
        self._label = QLabel()
        self.pixmap = QPixmap()
        # image = QImage
        response = requests.get(emoji['path_main'])
        self.pixmap.loadFromData(response.content)
        self._label.setPixmap(self.pixmap)
        self._label.setFixedSize(100,100)
        self._label.setScaledContents(True)
        self._label.setStyleSheet("border: 0px")
        self._layout.addWidget(self._label)
        self.setFixedSize(self._layout.sizeHint())
    
    def copy_favorite(self):
        new_copy = EmojiDisplay(self.mainwindow, self.emoji, 123)
        new_copy.setFixedSize(50,50)
        new_copy._label.setFixedSize(50,50)
        return new_copy
    
    def fill_img(self, pixmap):
        self._label.setPixmap(pixmap)
    
    def mousePressEvent(self, event):
        layout = self.mainwindow.emoji_elements.layout()
        self.mainwindow.main_stack.setCurrentIndex(1)
        self.mainwindow.search_stack.setCurrentIndex(1)
        self.mainwindow.current_emoji = self.emoji
        
        if self.emoji in self.mainwindow.favorite_list_cache:
            self.mainwindow.add_fav_btn.setChecked(True)
        else :
            self.mainwindow.add_fav_btn.setChecked(False)
            
        
        if layout.count() != 0:
            layout.itemAt(0).widget().deleteLater()
        
        layout.setContentsMargins(0,0,0,0)
        self.elements_container = FlowContainer()
        layout.addWidget(self.elements_container)    
        
        input_data = {
            "platform" : self.emoji['platform'],
            "emoji_id" : self.emoji['id'],
        }
        response = requests.post("http://mymoji.iptime.org:20000/api/detail", json=input_data)
        
        if response.status_code == 200:
            self.mainwindow.emoji_header_img.setPixmap(self.pixmap)
            self.mainwindow.emoji_description.setText(self.emoji['description'])
            self.mainwindow.emoji_description.setWordWrap(True)
            self.mainwindow.emoji_name.setText(self.emoji['name'])
            self.mainwindow.emoji_header_img.setScaledContents(True)
            
            for element in response.json():
                self.elements_container.add_emoji(EmojiElement(self.mainwindow, element))
        
        # self.click_tooltip.show()
        # QTimer.singleShot(500, self.click_tooltip.hide)
        # send_to_clipboard(win32clipboard.CF_DIB, self.img_path)

        log.info(self.mainwindow.favorite_web_element_cache)

class EmojiElement(QWidget):
    def __init__(self, mainwindow, element):
        super().__init__()
        self.mainwindow = mainwindow
        self.data = element
        self._layout = QGridLayout(self) # the layout is associated with the current widget, self    
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(1)
        self._label = QLabel()
        self.pixmap = QPixmap()
        
        
        self.response = requests.get(element['path'])
        self.pixmap.loadFromData(self.response.content)
        self._label.setPixmap(self.pixmap)
        self._label.setFixedSize(100,100)
        self._label.setScaledContents(True)
        self._layout.addWidget(self._label)
        # self._layout.addWidget(QLabel(str(k)))
        self.setFixedSize(self._layout.sizeHint())
        
        if self.data in mainwindow.favorite_web_element_cache :
            log.info("fav added")
            pixtemp = QPixmap(resource_path("star.png"))
            fav_label = QLabel(self)
            fav_label.setPixmap(pixtemp)
            fav_label.setFixedSize(20,20)
            fav_label.setScaledContents(True)
            fav_label.move(80,0)
        
        # click tooltip
        self.click_tooltip = QLabel(self)
        self.click_tooltip.setStyleSheet("background-color: gray;")
        self.click_tooltip.setText("복사 되었습니다")
        self.click_tooltip.setMouseTracking(True)
        self.click_tooltip.hide()
        self.setMouseTracking(True)
        
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Handle left mouse button press
            log.info("EmojiFavorite Left button pressed")
            self.click_tooltip.show()
            QTimer.singleShot(500, self.click_tooltip.hide)
            send_to_clipboard(win32clipboard.CF_DIB, io.BytesIO(self.response.content))
            
        elif event.button() == Qt.RightButton:
            # Handle right mouse button press
            log.info("Right button pressed")
            self.mainwindow.add_emoji_window()
            self.mainwindow.add_window.is_image_loaded = True
            self.mainwindow.add_window.is_img_local = False
            self.mainwindow.add_window.img_data = self.response.content
            self.mainwindow.add_window.img_name = self.data['platform'] + "_" + str(self.data['emoji_id']) + "_" + str(self.data['id'])
            self.mainwindow.add_window.img_type = "." + self.data['type']
            self.mainwindow.add_window.label.setPixmap(self.pixmap)
            self.mainwindow.add_window.element = self
            # addwinodw에서 favorite으로 저장을 하면, favorite element임을 cache에 저장해야함
            # 메모리 관리 측면에서 widget을 저장할게 아니라, is_favorite = True만 가지는게 좋겠음
        else:
            log.info("other button")
        
        
class EmojiFavorite(QWidget):
    def __init__(self, mainwindow, command, img_path, emoji_element_data):
        super().__init__()
        self.mainwindow = mainwindow
        self.command = command
        self.img_path = img_path
        self.emoji_element_data = emoji_element_data
        
        layout = QGridLayout(self) # the layout is associated with the current widget, self    
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(1)
        
        self.pixmap = QPixmap(img_path)
        self.img_label = QLabel(pixmap=self.pixmap)
        self.img_label.setFixedSize(100,100)
        self.img_label.setScaledContents(True)
        self.command_label = QLabel(str(command))
        self.command_label.setFixedSize(100,20)
        self.command_label.setStyleSheet("background-color: gray;")
        
        layout.addWidget(self.img_label)
        layout.addWidget(self.command_label)
        # layout.addWidget(self.button, 0, 1, 2, 1, alignment=Qt.AlignTop)
        self.setFixedSize(layout.sizeHint())
        
        # click tooltip
        self.click_tooltip = QLabel(self)
        self.click_tooltip.setStyleSheet("background-color: gray;")
        self.click_tooltip.setText("복사 되었습니다")
        self.click_tooltip.setMouseTracking(True)
        self.click_tooltip.hide()
        self.setMouseTracking(True)
        
        # Create context menu
        self.context_menu = QMenu(self)
        self.edit_action = self.context_menu.addAction("편집")
        self.delete_action = self.context_menu.addAction("삭제")
        self.edit_action.triggered.connect(self.edit_triggered)
        self.delete_action.triggered.connect(self.delete_triggered)
        
        # self.context_menu.setForegroundRole()
        stylestr = """QMenu::item:selected { background: rgb(192, 192, 192); }
                    QMenu::item:pressed { background: white; color: gray; }"""
        self.context_menu.setStyleSheet(stylestr)
        
    def contextMenuEvent(self, event):
        # Display context menu when right mouse button is clicked
        if event.type() == QEvent.ContextMenu:
            self.context_menu.exec_(event.globalPos())

    def edit_triggered(self):
        log.info("edit_triggered")
        log.info(self.img_path)
        
        self.mainwindow.add_emoji_window()
        self.mainwindow.add_window.editmode = True
        self.mainwindow.add_window.editmode_EmojiFavorite = self
        self.mainwindow.add_window.is_image_loaded = True
        self.mainwindow.add_window.is_img_local = True
        self.mainwindow.add_window.label.setPixmap(self.pixmap)
        self.mainwindow.add_window.lineEdit.setText(self.command)

    def delete_triggered(self):
        log.info("delete_triggered")
        self.mainwindow.main_container.remove_emoji(self, self.mainwindow.favorite_element_cache)
        log.info(self.mainwindow.favorite_element_cache)
    
    def mousePressEvent(self, event):
        log.info(self.img_path)
        if event.button() == Qt.LeftButton:
            # Handle left mouse button press
            log.info("EmojiFavorite Left button pressed")
            self.click_tooltip.show()
            QTimer.singleShot(500, self.click_tooltip.hide)
            send_to_clipboard(win32clipboard.CF_DIB, self.img_path)
        
    # def mouseMoveEvent(self, event):
    #     self.click_tooltip.move(event.pos())
    
    # compare 만들어서 sort가능하게?
    # 중복 없게
    # 수정

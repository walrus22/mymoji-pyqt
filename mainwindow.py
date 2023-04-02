import sys
import requests
import logging
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.uic import loadUi, loadUiType
from PyQt5.QtGui import QPixmap
import img_rc

from PIL import Image
from PIL.ImageQt import ImageQt

from package.tracker import send_to_clipboard
from package.tracker import Tracker

from package.ui.addwindow import add_emojiWindow
from package.ui.emojiframe import FlowContainer, EmojiFavorite, EmojiDisplay

# from ui import Ui_MainWindow

"""
TODO:
- 최우선 
    1. 디비 이미지 경로 바꾸기
    2. sqlalchemy relation m:n
    

    emoji-tag m:n으로 바꾸기 (1:1임)
    드래그 순서 바꾸기
    비동기 로드
    GUI 해상도
    UI https://m2.material.io/resources/color/#!/?view.left=0&view.right=0
    캐시
- 기능
    업로드시 편집기능
    이모지 추가했을때 넘치면 포커스 아래로
    디시콘 전체 다운로드 버튼
- 디자인
    출처 스티커 (로컬=컴퓨터, 디시 등)
    스크롤바 
- 불필요한 import 삭제

- mainwindow 객체 파라미터로 안주고 돌려쓰는법 없을까

<방장님>
오른쪽 부분은 싹다 웹뷰로 만들기
웹으로 만들고 껍데기만 만들어서 언어에서 해방
구글로그인, 세션
- 인증서 https://www.ssl.com/certificates/code-signing/
- 보안
    서버를 샌드박스에 두고 vm올리고 거기에 디플로이
    ec2쓸거면 비쌈 vultur
    엔드포인트에 클라우드플레어
    니 서버랑 클라우드 플레어만 통신하게 하고

<머규>
2. 내가 올리는 이미지 올리는걸 훨씬 쉽게 만들어야 할듯 => 드래그
3. 라이브러리 (폴더)
- 명령어 전체 초기화
- 즐찾 폴더화 만들기 (갠톡콘, 가족콘, 등)
- 도매인 구매

# 2.3 
- add 명령어 덮어쓰기
- 편집, 삭제
- 전체 삭제

- 즐겨찾기한 이모지 스티커
- 즐찾 이모지 우클릭으로 해제
- 검색 



main_stack -> stack 으로 바꾸는게 나을듯?

<a href="https://www.flaticon.com/free-icons/file" title="file icons">File icons created by Freepik - Flaticon</a>
    
"""

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(asctime)s pid:%(process)s module:%(module)s %(lineno)d: %(message)s',
    # datefmt='%d/%m/%y %H:%M:%S',
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
    return os.path.join(base_path, "designer", "mymoji-designer", relative_path)

class MainWindow(QMainWindow):
    # def __init__(self, *args, obj=None, **kwargs):
    def __init__(self): 
        super().__init__()
        loadUi("./designer/mymoji-designer/mainwindow.ui", self)
        # Ui_MainWindow, QtBaseClass = loadUiType(securitySearchForm)
        # loadUi(resource_path("mainwindow.ui"), self) 
        
        
        ###########  declare variable  #################
        # self.search_cache = []
        self.favorite_list_cache = []
        self.add_window = None
        self.favorite_element_cache = []
        self.favorite_web_element_cache = []
        self.item_num_limit = 20
        ################################################
        
        ################  tracker ######################
        self.keyboard_listener = Tracker(self)
        self.keyboard_listener.run()
        ################################################
        
        ################  home page ####################
        self.main_stack.setCurrentIndex(0)
        self.home_btn_add.clicked.connect(self.add_emoji_window)
        self.main_btn_home.clicked.connect(self.main_btn_home_clicked)
        self.main_btn_search.clicked.connect(self.main_btn_search_clicked)
        self.main_btn_setting.clicked.connect(self.main_btn_setting_clicked)
        self.main_btn_inform.clicked.connect(self.main_btn_inform_clicked)
        
        # main container        
        layout = QGridLayout(self.home_list)
        layout.setContentsMargins(0,0,0,0)
        self.main_container = FlowContainer()
        layout.addWidget(self.main_container)       
        
        # 상단 favorite list
        layout = QGridLayout(self.favorite_list)
        layout.setContentsMargins(0,0,0,0)
        self.favorite_container = FlowContainer()
        layout.addWidget(self.favorite_container)  
        self.favorite_container.setWrapping(False)
        self.favorite_container.setFixedHeight(60)
        self.favorite_container.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        ################################################
        
        ################  search page ##################
        self.search_btn.clicked.connect(self.search_btn_click)
        
        layout = QGridLayout(self.search_main)
        layout.setContentsMargins(0,0,0,0)
        self.search_main_container = FlowContainer()
        layout.addWidget(self.search_main_container)      
        ################################################
        
        ########### test
        self.addfavtestbtn.clicked.connect(self.test)
        # self.favbtn.clicked.connect(self.favtest)
        self.add_fav_btn.clicked.connect(self.add_favorite_list)
        self.remove_all_btn.clicked.connect(self.remove_all)
    
        # url = QUrl("https://dcimg5.dcinside.com/dccon.php?no=62b5df2be09d3ca567b1c5bc12d46b394aa3b1058c6e4d0ca41648b65ce22d6e9d8f998f16d840c4e268fd47078acb3895c369a8da555dc761a5345d397d8311c743b6278e3d67")
        # test load url image
        # self.manager = QNetworkAccessManager()
        # request = QNetworkRequest(url)
        # reply = self.manager.get(request)
        # reply.finished.connect(lambda: self.on_finish(reply))
    
    def remove_all(self):
        logging.info(self.main_container.count())
        self.main_container.clear()
    
    def add_favorite_list(self):
        if self.current_emoji in self.favorite_list_cache:
            print("빼기")
            self.favorite_container.remove_emoji(self.current_emoji, self.favorite_list_cache)
        else :
            print("추가")
            self.favorite_list_cache.append(self.current_emoji)
            emoji_temp = EmojiDisplay(self, self.current_emoji, 1)
            emoji_temp.setFixedSize(50,50)
            emoji_temp._label.setFixedSize(50,50)
            self.favorite_container.add_emoji(emoji_temp)

    def print_children(self, parent):
        for child in parent.findChildren(QWidget):
            print(f"{child.objectName()} ({child.__class__.__name__})")
    
    def favtest(self):
        response = requests.post(os.environ['API_URL'] + "/test")
        
        data = response.json()
        et = EmojiDisplay(self, data,1)
        et.setFixedSize(50,50)
        et._label.setFixedSize(50,50)
        self.favorite_container.add_emoji(et)
        
        
    def test(self):
        import random
        command = "command" + str(random.randrange(1,100))
        test_emoji = EmojiFavorite(self, command, "test.png")
        self.favorite_element_cache.append(test_emoji)
        self.main_container.add_emoji(test_emoji)
    
    def on_finish(self,reply):
        pixmap = QPixmap()
        pixmap.loadFromData(reply.readAll())
        # self.test_label.setPixmap(pixmap)

    def main_btn_search_clicked(self):
        self.main_stack.setCurrentIndex(1)
        self.search_stack.setCurrentIndex(0)
        self.search_page = 1
        self.order = "hot" # or new
        
        # pagination pyqt
        if self.search_main_container.count() == 0:
            input_data = {
                # "site": str(self.search_site.currentText()),
                # "kind" : str(self.search_kind.currentText()),
                # "input" : str(self.search_input.text()),
                "item_num" : self.item_num_limit,
                "page" : self.search_page,
                "order" : self.order
                }
            
            
            
            response = requests.post(os.environ['API_URL'] + "/search/main", json=input_data)
            # self.manager = QNetworkAccessManager()
            if response.status_code == 200:
                data = response.json()
                k=0
                for emoji in data:
                    k+=1
                    emoji_temp = EmojiDisplay(self, emoji, k)
                    self.search_main_container.add_emoji(emoji_temp)
            else :
                pass
        
    def o_f(self, reply, emoji_temp):
        pixmap = QPixmap()
        pixmap.loadFromData(reply.readAll())
        emoji_temp.fill_img(pixmap)
        
        
        
    
    def search_btn_click(self):
        self.search_page = 0
        self.order = "hot" # or new
        self.search_main_container.clear()
        input_data = {
                    "site": str(self.search_site.currentText()),
                    "kind" : str(self.search_kind.currentText()),
                    "input" : str(self.search_input.text()),
                    "page" : self.search_page,
                    "order" : self.order,
                    "item_num" : self.item_num_limit
                    }
    
        response = requests.post(os.environ['API_URL'] + "/search", json=input_data)
        
        if response.status_code == 200:
            data = response.json()
            k=0
            for emoji in data:
                k+=1
                emoji_temp = EmojiDisplay(self, emoji, k)
                self.search_main_container.add_emoji(emoji_temp)
        else :
            pass
    
        
    def main_btn_home_clicked(self):
        self.main_stack.setCurrentIndex(0)

    def main_btn_setting_clicked(self):
        self.main_stack.setCurrentIndex(2)
        print("sett")

    def main_btn_inform_clicked(self):
        self.main_stack.setCurrentIndex(3)
        print("inf")
        
    def add_emoji_window(self):
        if self.add_window is None:
            self.add_window = add_emojiWindow(self)
            self.add_window.show()
        else :    
            self.add_window.close()
            self.add_window = None         


if __name__ == '__main__':
    # try:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    # os.system('pause')
    # except Exception as e :
    #     print(e)




<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>551</width>
    <height>648</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>300</width>
    <height>0</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Mymoji</string>
  </property>
  <property name="windowIcon">
   <iconset resource="img.qrc">
    <normaloff>:/icon/img/mymoji_icon2.png</normaloff>:/icon/img/mymoji_icon2.png</iconset>
  </property>
  <property name="iconSize">
   <size>
    <width>30</width>
    <height>30</height>
   </size>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout_3">
    <item>
     <widget class="QWidget" name="main_menu_list" native="true">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Fixed" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>60</width>
        <height>0</height>
       </size>
      </property>
      <property name="maximumSize">
       <size>
        <width>60</width>
        <height>16777215</height>
       </size>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(244, 255, 254);</string>
      </property>
      <layout class="QVBoxLayout" name="verticalLayout_2">
       <property name="leftMargin">
        <number>0</number>
       </property>
       <property name="rightMargin">
        <number>0</number>
       </property>
       <item alignment="Qt::AlignTop">
        <widget class="QWidget" name="main_btns" native="true">
         <layout class="QVBoxLayout" name="verticalLayout">
          <property name="spacing">
           <number>20</number>
          </property>
          <item>
           <widget class="QPushButton" name="main_btn_home">
            <property name="styleSheet">
             <string notr="true">border: none;</string>
            </property>
            <property name="text">
             <string/>
            </property>
            <property name="icon">
             <iconset resource="img.qrc">
              <normaloff>:/icon/img/freepik/home_2.png</normaloff>:/icon/img/freepik/home_2.png</iconset>
            </property>
            <property name="iconSize">
             <size>
              <width>40</width>
              <height>40</height>
             </size>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="main_btn_search">
            <property name="styleSheet">
             <string notr="true">border: none;</string>
            </property>
            <property name="text">
             <string/>
            </property>
            <property name="icon">
             <iconset resource="img.qrc">
              <normaloff>:/icon/img/freepik/loupe.png</normaloff>:/icon/img/freepik/loupe.png</iconset>
            </property>
            <property name="iconSize">
             <size>
              <width>40</width>
              <height>40</height>
             </size>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="main_btn_setting">
            <property name="styleSheet">
             <string notr="true">border: none;</string>
            </property>
            <property name="text">
             <string/>
            </property>
            <property name="icon">
             <iconset resource="img.qrc">
              <normaloff>:/icon/img/freepik/settings_2.png</normaloff>:/icon/img/freepik/settings_2.png</iconset>
            </property>
            <property name="iconSize">
             <size>
              <width>40</width>
              <height>40</height>
             </size>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="main_btn_inform">
            <property name="styleSheet">
             <string notr="true">border: none;</string>
            </property>
            <property name="text">
             <string/>
            </property>
            <property name="icon">
             <iconset resource="img.qrc">
              <normaloff>:/icon/img/freepik/information.png</normaloff>:/icon/img/freepik/information.png</iconset>
            </property>
            <property name="iconSize">
             <size>
              <width>40</width>
              <height>40</height>
             </size>
            </property>
           </widget>
          </item>
         </layout>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
    <item>
     <widget class="QStackedWidget" name="main_stack">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 255);</string>
      </property>
      <property name="currentIndex">
       <number>3</number>
      </property>
      <widget class="QWidget" name="home">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 255, 255);</string>
       </property>
       <layout class="QVBoxLayout" name="verticalLayout_7">
        <item>
         <widget class="QWidget" name="favorite_list" native="true">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Expanding" vsizetype="Fixed">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="minimumSize">
           <size>
            <width>0</width>
            <height>60</height>
           </size>
          </property>
          <property name="styleSheet">
           <string notr="true">border: 1px solid black;</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QWidget" name="home_list" native="true">
          <property name="styleSheet">
           <string notr="true">background-color: rgb(255, 255, 255);
border: 1px solid black;</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QWidget" name="home_btn_list" native="true">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="minimumSize">
           <size>
            <width>0</width>
            <height>50</height>
           </size>
          </property>
          <layout class="QHBoxLayout" name="horizontalLayout">
           <item alignment="Qt::AlignRight">
            <widget class="QWidget" name="widget" native="true">
             <property name="minimumSize">
              <size>
               <width>0</width>
               <height>0</height>
              </size>
             </property>
             <layout class="QHBoxLayout" name="horizontalLayout_4">
              <item>
               <widget class="QPushButton" name="remove_all_btn">
                <property name="text">
                 <string>전체 삭제</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="addfavtestbtn">
                <property name="text">
                 <string>testbtn add fav_element</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="home_btn_add">
                <property name="sizePolicy">
                 <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
                  <horstretch>0</horstretch>
                  <verstretch>0</verstretch>
                 </sizepolicy>
                </property>
                <property name="text">
                 <string/>
                </property>
                <property name="icon">
                 <iconset resource="img.qrc">
                  <normaloff>:/icon/img/freepik/upload.png</normaloff>
                  <disabledoff>:/icon/img/plus-icon.png</disabledoff>:/icon/img/freepik/upload.png</iconset>
                </property>
               </widget>
              </item>
             </layout>
            </widget>
           </item>
          </layout>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="search">
       <layout class="QVBoxLayout" name="verticalLayout_8">
        <property name="leftMargin">
         <number>0</number>
        </property>
        <property name="topMargin">
         <number>0</number>
        </property>
        <property name="rightMargin">
         <number>0</number>
        </property>
        <property name="bottomMargin">
         <number>0</number>
        </property>
        <item>
         <widget class="QWidget" name="search_bar" native="true">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="maximumSize">
           <size>
            <width>16777215</width>
            <height>50</height>
           </size>
          </property>
          <layout class="QHBoxLayout" name="horizontalLayout_2">
           <item>
            <widget class="QComboBox" name="search_site">
             <item>
              <property name="text">
               <string>통합 검색</string>
              </property>
             </item>
             <item>
              <property name="text">
               <string>DC</string>
              </property>
             </item>
             <item>
              <property name="text">
               <string>New Item</string>
              </property>
             </item>
            </widget>
           </item>
           <item>
            <widget class="QComboBox" name="search_kind">
             <item>
              <property name="text">
               <string>이름</string>
              </property>
             </item>
             <item>
              <property name="text">
               <string>제작자</string>
              </property>
             </item>
             <item>
              <property name="text">
               <string>태그</string>
              </property>
             </item>
            </widget>
           </item>
           <item>
            <widget class="QLineEdit" name="search_input"/>
           </item>
           <item>
            <widget class="QPushButton" name="search_btn">
             <property name="text">
              <string>Search</string>
             </property>
            </widget>
           </item>
          </layout>
         </widget>
        </item>
        <item>
         <widget class="QStackedWidget" name="search_stack">
          <property name="styleSheet">
           <string notr="true">background-color: rgb(255, 255, 255);</string>
          </property>
          <property name="lineWidth">
           <number>0</number>
          </property>
          <property name="currentIndex">
           <number>1</number>
          </property>
          <widget class="QWidget" name="search_main"/>
          <widget class="QWidget" name="search_detail">
           <layout class="QVBoxLayout" name="verticalLayout_3">
            <property name="leftMargin">
             <number>0</number>
            </property>
            <property name="topMargin">
             <number>0</number>
            </property>
            <property name="rightMargin">
             <number>0</number>
            </property>
            <property name="bottomMargin">
             <number>0</number>
            </property>
            <item>
             <widget class="QWidget" name="emoji_header" native="true">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
                <horstretch>0</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="minimumSize">
               <size>
                <width>0</width>
                <height>80</height>
               </size>
              </property>
              <property name="maximumSize">
               <size>
                <width>16777215</width>
                <height>80</height>
               </size>
              </property>
              <property name="styleSheet">
               <string notr="true">background-color: rgb(201, 255, 224);</string>
              </property>
              <layout class="QHBoxLayout" name="horizontalLayout_5">
               <property name="leftMargin">
                <number>5</number>
               </property>
               <property name="topMargin">
                <number>0</number>
               </property>
               <property name="rightMargin">
                <number>5</number>
               </property>
               <property name="bottomMargin">
                <number>0</number>
               </property>
               <item>
                <widget class="QLabel" name="emoji_header_img">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="minimumSize">
                  <size>
                   <width>70</width>
                   <height>70</height>
                  </size>
                 </property>
                 <property name="maximumSize">
                  <size>
                   <width>70</width>
                   <height>70</height>
                  </size>
                 </property>
                 <property name="text">
                  <string>ICON</string>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QWidget" name="emoji_header_inform" native="true">
                 <layout class="QVBoxLayout" name="verticalLayout_4">
                  <item>
                   <widget class="QLabel" name="emoji_name">
                    <property name="text">
                     <string>TextLabel</string>
                    </property>
                   </widget>
                  </item>
                  <item>
                   <widget class="QLabel" name="emoji_description">
                    <property name="text">
                     <string>TextLabel</string>
                    </property>
                   </widget>
                  </item>
                 </layout>
                </widget>
               </item>
               <item>
                <widget class="QWidget" name="widget_2" native="true">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="minimumSize">
                  <size>
                   <width>70</width>
                   <height>70</height>
                  </size>
                 </property>
                 <property name="maximumSize">
                  <size>
                   <width>70</width>
                   <height>70</height>
                  </size>
                 </property>
                 <widget class="QPushButton" name="add_fav_btn">
                  <property name="geometry">
                   <rect>
                    <x>20</x>
                    <y>40</y>
                    <width>41</width>
                    <height>31</height>
                   </rect>
                  </property>
                  <property name="text">
                   <string/>
                  </property>
                  <property name="icon">
                   <iconset resource="img.qrc">
                    <normaloff>:/icon/img/freepik/favorites.png</normaloff>
                    <normalon>:/icon/img/freepik/heart.png</normalon>:/icon/img/freepik/favorites.png</iconset>
                  </property>
                  <property name="checkable">
                   <bool>true</bool>
                  </property>
                  <property name="checked">
                   <bool>false</bool>
                  </property>
                 </widget>
                </widget>
               </item>
              </layout>
             </widget>
            </item>
            <item>
             <widget class="QWidget" name="emoji_elements" native="true">
              <layout class="QGridLayout" name="gridLayout">
               <property name="leftMargin">
                <number>0</number>
               </property>
               <property name="topMargin">
                <number>0</number>
               </property>
               <property name="rightMargin">
                <number>1</number>
               </property>
               <property name="bottomMargin">
                <number>0</number>
               </property>
              </layout>
             </widget>
            </item>
           </layout>
          </widget>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="setting"/>
      <widget class="QWidget" name="info">
       <widget class="QLabel" name="label">
        <property name="geometry">
         <rect>
          <x>140</x>
          <y>570</y>
          <width>191</width>
          <height>31</height>
         </rect>
        </property>
        <property name="text">
         <string>contact : mymoji.cs@gmail.com</string>
        </property>
       </widget>
       <widget class="QTextEdit" name="textEdit">
        <property name="geometry">
         <rect>
          <x>0</x>
          <y>0</y>
          <width>461</width>
          <height>561</height>
         </rect>
        </property>
        <property name="html">
         <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;meta charset=&quot;utf-8&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
hr { height: 1px; border-width: 0; }
li.unchecked::marker { content: &quot;\2610&quot;; }
li.checked::marker { content: &quot;\2612&quot;; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'맑은 고딕'; font-size:9pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&amp;lt;사용법&amp;gt;&lt;/p&gt;
&lt;ol style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;
&lt;li style=&quot; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;홈버튼 
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;&quot;&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;상단의 박스는 즐겨찾기한 디시콘 묶음 바로가기 버튼&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;메인 박스는 즐겨찾기한 이모지 개체 
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 3;&quot;&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;좌클릭 시 클립보드로 복사&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;우클릭 시 편집 및 삭제 (2.3추가)&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;하단의 버튼은 로컬(내 컴퓨터)에서 사진 불러오기&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;전체 삭제 가능 → 옵션으로 나중에 옮길것(2.3)&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;검색버튼 
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;&quot;&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;검색 버튼 
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 3;&quot;&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;첫 번째는 사이트별 검색&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;두 번째는 이모지의 이름,제작자,태그 선택 
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 4;&quot;&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;제작자,태그는 아직 안됨&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;검색 결과의 이모지 클릭 
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 3;&quot;&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;별표 버튼 : 해당 디시콘 즐겨찾기 (홈버튼의 상단 박스)&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;이모지 개체 
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 4;&quot;&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;좌클릭 : 클립보드로 복사&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;우클릭 : 명령어 지정 및 즐겨찾기&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;즐겨찾기 추가 화면 
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;&quot;&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;불러오기 (로컬) 
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 3;&quot;&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;검색 버튼에서 불러온 이모지(디시콘 등)는 이미지 자동 로드&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;이미지가 없을 경우, 추가 할 수 없음&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;명령어 
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 3;&quot;&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;없어도 됨&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;있는 경우 (ex. ::ㅋㅋ) 카톡에서 타이핑시 자동으로 클립보드에서 불러옴&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;덮어쓰기 가능 (2.3)&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;자르기 
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 3;&quot;&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;todo&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ol&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&amp;lt;기타&amp;gt;&lt;/p&gt;
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;
&lt;li style=&quot; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;즐겨찾기한 이모지의 이미지 사본이 실행파일 디렉토리의 img 폴더에 저장&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;현재 명령어는 카톡에서만 가능&lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;gif, png투명도 클립보드에서 안되서 처리중.. &lt;/li&gt;&lt;/ul&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
       </widget>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusBar"/>
  <action name="action">
   <property name="text">
    <string>설정</string>
   </property>
  </action>
 </widget>
 <resources>
  <include location="img.qrc"/>
 </resources>
 <connections/>
</ui>

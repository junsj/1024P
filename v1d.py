from v1 import Ui_MainWindow

from PySide import QtCore, QtGui
from PySide.QtGui import *
from PySide.QtWebKit import *
from PySide.QtCore import *
import sys
from bs4 import BeautifulSoup

import urllib
import urllib.request
import re
import os
import socket
import json
import sys

class s1024:
    def __init__(self,trigger=None,d2='',deep=3):
        socket.setdefaulttimeout(30)
        self.url_root = 'http://93.cao1024lui99.xyz/pw/'
        self.url = 'http://93.cao1024lui99.xyz/pw/thread-htm-fid-14-page-%s.html'
        self.msg = trigger
        self.d2  = d2
        self.deep = deep

    def create_emit_json(self,num='',text='',img='',name=''):
        c = {}
        c['num'] = str(num)
        c['text'] = str(text)
        c['img']  = str(img)
        c['name'] = str(name)
        json_str = json.dumps(c)
        return json_str

    def get_single_page(self,url, decode='utf-8'):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        response = urllib.request.Request(url=url, headers=headers)
        html = urllib.request.urlopen(response, timeout=30).read().decode(decode, errors='ignore')
        return html

    def get_images(self,url):
        html = self.get_single_page(url, decode='utf-8')
        soup = BeautifulSoup(html, "html.parser")
        soup_div = soup.findAll("div", {"id": "read_tpc"})
        images = re.compile(r'src="(.*?)"').findall(str(soup_div))
        return images

    def get_pages(self,deep=3):
        all_pages = []
        for i in range(1,deep+1):
            try:
                url = self.url %str(i)
                if self.msg is not None:
                    text_l = '开始评估:' + url
                    num = int(i*100/(deep))
                    self.msg.emit(self.create_emit_json(num,text_l))
                html = self.get_single_page(url,decode='utf-8')
                soup = BeautifulSoup(html,"html.parser")
                soup_div = soup('h3')
                pages = re.compile(r'<a href="(htm_data.*?)" id="a_ajax_.*?">(.*?)</a>').findall(str(soup_div))
                all_pages =  all_pages + pages
            except:
                pass
        return all_pages

    def download_images(self,images,d2='pic\\',p_name=''):
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        img_all = len(images)
        i = 1
        bpic = True
        for img in images:
            img1,img2 = os.path.split(img)
            if not os.path.exists(img2):
                try:
                    text_l = '开始下载:' + img
                    num = int(i*100/img_all)
                    if self.msg is not None:
                        self.msg.emit(self.create_emit_json(num, text_l))
                    urllib.request.urlretrieve(img,img2)
                    if bpic:
                        text_l = 'BPIC'
                        self.msg.emit(self.create_emit_json(num,text_l,img2,p_name))
                        bpic = False
                except socket.timeout:
                    pass
                except:
                    pass
            i += 1

    def download_pages(self,deep=1):
        deep = int(deep)
        pages = self.get_pages(deep)
        for page in pages:
            p1, p2 = page
            p3 = p2
            p1 = self.url_root + p1
            p2 = self.d2 + p2 + '\\'
            if not os.path.exists(p2):
                os.makedirs(p2)
            if self.msg is not None:
                text_l = '-' * 50
                self.msg.emit(self.create_emit_json(0, text_l))
                text_l = '开始下载:' + p1
                self.msg.emit(self.create_emit_json(0, text_l))
                text_l = p3
                self.msg.emit(self.create_emit_json(0, text_l))
                text_l = '-' * 50
                self.msg.emit(self.create_emit_json(0, text_l))
            images = self.get_images(p1)
            self.download_images(images,p2,p3)

class myMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(myMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.p_path.setText('pic\\')
        self.ui.pb_find.clicked.connect(self.browse)
        self.ui.pb_download.clicked.connect(self.download)
        self.image = QtGui.QImage('x1.jpg')
        print(self.image)
        self.pixmap = QtGui.QPixmap.fromImage(self.image)

        self.ui.p_pic.setScaledContents(True)
        self.ui.p_pic.setPixmap(self.pixmap)

    def browse(self):
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Find Files",
                QtCore.QDir.currentPath())

        directory = directory + '\\'
        self.ui.p_path.setText(directory)

    def download(self):
        self.thread = MyThread(self,d2=self.ui.p_path.text(),deep=self.ui.spinBox.text())  # 创建线程
        self.thread.trigger.connect(self.update_text)  # 连接信号！
        self.thread.start()  # 启动线程


    def update_text(self, msg=None):
        msg = json.loads(msg)

        if msg['text'] == 'BPIC':
            print(msg['img'])
            self.image = QtGui.QImage(msg['img'])
            print(self.image)
            self.pixmap = QtGui.QPixmap.fromImage(self.image)
            self.ui.p_pic.setPixmap(self.pixmap)
            self.ui.p_name.setText(msg['name'])
        else:
            self.ui.progressBar.setProperty("value", msg['num'])
            self.ui.textBrowser.append(msg['text'])
            self.ui.textBrowser.showMaximized()

class MyThread(QThread):
    trigger = Signal(str)  # trigger传输的内容是字符串

    def __init__(self, parent=None,d2='',deep=1):
        super(MyThread, self).__init__(parent)
        self.d2=d2
        self.deep = deep

    def run(self):  # 很多时候都必重写run方法, 线程start后自动运行
        my1024 = s1024(trigger=self.trigger,d2=self.d2)
        my1024.download_pages(self.deep)

myApp = QApplication(sys.argv)
myWindow = myMainWindow()
myWindow.show()
myApp.exec_()
sys.exit(0)
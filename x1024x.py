from bs4 import BeautifulSoup

import urllib
import urllib.request
import re
import os
import socket
import json

class s1024:
    def __init__(self,trigger=None,d2='',deep=3):
        socket.setdefaulttimeout(30)
        self.url_root = 'http://93.cao1024lui99.xyz/pw/'
        self.url = 'http://93.cao1024lui99.xyz/pw/thread-htm-fid-14-page-%s.html'
        self.msg = trigger
        self.d2  = d2
        self.deep = deep

    def create_emit_json(self,num='',text='',img=''):
        c = {}
        c['num'] = str(num)
        c['text'] = str(text)
        c['img']  = str(img)
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

    def download_images(self,images,d2='pic\\'):
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        img_all = len(images)
        i = 1
        for img in images:
            img1,img2 = os.path.split(img)
            img2 = d2 + img2
            if not os.path.exists(img2):
                try:
                    text_l = '开始下载:' + img
                    num = int(i*100/img_all)
                    if self.msg is not None:
                        self.msg.emit(self.create_emit_json(num, text_l))
                    urllib.request.urlretrieve(img,img2)
                    if i == 1:
                        text_l = 'BPIC'
                        self.msg.emit(self.create_emit_json(num, text_l,img2))

                except socket.timeout:
                    pass
                except:
                    pass
            i += 1

    def download_pages(self,deep=3):
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
            self.download_images(images, p2)

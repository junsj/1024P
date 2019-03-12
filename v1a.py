from bs4 import BeautifulSoup

import urllib
import urllib.request
import re
import os


def get_single_page(url,decode='utf-8'):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    response = urllib.request.Request(url=url, headers=headers)  
    html = urllib.request.urlopen(response,timeout=20).read().decode(decode,errors='ignore')
    return html

url = 'http://93.cao1024lui99.xyz/pw/htm_data/14/1812/2341553.html'

html = get_single_page(url,decode='utf-8')
soup = BeautifulSoup(html,"html.parser")
soup_div = soup.findAll("div",{"id":"read_tpc"})

images = re.compile(r'src="(.*?)"').findall(str(soup_div))


opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

for img in images:
    img1,img2 = os.path.split(img)
    try:
        print(img2)
        urllib.request.urlretrieve(img,img2)
    except:
        pass

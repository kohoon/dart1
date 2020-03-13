# opendart - 1. 공시정보 - 3) 공시서류원본파일

import requests as rq
import zipfile
import pandas as pd
import xml.etree.ElementTree as ET

crtfc_key = '25320e73e479a8e8b9dcfa7a5a76faf0233652b5' # API 인증키
recept_no = '20200313000239' # 접수번호
dart_url = 'https://opendart.fss.or.kr/api/document.xml?crtfc_key='+crtfc_key+'&recept_no='+recept_no

res = rq.get(dart_url, allow_redirects=True)
open('opendart_document.zip', 'wb').write(res.content)

try:
    with zipfile.ZipFile('opendart_document.zip') as zf:
        zf.extractall()
        print("uncompress success")
except:
    print("uncompress failed")

# 현재 작동 안됨.
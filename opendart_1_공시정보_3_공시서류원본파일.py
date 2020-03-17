# opendart - 1. 공시정보 - 3) 공시서류원본파일

import requests as rq
import zipfile
import pandas as pd
import xml.etree.ElementTree as ET

crtfc_key = '25320e73e479a8e8b9dcfa7a5a76faf0233652b5' # API 인증키
rcept_no = '20190401004781' # 접수번호
dart_url = 'https://opendart.fss.or.kr/api/document.xml?crtfc_key='+crtfc_key+'&rcept_no='+rcept_no
zip_nm = 'opendart_document.zip'
res = rq.get(dart_url)
res.encoding = 'euc-kr'
# open(zip_nm, 'wb').write(res.content)
#
# try:
#     with zipfile.ZipFile(zip_nm) as zf:
#         zf.extractall()
#         print("uncompress success")
# except:
#     print("uncompress failed")
#
open(zip_nm, mode='wb').write(res.content)
with zipfile.ZipFile(zip_nm) as zf:
    zipInfo = zf.infolist()
    for member in zipInfo:
      zf.extract(member)
      with open(member.filename, 'r', encoding='cp949') as f:
        text = f.read()
        f.close()
      with open(member.filename, 'w', encoding='utf8') as f:
        f.write(text)
        f.close()

# opendart - 1. 공시정보 - 2) 기업개황

import requests as rq
import zipfile
import pandas as pd
import xml.etree.ElementTree as ET

crtfc_key = '25320e73e479a8e8b9dcfa7a5a76faf0233652b5' # API 인증키
corp_code = '01315963'
dart_url = 'https://opendart.fss.or.kr/api/company.xml?crtfc_key='+crtfc_key+'&corp_code='+corp_code

res = rq.get(dart_url)
com_info = res.content.decode('utf-8')

print(com_info)
print(type(com_info))
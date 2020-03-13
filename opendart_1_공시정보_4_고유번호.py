# opendart - 1. 공시정보 - 4) 고유번호

import requests as rq
import zipfile
import pandas as pd
import xml.etree.ElementTree as ET

crtfc_key = '25320e73e479a8e8b9dcfa7a5a76faf0233652b5'
dart_url = 'https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key='+crtfc_key

res = rq.get(dart_url, allow_redirects=True)
open('opendart_corpCode.zip', 'wb').write(res.content)

try:
    with zipfile.ZipFile('./opendart_corpCode.zip') as zf:
        zf.extractall()
        print("uncompress success")
except:
    print("uncompress failed")

# xml to dataframe

tree = ET.parse('CORPCODE.xml')
root = tree.getroot()
columns = ['corp_code', 'corp_name', 'stock_code', 'modify_date']
df = pd.DataFrame(columns=columns)

for node in root:
    corp_code = node.attrib.get('corp_code')
    corp_name = node.find('corp_name').text if node is not None else None
    stock_code = node.find('stock_code').text if node is not None else None
    modify_date = node.find('modify_date').text if node is not None else None
    df = df.append(pd.Series([corp_code, corp_name, stock_code, modify_date], index=columns), ignore_index=True)

print(root)
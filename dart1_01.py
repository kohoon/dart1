# 공시서류 rcp_no 받아오기

import requests as rq
import bs4
import re
import pandas as pd
from bs4 import BeautifulSoup
from io import BytesIO

auth = '25320e73e479a8e8b9dcfa7a5a76faf0233652b5' # api key
crp_cd = '005930' # 기업코드
start_dt = '19990101' # 검색시작
dart_url = 'http://dart.fss.or.kr/api/search.xml?auth='+auth+'&crp_cd='+crp_cd+'&start_dt='+start_dt+'&fin_rpt=Y'+'&bsn_tp=A001&page_set=100'

res = rq.get(dart_url, params={
    'auth' : auth,
    'crp_cd' : crp_cd,
    'start_dt' : start_dt
})

soup = bs4.BeautifulSoup(res.content.decode('UTF-8'), 'lxml')

str_soup = str(soup)
rpt_nm_list = re.findall(r'<rpt_nm>(.*?)</rpt_nm>', str_soup)
rcp_no_list = re.findall(r'<rcp_no>(.*?)</rcp_no>', str_soup)
rpt_rcp_zip = dict(zip(rpt_nm_list, rcp_no_list))

print(rpt_nm_list)


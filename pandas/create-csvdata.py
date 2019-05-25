import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.nikkansports.com/soccer/jleague/j1/data/standings/'
with urllib.request.urlopen(url) as res:
    html = res.read().decode('UTF-8')
    print(html)
    #print(html.decode('utf-8'))
    #print(res.read())
    #print(res.read().decode('utf-8'))

#print(res.read().decode('utf-8'))
    #html = res.read().decode('utf-8')

#print(html)
#
    #soup = BeautifulSoup(res, 'html.parser')
    #print(soup.select('#schWrap'))

#print(soup.html)R


#print(soup.find(id='standing'))
#print(soup.select('table#standing'))
#print(soup.select('table#standing > thread'))

#print(soup.select_one('table#standing'))

# for a in soup.select('table#standing'):
#     print(a).string



#print(soup.select('table#standing > thread > tr > th'))
#print(soup.select_one('#standing_wrapper > div > div.dataTables_scrollHead > div > table > thead > tr > th:nth-child(4)'))

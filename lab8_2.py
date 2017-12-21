import urllib.request
from bs4 import BeautifulSoup

target_url = 'http://52.68.130.249/textboard/'

# 게시글의 제목과 목록을 가져오는 함수
def fetch_post_list():
    URL = target_url
    res = urllib.request.urlopen(URL)
    html = res.read()

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='kingkongboard-table')

    title_list = table.find_all('td', class_='kingkongboard-list-title')

    links = []
    links = [td.find('a')['href'] for td in title_list]
    return links

result = fetch_post_list( )
print(result)
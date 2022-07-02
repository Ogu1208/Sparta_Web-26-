import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#old_content > table > tbody > tr:nth-child(2)
#old_content > table > tbody > tr:nth-child(3)
#old_content > table > tbody > tr

#select는 결과가 list로 나온다
trs = soup.select('#old_content > table > tbody > tr')

#old_content > table > tbody > tr:nth-child(2) > td.title > div > a  // 그린북 영화 이름 copy
#old_content > table > tbody > tr:nth-child(2) > td.point  # 그린북 영화 평점 copy
for tr in trs:

    a_tag = tr.select_one('td.title > div > a')
    # rank = tr.select_one('td:nth-child(1) > img')['alt']
    # print(rank)

    if a_tag is not None:
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        star = tr.select_one('td.point').text
        print(rank, title, star)



title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
print(title.text)   # 텍스트를 가져올 때는 . 사용
print(title['href'])  #속성을 가져올때는 [] 사용
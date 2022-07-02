from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta  # dbsparta라고 하는 이름으로 DB를 접속(없으면 자동 생성)

# (1) 영화제목 '매트릭스'의 평점을 가져오기
print('#영화제목 매트릭스의 평점을 가져오기')
fd_movie = db.movies.find_one({'title':'매트릭스'})['star']
print(fd_movie)


# (2) '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
print('#매트릭스의 평점과 같은 평점의 영화 제목들을 가져오기')
same_star = list(db.movies.find({'star':fd_movie},{'_id':False}))
for movie in same_star:
    print(movie['title'])


# (3) 매트릭스 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':0}})
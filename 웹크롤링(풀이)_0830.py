url = 'https://sports.news.naver.com/news?oid=411&aid=0000014539'

def crawling(str) :                 # url을 문자열로 받아 구문분석을 통해 Site 명을 추출하여 반환
    if str.find('://') == -1 :      # 입력 문자열이 url이 아니라면, 'No Site' 반환
        return 'No Site'
    x = str.split('/')              # '/'를 구분자로 구문 분류
    # print(x)
    return x[2]
    
s1 = crawling(url)
print(f'주어진 URL : {url}')
print(f'Site 이름 : {s1}')
      

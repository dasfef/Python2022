data = 'https://sports.news.naver.com/news?oid=411&aid=0000014539'


def crolling(a) :
    find = data.rfind('/')
    b = find
    c = data[:b]
    d = data[b+1 :]
    return c, d
    
final = crolling(data)
print('Web Site 명과 컨텐츠 명:', final)

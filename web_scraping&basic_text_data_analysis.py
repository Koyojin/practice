# 1.URL분석
#     어떤식으로 url구성되어있는지, 패턴존재여부,query종류 등 파악
# -from urllib.request import urlopen 
#  from bs4 import BeautifulSoup
#  이 두가지 라이브러리를 활용함

# 2.URL구성
#     url = 'https://alldic.daum.net/search.do?q=' + word
#     이런식으로해서 자동화시키기 위한 처리

# 3.HTML Response얻기
#     web = urlopen(url) 혹은 request.get(URL).contest를 사용

# 4.HTML source얻기
#     BeatifulSoup으로 web페이지상의 HTML구조를 파싱함.
#     web_page = BeautifulSoup(web, 'html.parser')

# 5.HTML Tag꺼내기:.find('Tag이름',{'Attr이름':'Attr값'})
#     .find()의 경우 1개의 Tag를 추출하는데, 여러개일경우 첫번째 Tag를 추출함
#     .find_all()은 여러개의 Tag를 찾는데, Tag가 아니기때문에,리스트같은 걸로 값이 반환되기때문에 for문이나 인덱싱 등으로 꺼내서 활용해야함
#     만약에, Attr조건은 여러개 달고싶을경우,
#     soup.find('a', attrs={"class": "Nbtn_upload"}) 원래 하나일때 이렇게 쓴다면,
#     attrs={"class":"~","id":"~"}요런식으로 딕셔너리 따로 선언해 활용하면된다

# 6.Tag로부터 텍스트 혹은 Attribute values 꺼내기:Tag.get_text() or Tag.attrs

# example)
# words=['state','character','emotion','content','intense']
# for word in words:

#     url='https://alldic.daum.net/search.do?q='+ word

#     http_response=urlopen(url)
#     html_source=BeautifulSoup(http_response,'html.parser')

#     print(html_source.find_all('span',{'class':'txt_search'})[0].get_text())

# -추가로 아래와 같이 with문을 이용해 특정파일에 내가 수집한 text들을 저장할 수 있다
# with open('brunch.txt','w',encoding = 'utf-8') as f:
    
#     all_text = source.find('div',{'class': 'wrap_body'})
#     article = all_text.find_all('p')
    
#     for content in article:
#         print(content.get_text())
#         f.write(content.get_text() + '\n') #줄바꿔서 저장하겠다는 뜻
from bs4 import BeautifulSoup
import urllib.request
import MovieList

class infoCrawl():

    def __init__(self, code):
        code = str(code)
        self.url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=' + code

        url = self.url
        html = urllib.request.urlopen(url)
        source = html.read()
        self.soup = BeautifulSoup(source, 'html.parser')


    def getImgurl(self):

        poster = self.soup.find('div', 'poster')
        img = poster.find('img')

        src = img.get('src')
        #urllib.request.urlretrieve(src, './img/' + 'Myimg2')  이미지 로컬에 저장하는 코드 근데 필요없을듯
        im = self.soup.find('meta', {'property':'og:image'}).get('content')
        # im은 큰사진 src는 작은사진 리턴함
        return src
    def getBigImgurl(self):
        poster = self.soup.find('div', 'poster')
        img = poster.find('img')

        src = img.get('src')
        # urllib.request.urlretrieve(src, './img/' + 'Myimg2')  이미지 로컬에 저장하는 코드 근데 필요없을듯
        im = self.soup.find('meta', {'property': 'og:image'}).get('content')
        # im은 큰사진 src는 작은사진 리턴함
        return im

    def getStory(self):
      #  story = str(self.soup.find('h5', 'h_tx_story').string)
        story2 = str(self.soup.find('p', 'con_tx'))

        story2 = story2.replace('<br/>','')
        story2 = story2.replace('</p>', '')
        story2 = story2.replace('<p class="con_tx">', '')
        story2 = story2.replace('\r', '')
        story2 = story2.replace('.', '. \n')
       # ret = story + '\n'+ story2
        return story2

    def getInfo(self):
        info = self.soup.find('dl' , 'info_spec')
        info2 = info.find_all('p')
        indo3 = info2[0].find_all('span')
        indo5 = []

        for i in range(1,len(info2)):
            a = info2[i]
            try:
                b = a.a.string
            except:
                pass
            if b not in indo5:
                indo5.append(b)

        indo4 = []
        for i in range(len(indo3)):
            a = indo3[i].find_all('a')
            for each in a:
                indo4.append(each.string)

        return indo4 , indo5

    def getReview(self):
        rvhtml = self.soup.find_all('div' , 'score_reple')
        reple = []
        for each in rvhtml:
            temp = str(each.find('p'))
            temp = temp.replace('<p>','')
            temp = temp.replace('</p>' , '')
            temp = temp.replace('<!-- 스포일러 컨텐츠로 처리되는지 여부 -->', '')
            temp = temp.replace('\n','')
            temp = temp.replace('\r', '')
            temp = temp.replace('\t', '')
            reple.append(temp)

        return reple

    def getScore(self):
        schtml = self.soup.find_all('div' , 'star_score')
        scoredic = {}
        cnt = 0
        for i in range(len(schtml)):
            a = schtml[i].find('em')
            if cnt == 0:
                try:
                    scoredic['관람객'] = int(a.string)
                except:
                    continue
            elif cnt == 1:
                try:
                    scoredic['네티즌'] = int(a.string)
                except:
                    continue
            elif cnt == 2:
                try:
                    scoredic['평론가'] = int(a.string)
                except:
                    continue
            else:
                break
            cnt += 1


        for key in scoredic.keys():
            if scoredic[key] == 1:
                scoredic[key] =10


        return scoredic

    def getLink(self):
        html = self.soup
        baseurl = 'https://movie.naver.com'
        linkurl = html.find('a' , {'title':'예매하기'}).get('href')
        ret = baseurl + linkurl

        return ret

    def getPowerReview(self):
        html = self.soup
        baseurl = 'https://movie.naver.com/movie/bi/mi'
        link = html.find('a', 'spc').get('href')
        link = link.replace('./','/')
        url = baseurl + link

        html = urllib.request.urlopen(url)
        source = html.read()
        pwhtml = BeautifulSoup(source, 'html.parser')
        rpline = pwhtml.find_all('div', 'reporter_line')
        ret = []
        for each in rpline:
            temp = []
            name = each.find('img').get('alt')
            jik = each.find('dt').text
            a = name + ': '

            jik = jik.replace(name, a)
            imsc = each.find('img').get('src')
            cap = each.find('dd').string


            temp.append(jik)
            temp.append(imsc)
            temp.append(cap)

            ret.append(temp)

        return ret


if __name__ == '__main__':
    inst = MovieList.MovieList()
    code = inst.getcode(3)

    testob = infoCrawl(code)

    a = testob.getStory()
    print(a)

    b , c = testob.getInfo()

    print(b)
    print(c)
    print(testob.getReview())
    print(testob.getScore())
    print(testob.getImgurl())
    print(testob.getLink())
    print(testob.getPowerReview())
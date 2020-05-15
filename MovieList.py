from bs4 import BeautifulSoup
from urllib.request import urlopen

class MovieList():

    def __init__(self):
        self.oriurl = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel='
        self.title_n = []
        self.sortByScore()

    def sortByScore(self):
        url = self.oriurl + 'cur&date=99999999'
        page = urlopen(url)
        soup = BeautifulSoup(page, "html.parser")

        self.title_n = soup.find_all('div', 'tit5')
        num =len(self.title_n)


        movie_name = [soup.find_all('div', 'tit5')[n].a.string for n in range(num)]
        movie_point = [soup.find_all('td', 'point')[n].string for n in range(num)]
        movie_dict = {}

        for i in range(num):
            movie_dict[movie_name[i]] = movie_point[i]

        return movie_dict

    def sortByWatch(self):
        url = self.oriurl + 'cnt&date=99999999'
        page = urlopen(url)
        soup = BeautifulSoup(page, "html.parser")

        self.title_n = soup.find_all('div', 'tit3')
        num = len(self.title_n)
        movie_name = [soup.find_all('div', 'tit3')[n].a.string for n in range(num)]

        dicc = {}
        for i in range(num):
            dicc[i+1] = movie_name[i]

        return dicc

    def sortByScore2(self):
        url = self.oriurl + 'cur&date=99999999'
        page = urlopen(url)
        soup = BeautifulSoup(page, "html.parser")

        self.title_n = soup.find_all('div', 'tit5')
        num = len(self.title_n)
        movie_name = [soup.find_all('div', 'tit5')[n].a.string for n in range(num)]

        movie_dict = {}

        for i in range(num):
            movie_dict[i + 1] = movie_name[i]
        return movie_dict

    def getcode(self, ind):
        urlstr= self.title_n[ind].a.get('href')
        codeind = urlstr.find('=') +1
        code = urlstr[codeind:]

        return code


if __name__ == "__main__":
    test = MovieList()
    dicc = test.sortByScore()
   # for each in dicc:
    #    print(each ,':',dicc[each] )

    a = test.getcode(3)
    print(a)
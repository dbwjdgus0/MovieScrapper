import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from os.path import dirname, join
from bs4 import BeautifulSoup

import MovieList
import infocrawl
import urllib.request
import functools

current_dir = dirname(__file__)
file_path = join(current_dir, "./main.ui")
form_class = uic.loadUiType(file_path)[0]

sub_file_path = join(current_dir, "./movieinfo.ui")
sub_form_class = uic.loadUiType(sub_file_path)[0]

movieTitle = 'movieTitle'
movieCode = 'movieCode'


class MovieInfo(QMainWindow, sub_form_class):
    def __init__(self, parent=None):
        super(MovieInfo, self).__init__(parent)
        self.setupUi(self)

        # title
        self.movieTitleKor.setText(movieTitle)
        self.info = infocrawl.infoCrawl(movieCode)

        # poster image load
        self.imgURL = self.info.getBigImgurl()
        self.posterImg = urllib.request.urlopen(self.imgURL).read()
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(self.posterImg)
        self.moviePoster.setPixmap(self.pixmap)

        # subtitle
        firstinfo, secondinfo = self.info.getInfo()
        self.movieInfo1.setText(str(firstinfo))
        self.movieInfo2.setText(str(secondinfo))

        # story
        self.movieInform.setText('\n ' + self.info.getStory())

        # star
        movieStar = self.info.getScore()
        audienceScore = movieStar['관람객'] // 2
        netizenScore = movieStar['네티즌'] // 2
        reviewerScore = movieStar['평론가'] // 2

        self.audienceStar.setText('★' * audienceScore + '☆' * (5 - audienceScore))
        self.netizenStar.setText('★' * netizenScore + '☆' * (5 - netizenScore))
        self.reviewerStar.setText('★' * reviewerScore + '☆' * (5 - reviewerScore))

        # review
        self.audienceReview.clicked.connect(self.audienceButtonClicked)
        self.reviewerReview.clicked.connect(self.reviewerButtonClicked)

    def audienceButtonClicked(self):
        self.reviewerPic1.clear()
        self.reviewerPic2.clear()
        self.reviewerPic3.clear()
        self.reviewerSpace1.clear()
        self.reviewerSpace2.clear()
        self.reviewerSpace3.clear()

        reviewText = self.info.getReview()
        review = ''
        for i in range(0, 5):
            review += '\n' + str(i + 1) + '. ' + reviewText[i] + '\n'
        self.movieReview.setText(review)

    def reviewerButtonClicked(self):
        self.movieReview.clear()

        # reviewer's Picture
        self.revPic1 = self.info.getPowerReview()[0][1]
        self.revPic2 = self.info.getPowerReview()[1][1]
        self.revPic3 = self.info.getPowerReview()[2][1]
        self.revImg1 = urllib.request.urlopen(self.revPic1).read()
        self.revImg2 = urllib.request.urlopen(self.revPic2).read()
        self.revImg3 = urllib.request.urlopen(self.revPic3).read()
        self.revPixmap1 = QPixmap()
        self.revPixmap2 = QPixmap()
        self.revPixmap3 = QPixmap()
        self.revPixmap1.loadFromData(self.revImg1)
        self.revPixmap2.loadFromData(self.revImg2)
        self.revPixmap3.loadFromData(self.revImg3)
        self.reviewerPic1.setPixmap(self.revPixmap1)
        self.reviewerPic2.setPixmap(self.revPixmap2)
        self.reviewerPic3.setPixmap(self.revPixmap3)

        # reviewer's Review
        self.revName1 = self.info.getPowerReview()[0][0]
        self.revName2 = self.info.getPowerReview()[1][0]
        self.revName3 = self.info.getPowerReview()[2][0]
        self.revReview1 = self.info.getPowerReview()[0][2]
        self.revReview2 = self.info.getPowerReview()[1][2]
        self.revReview3 = self.info.getPowerReview()[2][2]
        self.reviewerSpace1.setText(' ' + self.revName1 + '\n ' + self.revReview1)
        self.reviewerSpace2.setText(' ' + self.revName2 + '\n ' + self.revReview2)
        self.reviewerSpace3.setText(' ' + self.revName3 + '\n ' + self.revReview3)


class MovieScrapper(QMainWindow, form_class):
    def __init__(self, parent=None):
        super(MovieScrapper, self).__init__(parent)
        self.setupUi(self)

        self.movielist = MovieList.MovieList()

        self.ViewOrder.clicked.connect(self.viewButtonClicked)
        self.RankOrder.clicked.connect(self.rankButtonClicked)

        self.RankTitle1.clicked.connect(self.movieTitleClicked)
        self.RankTitle2.clicked.connect(self.movieTitleClicked)
        self.RankTitle3.clicked.connect(self.movieTitleClicked)
        self.RankTitle4.clicked.connect(self.movieTitleClicked)
        self.RankTitle5.clicked.connect(self.movieTitleClicked)
        self.RankTitle6.clicked.connect(self.movieTitleClicked)
        self.RankTitle7.clicked.connect(self.movieTitleClicked)
        self.RankTitle8.clicked.connect(self.movieTitleClicked)
        self.RankTitle9.clicked.connect(self.movieTitleClicked)
        self.RankTitle10.clicked.connect(self.movieTitleClicked)
        self.RankTitle11.clicked.connect(self.movieTitleClicked)
        self.RankTitle12.clicked.connect(self.movieTitleClicked)
        self.RankTitle13.clicked.connect(self.movieTitleClicked)
        self.RankTitle14.clicked.connect(self.movieTitleClicked)
        self.RankTitle15.clicked.connect(self.movieTitleClicked)
        self.RankTitle16.clicked.connect(self.movieTitleClicked)
        self.RankTitle17.clicked.connect(self.movieTitleClicked)
        self.RankTitle18.clicked.connect(self.movieTitleClicked)
        self.RankTitle19.clicked.connect(self.movieTitleClicked)
        self.RankTitle20.clicked.connect(self.movieTitleClicked)

        '''
        self.mainPoster1.mousePressEvent = self.movieTitleClicked
        self.mainPoster2.mousePressEvent = self.movieTitleClicked
        self.mainPoster3.mousePressEvent = self.movieTitleClicked
        self.mainPoster4.mousePressEvent = self.movieTitleClicked
        self.mainPoster5.mousePressEvent = self.movieTitleClicked
        self.mainPoster6.mousePressEvent = self.movieTitleClicked
        self.mainPoster7.mousePressEvent = self.movieTitleClicked
        self.mainPoster8.mousePressEvent = self.movieTitleClicked
        self.mainPoster9.mousePressEvent = self.movieTitleClicked
        self.mainPoster10.mousePressEvent = self.movieTitleClicked
        '''

        self.dialogs = list()

    def rankButtonClicked(self):
        self.rankOrder = self.movielist.sortByScore2()

        self.mlist = []
        for val in self.rankOrder.values():
            self.mlist.append(val)

        self.RankingBox.setTitle("평점순랭킹")

        self.RankTitle1.setText(self.rankOrder.get(1))
        self.RankTitle2.setText(self.rankOrder.get(2))
        self.RankTitle3.setText(self.rankOrder.get(3))
        self.RankTitle4.setText(self.rankOrder.get(4))
        self.RankTitle5.setText(self.rankOrder.get(5))
        self.RankTitle6.setText(self.rankOrder.get(6))
        self.RankTitle7.setText(self.rankOrder.get(7))
        self.RankTitle8.setText(self.rankOrder.get(8))
        self.RankTitle9.setText(self.rankOrder.get(9))
        self.RankTitle10.setText(self.rankOrder.get(10))
        self.RankTitle11.setText(self.rankOrder.get(11))
        self.RankTitle12.setText(self.rankOrder.get(12))
        self.RankTitle13.setText(self.rankOrder.get(13))
        self.RankTitle14.setText(self.rankOrder.get(14))
        self.RankTitle15.setText(self.rankOrder.get(15))
        self.RankTitle16.setText(self.rankOrder.get(16))
        self.RankTitle17.setText(self.rankOrder.get(17))
        self.RankTitle18.setText(self.rankOrder.get(18))
        self.RankTitle19.setText(self.rankOrder.get(19))
        self.RankTitle20.setText(self.rankOrder.get(20))

        self.url1 = self.movielist.getcode(0)
        self.url2 = self.movielist.getcode(1)
        self.url3 = self.movielist.getcode(2)
        self.url4 = self.movielist.getcode(3)
        self.url5 = self.movielist.getcode(4)
        self.url6 = self.movielist.getcode(5)
        self.url7 = self.movielist.getcode(6)
        self.url8 = self.movielist.getcode(7)
        self.url9 = self.movielist.getcode(8)
        self.url10 = self.movielist.getcode(9)

        self.infocr1 = infocrawl.infoCrawl(self.url1)
        self.infocr2 = infocrawl.infoCrawl(self.url2)
        self.infocr3 = infocrawl.infoCrawl(self.url3)
        self.infocr4 = infocrawl.infoCrawl(self.url4)
        self.infocr5 = infocrawl.infoCrawl(self.url5)
        self.infocr6 = infocrawl.infoCrawl(self.url6)
        self.infocr7 = infocrawl.infoCrawl(self.url7)
        self.infocr8 = infocrawl.infoCrawl(self.url8)
        self.infocr9 = infocrawl.infoCrawl(self.url9)
        self.infocr10 = infocrawl.infoCrawl(self.url10)

        self.img1url = self.infocr1.getImgurl()
        self.img2url = self.infocr2.getImgurl()
        self.img3url = self.infocr3.getImgurl()
        self.img4url = self.infocr4.getImgurl()
        self.img5url = self.infocr5.getImgurl()
        self.img6url = self.infocr6.getImgurl()
        self.img7url = self.infocr7.getImgurl()
        self.img8url = self.infocr8.getImgurl()
        self.img9url = self.infocr9.getImgurl()
        self.img10url = self.infocr10.getImgurl()

        self.posterimg1 = urllib.request.urlopen(self.img1url).read()
        self.posterimg2 = urllib.request.urlopen(self.img2url).read()
        self.posterimg3 = urllib.request.urlopen(self.img3url).read()
        self.posterimg4 = urllib.request.urlopen(self.img4url).read()
        self.posterimg5 = urllib.request.urlopen(self.img5url).read()
        self.posterimg6 = urllib.request.urlopen(self.img6url).read()
        self.posterimg7 = urllib.request.urlopen(self.img7url).read()
        self.posterimg8 = urllib.request.urlopen(self.img8url).read()
        self.posterimg9 = urllib.request.urlopen(self.img9url).read()
        self.posterimg10 = urllib.request.urlopen(self.img10url).read()

        self.pixmap1 = QPixmap()
        self.pixmap2 = QPixmap()
        self.pixmap3 = QPixmap()
        self.pixmap4 = QPixmap()
        self.pixmap5 = QPixmap()
        self.pixmap6 = QPixmap()
        self.pixmap7 = QPixmap()
        self.pixmap8 = QPixmap()
        self.pixmap9 = QPixmap()
        self.pixmap10 = QPixmap()

        self.pixmap1.loadFromData(self.posterimg1)
        self.pixmap2.loadFromData(self.posterimg2)
        self.pixmap3.loadFromData(self.posterimg3)
        self.pixmap4.loadFromData(self.posterimg4)
        self.pixmap5.loadFromData(self.posterimg5)
        self.pixmap6.loadFromData(self.posterimg6)
        self.pixmap7.loadFromData(self.posterimg7)
        self.pixmap8.loadFromData(self.posterimg8)
        self.pixmap9.loadFromData(self.posterimg9)
        self.pixmap10.loadFromData(self.posterimg10)

        self.mainPoster1.setPixmap(self.pixmap1)
        self.mainPoster2.setPixmap(self.pixmap2)
        self.mainPoster3.setPixmap(self.pixmap3)
        self.mainPoster4.setPixmap(self.pixmap4)
        self.mainPoster5.setPixmap(self.pixmap5)
        self.mainPoster6.setPixmap(self.pixmap6)
        self.mainPoster7.setPixmap(self.pixmap7)
        self.mainPoster8.setPixmap(self.pixmap8)
        self.mainPoster9.setPixmap(self.pixmap9)
        self.mainPoster10.setPixmap(self.pixmap10)

    def viewButtonClicked(self):
        self.viewOrder = self.movielist.sortByWatch()

        self.mlist = []
        for val in self.viewOrder.values():
            self.mlist.append(val)

        self.RankingBox.setTitle("조회순랭킹")

        self.RankTitle1.setText(self.viewOrder.get(1))
        self.RankTitle2.setText(self.viewOrder.get(2))
        self.RankTitle3.setText(self.viewOrder.get(3))
        self.RankTitle4.setText(self.viewOrder.get(4))
        self.RankTitle5.setText(self.viewOrder.get(5))
        self.RankTitle6.setText(self.viewOrder.get(6))
        self.RankTitle7.setText(self.viewOrder.get(7))
        self.RankTitle8.setText(self.viewOrder.get(8))
        self.RankTitle9.setText(self.viewOrder.get(9))
        self.RankTitle10.setText(self.viewOrder.get(10))
        self.RankTitle11.setText(self.viewOrder.get(11))
        self.RankTitle12.setText(self.viewOrder.get(12))
        self.RankTitle13.setText(self.viewOrder.get(13))
        self.RankTitle14.setText(self.viewOrder.get(14))
        self.RankTitle15.setText(self.viewOrder.get(15))
        self.RankTitle16.setText(self.viewOrder.get(16))
        self.RankTitle17.setText(self.viewOrder.get(17))
        self.RankTitle18.setText(self.viewOrder.get(18))
        self.RankTitle19.setText(self.viewOrder.get(19))
        self.RankTitle20.setText(self.viewOrder.get(20))

        self.url1 = self.movielist.getcode(0)
        self.url2 = self.movielist.getcode(1)
        self.url3 = self.movielist.getcode(2)
        self.url4 = self.movielist.getcode(3)
        self.url5 = self.movielist.getcode(4)
        self.url6 = self.movielist.getcode(5)
        self.url7 = self.movielist.getcode(6)
        self.url8 = self.movielist.getcode(7)
        self.url9 = self.movielist.getcode(8)
        self.url10 = self.movielist.getcode(9)

        self.infocr1 = infocrawl.infoCrawl(self.url1)
        self.infocr2 = infocrawl.infoCrawl(self.url2)
        self.infocr3 = infocrawl.infoCrawl(self.url3)
        self.infocr4 = infocrawl.infoCrawl(self.url4)
        self.infocr5 = infocrawl.infoCrawl(self.url5)
        self.infocr6 = infocrawl.infoCrawl(self.url6)
        self.infocr7 = infocrawl.infoCrawl(self.url7)
        self.infocr8 = infocrawl.infoCrawl(self.url8)
        self.infocr9 = infocrawl.infoCrawl(self.url9)
        self.infocr10 = infocrawl.infoCrawl(self.url10)

        self.img1url = self.infocr1.getImgurl()
        self.img2url = self.infocr2.getImgurl()
        self.img3url = self.infocr3.getImgurl()
        self.img4url = self.infocr4.getImgurl()
        self.img5url = self.infocr5.getImgurl()
        self.img6url = self.infocr6.getImgurl()
        self.img7url = self.infocr7.getImgurl()
        self.img8url = self.infocr8.getImgurl()
        self.img9url = self.infocr9.getImgurl()
        self.img10url = self.infocr10.getImgurl()

        self.posterimg1 = urllib.request.urlopen(self.img1url).read()
        self.posterimg2 = urllib.request.urlopen(self.img2url).read()
        self.posterimg3 = urllib.request.urlopen(self.img3url).read()
        self.posterimg4 = urllib.request.urlopen(self.img4url).read()
        self.posterimg5 = urllib.request.urlopen(self.img5url).read()
        self.posterimg6 = urllib.request.urlopen(self.img6url).read()
        self.posterimg7 = urllib.request.urlopen(self.img7url).read()
        self.posterimg8 = urllib.request.urlopen(self.img8url).read()
        self.posterimg9 = urllib.request.urlopen(self.img9url).read()
        self.posterimg10 = urllib.request.urlopen(self.img10url).read()

        self.pixmap1 = QPixmap()
        self.pixmap2 = QPixmap()
        self.pixmap3 = QPixmap()
        self.pixmap4 = QPixmap()
        self.pixmap5 = QPixmap()
        self.pixmap6 = QPixmap()
        self.pixmap7 = QPixmap()
        self.pixmap8 = QPixmap()
        self.pixmap9 = QPixmap()
        self.pixmap10 = QPixmap()

        self.pixmap1.loadFromData(self.posterimg1)
        self.pixmap2.loadFromData(self.posterimg2)
        self.pixmap3.loadFromData(self.posterimg3)
        self.pixmap4.loadFromData(self.posterimg4)
        self.pixmap5.loadFromData(self.posterimg5)
        self.pixmap6.loadFromData(self.posterimg6)
        self.pixmap7.loadFromData(self.posterimg7)
        self.pixmap8.loadFromData(self.posterimg8)
        self.pixmap9.loadFromData(self.posterimg9)
        self.pixmap10.loadFromData(self.posterimg10)

        self.mainPoster1.setPixmap(self.pixmap1)
        self.mainPoster2.setPixmap(self.pixmap2)
        self.mainPoster3.setPixmap(self.pixmap3)
        self.mainPoster4.setPixmap(self.pixmap4)
        self.mainPoster5.setPixmap(self.pixmap5)
        self.mainPoster6.setPixmap(self.pixmap6)
        self.mainPoster7.setPixmap(self.pixmap7)
        self.mainPoster8.setPixmap(self.pixmap8)
        self.mainPoster9.setPixmap(self.pixmap9)
        self.mainPoster10.setPixmap(self.pixmap10)

    def movieTitleClicked(self, event):
        global movieTitle
        global movieCode
        sender = self.sender()
        movieTitle = sender.text()
        inx = 0
        for i in range(len(self.mlist)):
            if movieTitle == self.mlist[i]:
                inx = i
        movieCode = self.movielist.getcode(inx)

        dialog = MovieInfo(self)
        self.dialogs.append(dialog)
        dialog.show()

        print(movieCode)
        print(movieTitle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    movieScrapper = MovieScrapper()
    movieScrapper.show()
    app.exec_()
from discord import team
import requests
from bs4 import BeautifulSoup


#Bu python dosyasında fotomaç sitesinden veri kazıyoruz
#(Not: Kütüphaneleri indirmeyi unutmayın eğer html.parser yerine 
#başka bir kütüphane kullanıyorsanız o kütüphaneyide indirmek zorundasınız){bkz. satır 14}


def trabzonspor():
    tsLink = "https://www.fotomac.com.tr/trabzonspor"
    r = requests.get(tsLink)
    soupTs = BeautifulSoup(r.content,"html.parser")
    founddata = soupTs.find_all("div",attrs={"id":"fixture"})
    tsLi = founddata[0].contents[1]
    history = tsLi.contents[1].find_all("span",attrs={"class":"date"})
    teamOne = tsLi.contents[1].find_all("a",attrs={"class":"team1"})
    teamTwo = tsLi.contents[1].find_all("a",attrs={"class":"team2"})
    teamOne = teamOne[0].contents
    teamOne = teamOne[3]
    teamOne = str(teamOne)
    teamOne = teamOne.replace("<i>","")
    teamOne = teamOne.replace("</i>","")   
    teamTwo = teamTwo[0].contents
    teamTwo = teamTwo[3]
    teamTwo = str(teamTwo)
    teamTwo = teamTwo.replace("<i>","")
    teamTwo = teamTwo.replace("</i>","")
    history = str(history)
    history = history.replace('<span class="date">',"")
    history = history.replace("</span>","")
    history = history.replace("[","")
    history = history.replace("]","")
    dataTs = [teamOne,teamTwo,history]
    return dataTs
    
def besiktas():
    bsLink = "https://www.fotomac.com.tr/besiktas"
    r = requests.get(bsLink)
    soupBs = BeautifulSoup(r.content,"html.parser")
    founddata = soupBs.find_all("div",attrs={"id":"fixture"})
    BsLi = founddata[0].contents[1]
    history = BsLi.contents[1].find_all("span",attrs={"class":"date"})
    teamOne = BsLi.contents[1].find_all("a",attrs={"class":"team1"})
    teamTwo = BsLi.contents[1].find_all("a",attrs={"class":"team2"})
    teamOne = teamOne[0].contents
    teamOne = teamOne[3]
    teamOne = str(teamOne)
    teamOne = teamOne.replace("<i>","")
    teamOne = teamOne.replace("</i>","")
    teamTwo = teamTwo[0].contents
    teamTwo = teamTwo[3]
    teamTwo = str(teamTwo)
    teamTwo = teamTwo.replace("<i>","")
    teamTwo = teamTwo.replace("</i>","")
    history = str(history)
    history = history.replace('<span class="date">',"")
    history = history.replace("</span>","")
    history = history.replace("[","")
    history = history.replace("]","")
    databs = [teamOne,teamTwo,history]
    return databs

def galatasaray():
    gsLink = "https://www.fotomac.com.tr/galatasaray"
    r = requests.get(gsLink)
    soupGs = BeautifulSoup(r.content,"html.parser")
    founddata = soupGs.find_all("div",attrs={"id":"fixture"})
    gsLi = founddata[0].contents[1]
    history = gsLi.contents[1].find_all("span",attrs={"class":"date"})
    teamOne = gsLi.contents[1].find_all("a",attrs={"class":"team1"})
    teamTwo = gsLi.contents[1].find_all("a",attrs={"class":"team2"})
    teamOne = teamOne[0].contents
    teamOne = teamOne[3]
    teamOne = str(teamOne)
    teamOne = teamOne.replace("<i>","")
    teamOne = teamOne.replace("</i>","")
    teamTwo = teamTwo[0].contents
    teamTwo = teamTwo[3]
    teamTwo = str(teamTwo)
    teamTwo = teamTwo.replace("<i>","")
    teamTwo = teamTwo.replace("</i>","")
    history = str(history)
    history = history.replace('<span class="date">',"")
    history = history.replace("</span>","")
    history = history.replace("[","")
    history = history.replace("]","")
    datags = [teamOne,teamTwo,history]
    return datags
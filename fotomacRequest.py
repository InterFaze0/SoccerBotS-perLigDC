import requests
from bs4 import BeautifulSoup


def returnPuand():
    fotomaclink = "https://www.fotomac.com.tr/canli-skor/puan-durumu/super-lig-21-22"
    r = requests.get(fotomaclink)
    soupFoto = BeautifulSoup(r.content,"lxml")
    foundData = soupFoto.find_all("table",{"class":"table table-team-list table-bottom-border team-status"})
    foundData = foundData[0].contents[3]
    foundData = foundData.find_all("td",{"class":"team-logo text-left"})
    teams =[]
    for team in foundData:
        team = team.contents[1].contents[2]
        team = str(team)
        team = team.replace("<span>","")
        team = team.replace("</span>","")
        teams = teams + [team] 
    return teams

def istatistik():
    fotomaclink = "https://www.fotomac.com.tr/canli-skor/puan-durumu/super-lig-21-22"
    r = requests.get(fotomaclink)
    soupFoto = BeautifulSoup(r.content,"lxml")
    foundDataCountPoint = soupFoto.find_all("table",{"class":"table table-team-list table-bottom-border team-status"})
    foundDataCountPoint = foundDataCountPoint[0].contents[3]
    foundDataCountPoint = foundDataCountPoint.contents
    points =[]
    for i in range(1,41,2):
        CountPoints = str(foundDataCountPoint[i].contents[21])
        CountPoints = CountPoints.replace("<td>","")
        CountPoints = CountPoints.replace("</td>","")
        points = points + [CountPoints]
    return points     


import discord
from discord.ext import commands
from fotomacRequest import * 
from teamsfixture import *

#Procfile , requirements.txt ve runtime dosyası botumuzu çalıştırcağımız Heroku platformu için gerekli olan dosyalardır.
#Heroku {heroku.com}

macbot = commands.Bot("!sb ") #Dökümantasyon {https://discordpy.readthedocs.io/en/latest/index.html} 

@macbot.event
async def on_ready():
    print('Komutlar Kullanılmaya Hazır')

    

@macbot.command(aliases =["sonrakimaçTs","sonrakikarşılaşmaTs"])
async def sonts(message):
    sonmac = trabzonspor()
    tablets = discord.Embed(title=sonmac[0],description= sonmac[2],color =0x00A5FF)
    tablets.add_field(name=sonmac[1],value="Soccer Match",inline=False)
    await message.send(embed=tablets)

@macbot.command(aliases =["sonrakimaçBs","sonrakikarşılaşmaBs"])
async def sonbs(message):
    sonmac = besiktas()
    tablebs = discord.Embed(title=sonmac[0],description= sonmac[2],color =0xF3F3F3)
    tablebs.add_field(name=sonmac[1],value="Soccer Match",inline=False)
    await message.send(embed=tablebs)



@macbot.command(aliases =["sonrakimaçGs","sonrakikarşılaşmaGs"])
async def songs(message):
    sonmac = galatasaray()
    tablegs = discord.Embed(title=sonmac[0],description= sonmac[2],color =0xFFEC02)
    tablegs.add_field(name=sonmac[1],value="Soccer Match",inline=False)
    await message.send(embed=tablegs)



@macbot.command(aliases =["puand","sıralama"])
async def puandurumu(message):
    teams = returnPuand()
    points = istatistik()
    table = discord.Embed(title = "Puan Durumu",description="Süper Toto Süper Lig",color=0x000000)
    table.add_field(name ="1. " + str(teams[0]),value="Karşılaşmalarda Toplanan Toplam Puan: " +points[0] ,inline=False)
    table.add_field(name ="2. " + str(teams[1]),value="Karşılaşmalarda Toplanan Toplam Puan: " +points[1] ,inline=False)
    table.add_field(name ="3. " + str(teams[2]),value="Karşılaşmalarda Toplanan Toplam Puan: " +points[2] ,inline=False)
    table.add_field(name ="4. " + str(teams[3]),value="Karşılaşmalarda Toplanan Toplam Puan: " +points[3] ,inline=False)
    await message.send(embed=table)






@macbot.command(aliases =["yardım"])
async def yardim(message):
    tableHelp = discord.Embed(title="Komutlar",description ="Kullanım Komutları",color=0x000000)
    tableHelp.add_field(name="!sb sıralama",value="Süper Lig de sıralamada ilk 4 takımı gösterir",inline=False)
    tableHelp.add_field(name="!sb sonrakikarşılaşmaTs",value="Trabzonspor takımının yapacağı karşılaşmayı gösterir",inline=False)
    tableHelp.add_field(name="!sb sonrakikarşılaşmaBs",value="Beşiktaş takımının yapacağı karşılaşmayı gösterir",inline=False)
    tableHelp.add_field(name="!sb sonrakikarşılaşmaGs",value="Galatasaray takımının yapacağı karşılaşmayı gösterir",inline=False)
    await message.send(embed = tableHelp)
    


token = '' #Kendi botunuzun token dizisini buraya girmeniz gereklidir(Not: Tokeninizi kimseyle paylaşmayın)
macbot.run(token)

import pandas as pd
import json
import csv
import re
from TeamListGenerator import FileUploader, FileParser, MatchupGenerator
from scheduler import findteam, findmatchinggame, fliphomeaway, FindAllOpponents, PickOppTeam

directory = 'MLBTeams.csv'
teamlist = FileParser(directory)
rot = "A"
home = "#"
away = "@"
four = "4"
three = "3"
teamlist = MatchupGenerator(teamlist, rot, home, away, four, three)
wteamlist = teamlist


listOfWeeks = []

i=0
while i<=11:#len(teamlist[0]['ScheduleList']):
    wteamlist = []
    wUnsched = []
    wSched = []
    wteamlist = teamlist.copy()
    #print(f"Pre Process: {wUnsched}")
    for team in teamlist:
        #print(team['Abbrev'])
        xx = team['Abbrev']
        wUnsched.append(xx)
    #print(f"Post Process: {wUnsched}")
       
    #input("Test")
        
    for team in wteamlist:
        print(f"Beginning of Match Attempt \n{team['Abbrev']}")
        opponentlist = FindAllOpponents(team, wteamlist)
        print(opponentlist)
        oppteam = PickOppTeam(team['Abbrev'], wteamlist, opponentlist, wUnsched)
        print(oppteam)

        print(f"{team['Team']}")
        print(f"{team['ScheduleList']}")
        a = findteam(oppteam,teamlist)
        b = findteam(team['Abbrev'],teamlist)
        

        oppgamestring = findmatchinggame(b['Abbrev'], a['ScheduleList'])
        fliphomeaway(home, away, oppgamestring, a['Abbrev'], four, three, b['ScheduleList'], a['ScheduleList'], wSched)

        # print(wUnsched)
        # print(wSched)
    
        c = [d for i, d in enumerate(wteamlist) if a['Abbrev'] in d['Abbrev']][0]
        rindex = wteamlist.index(c)  
        wteamlist.pop(rindex)
    listOfWeeks.append(wSched)
    print(listOfWeeks)
    i+=1
    

with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(listOfWeeks)
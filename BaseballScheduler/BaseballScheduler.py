import pandas as pd
import json
import csv
import re
import random
from TeamListGenerator import FileUploader, FileParser, MatchupGenerator
from scheduler import findteam, findmatchinggame, fliphomeaway, FindAllOpponents, PickOppTeam

directory = 'MLBTeams.csv'
teamlist = FileParser(directory)
rot = "A"
home = "#"
away = "@"
four = "4"
three = "3"
two = "2"
teamlist = MatchupGenerator(teamlist, rot, home, away, four, three, two)
wteamlist = teamlist


listOfWeeks = []

i=0
print(len(teamlist[0]['ScheduleList']))
while i<52:#len(teamlist[0]['ScheduleList']):
    print(f"###### \nSTARTING WEEK: {i}\n######\n######\n######")
    weekcheck=False
    while weekcheck==False: 
        print("####################################################AT TOP OF LOOP")
        wteamlist = []
        wUnsched = []
        wSched = []
        weeklyremovals = []
        wteamlist = teamlist.copy()
        random.shuffle(wteamlist)
        for team in teamlist:
            xx = team['Abbrev']
            wUnsched.append(xx)
        
        for team in wteamlist:
            print(f"Beginning of Match Attempt \n{team['Abbrev']}")
            opponentlist = FindAllOpponents(team, wteamlist)
            print(f"WEEK {i+1}")
            print(opponentlist)
            print(f"{wUnsched}")
            try:
                oppteam = PickOppTeam(team['Abbrev'], wteamlist, opponentlist, wUnsched)
                weekcheck=True
            except:
                weekcheck=False
            print(oppteam)

            print(f"{team['Team']}")
            print(f"{team['ScheduleList']}")
            #print(oppteam)
            if weekcheck==True:
                try:
                    a = findteam(oppteam,wteamlist)
                    b = findteam(team['Abbrev'],wteamlist)
                except: 
                    weekcheck=False
                    break
                oppgamestring = findmatchinggame(b['Abbrev'], a['ScheduleList'])
                x = fliphomeaway(home, away, oppgamestring, a['Abbrev'], b['Abbrev'], four, three, two, wSched, weeklyremovals)
                
                opp = [d for i, d in enumerate(wteamlist) if a['Abbrev'] in d['Abbrev']][0]
                star = [d for i, d in enumerate(wteamlist) if b['Abbrev'] in d['Abbrev']][0]
                print("removedmatchups")
                #opp['ScheduleList'].remove(x[1])
                #star['ScheduleList'].remove(x[0])
                # print(wUnsched)
                # print(wSched)
    
                c = [d for i, d in enumerate(wteamlist) if a['Abbrev'] in d['Abbrev']][0]
                rindex = wteamlist.index(c)  
                wteamlist.pop(rindex)
            else:
                pass   
        if weekcheck==True:
            
            print(f"Weekly Removals{weeklyremovals}\n")
            print(*weeklyremovals[0].keys())
            for removal in weeklyremovals:
                c = [d for i, d in enumerate(teamlist) if list(removal.keys())[0] in d['Abbrev']][0]
                print(f"Find Team: {list(removal.keys())[0]}")                
                print(f"Find Matchup: {list(removal.values())[0]}")
                print("REMOVING...")
                c['ScheduleList'].remove(list(removal.values())[0])
                print(c)
            
            listOfWeeks.append(wSched)
            print(f"Schedule: \n{listOfWeeks}\n")
            i+=1
   

with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(listOfWeeks)
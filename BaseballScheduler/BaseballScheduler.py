import pandas as pd
import json
import csv
from itertools import chain
import random
import re



directory = 'MLBTeams.csv'
teams = csv.DictReader(open(directory))

rot = "A"
home = "#"
away = "@"
four = "4"
three = "3"
teamlist = []

for team in teams: 
    x = team
    team['LDiv'] = team['League']+team['Division']
    teamlist.append(x)

for team in teamlist:
    gameslist = []
    #Home 7 game division rotation (4,3)
    for iteam in teamlist:
        if team['LDiv'] == iteam['LDiv'] and not(team['Team'] == iteam['Team']):
            if team['InterleagueRotation'] == iteam['InterleagueRotation']:
                gameslist.append(home+iteam['Abbrev']+four)
                gameslist.append(away+iteam['Abbrev']+three)
            else: 
                gameslist.append(home+iteam['Abbrev']+three)
                gameslist.append(away+iteam['Abbrev']+four)                
    
    #Home 3 game divional rotation (3,3)
    for iteam in teamlist:
        if team['LDiv'] == iteam['LDiv'] and not(team['Team'] == iteam['Team']):
            gameslist.append(home+iteam['Abbrev']+three)
            gameslist.append(away+iteam['Abbrev']+three)

    #3 game interleague
    for iteam in teamlist:
        if not(team['League'] == iteam['League']) and not(iteam['Abbrev'] == team['Rivals']):
            #if league is AL, then matching rotation means away game.
            if team['League'] == "AL":
                if team['InterleagueRotation'] == iteam['InterleagueRotation']:
                    gameslist.append(away+iteam['Abbrev']+three)
                else: 
                    gameslist.append(home+iteam['Abbrev']+three) 
            else: #if NL is team league, rules switch
                if team['InterleagueRotation'] == iteam['InterleagueRotation']:
                    gameslist.append(home+iteam['Abbrev']+three)
                else: 
                    gameslist.append(away+iteam['Abbrev']+three) 
           
    #6 game intraleague rotation (3,3)
    for iteam in teamlist:
        if team['League'] == iteam['League'] and not(team['LDiv'] == iteam['LDiv']):
            if team['IR1'] == iteam['IntraStaticID']:
                gameslist.append(home+iteam['Abbrev']+three)
                gameslist.append(away+iteam['Abbrev']+four)
            elif team['IR2'] == iteam['IntraStaticID']:
                gameslist.append(home+iteam['Abbrev']+four)
                gameslist.append(away+iteam['Abbrev']+three)                
            else: 
                gameslist.append(home+iteam['Abbrev']+three)
                gameslist.append(away+iteam['Abbrev']+three)
            
    #4 game rival
    for iteam in teamlist:
        if team['Abbrev'] == iteam['Rivals']:
            if team['RivalRot'] == rot:
                gameslist.append(home+iteam['Abbrev']+four)
            else: 
                gameslist.append(away+iteam['Abbrev']+four)
        
    team['ScheduleList'] = gameslist
    team['SelfList'] = [home+team['Abbrev']+four, away+team['Abbrev']+four, home+team['Abbrev']+three, away+team['Abbrev']+three]
    #print(team)
    #print("\n")

h = teamlist[0]['ScheduleList']
x = teamlist[0]['SelfList']
w = str(teamlist[0]['Abbrev'])
my_item1 = (item['Abbrev'] for item in teamlist if item['ScheduleList'].count(x[0])>=1)
my_item2 = (item['Abbrev'] for item in teamlist if item['ScheduleList'].count(x[1])>=1)
my_item3 = (item['Abbrev'] for item in teamlist if item['ScheduleList'].count(x[2])>=1)
my_item4 = (item['Abbrev'] for item in teamlist if item['ScheduleList'].count(x[3])>=1)

wUnsched = []
for team in teamlist:
    xx = team['Abbrev']
    wUnsched.append(xx)

wSched = []

y = list(chain(my_item1, my_item2, my_item3, my_item4))

#print(len(y))

z = random.choice(y)


print(f"SELECTED TEAM: {z}")


# a = [d for i, d in enumerate(teamlist) if z in d['Abbrev']][0]
# a['ScheduleList']

print(w)

def findopposingteam(string, teamlist):
    a = [d for i, d in enumerate(teamlist) if string in d['Abbrev']][0]
    return a


def findmatchinggame(string, list):
    for x in list:
        if string in x:
            return x
        else:
            pass
    return None

def fliphomeaway(home, away, string, oppteam):
    if home in string:
        x = away
    else:
        x = home

    if four in string:
        return f"{x}{oppteam}{four}"
    else:
        return f"{x}{oppteam}{three}"

a = findopposingteam(z,teamlist)
oppgamestring = findmatchinggame(w, a['ScheduleList'])
teamgamestring = fliphomeaway(home, away, oppgamestring, a['Abbrev'])
print(oppgamestring)
print(teamgamestring)

t2index = a['ScheduleList'].index(oppgamestring)
t1index = h.index(teamgamestring)

team2 = a['ScheduleList'].pop(t2index)

team1 = h.pop(t1index)





print(team2)
print(team1)

print(a['ScheduleList'])
print(h)

print(wUnsched)
wUnsched.remove(z)
wUnsched.remove(w)
print(wUnsched)
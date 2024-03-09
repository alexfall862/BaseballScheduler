from ast import While
from itertools import chain
import random

def findteam(string, teamlist):
    a = [d for i, d in enumerate(teamlist) if string in d['Abbrev']][0]
    return a

def findmatchinggame(string, list):
    for x in list:
        if string in x:
            return x
        else:
            pass

def fliphomeaway(home, away, string, oppteam, mteam, four, three, weeklyg, weeklyremoval):
    if home in string:
        x = away
    else:
        x = home
    if four in string:
        y = f"{x}{oppteam}{four}"
        weeklyg.append({y, string})
    else:
        y = f"{x}{oppteam}{three}"
        weeklyg.append({y, string})        
    weeklyremoval.append({mteam: y})
    weeklyremoval.append({oppteam: string})
    z = {oppteam: string}
    zz = {mteam: y}
    return y, string

    
def FindAllOpponents(team, teamlist):
    team['SelfList']  
    my_item1 = (item['Abbrev'] for item in teamlist if item['ScheduleList'].count(team['SelfList'][0])>=1)
    my_item2 = (item['Abbrev'] for item in teamlist if item['ScheduleList'].count(team['SelfList'][1])>=1)
    my_item3 = (item['Abbrev'] for item in teamlist if item['ScheduleList'].count(team['SelfList'][2])>=1)
    my_item4 = (item['Abbrev'] for item in teamlist if item['ScheduleList'].count(team['SelfList'][3])>=1)
    y = list(chain(my_item1, my_item2, my_item3, my_item4))
    print(f"LIST OF TEAMS TO MATCH: {y}")
    return y

def PickOppTeam(t, teamlist, opponentlist, schedulelist):
    i=0
    
    while (i<=50):
        ot = random.choice(opponentlist)
        if ot in schedulelist:
            ti = schedulelist.remove(t)
            oti = schedulelist.remove(ot)
            return ot                 
            exit()
        else:
            i+=1
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
    return None

def fliphomeaway(home, away, string, oppteam, four, three, tlist, olist, weeklyg):
    if home in string:
        x = away
    else:
        x = home
    if four in string:
        y = f"{x}{oppteam}{four}"
        #print(f"RETURNING {y} for {string}")
        #print(tlist)
        tlist.remove(y)
        olist.remove(string)
        weeklyg.append({y, string})
    else:
        y = f"{x}{oppteam}{three}"
        #print(f"RETURNING {y} for {string}")
        tlist.remove(y)
        olist.remove(string)
        weeklyg.append({y, string})

    
def FindAllOpponents(team, teamlist):
    team['SelfList']  
    my_item1 = (item['Abbrev'] for item in teamlist if item['ScheduleList'].count(team['SelfList'][0])>=1)
    my_item2 = (item['Abbrev'] for item in teamlist if item['ScheduleList'].count(team['SelfList'][1])>=1)
    my_item3 = (item['Abbrev'] for item in teamlist if item['ScheduleList'].count(team['SelfList'][2])>=1)
    my_item4 = (item['Abbrev'] for item in teamlist if item['ScheduleList'].count(team['SelfList'][3])>=1)
    y = list(chain(my_item1, my_item2, my_item3, my_item4))
    return y

def PickOppTeam(t, teamlist, opponentlist, schedulelist):
    i=0
    #print(f"Options: {opponentlist}")
    #print(f"Sched: {schedulelist}")
    
    while (i<=150):
        ot = random.choice(opponentlist)
        print(f"OG Team: {t}")
        print(f"Ma Team: {ot}")
        if ot in schedulelist:
            ti = schedulelist.remove(t)
            oti = schedulelist.remove(ot)
            return ot                 
            exit()
        else:
            i+=1
            print(i)
            print("Didn't Find Team")
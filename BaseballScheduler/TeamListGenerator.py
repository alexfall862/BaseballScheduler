import csv

def FileParser(directory):
    x = FileUploader(directory)
    z = []
    for y in x:
        y['LDiv'] = y['League']+y['Division']
        z.append(y)
    return z

def FileUploader(directory):
    x = csv.DictReader(open(directory))
    return x

def MatchupGenerator(teamlist, rot, home, away, four, three, two):
    for team in teamlist:
        gameslist = []
        #Home 7 game division rotation (4,3)
        i = 0
        for iteam in teamlist:
            if team['LDiv'] == iteam['LDiv'] and not(team['Team'] == iteam['Team']):              
                i += 1
                if team['InterleagueRotation'] == 'A':
                    if i==1: 
                        gameslist.append(home+iteam['Abbrev']+four)
                        gameslist.append(away+iteam['Abbrev']+three)
                    elif i==2: 
                        gameslist.append(away+iteam['Abbrev']+four)
                        gameslist.append(home+iteam['Abbrev']+three)
                    elif i==3: 
                        gameslist.append(home+iteam['Abbrev']+four)
                        gameslist.append(away+iteam['Abbrev']+three)
                    elif i==4: 
                        gameslist.append(away+iteam['Abbrev']+four)
                        gameslist.append(home+iteam['Abbrev']+three)                                              
                elif team['InterleagueRotation'] == 'B': 
                    if i==1: 
                        gameslist.append(away+iteam['Abbrev']+four)
                        gameslist.append(home+iteam['Abbrev']+three)
                    elif i==2: 
                        gameslist.append(home+iteam['Abbrev']+four)
                        gameslist.append(away+iteam['Abbrev']+three)
                    elif i==3: 
                        gameslist.append(away+iteam['Abbrev']+four)
                        gameslist.append(home+iteam['Abbrev']+three)
                    elif i==4: 
                        gameslist.append(home+iteam['Abbrev']+four)
                        gameslist.append(away+iteam['Abbrev']+three)       
    
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
            
        #4 game rival (2, 2)
        for iteam in teamlist:
            if team['Abbrev'] == iteam['Rivals']:
                gameslist.append(home+iteam['Abbrev']+two)
                gameslist.append(away+iteam['Abbrev']+two)
        
        team['ScheduleList'] = gameslist
        team['SelfList'] = [home+team['Abbrev']+four, away+team['Abbrev']+four, home+team['Abbrev']+three, away+team['Abbrev']+three, home+team['Abbrev']+two, away+team['Abbrev']+two]
    return teamlist
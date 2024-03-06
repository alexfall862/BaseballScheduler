import pandas as pd
import json
import csv

directory = 'MLBTeams.csv'

primary_fields = ['Team', 'Abbrev', 'League', 'Division', 'Rivals', 'InterleagueRotation', 'IntraleagueRotation']

result = []

with open(directory) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        d = {k: v for k, v in row.items() if k in primary_fields}
        result.append(d)

#print(result)
result = pd.DataFrame(result)
#print(result)
print(result.groupby('Team'))
result = result.to_json(orient='records')
#print(result)

print(json.dumps(result))
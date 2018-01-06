import json

def writeLeaders(leaders):
    with open('leaderboard.txt','w') as outfile:
        json.dump(leaders, outfile)
    outfile.close()
        
def readLeaders():
    try:
        with open('leaderboard.txt') as file:
            data = json.load(file)
            file.close()
            return data
    except:
        try:
            file.close()
        except:
            pass
        return None
        
    
def updateLeaders(leaders):
    playerList = [leaders['players'][i]['name'] for i in range(len(leaders['players']))]
    data = readLeaders()
    if data is not None:
        for player in data['players']:
            if player['name'] in playerList:
                i = playerList.index(player['name'])
                player['kills']+=leaders['players'][i]['kills']
                player['deaths']+=leaders['players'][i]['death']
                player['loses']+=1 if not leaders['players'][i]['victor'] else 0
                player['wins']+=int(leaders['players'][i]['victor'])
                leaders['players'].pop(i)
                playerList.pop(i)
        for player in leaders['players']:
            data['players'].append({
                    "name":player['name'],
                    'kills':player['kills'],
                    'deaths':int(player['death']),
                    'wins':int(player['victor']),
                    'loses':1 if not leaders['players'][i]['victor'] else 0})
    else:
        data = {}
        data['players'] = []
        for player in leaders['players']:
            data['players'].append({
                "name":player['name'],
                'kills':player['kills'],
                'deaths':int(player['death']),
                'wins':int(player['victor']),
                'loses':1 if not player['victor'] else 0})
    writeLeaders(data)
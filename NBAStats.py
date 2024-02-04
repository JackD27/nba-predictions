import requests
import pandas as pd
from DK import DraftKingsWebsite


class NBAStatsClass:


    def __init__(self):
        self.DKClass = DraftKingsWebsite()
        pass

    def getNBAstats(self):
        nba_url = 'https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/statistics/byathlete?region=us&lang=en&contentorigin=espn&isqualified=true&page=1&limit=500&sort=offensive.avgPoints%3Adesc'
        response = requests.get(url=nba_url,).json()
        player_info = response['athletes']

        d = []
        for player_list in player_info:
            playerName = player_list['athlete']['displayName']
            mins = player_list['categories'][0]['totals'][1]
            pts = player_list['categories'][1]['totals'][0]        
            rebs = player_list['categories'][0]['totals'][11]
            asts = player_list['categories'][1]['totals'][10]
            playerInfo = {"Player": str(playerName), 
                "MPG": float(mins),
                "Points": float(pts), 
                "Rebounds": float(rebs), 
                "Assists": float(asts)
                }
            d.append(playerInfo)
        return pd.DataFrame(d)
    
    def merged_files(self):
        nbaStats = self.getNBAstats()
        nbaStats = nbaStats.melt(id_vars=["Player", "MPG"], 
            value_vars=["Points", "Rebounds", "Assists"], 
            var_name="Prop Name", 
            value_name="Stat")
        
        nbaStats['AvgPerMin'] = round((nbaStats['Stat'] / nbaStats['MPG']), 2)
        nbaStats['EstimatedLine'] = ""

        mergedFrame = nbaStats.merge(self.DKClass.get_dataframe(), on=['Player', 'Prop Name'])
        minsFrame = pd.read_csv('Mins.csv')
        minsFrame['Player'] = minsFrame['Player'].apply(lambda x: " ".join(x.split()[:2]))
        finalFrame = mergedFrame.merge(minsFrame, on=['Player'])
        finalFrame = finalFrame[['Player', 'MPG','Prop Name', 'Stat', 'AvgPerMin', 'Mins', 'EstimatedLine','Under', 'Line', 'Over']]
        finalFrame['EstimatedLine'] = round(finalFrame['Mins'] * finalFrame['AvgPerMin'], 2)
        finalFrame['Diff'] = round(finalFrame['EstimatedLine'] - finalFrame['Line'], 2)
        finalFrame.to_csv('FinalDataframe.csv', index=False)

lol = NBAStatsClass()
lol.merged_files()

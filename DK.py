import requests
import pandas as pd

class DraftKingsWebsite:
    def __init__(self):
        pass

    def parse_contest_info(self, response_info, categoryId):
        if categoryId == 1215:
            prop_name = "Points"
        elif categoryId == 1216:
            prop_name = "Rebounds"  
        elif categoryId == 1217:
            prop_name = "Assists"
        else:
            prop_name = "Unknown"

        contest_info = response_info['offerSubcategoryDescriptors'][0]['offerSubcategory']['offers']
        d = []
        for game in contest_info:
            for player in game:
                curr_label = " ".join(player['label'].split()[:2])
                curr_line = player['outcomes'][0]['line']        
                curr_over = player['outcomes'][0]['oddsAmerican']
                curr_under = player['outcomes'][1]['oddsAmerican']
                playerInfo = {"Player ": curr_label, 
                    "Prop Name": prop_name,
                    "Line": curr_line, 
                    "Over":curr_over, 
                    "Under": curr_under}
                d.append(playerInfo)
        return d

    def get_NBA_DKplayer_stats(self, categoryId): # categoryId 1215 for points | 1216 for rebounds | 1217 for assists
        website_url = f'https://sportsbook-nash-usma.draftkings.com/sites/US-MA-SB/api/v5/eventgroups/42648/categories/{categoryId}?format=json'
        response = requests.get(url=website_url).json()
        offerCategories = response['eventGroup']['offerCategories']
        for category in offerCategories:
            if category['offerCategoryId'] == categoryId:
                mainCategory = category
        
        return self.parse_contest_info(mainCategory, categoryId)   


    def get_dataframe(self):
        pointsDataframe = pd.DataFrame(self. get_NBA_DKplayer_stats(1215))
        reboundsDataframe = pd.DataFrame(self.get_NBA_DKplayer_stats(1216))
        assistsDataframe = pd.DataFrame(self.get_NBA_DKplayer_stats(1217))
        finalDataframe = pd.concat([pointsDataframe, reboundsDataframe, assistsDataframe])
        finalDataframe.to_csv('FinalDKDataframe.csv', index=False)

        
import requests
import pandas as pd

class DraftKingsWebsite:
    def __init__(self):
        pass

    def parse_contest_info(self, contest_info, prop_name):
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

    def get_NBA_player_points(self):
        website_url = 'https://sportsbook-nash-usma.draftkings.com/sites/US-MA-SB/api/v5/eventgroups/42648/categories/1215/subcategories/12488?format=json'
        response = requests.get(url=website_url).json()
        contest_info = response['eventGroup']['offerCategories'][3]['offerSubcategoryDescriptors'][0]['offerSubcategory']['offers']
        return self.parse_contest_info(contest_info, "Points")


    def get_NBA_player_rebounds(self):
        website_url = 'https://sportsbook-nash-usma.draftkings.com/sites/US-MA-SB/api/v5/eventgroups/42648/categories/1216?format=json'
        response = requests.get(url=website_url).json()
        contest_info = response['eventGroup']['offerCategories'][6]['offerSubcategoryDescriptors'][0]['offerSubcategory']['offers']
        return self.parse_contest_info(contest_info, "Rebounds")

    def get_NBA_player_assists(self):
        website_url = 'https://sportsbook-nash-usma.draftkings.com/sites/US-MA-SB/api/v5/eventgroups/42648/categories/1217?format=json'
        response = requests.get(url=website_url).json()
        contest_info = response['eventGroup']['offerCategories'][7]['offerSubcategoryDescriptors'][0]['offerSubcategory']['offers']
        return self.parse_contest_info(contest_info, "Assists")
    
    
if __name__ == "__main__":
    dk = DraftKingsWebsite()
    pointsDataframe = pd.DataFrame(dk.get_NBA_player_points())
    reboundsDataframe = pd.DataFrame(dk.get_NBA_player_rebounds())
    assistsDataframe = pd.DataFrame(dk.get_NBA_player_assists())
    finalDataframe = pd.concat([pointsDataframe, reboundsDataframe, assistsDataframe])
    finalDataframe.to_csv('FinalDKDataframe.csv', index=False)

        
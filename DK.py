import requests
import pandas as pd

def parse_contest_info(contest_info, prop_name):
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

def getNBAPlayerPoints():

    website_url = 'https://sportsbook-nash-usma.draftkings.com/sites/US-MA-SB/api/v5/eventgroups/42648/categories/1215/subcategories/12488?format=json'
    response = requests.get(url=website_url).json()

    contest_info = response['eventGroup']['offerCategories'][2]['offerSubcategoryDescriptors'][0]['offerSubcategory']['offers']

    return parse_contest_info(contest_info, "Points")


def getNBAPlayerRebounds():

    website_url = 'https://sportsbook-nash-usma.draftkings.com/sites/US-MA-SB/api/v5/eventgroups/42648/categories/1216?format=json'
    response = requests.get(url=website_url).json()

    contest_info = response['eventGroup']['offerCategories'][5]['offerSubcategoryDescriptors'][0]['offerSubcategory']['offers']
    
    return parse_contest_info(contest_info, "Rebounds")

def getNBAPlayerAssists():

    website_url = 'https://sportsbook-nash-usma.draftkings.com/sites/US-MA-SB/api/v5/eventgroups/42648/categories/1217?format=json'
    response = requests.get(url=website_url).json()

    contest_info = response['eventGroup']['offerCategories'][6]['offerSubcategoryDescriptors'][0]['offerSubcategory']['offers']
    
    return parse_contest_info(contest_info, "Assists")



pointsDataframe = pd.DataFrame(getNBAPlayerPoints())
reboundsDataframe = pd.DataFrame(getNBAPlayerRebounds())
assistsDataframe = pd.DataFrame(getNBAPlayerAssists())
finalDataframe = pd.concat([pointsDataframe, reboundsDataframe, assistsDataframe])
finalDataframe.to_csv('FinalDKDataframe.csv', index=False)

        
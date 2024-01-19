import requests
import pandas as pd

games = []


def parse_contest_info(contest_info, prop_name, ):
    for game in contest_info:
        for player in game:
            curr_label = " ".join(player['label'].split()[:2])
            curr_line = player['outcomes'][0]['line']        
            curr_over = player['outcomes'][0]['oddsAmerican']
            curr_under = player['outcomes'][1]['oddsAmerican']
            print("Player: " + curr_label + ", their " + prop_name +"'s line is set to: " + str(curr_line) + " with the Over odds as: " + curr_over +" and the Under odds as: " + curr_under)

def getNBAPlayerPoints():

    website_url = 'https://sportsbook-nash-usma.draftkings.com/sites/US-MA-SB/api/v5/eventgroups/42648/categories/1215/subcategories/12488?format=json'
    response = requests.get(url=website_url).json()

    contest_info = response['eventGroup']['offerCategories'][2]['offerSubcategoryDescriptors'][0]['offerSubcategory']['offers']

    parse_contest_info(contest_info, "points")

    # for game in contest_info:
    #     for player in game:
    #         curr_label = " ".join(player['label'].split()[:2])
    #         curr_line = player['outcomes'][0]['line']        
    #         curr_over = player['outcomes'][0]['oddsAmerican']
    #         curr_under = player['outcomes'][1]['oddsAmerican']
    #         print(f"For the player: " + curr_label + ", their point's line is set to: " + str(curr_line) + " with the Over odds as: " + curr_over +" and the Under odds as: " + curr_under)

def getNBAPlayerRebounds():

    website_url = 'https://sportsbook-nash-usma.draftkings.com/sites/US-MA-SB/api/v5/eventgroups/42648/categories/1216?format=json'

    response = requests.get(url=website_url).json()

    contest_info = response['eventGroup']['offerCategories'][5]['offerSubcategoryDescriptors'][0]['offerSubcategory']['offers']
    
    parse_contest_info(contest_info, "rebounds")

def getNBAPlayerAssists():

    website_url = 'https://sportsbook-nash-usma.draftkings.com/sites/US-MA-SB/api/v5/eventgroups/42648/categories/1217?format=json'

    response = requests.get(url=website_url).json()

    contest_info = response['eventGroup']['offerCategories'][6]['offerSubcategoryDescriptors'][0]['offerSubcategory']['offers']
    
    parse_contest_info(contest_info, "assists")
    assistDF = pd.DataFrame(contest_info)

getNBAPlayerPoints()
getNBAPlayerRebounds()
getNBAPlayerAssists()
        
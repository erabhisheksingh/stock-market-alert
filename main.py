'''
This script scrapes a website for the level of Sensex Stock Exchange,
tracks it and sends a notification on your phone via IFTTT webhooks
and if you plan on being annoying then can play You Suffer by Napalm Death
as a Desktop alert 
'''
import os
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from playsound import playsound

load_dotenv()

def track_markets():
    '''
    This script scrapes a website for the level of Sensex Stock Exchange,
    tracks it and sends a notification on your phone via IFTTT webhooks.It waits
    10 mins after sending notifications and then starts tracking the value again
    '''
    
    # Calling the website
    html_text = requests.get('https://www.moneycontrol.com/stocksmarketsindia/').text

    # Loading the response text for scraping
    soup = BeautifulSoup(html_text, 'lxml')

    market_info = soup.find('div', class_='marketatc_actcont')

    stats_table = market_info.find('table', class_='mctable1')

    table_row_stats = stats_table.find_all('tr')[2:3]

    sensex_level = table_row_stats[0].find_all('td')[1:2]

    # Finding the current level of Sensex
    sensex_current_level = sensex_level[0].text

    print(f'The current level of Sensex :- {sensex_current_level}')

    level_to_track = input('Please enter the level to track:- ')

    alert_name = os.getenv('ALERT_NAME')
    api_key = os.getenv('API_KEY')
    
    if float(level_to_track) > float(sensex_current_level):
        # The payload that will be sent to IFTTT service
        requests.post(f'https://maker.ifttt.com/trigger/{alert_name}/json/with/key/{api_key}')
        # Uncomment at your own risk
        playsound('Napalm_Death_You_Suffer.mp3')
        print('Alert!! Sensex is below your desired level. Start buying.....')
        time.sleep(600)
 

if __name__ == '__main__':
    
    while True:
        track_markets()
        time.sleep(300) 

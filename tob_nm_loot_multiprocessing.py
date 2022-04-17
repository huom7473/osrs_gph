#!/usr/bin/python3
# import bs4
# import cloudscraper
# from multiprocessing import Pool
import requests
from config import * # item data and whatnot

# def get_price(item):
#     '''
#     Gets GETracker price of item. Attempts to use Current Price, else average of offer and sell prices.
#     Returns a tuple of (name, price) for use in updating the prices dictionary.
#     '''
#     link = 'http://ge-tracker.com/item/' + item
#     scraper = cloudscraper.create_scraper()
#     soup = bs4.BeautifulSoup(scraper.get(link).text, 'lxml')
#     if price := int(soup.select('#item_stat_overall')[0].text.replace(',','')):
#             return (item, price)
#     else:
#         offer = int(soup.select('#item_stat_offer_price > span')[0].text.replace(',',''))
#         sell = int(soup.select('#item_stat_sell_price > span')[0].text.replace(',','')) 
#         return (item, round((offer + sell) / 2))

def fill_prices():
    "Fills the item prices dictionary with the RuneLite-powered GEtracker API."
    headers = { # spoof headers since API doesn't like generic bot ones
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    response = requests.get('https://prices.runescape.wiki/api/v1/osrs/latest', headers=headers)
    prices_dict = response.json()
    for iid in item_names:
        item_prices[id_to_legacy[iid]] = prices_dict["data"][iid]["low"] # use sell price, as this is more realistic
    
    
def show_price(item):
    'Prints item name and its price, then returns the price'
    item_price = item_prices[item]
    print(f'{item_names_legacy[item]}: {item_price:,}')
    return item_price
    
def main():
    'Displays price info and estimated profit/h for TOB/NM'
    
    # with Pool(len(item_prices)) as p:
    #     print('Grabbing prices...')
    #     # loop through item names and update dictionary data
    #     for name, price in p.imap_unordered(get_price, item_prices):
    #         item_prices[name] = price

    fill_prices()
    
    show_price('elysian-spirit-shield')
    
    print("\nCurrent TOB Prices:")
    tob_avg = 0
    for item in tob_items:
        tob_avg += show_price(item) * tob_items[item] / TOB_WEIGHT_DENO
    tob_avg *= TOB_DROP_CHANCE # average loot from uniques per raid

    nm_armor_avg = 0
    nm_orb_avg = 0
    
    print('\nCurrent Nightmare Prices:')
    for item in nightmare_armor:
        price = show_price(item)
        nm_armor_avg += price * nightmare_armor[item] / NIGHTMARE_ARMOR_DENO
        
    nm_armor_avg *= NIGHTMARE_ARMOR_CHANCE
    for item in nightmare_orbs:
        nm_orb_avg += show_price(item) * nightmare_orbs[item] / NIGHTMARE_ORBS_DENO
    nm_orb_avg *= NIGHTMARE_ORB_CHANCE

    cox_avg = 0 # GP per point, not per kill
    print('\nCurrent COX Prices:')
    for item in cox_items:
        cox_avg += show_price(item) * cox_items[item] / COX_WEIGHT_DENO
    cox_avg /= COX_PTS_PER_ITEM

    print('\nLoot From Uniques:')
    print(f'\nTOB/kill: {round(tob_avg):,}')
    print(f'TOB/hr/person (assuming {TOB_KPH} kph and trio): {round(tob_avg * TOB_KPH/3):,}')
    print(f'\nCOX/pt: {round(cox_avg, 2)}')
    print(f'COX/hr/person (assuming {COX_PTS_PER_HOUR} pts/hour/person): {round(cox_avg * COX_PTS_PER_HOUR):,}')
    print(f"\nPhosani's/kill: {round(nm_armor_avg + nm_orb_avg):,}")
    print(f"Phosani's/hr/person (assuming {NIGHTMARE_KPH} kph): "
          f'{round((nm_armor_avg + nm_orb_avg)*NIGHTMARE_KPH):,}')
    

if __name__ == '__main__':
    main()
    input()

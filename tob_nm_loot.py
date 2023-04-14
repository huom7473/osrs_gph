#!/usr/bin/python3
# import bs4
# import cloudscraper
# from multiprocessing import Pool
import requests
from config import * # item data and whatnot
from util import *

def fill_prices():
    "Fills a global item prices dictionary with the RuneLite-powered OSRS Wiki API."
    global item_prices
    item_prices = dict()
    
    headers = { # spoof headers since API doesn't like generic bot ones
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    response = requests.get('https://prices.runescape.wiki/api/v1/osrs/latest', headers=headers)
    prices_dict = response.json()
    
    for iid in ITEM_LIST:
        item_prices[iid] = prices_dict["data"][iid]["low"] # use sell price, as this is more realistic
    
    
def show_price(iid):
    """
    Prints item name and its price (before GE tax) given its IID, then returns the sell price (after GE tax).

    If repair/augments are available (e.g. repairing torva platebody damaged) as indicated in
    config.py's ITEM_UPGRADE in the form {IID: (New_IID, ((Ingredient_IID, Quantity), ...)), ...}
    they will be taken into account and noted in the output.
    """
    
    item_price = item_prices[iid]

    if iid in ITEM_UPGRADES:
        upgraded_price = item_prices[ITEM_UPGRADES[iid][0]]

        for component_iid, qty in ITEM_UPGRADES[iid][1]:
            upgraded_price -= item_prices[component_iid] * qty

        if upgraded_price > item_price: # if the upgraded price isn't better, fall through to default behavior
            print(f'{ITEM_LIST[iid]}: {upgraded_price:,} (upgrade to {ITEM_LIST[ITEM_UPGRADES[iid][0]]})')
            return upgraded_price - min(5_000_000, upgraded_price / 100) 

    print(f'{ITEM_LIST[iid]}: {item_price:,}')
    return item_price - min(5_000_000, item_price / 100)

def main():
    'Displays price info and estimated profit/h for TOB/NM/COX/Nex'
    
    fill_prices()
    
    show_price('12817') # elysian spirit shield
    
    print("\nCurrent TOB Prices:")
    tob_avg = 0
    for item in TOB_ITEMS:
        tob_avg += show_price(item) * TOB_ITEMS[item] / TOB_WEIGHT_DENO
    tob_avg *= TOB_DROP_CHANCE # average loot from uniques per raid

    nm_armor_avg = 0
    nm_orb_avg = 0
    
    print('\nCurrent Nightmare Prices:')
    for item in NIGHTMARE_ARMOR:
        nm_armor_avg += show_price(item) * NIGHTMARE_ARMOR[item] / NIGHTMARE_ARMOR_DENO  
    nm_armor_avg *= NIGHTMARE_ARMOR_CHANCE
    
    for item in NIGHTMARE_ORBS:
        nm_orb_avg += show_price(item) * NIGHTMARE_ORBS[item] / NIGHTMARE_ORBS_DENO
    nm_orb_avg *= NIGHTMARE_ORB_CHANCE

    cox_avg = 0 # GP per point, not per kill
    print('\nCurrent COX Prices:')
    for item in COX_ITEMS:
        cox_avg += show_price(item) * COX_ITEMS[item] / COX_WEIGHT_DENO
    cox_avg /= COX_PTS_PER_ITEM

    nex_avg = 0
    print('\nCurrent Nex Prices:')
    for item in NEX_ITEMS:
        nex_avg += show_price(item) * NEX_ITEMS[item] / NEX_WEIGHT_DENO
    nex_avg *= NEX_DROP_CHANCE

    toa_avg = 0
    print('\nCurrent TOA Prices:')
    for item in TOA_ITEMS:
        toa_avg += show_price(item) * TOA_ITEMS[item] / TOA_WEIGHT_DENO
    
    print('\nLoot From Uniques:')

    print(f'\nNex/kill: {round(nex_avg):,}')
    print(f'Nex/hr/person ({NEX_KPH} kph and duo): {round(nex_avg * NEX_KPH / 2):,}')
    print(f'Nex/hr/person (5.5 kph and duo): {round(nex_avg * 5.5 / 2):,}')
    print(f'Nex/hr/person (7 kph and 2+1, 45-55): {round(nex_avg * 7 * 0.45):,}-{round(nex_avg * 7 * 0.55):,}')
    
    print(f'\nTOB/kill: {round(tob_avg):,}')
    print(f'TOB/hr/person (assuming {TOB_KPH} kph and trio): {round(tob_avg * TOB_KPH / 3):,}')
    
    print(f'\nCOX/pt: {round(cox_avg, 2)}')
    print(f'COX/hr/person (assuming {COX_PTS_PER_HOUR} pts/hour/person): {round(cox_avg * COX_PTS_PER_HOUR):,}')
    
    print(f"\nPhosani's/kill: {round(nm_armor_avg + nm_orb_avg):,}")
    print(f"Phosani's/hr/person (assuming {NIGHTMARE_KPH} kph): "
          f'{round((nm_armor_avg + nm_orb_avg)*NIGHTMARE_KPH):,}')

    print(f'\nTOA Average Unique: {round(toa_avg):,}')
    print(f'TOA/Solo Expert (25.7k pts, 400): {round(toa_avg * toa_uc(400, 25700)):,}')
    print(f'@ 2 kph: {round(toa_avg * toa_uc(400, 25700)) * 2:,}')
    print(f'TOA/4 man Expert (75.5k pts, 400): {round(toa_avg * toa_uc(400, 75500) / 4):,}')
    print(f'@ 2.6 kph: (75.5k pts, 400): {round(toa_avg * toa_uc(400, 75500) / 4 * 2.6):,}')


if __name__ == '__main__':
    main()
    input()

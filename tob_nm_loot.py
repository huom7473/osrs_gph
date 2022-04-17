#!/usr/bin/python3
import bs4
import cloudscraper

tob_items = {
    'scythe-of-vitur-uncharged': 1, # getracker link, weight (out of 19)
    'ghrazi-rapier': 2,
    'sanguinesti-staff-uncharged': 2,
    'justiciar-faceguard': 2,
    'justiciar-chestguard': 2,
    'justiciar-legguards': 2,
    'avernic-defender-hilt': 8
}
nightmare_armor = {
    'nightmare-staff': 3, #weight out of 10
    'inquisitor-s-great-helm': 2,
    'inquisitor-s-hauberk': 2,
    'inquisitor-s-plateskirt': 2,
    'inquisitor-s-mace': 1
}
nightmare_orbs = {
    'eldritch-orb': 1, #weight out of 3
    'harmonised-orb': 1,
    'volatile-orb': 1
}
item_names = { # store better formatted item names
    'scythe-of-vitur-uncharged': 'Scythe of Vitur',
    'ghrazi-rapier': 'Ghrazi Rapier',
    'sanguinesti-staff-uncharged': 'Sanguinesti Staff',
    'justiciar-faceguard': 'Justiciar Faceguard',
    'justiciar-chestguard': 'Justiciar Chestguard',
    'justiciar-legguards': 'Justiciar Legguards',
    'avernic-defender-hilt': 'Avernic Defender Hilt',
    'nightmare-staff': 'Nightmare Staff',
    'inquisitor-s-great-helm': "Inquisitor's Great Helm",
    'inquisitor-s-hauberk': "Inquisitor's Hauberk",
    'inquisitor-s-plateskirt': "Inquisitor's Plateskirt",
    'inquisitor-s-mace': "Inquisitor's Mace",
    'eldritch-orb': 'Eldritch Orb',
    'harmonised-orb': 'Harmonised Orb',
    'volatile-orb': 'Volatile Orb',
    'twisted-bow': 'Twisted Bow'
}
TOB_WEIGHT_DENO = sum(tob_items.values())
NIGHTMARE_ARMOR_DENO = sum(nightmare_armor.values())
NIGHTMARE_ORBS_DENO = sum(nightmare_orbs.values())
NIGHTMARE_ARMOR_CHANCE = 1/120
NIGHTMARE_ORB_CHANCE = 1/600
TOB_DROP_CHANCE = 0.10665 # uses average of 0.5 deaths per raid
NIGHTMARE_KPH = 8.5
TOB_KPH = 2.7

def get_price(item):
    'Gets GETracker price of item. Attempts to use Current Price, else average of offer and sell prices'
    link = 'http://ge-tracker.com/item/' + item
    scraper = cloudscraper.create_scraper()
    soup = bs4.BeautifulSoup(scraper.get(link).text, 'lxml')
    if price := int(soup.select('#item_stat_overall')[0].text.replace(',','')):
            return price
    else:
        offer = int(soup.select('#item_stat_offer_price > span')[0].text.replace(',',''))
        sell = int(soup.select('#item_stat_sell_price > span')[0].text.replace(',','')) 
        return round((offer + sell) / 2)

def show_price(item):
    'Prints item name and its price, then returns the price'
    item_price = get_price(item)
    print(f'{item_names[item]}: {item_price:,}')
    return item_price
    
def main():
    'Displays price info and estimated profit/h for TOB/NM'
    show_price('twisted-bow')
    
    print("\nCurrent TOB Prices:")
    tob_avg = 0
    for item in tob_items:
        tob_avg += show_price(item) * tob_items[item] / TOB_WEIGHT_DENO
    tob_avg *= TOB_DROP_CHANCE # average loot from uniques per raid

    nm_armor_avg = 0
    nm_orb_avg = 0
    
    nm_inq_total = 0 # personal use
    nm_inq_purchased = 862000000
    
    print('\nCurrent Nightmare Prices:')
    for item in nightmare_armor:
        price = show_price(item)
        nm_armor_avg += price * nightmare_armor[item] / NIGHTMARE_ARMOR_DENO
        if nightmare_armor[item] == 2: # if the weight is two, i.e. it's an armor piece
            nm_inq_total += price
    nm_armor_avg *= NIGHTMARE_ARMOR_CHANCE
    for item in nightmare_orbs:
        nm_orb_avg += show_price(item) * nightmare_orbs[item] / NIGHTMARE_ORBS_DENO
    nm_orb_avg *= NIGHTMARE_ORB_CHANCE

    print(f"\nInquisitor's Set Value Gain: {nm_inq_total - nm_inq_purchased:,}")
    print('\nLoot From Uniques:')
    print(f'\nNightmare/kill: {round(nm_armor_avg + nm_orb_avg):,}')
    print(f'Nightmare/hr/person (assuming {NIGHTMARE_KPH} kph and trio): '
          f'{round((nm_armor_avg + nm_orb_avg)*NIGHTMARE_KPH/3):,}')
    print(f'\nTOB/kill: {round(tob_avg):,}')
    print(f'TOB/hr/person (assuming {TOB_KPH} kph and trio): {round(tob_avg * TOB_KPH/3):,}')

if __name__ == '__main__':
    main()
    input()

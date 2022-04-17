tob_items = {
    'scythe-of-vitur-uncharged': 1, # getracker link, weight (out of 19)
    'ghrazi-rapier': 2,
    'sanguinesti-staff-uncharged': 2,
    'justiciar-faceguard': 2,
    'justiciar-chestguard': 2,
    'justiciar-legguards': 2,
    'avernic-defender-hilt': 8
}
cox_items = {
    'dexterous-prayer-scroll': 20,
    'arcane-prayer-scroll': 20,
    'twisted-buckler': 4,
    'dragon-hunter-crossbow': 4,
    'dinh-s-bulwark': 3,
    'ancestral-hat': 3,
    'ancestral-robe-top': 3,
    'ancestral-robe-bottom': 3,
    'dragon-claws': 3,
    'elder-maul': 2,
    'kodai-insignia': 2,
    'twisted-bow': 2
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
item_names = { # item ID (string) to item name (for Runelite/Wiki API)
    '22486': 'Scythe of Vitur',
    '22324': 'Ghrazi Rapier',
    '22481': 'Sanguinesti Staff',
    '22326': 'Justiciar Faceguard',
    '22327': 'Justiciar Chestguard',
    '22328': 'Justiciar Legguards',
    '22477': 'Avernic Defender Hilt',
    '24422': 'Nightmare Staff',
    '24419': "Inquisitor's Great Helm",
    '24420': "Inquisitor's Hauberk",
    '24421': "Inquisitor's Plateskirt",
    '24417': "Inquisitor's Mace",
    '24517': 'Eldritch Orb',
    '24511': 'Harmonised Orb',
    '24514': 'Volatile Orb',
    '20997': 'Twisted Bow',
    '12817': 'Elysian Spirit Shield',
    '21034': 'Dexterous Prayer Scroll',
    '21079': 'Arcane Prayer Scroll',
    '21000': 'Twisted Buckler',
    '21012': 'Dragon Hunter Crossbow',
    '21015': "Dinh's Bulwark",
    '21018': 'Ancestral Hat',
    '21021': 'Ancestral Robe Top',
    '21024': 'Ancestral Robe Bottom',
    '13652': 'Dragon Claws',
    '21003': 'Elder Maul',
    '21043': 'Kodai Insignia'
}
item_names_legacy = { # store better formatted item names (for GEtracker and code work reasons)
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
    'twisted-bow': 'Twisted Bow',
    'elysian-spirit-shield': 'Elysian Spirit Shield',
    'dexterous-prayer-scroll': 'Dexterous Prayer Scroll',
    'arcane-prayer-scroll': 'Arcane Prayer Scroll',
    'twisted-buckler': 'Twisted Buckler',
    'dragon-hunter-crossbow': 'Dragon Hunter Crossbow',
    'dinh-s-bulwark': "Dinh's Bulwark",
    'ancestral-hat': 'Ancestral Hat',
    'ancestral-robe-top': 'Ancestral Robe Top',
    'ancestral-robe-bottom': 'Ancestral Robe Bottom',
    'dragon-claws': 'Dragon Claws',
    'elder-maul': 'Elder Maul',
    'kodai-insignia': 'Kodai Insignia',
}
id_to_legacy = dict(zip(item_names.keys(), item_names_legacy.keys()))
item_prices = dict(item_names_legacy) # copy this for the names/ids, we'll replace the names with prices later

TOB_WEIGHT_DENO = sum(tob_items.values())
NIGHTMARE_ARMOR_DENO = sum(nightmare_armor.values())
COX_WEIGHT_DENO = sum(cox_items.values())
NIGHTMARE_ORBS_DENO = sum(nightmare_orbs.values())
NIGHTMARE_ARMOR_CHANCE = 1/192 # 1/120
NIGHTMARE_ORB_CHANCE = 1/960 # 1/600
TOB_DROP_CHANCE = 0.10665 # uses average of 0.5 deaths per raid
NIGHTMARE_KPH = 7
TOB_KPH = 2.7
COX_PTS_PER_ITEM = 867600
COX_PTS_PER_HOUR = 70000

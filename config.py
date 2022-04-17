# items dictionaries store id to relative weight
TOB_ITEMS = {
    '22486': 1,
    '22324': 2,
    '22481': 2,
    '22326': 2,
    '22327': 2,
    '22328': 2,
    '22477': 8,
}

COX_ITEMS = {
    '21034': 20,
    '21079': 20,
    '21000': 4,
    '21012': 4,
    '21015': 3,
    '21018': 3,
    '21021': 3,
    '21024': 3,
    '13652': 3,
    '21003': 2,
    '21043': 2,
    '20997': 2,
}

NIGHTMARE_ARMOR = {
    '24422': 3,
    '24419': 2,
    '24420': 2,
    '24421': 2,
    '24417': 1,
}

NIGHTMARE_ORBS = {
    '24517': 1,
    '24511': 1,
    '24514': 1,
}

NEX_ITEMS = {
    '26235': 3,
    '26372': 2,
    '26376': 2,
    '26378': 2,
    '26380': 2,
    '26370': 1,
}

ITEM_LIST = { # item ID (string) to item name (for Runelite/Wiki API)
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
    '21043': 'Kodai Insignia',
    '26235': 'Zaryte Vambraces',
    '26372': 'Nihil Horn',
    '26374': 'Zaryte Crossbow',
    '26376': 'Torva Full Helm (damaged)',
    '26382': 'Torva Full Helm',
    '26378': 'Torva Platebody (damaged)',
    '26384': 'Torva Platebody',
    '26380': 'Torva Platelegs (damaged)',
    '26386': 'Torva Platelegs',
    '26370': 'Ancient Hilt',
    '26233': 'Ancient Godsword',
    '26394': 'Bandosian Components',
    '11798': 'Godsword Blade',
    '11785': 'Armadyl Crossbow',
    '26231': 'Nihil Shard',
}

ITEM_UPGRADES = {
    '26372': ('26374', (('11785', 1), ('26231', 250))), # nihil horn -> zaryte crossbow
    '26376': ('26382', (('26394', 1),)), # torva full helm (damaged) -> torva full helm
    '26378': ('26384', (('26394', 2),)), # torva platebody (damaged) -> torva platebody
    '26380': ('26386', (('26394', 2),)), # torva platelegs (damaged) -> torva platelegs
    '26370': ('26233', (('11798', 1),)), # ancient hilt -> ancient godsword
}

TOB_WEIGHT_DENO = sum(TOB_ITEMS.values())
TOB_DROP_CHANCE = 0.10665 # uses average of 0.5 deaths per raid
TOB_KPH = 2.7 # trio

COX_WEIGHT_DENO = sum(COX_ITEMS.values())
COX_PTS_PER_ITEM = 867600
COX_PTS_PER_HOUR = 70000

NIGHTMARE_ARMOR_DENO = sum(NIGHTMARE_ARMOR.values())
NIGHTMARE_ORBS_DENO = sum(NIGHTMARE_ORBS.values())
NIGHTMARE_ARMOR_CHANCE = 1/192
NIGHTMARE_ORB_CHANCE = 1/960
NIGHTMARE_KPH = 7

NEX_WEIGHT_DENO = sum(NEX_ITEMS.values())
NEX_DROP_CHANCE = 1/43
NEX_KPH = 5.3 # duo

essentials = {'backpack': ['laptop', 'mouse', 'charger', 'adapter', 'speaker'],
              'cash': 300,
              'wallet': ['coins', 'cards'], 'pocket': ['earphones', 'golds']}

#adding new key
essentials['cash'] = essentials['cash'] + 1200

#sorting key values
essentials['wallet'].sort()
essentials['backpack'].sort()

#removing key valuea
essentials['backpack'].remove('adapter')

print(essentials)
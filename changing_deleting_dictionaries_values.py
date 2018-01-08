animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

del animals['Sloth']
del animals['Unicorn']
del animals['Atlantic Puffin']

animals['Bengal Tiger'] = 'Random Forests'

print(animals)
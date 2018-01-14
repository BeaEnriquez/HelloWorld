planets = ['earth', 'venus', 'mars', 'jupiter', 'saturn']

for p in planets: 
  if p == 'jupiter': 
    print ("Eyy that's the fifth planet out from the sun!")
    break
else: 
  print (", ".join(planets), "Are the planets from our Solar System")
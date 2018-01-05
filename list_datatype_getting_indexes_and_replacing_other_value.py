planets = ["mars", 'jupiter', 'saturn', 'venus', 'earth']
saturn_index = planets.index('saturn')

planets.insert(saturn_index, "pluto")
print(planets)
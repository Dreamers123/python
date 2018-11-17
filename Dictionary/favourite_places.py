
places=[]
favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'ever': ['mt. verstovia', 'the playground', 'south carolina']
    }
places.append(favorite_places)


favorite_places = {
    'Abeer': ['USA', 'SPAIN', 'ITALY'],
    'Lisa': ['Swizerlan', 'Canada'],
    'Cornea': ['Australia', 'England', 'USA']
    }
places.append(favorite_places)

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())
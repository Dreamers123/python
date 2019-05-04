def build_album(name,artist,**info):
    album={}
    album['Album Name']=name.title()
    album['Artist Name']=artist.title()
    for key,value in info.items():
        album[key]=value
    return album
name_prompt="\nWhat the name of the Album?"
artist_prompt="What The artist name of the album?"
track_prompt="What is the title?"
track_number="What is the track number?"
print("Enter 'quit' at any time to stop.")
while True:
    name=input(name_prompt)
    if name=='quit':
        break
    artist=input(artist_prompt)
    if artist=='quit':
        break
    track_name=input(track_prompt)
    if track_name=='quit':
        break
    track_number=input(track_number)
    if track_number=='quit':
        break
    user_album=build_album(name,artist,Track_Name=track_name,Track_number=track_number)
    print(user_album)
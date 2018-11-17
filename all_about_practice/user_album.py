def make_album(artist, title, **tracks):
   album_dic =  { 'artist': artist.title(),
       'title':title.title()
        }
   for key,value in tracks.items():
       album_dic[key]=value;
   return album_dic;
# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "
tracks_prompt="track number? "
name_prompt="track name? "
# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break


    key= input(name_prompt)
    tracks = input(tracks_prompt)
    if tracks == 'quit':
        break

    album = make_album(artist,title,name=key,track_number=tracks)
    print(album)

print("\nThanks for responding!")
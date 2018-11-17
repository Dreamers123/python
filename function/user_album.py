def make_album(artist, title, tracks):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }

    if tracks:
     album_dict['tracks'] = tracks
    return album_dict

# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "
tracks_prompt="track number? "
# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    tracks = input(tracks_prompt)
    if tracks == 'quit':
        break
    album = make_album(artist, title, tracks)
    print(album)

print("\nThanks for responding!")
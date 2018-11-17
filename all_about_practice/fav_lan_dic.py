favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("\n")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle','jen']

for coder in coders:
    if coder in favorite_languages.keys():
        print("Yhank you "+coder.title()+ " for taking the poll")
    else:
        print("Hey "+coder.title()+" be a poll member")

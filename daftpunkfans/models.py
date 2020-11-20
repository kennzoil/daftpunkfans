discovery = [
    'One More Time',
    'Aerodynamic',
    'Digital Love',
    'Harder, Better, Faster, Stronger',
    'Crescendolls',
    'Nightvision',
    'Superheroes',
    'High Life',
    'Something About Us',
    'Voyager',
    'Veridis Quo',
    'Short Circuit',
    'Face To Face',
    'Too Long'
]


def name_favorite():
    """asks user to name their favorite Discovery song and responds"""

    # assign 'Digital Love' as the computer's favorite song
    favorite_song = discovery[2]

    # ask user what their favorite Daft Punk song from Discovery is
    print("What's your favorite song from Discovery?")

    # store user response in a variable
    users_favorite_song = input().title()

    # initialize variable to false
    song_is_in_discovery = False

    # check each song in discovery to see if it matches users song
    for song in discovery:

        # if the current song being looped over matches users song:
        if song == users_favorite_song:
            # reassign this variable to True
            song_is_in_discovery = True

    # now song_is_in_discovery will tell us if it is in discovery or not

    if song_is_in_discovery:
        if users_favorite_song == favorite_song:
            print("Hey, that's my favorite song from Discovery too! You're pretty cool!")
        else:
            print("Oh yeah, that's a good one!")
    else:
        print("Uh, I don't think that's on Discovery. Do you even listen to Daft Punk, bro?")
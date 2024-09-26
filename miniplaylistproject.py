print("\033c")

#playlist project

username = input("Hello! Please make a username: ")
password = input("Please make a password: ")

print("Welcome! Please sign-in with your new credentials below")

#signin

while True:
    signinusername = input("Please enter your username: ")
    signinpassword = input("Please enter your password: ")

    if signinusername != username:
        print("That username is incorrect, please try again.")
    elif signinpassword != password:
        print("The password is incorrect, please try again.")
    else:
        print("\nYour credentials are correct, signing in...\n")
        break
print("Welcome!\n")

##options to either make a New Playlist, or just go to their Liked Songs.

options = ['Create a new playlist +', 'Go to liked songs']
liked_songs = {}
like_menu = ['Add new likes', 'View liked songs', 'Return to menu']

while True:    
    for index, value in enumerate(options, 1):
        print(index, value)
    options_choice = input("\nPlease choose one of the options from the list (using the number): ")
    
    if not options_choice.isdigit() or int(options_choice) not in [1,2]:
        print("\nError. Not an option; please try again. \n")
        continue
    
    options_choice = int(options_choice)
    
    if options_choice == 1:
        playlist_name = input("\nWelcome to your new playlist! Add a name if wanted: \n")
        options.append(playlist_name)
    else:
        while True:
            for index, value in enumerate(like_menu, 1):
                print(index,value)
            like_menu_choice = input("\nPlease choose one of the options from the list (1-3): ")
            
            if not like_menu_choice.isdigit() or int(like_menu_choice) not in [1,2,3]:
                print("\nError. Not an option; please try again. \n")
                continue

            like_menu_choice = int(like_menu_choice)

            if like_menu_choice == 1:
                artist = input("What is the name of the artist? ")
                song =  input("What is the song title? ")
                if artist in liked_songs:
                    liked_songs[artist].append(song)
                else:
                    liked_songs[artist] = [song]
                print("\nLiked new song.\n")    
            elif like_menu_choice == 2:
                print(f"\nHere are your liked songs: {liked_songs}\n")
            elif like_menu_choice == 3:
                break

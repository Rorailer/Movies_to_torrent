#!/usr/bin/env python3

# Import necessary modules and functions
from MyModules import *
import time


# Entry point of the script
if __name__ == '__main__':
    # Start an infinite loop for user interaction
    while True:
        clear_screen()  # Clear the screen at the beginning of each loop iteration
        
        # Display the main menu options
        print('''What would you like to do?
1. Search for a movie
2. List running Torrents
3. Exit''')
        
        # Get user input for the main menu choice
        first_choice = input('Enter choice: ')
        
        # Check the user's choice and perform corresponding actions
        if first_choice == '1':  # User wants to search for a movie
            clear_screen()  # Clear the screen for a cleaner interface
            
            # Call the list_movies() function to search for movies and get a formatted list
            table, Movies_list = list_movies()
            
            # Check if there are movies available in the list
            if Movies_list != None:
                # Display the list of movies to the user
                print(Movies_list)
                
                # Ask the user for further actions on the movie list
                print('''What do you want to do?
1. Get details of a Movie.
2. Download a Movie.
3. Go Back.''')
                while True:
                    choice = input("Enter Choice index: ")
                    if choice == '1' or choice == '2' or choice == '3':
                        break
                    else:
                        print("Invalid choice! Try again.")
                        
                if choice == '1':  # User wants to get details of a movie
                   clear_screen()  # Clear the screen for a cleaner interface

                   print(Movies_list)  # Display the movie list again for reference

                   # Ask the user to select a movie for details
                   selection = input("Enter index of movie to get details: ")

                   imdb_id = table[int(selection)]  # Get the IMDb ID of the selected movie
                   
                   clear_screen()  # Clear the screen for a cleaner interface
                   
                   # Call the movie_details() function to fetch and display details of the selected movie
                   movie_details(imdb_id)

                   _ = input("Press Enter to continue...")  # Wait for user input to continue
                  
                elif choice == '2':  # User wants to download a movie
                    clear_screen()  # Clear the screen for a cleaner interface

                    print(Movies_list)  # Display the movie list again for reference

                    # Ask the user to select a movie for download
                    selection = input("Enter index of movie to download: ") 

                    print("Starting Download! Please wait.")

                    # Call functions to download and manage the movie torrent
                    info = search_by_id(table[int(selection)])
                    url = torrent_url(info)
                    name = info[0]['Title']
                    name = name_cleanup(name) + '.torrent'
                    torrent_file(url, name )
                    clear_screen()
                    qbittorrent(name)
                    subprocess.run('rm ~/Downloads/Torrents/' + name, shell=True)

                    print("Download Started!")
                    time.sleep(2)  # Add a delay for better user experience

                elif choice == '3':  # User wants to go back to the main menu
                    pass  # Do nothing and continue the loop

            elif Movies_list == None:  # No movies found in the list
                print("No Movies!")
                time.sleep(1)  # Add a short delay for better user experience
                clear_screen()  # Clear the screen for a cleaner interface

        elif first_choice == '2':  # User wants to list running torrents
            pass  # Functionality for listing torrents is not yet implemented

        elif first_choice == '3':  # User wants to exit the program
            print("Good Bye!")  # Display a farewell message
            time.sleep(2)  # Add a delay before exiting
            clear_screen()  # Clear the screen for a cleaner exit
            break  # Exit the infinite loop and end the program

        else:  # Invalid input from the user
            print("Invalid Input! Please try again.")
            time.sleep(2)  # Add a delay for better user experience

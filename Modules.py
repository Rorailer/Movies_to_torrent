#!/usr/bin/env python
import requests
import subprocess
import re
import qbittorrentapi
import os


base = 'https://yts.mx/api/v2/'
list_url = 'list_movies.json'
query = 'query_term='

connection_info = dict(host='127.0.0.1',
                       port='8080',
                       username='user',
                       password='password')
qb = qbittorrentapi.Client(**connection_info, VERIFY_WEBUI_CERTIFICATE=False)

try:
    qb.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)




# Function to clear the terminal screen based on the operating system
def clear_screen():
    if os.name == 'nt':  # Check if the operating system is Windows
        _ = os.system('cls')  # Clear the screen using 'cls' command
    else:
        _ = os.system('clear')  # Clear the screen using 'clear' command





def name_cleanup(input_string):
    # Define a regular expression pattern to match special characters and spaces
    pattern = r'[^a-zA-Z0-9]'

    # Use re.sub() to replace the matched pattern with an empty string
    result = re.sub(pattern, '', input_string)

    return result

def print_bold(text):
    bold_text = f"\033[1m{text}\033[0m"
    print(bold_text, end='')

def search():
    user_input = input("Enter search term: ")

    response = requests.get(f"{base}{list_url}?quality=1080p&{query}{user_input}")

    response = response.json()
    movie_count = response['data']['movie_count']

    if int(movie_count) != 0:
        names = [{"Title":movie['title_english'],'Year':movie['year'],'id':movie['imdb_code'],'torrents':movie['torrents']    }
                for movie in response['data']['movies']]
    
    
    #If results are less than 20
        if int(int(movie_count)/20) == 0:
        
            pass
            
        else:    
            for i in range(int(int(movie_count)/20)):

                more_response = requests.get(f"{base}{list_url}?{query}{user_input}&page={i+2}")

                more_response = more_response.json()

                more_names = [{"Title":movie['title_english'],'Year':movie['year'], 'id':movie['imdb_code'],'torrents':movie['torrents']}
                              for movie in more_response['data']['movies']]

                unique_ids = set(item["id"] for item in names)

                unique_names = [item for item in more_names if item['id'] not in unique_ids]

                names = names + unique_names

            
        return names, user_input
    
    elif int(movie_count) == 0:
        return 'No Results', None 
            
def list_movies():
    names, user_input = search()
    if user_input != None:
        print(f"Term  : {user_input}")
        table = {}
        Movies_list = ''
        j=1
        for _,dictionary in enumerate(names):
            if str(dictionary['Year']) != user_input:
                table[j] = dictionary['id']
                Movies_list += f"{j}. {dictionary['Title']}\n Year: {dictionary['Year']}\n" 
                j=j+1            
        
        return table , Movies_list
    
    
    else:
        return names, None

def movie_details(imdb_id):
    info = search_by_id(imdb_id)
    
    #Print Title in BOLD
    print_bold(info[0]['Title'])
    print('')
    
    #Print Year
    print_bold('Year: ')
    print(info[0]['Year'])
    
    #Print Rating
    print_bold('Rating: ')
    print(info[0]['Rating'])
    
    #Print Genre
    print_bold('Genre: ')
    for i in info[0]['Genre']:
        print(f'| {i} | ', end=' ')
    print('\n\n')
    
    #Print Summary
    print_bold('Summary;')
    print(f"\n{info[0]['Summary']}")
    
    
def torrent_file(url,name):
    command = 'curl -o '
    subprocess.run(command + '~/Downloads/Torrents/' +name +' '+ url , shell=True)
    
    
def torrent_url(info):
    torrents = info[0]['torrents']
    HD = [torrent for torrent in torrents if torrent['quality'] == '1080p']
    url = HD[0]['url']
    return url

       

def search_by_id(imdb_id):
    
    response = requests.get(f"{base}{list_url}?{query}{imdb_id}")

    response = response.json()

    info = [{"Title":movie['title_english'],'Year':movie['year'],'id':movie['imdb_code'],'torrents':movie['torrents'], 'Rating': movie['rating'], 'Genre': movie['genres'],
             'Summary': movie['summary'], 'Runtime': movie['runtime'], 'Language': movie['language']}
             for movie in response['data']['movies']]
    
    return info

def qbittorrent(file_name):
    
    qb.torrents_add(torrent_files='~/Downloads/Torrents/' + file_name)
    










if __name__ == '__main__':
    
    table = list_movies()
    # print(table)
    
    selection = input("Enter index of movie to download: ") 
   
   
    

    info = search_by_id(table[int(selection)])
    
    url = torrent_url(info)
    
    name = info[0]['Title']
    
    
    name = name_cleanup(name) + '.torrent'
    
    torrent_file(url, name )
    
    qbittorrent(name)
    
    subprocess.run('rm ~/Downloads/Torrents/' + name, shell=True)
    
    
    
''''''    

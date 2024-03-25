import requests
import subprocess
import re
import qbittorrentapi


base = 'https://yts.mx/api/v2/'
list_url = 'list_movies.json'
query = 'query_term='

connection_info = dict(host='127.0.0.1',
                       port='8080',
                       username='admin',
                       password='password')
qb = qbittorrentapi.Client(**connection_info, VERIFY_WEBUI_CERTIFICATE=False)

try:
    qb.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)







def name_cleanup(input_string):
    # Define a regular expression pattern to match special characters and spaces
    pattern = r'[^a-zA-Z0-9]'

    # Use re.sub() to replace the matched pattern with an empty string
    result = re.sub(pattern, '', input_string)

    return result


def search():
    user_input = input("Enter search term: ")

    response = requests.get(f"{base}{list_url}?quality=1080p&{query}{user_input}")

    response = response.json()

    names = [{"Title":movie['title_english'],'Year':movie['year'],'id':movie['imdb_code'],'torrents':movie['torrents']    }
             for movie in response['data']['movies']]
    
    movie_count = response['data']['movie_count']
    
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
            
            
def list_movies():
    names, user_input = search()
    print(f"Term  : {user_input}")
    table = {}
    j=1
    for _,dictionary in enumerate(names):
        if str(dictionary['Year']) != user_input:
            table[j] = dictionary['id']
            print(f"{j}. {dictionary['Title']}\n   Year: {dictionary['Year']}\n")
            j=j+1            
    return table



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

    info = [{"Title":movie['title_english'],'Year':movie['year'],'id':movie['imdb_code'],'torrents':movie['torrents']    }
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

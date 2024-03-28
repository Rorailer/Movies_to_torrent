#!/usr/bin/env python3

from Modules import *


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
    

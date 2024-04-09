# Movies_to_torrent
A simple program that searches for movies using YTS API , downloads its .torrent file and then automatically starts to download it using qbittorrent web ui.
---
# DON'T USE THIS
This program has very confusing code. I had zero idea going into this program on how to propperly order and reuse my code.
I have created a new repo https://github.com/Rorailer/xyz use this instead
---
## Replace user and password
In Modules.py replace 'user' and 'password' with the username and password of your qbittorrent webui.

Got it! Here's the updated README.md content with your GitHub username and repository name:

---

## rename.py
rename.py is an additional file that you may or may not need. This file cleans up the name of the folder and files within that folder and moves it to your desired location. For example:
'300 Rise of an Empire (2014) [1080p]' This turns into '300 Rise of an Empire (2014)' and 
'300.Rise.of.an.Empire.2014.1080p.BluRay.x264.YIFY.mp4' This turns into '300 Rise of an Empire.mp4'

This file is useful if you are using a media server which requires naming to be pretty precise.

---

## What is Where

### MyModules.py

1. **Dependencies**: The script requires the following dependencies:
   - Python 3.x
   - Requests module (`requests`) ! You'll have to install this (I Think) using pip
    `pip install requests`
   - Subprocess module (`subprocess`) ! You'll have to install this usig pip.
   - Regular Expression module (`re`)
   - qBittorrent API (`qbittorrentapi`) ! You'll have to install this too (Its module name is qbittorrent-api not qbittorrentapi)
   - Operating System module (`os`)

2. **Functionality**:
   - **Clear Screen**: `clear_screen()` function clears the terminal screen based on the operating system.
   - **Name Cleanup**: `name_cleanup(input_string)` function cleans up special characters from a given string.
   - **Bold Text**: `print_bold(text)` function prints text in bold format in the terminal.
   - **Search**: `search()` function sends a search request to the YTS API and retrieves movie data based on user input.
   - **List Movies**: `list_movies()` function lists movies based on search results and user input.
   - **Movie Details**: `movie_details(imdb_id)` function fetches and displays details of a selected movie using its IMDb ID.
   - **Torrent File**: `torrent_file(url, name)` function downloads a torrent file using its URL.
   - **Torrent URL**: `torrent_url(info)` function retrieves the torrent URL for a movie.
   - **Search by ID**: `search_by_id(imdb_id)` function searches for a movie by IMDb ID and fetches its details.
   - **qBittorrent**: `qbittorrent(file_name)` function adds a torrent file to qBittorrent for downloading.

### main.py

1. **Dependencies**: The script requires `MyModules.py` and the specified dependencies in `MyModules.py` to function properly.

2. **Usage**:
   - The script provides a menu-driven interface to search for movies, view details, and download torrents.
   - Users can select options like searching for a movie, getting details, downloading a movie, and listing running torrents (not yet implemented).
   - The program utilizes functions from `MyModules.py` for movie search, details fetching, and torrent management.

## How It Works

### YTS API
API = 'http://yts.mx/api/v2' and to list movies you add 'list_movies.json'
### Searching

The program sends a request to the API with the user's query and retrieves a JSON file containing all movies that match the search words. It extracts some of the information from the JSON file, such as the name, rating, year, description, and most importantly, the IMDb ID. The names of the movies are then displayed to the user alongside the year of release for better identification of the required movie. A dictionary is created alongside the display, which uses the index value displayed to the user as the 'key' and the IMDb ID of the movie as its value.

### Data Manipulation

When the user has selected the movie to download, the program extracts the IMDb ID of the movie and sends a request to the API to get the data of the selected movie using the IMDb ID. This time, the program grabs all the same information it grabbed before, but it also fetches the download link for the '.torrent' file of 1080p resolution. This .torrent file is then downloaded and renamed to the movie name for easier use.

## qBittorrent Api module

Now comes the turn of the qBittorrent API. The program gives the path to the '.torrent' file to the API, which adds the movie torrent to the client and starts the download. The program then deletes the now-useless '.torrent' file.


## How to Use It

1. Clone the repository:
   ```bash
   git clone https://github.com/RoRailer/Movies_to_torrent.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Movies_to_torrent
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Make sure you have a BitTorrent client installed on your system (e.g., qBittorrent).

5. Execute the `main.py` script:
   ```bash
   ./moviesapi/bin/python3 main.py
   ```

6. Follow the on-screen instructions to search for movies, get details, and download torrents.

## Contributors

- [RoRailer](https://github.com/RoRailer)

---

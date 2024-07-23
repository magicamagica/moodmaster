# 🎵 Mood Master 🎵

Mood Master is a Python application that interacts with the Spotify API to recommend songs based on your current mood. The application also provides features to analyze the mood of your saved tracks and add songs to your Spotify queue. This is a simple hobbyist Python application that uses api calls to get track IDs from Spotify and recognize whether they're happy or sad by analysing the valence value Spotify returns. Made with Spotipy, the Spotify api and a simple tkinter GUI.


## Requirements

- Python 3.x
- Spotify Developer Dashboard
- Spotipy

## Features

- **Mood Selection**: Choose your mood (Happy or Sad) and get song recommendations tailored to your mood.
- **Track ID and Audio Feature Retrieval**: Retrieve and save track IDs and their audio features from your Spotify account.
- **Mood Analysis**: Calculate the percentage of happy and sad songs from your saved tracks.
- **Queue Management**: Add a specified number of random songs matching your mood to your Spotify queue.


## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/magicamagica/moodmaster.git
    cd moodmaster
    ```

3. **Set up your Spotify API credentials**:
    - Go to the `config.py` file in the root directory of the project.
    - Add your Spotify API credentials (if you don't have this or are not sure where to get it please check out [this link by spotify](https://developer.spotify.com/documentation/web-api/concepts/apps)).
      ```python
      SPOTIFY_CLIENT_ID = 'your_client_id'
      SPOTIFY_CLIENT_SECRET = 'your_client_secret'
      SPOTIFY_REDIRECT_URI = 'your_redirect_uri'
      ```

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Interact with the GUI**:
    - Retrieve and save track IDs and audio features by clicking the "Get Track IDs and Audio Features" button. (This might take a minute depending on how many tracks you have liked!)
    - Select your mood.
    - Click "Recommend me a song!" while you have an active spotify device.
    - Calculate the mood percentage of your songs by clicking the "Calculate Song Mood Percentage" button.
    - Add random songs to your queue by entering the number of songs (1-10) and clicking the "Add to Queue" button.

## Dependencies

- `spotipy`

## Contributing

Contributions are welcome! Please create a new branch and open a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [Spotipy Library](https://spotipy.readthedocs.io/)

## Contact

- **Author**: Dimitris S.
- **GitHub**: [magicamagica](https://github.com/magicamagica)

---

_Fun Fact: This project used to contain Julia code for analysis but it was replaced with python code for simplicity and consistency reasons_

_“Where words fail, music speaks.” – Hans Christian Andersen_

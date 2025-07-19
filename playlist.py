class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"✅ '{song}' added to the playlist!")

    def show(self):
        if not self.songs:
            print("🎶 Your playlist is empty.")
        else:
            print("🎶 Your Playlist:")
            for index, song in enumerate(self.songs, start=1):
                print(f"{index}.{song}")

class Music():

    def __init__(self, performer, song, album, year):
        self.performer = performer 
        self.song = song 
        self.album = album 
        self.year = year

    def __str__(self):
        return f"Performer: {self.performer}\nSong: {self.song}\nAlbum: {self.album}\nYear: {self.year}"

muzyka = Music("Ed Sheeran","Hearts Don't Break Around Here","Divide","2017")
muzyka1 = Music("The Score","Unstoppable","Atlas","2017")
muzyka2 = Music("Imagine Dragons","Radioactive","Night Visions","2012")
print(muzyka)
print()
print(muzyka1)
print()
print(muzyka2)
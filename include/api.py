from pytube import YouTube
from pytube.cli import on_progress



class Yt():
    def __init__(self, l):
        self.Search_Movie = YouTube(l, on_progress_callback=on_progress)
        
    def ShowNameMovie(self):
        return self.Search_Movie.title
    def DownloadMovie(self):
        download = self.Search_Movie.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first().download()
        
        
if __name__ =='__main__':
    link = input('>')
    print (Yt(link).ShowNameMovie())
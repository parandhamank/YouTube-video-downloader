from pytube.cli import on_progress
import pytube
import sys
import os
#-------------------------------------------------------------------------------
def remove_punc(string):
    for i in ['/', '\\', ':', '*', '?', '"', '<', '>', '|', ',']:
        string = string.replace(i, '')
    return string
#-------------------------------------------------------------------------------
def main():
    p = pytube.Playlist(sys.argv[1])
    i = int(sys.argv[2])
    print('----------------------------------------------------------------------')
    print('Pandhu - YouTube Downloader')
    print('----------------------------------------------------------------------')
    video_urls = list(p.video_urls)
    for url in video_urls[int(sys.argv[2]):]:
        title = ''
        try:
            yt = pytube.YouTube(url, on_progress_callback=on_progress)
            title = remove_punc(yt.title)
            yt.streams.filter(file_extension='mp4').get_highest_resolution().download()
        except EOFError as err:
            print(err)
        print('\n')
        try:
            os.rename(f'{title}.mp4', f'{i}. {title}.mp4')
        except:
            print(f'Error : {title}.mp4', f'{i}. {title}.mp4')
        print(f'{i}. {title}.mp4 Downloaded succesfully')
        print('----------------------------------------------------------------------')
        i = i + 1
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------
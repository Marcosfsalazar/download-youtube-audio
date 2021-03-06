import pafy

DOWNLOAD_FOLDER = './downloads'

print('Enter video Link:')
rawLink = input()

url = str(rawLink)
video = pafy.new(url)
audiostreams = video.audiostreams

for i in audiostreams:
    print('bitrate: %s, ext: %s, size: %0.2fMb' %
          (i.bitrate, i.extension, i.get_filesize()/1024/1024))
    if i.extension == "m4a" and i.bitrate != '0k':
        i.download(filepath=DOWNLOAD_FOLDER)

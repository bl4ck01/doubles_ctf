#ffmpeg -i file.mkv -map 0:s:0 subs.srt

dat = open('subs.srt', 'r').read().split('\n')

flag = ''
for i in range(2, len(dat), 4):
    flag += dat[i]

print flag


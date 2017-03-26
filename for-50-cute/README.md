## Solve
- 실행을 시키면 중간중간에 자막같은것이 보인다.

```
ffmpeg -i file.mkv -map 0:s:0 subs.srt
```
- 명령어를 통해 자막을 추출한 뒤, 적당히 자른 뒤, 간단한 코드를 짜서 읽었다.

```python
dat = open('subs.srt', 'r').read().split('\n')

flag = ''
for i in range(2, len(dat), 4):
    flag += dat[i]

print flag
```

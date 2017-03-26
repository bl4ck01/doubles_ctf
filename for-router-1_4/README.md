# Solve
- 문제에서 iptime 펌웨어 파일을 주는데 **binwalk -Me file** 명령어를 이용해 파일시스템을 추출한다.</br>
그리고 난 뒤, 공유기 파일시스템 내에서 문제에서 제시하는 답을 찾으면 된다.

### 1. 계정정보
- /default/etc/iconfig.cfg 에 계정정보가 적혀있다.

![1](https://github.com/st1tch/doubles_ctf/blob/master/for-router-1_4/1.png)

### 2. C&C 서버 정보
- 네이버에 접속했을 때, 다른 피싱사이트로 이동 한다고 했으니, 호스트파일 변조 등을 원인으로 생각할 수 있다.
```
grep -rn "dns"
```
명령어를 통해 C&C 서버의 주소를 알아낼 수 있었다.

![2](https://github.com/st1tch/doubles_ctf/blob/master/for-router-1_4/2.png)

### 3. 수상한 포트 조사
- 수상한 포트가 열려 있다고 해서, 서비스를 조사 해 보았다.
**/default/etc/services** 경로를 보면 수상한 포트에 서비스가 등록되어 있다.

![3](https://github.com/st1tch/doubles_ctf/blob/master/for-router-1_4/3.png)

### 4. 수상한 페이지 원인 분석
- 펌웨어의 버전이 9.984인 것을 알기 때문에, iptime홈페이지에서 원본 펌웨어를 다운받았다. 그리고 디핑을 통해 **/home/httpd/js/wirelesswizard.js** 에 숨겨진 플래그가 있는 것을 확인하였다.

![4](https://github.com/st1tch/doubles_ctf/blob/master/for-router-1_4/4.png)

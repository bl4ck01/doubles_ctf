## Solve
```
hui awavmiis hqklse mx o gvslfr tn zrqecuhcef ecdmiwihvg ysrk ac lgnvb e grvnsm fe mehjzrsjrr hoyjzv twupzvg oexsx fm xys qmoxsew tt u bdcncwl. dx wf e kcld nj gcqgvpduegsnzb wlpxbdxigmtb. zczk zg mmgpc_imlshvqi
```

- 암호문을 살펴보고 우선 첫 hui는 the라고 예상을 했다.</br>
그리고 뒤쪽의 zczk zg는 flag is라고 예상을 했다.

- 위 예상대로면 f -> z, i -> z 이기 때문에, 비제네르 암호라고 예상을 했다.

- hui가 the가 되려면 key가 one이 되야하고, zczkzg가 flagis가 되려면 urzero가 되야한다.</br>
즉, one??urzero???? 이런식이 되야하는데 대회이름이 DoubleS1405 인게 생각이나서 key에 onefourzerofive를 입력하니 정상적으로 flag가 출력이 됬다.



## Result
```
-- MESSAGE w/Key #1 = 'onefourzerofive' ----------------
the vigenere cipher is a method of encrypting alphabetic text by using a series of interwoven caesar ciphers based on the letters of a keyword. it is a form of polyalphabetic substitution. flag is hello_vigenere
```

## Solve
- 온라인 디컴파일러를 이용해서 바이너리를 디컴파일하면 c코드로 보여준다.</br>

```c
int main(int argc, char ** argv) {
    int32_t v1; // bp-240
    v1 = &v1;
    int32_t v2;
    memcpy((char *)&v2, (char *)L"flagis_MY_TRAP_CARD", 80);
    int32_t v3;
    memcpy((char *)&v3, (char *)&g1, 80);
    puts("Welcome");
    printf("password: ");
    int32_t str;
    scanf("%s", &str);
    int32_t str2;
    int32_t v4 = &str2; // 0x100006f8_0
    // branch -> 0x100006b4
    for (int32_t i = 0; i < 20; i++) {
        // 0x100006b4
        int32_t v5;
        int32_t v6 = 4 * i + (int32_t)&v5; // 0x100006c0
        int32_t v7 = *(int32_t *)(v6 - 204); // 0x100006c8
        int32_t v8 = *(int32_t *)(v6 - 124); // 0x100006e4
        *(char *)(i + v4) = (char)(v8 ^ v7);
        // continue -> 0x100006b4
    }
    // 0x10000720
    if (strcmp((char *)&str, (char *)&str2) == 0) {
        // 0x10000740
        puts("Success!");
        // branch -> 0x1000075c
    } else {
        // 0x10000750
        puts("Fail!");
        // branch -> 0x1000075c
    }
    // 0x1000075c
    return 0;
}
```

- c코드를 보면 flag가 20자리인 것을 알 수 있고, ida를 통해 확인해 보면 "flagis_MY_TRAP_CARD" 문자열과 바로 뒤에 있는 hex값들이 xor 되는것을 확인 할 수 있다.

- 따라서 ida에서 해당 데이터들을 복사해서 xor해주는 코드를 작성하면 flag가 출력된다.

## Result
```
~/machome/ctf/doubles_ctf/rev-100-exec(master*) » python solve.py                                    stitch@certis
Y0u_le4rned_pow3rpc
```

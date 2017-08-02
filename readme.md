
* 生成使用命令
```
$touch 1.cpp
$cpp -dM 1.cpp 
```

or

```
gcc -dM -E - </dev/null
```

* predef macros https://sourceforge.net/p/predef/wiki/OperatingSystems/


目前代码中使用宏区分：

mac  __APPLE__

mips __mips__

arm64 __aarch64__
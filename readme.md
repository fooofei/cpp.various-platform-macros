
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


### In Cpp 目前代码中使用宏区分：
```
mac  __APPLE__ or __MACH__

mips __mips__

arm64 __aarch64__
```
### In makefile 
```
TARGETNAME = $(shell $(CC) -dumpmachine)
ARCH = $(word 1, $(subst -, , $(TARGETNAME)))
PLATFORM = $(word 3, $(subst -, , $(TARGETNAME)))

ifeq ($(ARCH),mipsel)
	# found 
else
	# not found
endif

ifneq (,$(findstring darwin, $(PLATFORM)))
	# found
else
	# not found
#endif

```


### 去符号

```
strip --strip-unneeded libxxx.so

or 

objcopy -S libxxx.so

这两种方法生成的 binary 二进制一样，md5 相同

去符号之前可以使用命令 

objcopy --only-keep-debug libxxx.so libxxx.so.dbg

把符号保存下来，说是为了调试的时候使用，但是实践并不实用。

```
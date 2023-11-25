# 使用说明

## MPOE2One.py

`MPOE2One.py` 用于将一个 .MPO 文件转换为两个左右jpg和一个合成的jpg
命令格式如下
```
{your path}/MPOE2One.py DSCF2170.MPO
```

## mpo2pic.sh

`mpo2pic.sh` 脚本用于将一个文件夹下所有的 .MPO 文件转换为合成的jpg
使用方法如下
1. 设置环境变量 `$MPOE="{your path}/MPOE2One.py"` 并启用
2. 运行脚本

```
{your path}/mpo2pic.sh {your path}/mpo_test
```

或

```
cd {your path}/mpo_test
{your path}/mpo2pic.sh $PWD
```

# Usage

## MPOE2One.py

`MPOE2One.py` is used to convert a .MPO file into two left and right jpgs and a synthesized jpg
The command format is as follows
```
{your path}/MPOE2One.py DSCF2170.MPO
```

## mpo2pic.sh

`mpo2pic.sh` script is used to convert all .MPO files in a folder into synthesized jpgs
The usage is as follows
1. Set the environment variable `$MPOE="{your path}/MPOE2One.py"` and enable it
2. Run the script

```
{your path}/mpo2pic.sh {your path}/mpo_test
```

or

```
cd {your path}/mpo_test
{your path}/mpo2pic.sh $PWD
```
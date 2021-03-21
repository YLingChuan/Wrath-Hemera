### Wrath Hemera - a vulnerability scanner that supports customization

> Wrath Hemera is a highly customized vulnerability scanner.All RCE vulnerabilities can be scanned.（Soon, we will develop a program for Linux/Windows local vulnerability privilege escalation.）

[中文](https://github.com/JustYoomoon/Wrath-Hemera/blob/main/README_zh.md)



#### Installation

The operating system must have python3/Python2 and Java environment（It depends on the POC）.
For other questions, please read the [Wiki](https://github.com/JustYoomoon/Wrath-Hemera/wiki).

```bash
git clone https://github.com/JustYoomoon/Wrath-Hemera.git

pip3 install -r requirements.txt

sudo python3 hemera.py --help
```



#### Usage

You must run the program under ROOT.

```
sudo python3 hemera.py [option]

#Set the target address:
$ sudo python3 hemera.py -t 127.0.0.1
#or
$ sudo python3 hemera.py -t https://www.google.com
#We recommend that your target is an IP address.
```

View all available modules:

```bash
$ sudo python3 hemera.py --allmodules
```

![](https://ftp.bmp.ovh/imgs/2021/03/e00502bcc8679aa2.jpg)

#### video demo







#### Examples

Test whether the target has solr related vulnerabilities:

```bash
$ sudo python3 hemera.py -t 127.0.0.1

$ sudo python3 hemera.py --module solr

```

Automatically scan :

```bash
$ sudo python3 hemera.py -t 127.0.0.1

$ sudo python3 hemera.py --autoscan
```

Clear cache:

```bash
$ sudo python3 hemera.py --clean
```


#### Thanks

[exphub](https://github.com/zhzyker/exphub)



#### License

MIT License.


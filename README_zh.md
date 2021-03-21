### Wrath Hemera - 高度自定義的漏洞掃描程序
>Wrath Hemera是一個高度定制的漏洞掃描程序，可以掃描所有RCE漏洞。（不久後，我們將開發一個用於Linux/Windows本地漏洞特權提升的程序。）

#### 安裝
操作系統必須具有python3/Python2和Java環境（取決於POC）。
如有其他疑問，請閱讀[Wiki](https://github.com/JustYoomoon/Wrath-Hemera/wiki)。

```bash
git clone https://github.com/JustYoomoon/Wrath-Hemera.git

pip3 install -r requirements.txt

sudo python3 hemera.py --help
```

#### 使用
該程序必須在ROOT下運行。


```
sudo python3 hemera.py [option]

#Set the target address:
$ sudo python3 hemera.py -t 127.0.0.1
#或者
$ sudo python3 hemera.py -t https://www.google.com
#我們推薦目標是IP地址，存在CDN的域名可能導致程序崩潰。
```

### 查看所有可用模塊：
```bash
$ sudo python3 hemera.py --allmodules
```

![](https://ftp.bmp.ovh/imgs/2021/03/e00502bcc8679aa2.jpg)


#### 視頻演示


#### 舉例

驗證目標127.0.0.1是否存在Solr相關的漏洞：

```bash
$ sudo python3 hemera.py -t 127.0.0.1

$ sudo python3 hemera.py --module solr

```

自動掃描：

```bash
$ sudo python3 hemera.py -t 127.0.0.1

$ sudo python3 hemera.py --autoscan
```

清理緩存：

```bash
$ sudo python3 hemera.py --clean
```


#### 感謝

[exphub](https://github.com/zhzyker/exphub)



#### 許可證

MIT License.

### Telegram群組
https://t.me/zhpentest

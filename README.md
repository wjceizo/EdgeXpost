# 发送Events给EdgeX的python脚本

这是一个python脚本，是为了更方便的向EdgeX发送events。  
测试脚本采用python=3.9.7版本，EdgeX采用[jakarta版本的docker-compose-no-secty-with-app-sample](https://github.com/edgexfoundry/edgex-compose/blob/jakarta/docker-compose-no-secty-with-app-sample.yml)。  
1.首先安装requirements.txt中的python依赖。  
2.test.csv提供了脚本配置文件的样例。脚本会根据配置文件中的时间(time)依次发送events，由于发送给EdgeX用时约为2s，所以event之间间隔尽量大于2s，如小于2s，脚本会依次发送接近同时的event，然后继续按照指定时间继续依次发送events。    
3.本脚本可以指定配置文件和host_ip，-i来选择配置文件，-o来指定host_ip,运行脚本是在终端中运行 `python .\postcsvevents.py -i test.csv -o localhost:59880`  (默认的csv为当前目录下test.csv，默认的ip_host为localhost:59880)。  
4.终端返回第一行为发送event的时间，第二行返回发送结果。  
5.json版本不建议使用。
### 终端运行图片  
![post.PNG](https://s2.loli.net/2022/02/05/o6nZ4afscdmOr7v.png)



## pip3 install --upgrade pip

pip3 install pluginbase
pip3 install schedule
pip3 install requests
pip3 install bs4
pip3 install user_agent

## 使用 pm2 启动

/home/liyang/.nvm/versions/node/v11.9.0/bin/pm2 start /home/liyang/beehive/main.py --interpreter python3
/home/liyang/.nvm/versions/node/v11.9.0/bin/pm2 startup
/home/liyang/.nvm/versions/node/v11.9.0/bin/pm2 save

## 设置开机启动

vi /etc/rc.d/rc.local 
/home/liyang/.nvm/versions/node/v11.9.0/bin/pm2 startup
/home/liyang/.nvm/versions/node/v11.9.0/bin/pm2 save

## 部署时python的编码问题
vi /etc/locale.conf

```

## LANG=C
LANG="en_US.UTF-8"

```


vim /etc/environment

```

LC_ALL=en_US.UTF-8
LANG=en_US.UTF-8

```

## 安装node环境

```

nvm git地址点击打开链接，安装命令

curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

source ~/.bashrc

nvm --version

nvm ls-remote  查看node所有版本

通过 nvm install <version>(版本号) 例如：nvm install v10.6.0

node -v ,npm -v 查看版本

```
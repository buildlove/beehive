# Python 插件式的信息爬虫

>  🐝 一群不辞劳苦采花小蜜蜂

本项目运行在可以运行在本地或者服务器端，将不同插件程序获取的信息如：每日天气、新闻等，通过 Github Api 上传到仓库进行保存。当然，你还可以你日常机械重复性的劳动在插件中帮你完成，比如煮咖啡、发邮件等等，真是棒极了。

> **额外收获** ：定期稳定运行在服务器上，还可以每日贡献一次 Github 贡献度 ... 点亮你的人生！

## 工程说明
```
├── app
│   └── plugins
│       └── weather.py
├── builtin_plugins
├── config
│   └── config.json
├── main.py
└── upload_github.py

```

- `main.py` : 加载 `builtin_plugins/` 和 `app/` 下的插件；
- `app/plugins/` : 插件程序存放路径；
- `builtin_plugins` ： 内置插件路径；
- `upload_github.py` : 通过 Github Api 提交一次 Commit；

## 使用步骤

- 生成 Github Token 

- 运行代码
    ```bash
    python main.py
    ```


## 插件接口 Json 格式

可以自己补充插件，各个插件的返回值为字典类型，必须满足如下格式

```json
{
  "code": 0,
  "type": "weather",
  "date": "2018-04-23 20:18:03",
  "content": {
    "city": "\u6df1\u5733", "weather": "\u591a\u4e91", "temperature": "21 ~ 26\u2103", "humidity": "\u6e7f\u5ea6\uff1a63%", "wind": "\u98ce\u5411\uff1a\u5317\u98ce 2\u7ea7", "radiation": "\u7d2b\u5916\u7ebf\uff1a\u5f31", "air": "PM: 43"
  }
}
```

**参数说明**

- `code`: `0` 成功、`-1` 失败；
- `type`: 例如 [`weather`, `stock`, `news`] 等；
- `date`: 当天日期，如 `2018-05-01`；
- `content`: 获取的 Json 格式信息，这部分提交到仓库保存；


## Todo
- [x] Python 插件化信息管理，可拓展；
- [x] 信息保存到 Github 仓库；
- [ ] 更多插件补充；
- [ ] Docker 一键部署到本地或服务器；

- [ ] 信息可视化
    - [ ] Pyeacharts 网页显示
    - [ ] Gitpage 静态页面每日渲染

- [ ] Itchat 微信推送
    - [ ] 自动登录
    - [ ] 自动推送
    - [ ] 信息查询
 
- [ ] 补充插件内容
    - [ ] 插件思路收集
    - [ ] **大新闻**日常备份
    - [ ] 商品价格记录插件
# ImNotSpider浏览器User Agent生成器

## demo
Python3.5下测试通过
```python
from ImNotSpider import ImNotSpider as imsp
ins = imsp.ImNotSpider()
#随机
ua = ins.random()
ua = ins.pc()
ua = ins.wap()
ua = ins.pc_linux()
ua = ins.pc_windows()
ua = ins.pc_mac()
ua = ins.internet_explorer()#Windows PC
ua = ins.chrome_pc()
ua = ins.chrome_pc_linux()
ua = ins.chrome_pc_mac()
ua = ins.chrome_pc_windows()
ua = ins.firefox_pc()
ua = ins.firefox_pc_linux()
ua = ins.firefox_pc_mac()
ua = ins.firefox_pc_windows()
ua = ins.android()
ua = ins.iphone()
ua = ins.chrome_wap()
ua = ins.chrome_wap_android()
ua = ins.chrome_wap_iphone()
ua = ins.wechat()
ua = ins.wechat_android()
ua = ins.wechat_iphone()
ua = ins.uc_browser_android() #UC浏览器
ua = ins.baidu_box_app() #手机百度
ua = ins.baidu_box_app_android()
ua = ins.baidu_box_app_iphone()
```

### 其他语言（Java、PHP等）

使用[https://github.com/lbp0200/ImNotSpiderWebAPI](https://github.com/lbp0200/ImNotSpiderWebAPI)，搭建一个Web接口，调用Web接口即可

## 安装
```bash
pip install git+https://github.com/lbp0200/ImNotSpiderWebAPI.git
```

## 爬虫经验分享
很多网站判断爬虫，一般用IP+UserAgent。本项目主要解决UserAgent问题，但是个别变态（low）的
网站使用IP来判断，这样会有一个很大的问题。比如二级运行商（长城宽带、方正宽带、宽带通）或者移动
都是使用NAT网络，说白了，就是整个帝都长城宽带就是一个超级局域网，访问某个网站都是同一个IP，
这就给爬虫留下机会，比如把爬虫通过长城宽带来抓内容，难不成网站要把整个帝都长城宽带都封掉？有资源
的朋友可以分享下经验。

动态IP的常见解决方案：
#### ADSL拨号
淘宝有很多这样的服务器售卖
#### 代理IP
有免费和付费的，免费的不够稳定，原理很简单，到发布免费代理的网站抓，然后测试或在使用时扔掉失败次数超过N的。
付费的也不少，搜索“代理IP API”，一大把，没有推荐，因为我也没用过。
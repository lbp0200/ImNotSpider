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

使用https://github.com/lbp0200/ImNotSpiderWebAPI，搭建一个Web接口，调用Web接口即可

## 安装
```bash
pip install git+https://github.com/lbp0200/ImNotSpiderWebAPI.git
```
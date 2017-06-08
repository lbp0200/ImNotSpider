import random as rd


def rand_android():
    return '{0}.{1}.{2}'.format(rd.randint(4, 7), rd.randint(0, 9), rd.randint(0, 9))


def rand_apple_webkit():
    return '{0}.{1}'.format(rd.randint(100, 999), rd.randint(0, 99))


def rand_chrome():
    return '{0}.{1}.{2}.{3}'.format(rd.randint(20, 59), rd.randint(0, 9), rd.randint(1000, 9999), rd.randint(10, 99))


def rand_safari():
    return '{0}.{1}'.format(rd.randint(100, 999), rd.randint(0, 99))


class ImNotSpider:
    def random(self):
        pass

    def pc(self):
        pass

    def wap(self):
        pass

    def pc_linux(self):
        pass

    def pc_windows(self):
        pass

    def pc_mac(self):
        pass

    def android(self):
        pass

    def iphone(self):
        pass

    def windows_phone(self):
        pass

    def wechat(self):
        # Mozilla/5.0 (Linux; Android 7.1.2; Z2 Plus Build/N2G47O; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN
        return 'Mozilla/5.0 (Linux; Android {android}; Z2 Plus Build/N2G47O; wv) AppleWebKit/{AppleWebKit} (KHTML, like Gecko) Version/4.0 Chrome/{Chrome} Mobile MQQBrowser/6.2 TBS/{TBS} Safari/{Safari} MicroMessenger/{MicroMessenger} NetType/WIFI Language/zh_CN'.format(
            **{'android': rand_android(), 'AppleWebKit': rand_apple_webkit(), 'Chrome': rand_chrome(),
               'TBS': str(rd.randint(1, 999999)).zfill(6), 'Safari': rand_safari(),
               'MicroMessenger': '6.{0}.{1}.{2}'.format(rd.randint(0, 9), rd.randint(0, 9), rd.randint(1, 9999))})


if __name__ == 'main':
    pass

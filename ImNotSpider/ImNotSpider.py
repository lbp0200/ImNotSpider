import random as rd

# 感谢chrome
# https://www.fynas.com提供Android机型、手机浏览器大全
android_phone_list = [
    'Nexus 4 Build/KOT49H', 'Nexus 5 Build/MRA58N', 'Nexus 6 Build/LYZ28E',
    'Nexus 7 Build/JSS15Q', 'Nexus 5 Build/MRA58N', 'Nexus 6 Build/LYZ28E',
    # 三星
    'SM-G900P Build/LRX21T', 'SM-N900T Build/JSS15J',
    'GT-N7100 Build/JRO03C', 'GT-I9300 Build/IMM76D',
    # LG
    'LGMS323 Build/KOT49I.MS32310c',
    # OPPO/VIVO
    'OPPO A59m Build/LMY47I',
    # 华为
    'VIE-AL10 Build/HUAWEIVIE-AL10; wv', 'HUAWEI NXT-AL10 Build/HUAWEINXT-AL10', 'HUAWEI NXT-CL00 Build/HUAWEINXT-CL00',
    'Che2-TL00M Build/HonorChe2-TL00M; wv', 'FRD-AL10 Build/HUAWEIFRD-AL10', 'HUAWEI RIO-AL00 Build/HuaweiRIO-AL00',
    'HUAWEI C199 Build/HuaweiC199', 'HUAWEI RIO-TL00 Build/HUAWEIRIO-TL00; wv', 'HUAWEI TAG-TL00 Build/HUAWEITAG-TL00',
    'HUAWEI MT7-CL00 Build/HuaweiMT7-CL00; wv', 'PLE-703L Build/HuaweiMediaPad; wv', 'PLK-TL01H Build/HONORPLK-TL01H',
    'EVA-AL10 Build/HUAWEIEVA-AL10',
    # 小米
    'MI MAX Build/MMB29M',
    # 联想ZUK
    'Z2 Plus Build/N2G47O; wv',

]


def rand_android_version():
    return '{0}.{1}.{2}'.format(rd.randint(4, 7), rd.randint(0, 9), rd.randint(0, 9))


def rand_android_phone():
    i = rd.randrange(0, len(android_phone_list))
    return android_phone_list[i]


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
        safari = rand_safari()
        return 'Mozilla/5.0 (Linux; Android {androidVersion}; {androidPhone}) AppleWebKit/{AppleWebKit} (KHTML, like Gecko) Version/4.0 Chrome/{Chrome} Mobile MQQBrowser/6.2 TBS/{TBS} Safari/{Safari} MicroMessenger/{MicroMessenger} NetType/WIFI Language/zh_CN'.format(
            **{'androidVersion': rand_android_version(), 'androidPhone': rand_android_phone(), 'AppleWebKit': safari,
               'Chrome': rand_chrome(), 'TBS': str(rd.randint(1, 999999)).zfill(6), 'Safari': safari,
               'MicroMessenger': '6.{0}.{1}.{2}'.format(rd.randint(0, 9), rd.randint(0, 9), rd.randint(1, 9999))})


if __name__ == 'main':
    pass

from uiautomator2 import Device
from wda import Client


class AndroidDriver(Device):
    """安卓设备"""
    def __call__(self, **kwargs):
        if len(kwargs) == 1 and "xpath" in kwargs:
            return self.xpath(kwargs["xpath"])
        else:
            return Device.__call__(self, **kwargs)

    def find_element(self, **kwargs):
        if len(kwargs) == 1 and "xpath" in kwargs:
            return self.xpath(kwargs["xpath"])
        else:
            return Device.__call__(self, **kwargs)


class AppleDevice(Client):
    """苹果设备"""

    def find_element(self, **kwargs):
        return self.__call__(self, **kwargs)


def connect_device(system: str, url: str):
    if system.lower() == "android":
        return AndroidDriver(url)
    else:
        return AppleDevice(url)


class Operation(object):
    def __init__(self, test, device):
        self.device = device
        self.test = test

    def find_element(self, ele):
        """查找单个元素"""
        try:
            element = self.device.find_element(**ele)
            self.test.debugLog("定位元素: %s" % str(ele))
            return element
        except Exception as e:
            self.test.errorLog("定位元素出错: %s" % str(ele))
            raise e

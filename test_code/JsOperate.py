from selenium import webdriver
import unittest

def addAttribute(driver, elementobj, attributeName, value):
    '''
    封装向页面标签添加新属性的方法
    调用JS给页面标签添加新属性，arguments[0]~arguments[2]分别
    会用后面的element，attributeName和value参数进行替换
    添加新属性的JS代码语法为：element.attributeName=value
    比如input.name='test'
    '''
    driver.execute_script("arguments[0].%s=arguments[1]" % attributeName, elementobj, value)


def setAttribute(driver, elementobj, attributeName, value):
    '''
    封装设置页面对象的属性值的方法
    调用JS代码修改页面元素的属性值，arguments[0]~arguments[1]分别
    会用后面的element，attributeName和value参数进行替换
    '''
    driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", elementobj, attributeName, value)


def getAttribute(elementobj, attributeName):
    # 封装获取页面对象的属性值方法
    return elementobj.get_attribute(attributeName)


def removeAttribute(driver, elementobj, attributeName):
    '''
    封装删除页面属性的方法
    调用JS代码删除页面元素的指定的属性，arguments[0]~arguments[1]分别
    会用后面的element，attributeName参数进行替换
    '''
    driver.execute_script("arguments[0].removeAttribute(arguments[1])",
                          elementobj, attributeName)


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_dataPicker(self):
        url = "D:\PycharmProjects\zouzou\dom.html"
        self.driver.get(url)
        element = self.driver.find_element_by_xpath('//input')

        # 向页面文本框input标签中添加新属性name='search'
        addAttribute(self.driver, element, 'name', 'search')
        # 添加新属性后，查看一下新属性值
        print('添加的新属性值%s="%s"' % ("name", getAttribute(element, "name")))

        print('更改文本框中内容前的value的值：', getAttribute(element, 'value'))
        # 更改value的属性值为“这是更改后的值”
        setAttribute(self.driver, element, 'value', '这是更改后的值')
        print('更改后value的值为：', getAttribute(element, 'value'))

        # 查看更改前input页面元素中size属性值
        print('更改前size的属性值为：', getAttribute(element, 'size'))
        # 更改input的属性值为20
        setAttribute(self.driver, element, 'size', 20)
        print('更改后size的属性值为：', getAttribute(element, 'size'))

        # 查看删除input页面元素value属性前的值
        print('删除前文本框value的值：', getAttribute(element, 'value'))
        # 删除属性值
        removeAttribute(self.driver, element, 'value')
        print('删除后文本框value的值：', getAttribute(element, 'value'))


if __name__ == '__main__':
    unittest.main()

# 类的高级魔法
>author: 波比小金刚

<br/>

千里之行，始于足下。
几乎所有的编程语言都是始于数据存储、运算、逻辑...
so, 开始我们的python旅程。
本章节代码都在./code/chapter17.py
<a href="#">图片没加载出来，请直接下载并打开对应的html页面</a>

## 简介

本节主要记录两个类的高级魔法。type() & metaclass

## type()

常用的type()方法，我们熟知的是检查类型，type('123') --> str 这样。
其实type()可以动态的创建一个类。<br/>
Python是一门动态类型的语言。动态语言和静态语言的最大区别就是类和函数的定义是在运行期定义的。静态语言则是你按照class...结构写了，在编译期确定的。<br/>

由此可以预见，我们在定义python中的类的时候，解释器其实也是调用了type()的方式来创建的类。

语法:

>type(name, supers, fn) name-> 类名，supers-> 基类列表， fn-> 函数

```
# type()动态创建一个类

def fn(self, name='Tom'):
    print('Hello, {}'.format(name))

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
s = Hello()
s.hello() # Hello, Tom
print(type(s)) # <class '__main__.Hello'> 
print(type(Hello)) # <class 'type'> 类的类型就是type

```



## metaclass

我们都知道类是实例的模板，通过类的定义刻画出实例的轮廓。那么?<br/>
类又是通过什么模板刻画出来的呢，答案就是metaclass。我们可以称之为元类。

语法：
```
最关键的__new__函数：
__new__(cls, name, bases, attrs)
参数依次是：类，类名，基类，方法
```

现在我们制定一个list,为其添加add方法，因为python中的list只有append。

```
class ListMetaClass(type): #=> 必须继承type
    def __new__(cls, name, bases, fns):
        fns['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, fns)

class myList(list, metaclass=ListMetaClass):
    pass

L = myList()
L.add(1)
print(L) #[1]
```
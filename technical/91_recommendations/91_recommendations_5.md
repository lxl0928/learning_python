## 编写高质量代码(改善Python程序的91个建议)_5: 设计模式

[TOC]

### 50. 利用模块实现单例模式

通过单例模式可以保证系统中一个类只有一个实例而且该实例易于被外界访问，从而方便对实例个数的控制并节约系统资源。

采用模块是天然的单例实现方式:
```
1. 所有的变量都会绑定到模块
2. 模块值初始化一次
3. import 机制是线程安全的(保证了在并发状态下模块也只有一个实例)
```

当我们想要实现一个游戏世界时候，只需要简单的创建world.py就可以
```
# world.py
imoprt Sun
def run():
    while True:
        Sun.rise()
        Sun.set()
```

然后在入后文件main.py里导入，并调用run()函数。
```
# main.py
import World
World.run()
```

### 51. 用mixin模式让程序更加灵活

在理解mixin之前，模板方法模式: 所谓的模板方法模式就是在一个方法中定义一个算法的骨架，并将一些实现步骤延迟到子类中，模板方法可以使子类在不该便算法结构的情况下，重新定义算法中的某些步骤。在这里，算法可以理解为行为。

模板方法模式在C++或其它语言中并无不妥，但是在python语法中，则颇有点画蛇添足的味道。
比如模板方法，需要先定义一个基类，而实现行为的某些步骤则必须在其子类中，在python中并无必要:
```
class People(object):
    def make_tea(self):
        teapot = self.get_teapot()
        teapot.put_in_tea()
        teapot.put_in_water()
        return teapot
```

在这个例子中，get_teapot()方法不需要定义。
假设在上班时，使用的是简易茶壶，而在家里，使用的是功夫茶壶，那么可以这样编写代码：
```
class OfficePeople(People):
    def get_teapot(self):

        return SimpleTeapot()

class HomePeople(People):
    def get_teapot(self):
        return KungfuTeapot()
```

这段代码工作得很好，虽然看起来像模板方法，但是基类并不需要预先声明抽象方法，甚至还带来调试代码的便利。

假定存在一个People的子类StreetPeople, 用以描述“正走在街上的人”，作为“没有人会随身携带茶壶”的常识的反映，这个类将不会实现get_teapot()方法，所以一调用make_tea()就会产生一个找不到get_teapot()方法的AttributeError由此程序员马上会想到“正走在街上的人”边走边泡茶这样的需求是不合理的，从而能够在更高层次上考虑业务的合理性，在更接近本源的地方修正错误。

但是，这段代码并不完美。老板（OfficePeople的一个实例）拥有巨大的办公室，他购置了功夫茶具，他要在办公室喝功夫茶，怎么办？

答案一: 从OfficePeople继承子类Boss，重写它的get_teapot(),使它返回功夫茶具；另一个则是把get_teapot()方法提取出来，把它以多继承的方式做一次静态混入。

```
class UseSimpleTeapot(object):
    def get_teapot(self):
        return SimpleTeapot()

class UseKungfuTeapot(object):
    def get_teapot(self):
        return KungfuTeapot()

class OfficePeople(People, UseSimpleTeapot):
    pass

class HomePeople(People, UseKungfuTeapot):
    pass

class Boss(People, UseKungfuTeapot):
    pass
```

这样就很好的解决了老板在办公室也要喝功夫茶的需求。但是这样的代码仍然没有把python的动态性表现出来: 当新的需求出现时，需要更改类的定义。比如随着公司的扩张，越来越多的人入职，OfficePeople的需求越来越多，开始出现有人不喝茶而是喝咖啡，也有人喜欢喝茶也喜欢喝咖啡。出现了喜欢在独立办公室抽雪茄的职业经理人...

这些类越来越多，代码越来越难以维护。让我们开始寄希望于动态的生成不同的实例:
```
def simple_tea_people():
    people = People()
    people.__bases__ += (UseSimpleTeapot, )
    return people

def coffee_people():
    people = People()
    people.__bases__ += (UseCoffeepot, )
    return people

def tea_and_coffee_people():
    people = People()
    people.__bases__ += (UseSimpleTeapot, UseCoffeepot, )

def boss():
    people = People()shengzhi
    people.__bases__ += (KungfuTeapot, UseCoffeepot, )
    return people
```

这个代码能够运行的原理是: 每一个类都有一个__bases__属性，它是一个元组，用来存放所有的基类。与其它静态语言不同，python语言中的基类在运行中可以动态的改变。
所以当我们向其中增加新的基类时，这个类就拥有了新的方法，也就是所谓的混入(mixin).

这种动态性的好处在于代码获得了更丰富扩展功能。想象以下，你之前写好的代码并不需要个性，只要后期为它增加基类，就能够增强功能（或替换原有行为），这多么方便。值得进一步探索的是，利用反射技术，甚至不需要修改代码。

假定我们OA系统里定义员工的时候，有一个特性选择页面，在里面可以勾选该员工的需求。

比如对于Boss，可以勾选功夫茶和咖啡，那么通过代码可能如下:
```
import mixins
def staff():
    people = People()
    bases = []
    for i in config.checked():
        bases.append(getattr(mixins, i))
    people.__bases__ += tuple(bases)
    return people
```

通过这个框架代码, OA系统的开发人员只需要把员工常见的需求定义成Mixin预告放在mixins模块中，就可以在不修改代码的情况下通过管理界面满足几乎所有的需求了。

python的动态性优势也在这个例子中得到了很好的体现。


### 52. 用发布订阅模式实现松耦合

发布订阅模式(publish/subscribe或pub/sub)是一种编程模式，消息的发送者(发布者)不会发送其消息给特定的接受者(订阅者)，而是将发布的消息分为不同的类别直接发布，并不关注订阅者是谁。

而订阅者可以对一个或多个类别感兴趣，且只接收感兴趣的消息，并且不关注是哪个发布者发布的消息。这种发布者和订阅者的解藕可以允许更好的可扩展放性和更为动态的网络拓扑，故受到大家的喜爱。

发布订阅模式的有点是发布者与订阅者松散的耦合，双方不需要知道对方的存在。由于主题是被关注的，发布者和订阅者可以对系统拓扑毫无所知。

无论对方是否存在， 发送者和订阅者都可以继续正常操作。要实现这个模式，就需要有一个中间代理人，在实现中一般被成为Broker，它维护着发布者和订阅者的关系: 订阅者把感兴趣的主题告诉它，而发布者的信息也通过它的路由到各个订阅者处。简单实现如下:
```
from collection import defaultdict
route_table = defaultdict(list)

def sub(self, topic, callback):
    if callback in route_table[topic]
        return 
    route_table[topic].append(callback)

def pub(self, topic, *a, **kw):
    for func in route_table[topic]:
        func(*a, **kw)
```
这个实现非常简单，直接放在一个叫Broker.py的模块中(这显然是单件)，省去了各种参数检测，有限处理需求等，
甚至没有取消订阅的函数，但它的确展现了发布订阅者模式实现的最基础的结构，它的应用代码也可以运行:
```
import Broker
def greeting(name):
    print("Hello %s"%name)

Broker.sub('greet', greeting)
Broker.pub('greet', 'LaiYonghao')

# 输出
# Hello LaiYonghao
```
相对于这个简化版本，blinker和python-message两个模块的实现要完备的多。blinker已经被用在了多个广受欢迎的项目上，比如flask和django；
而python-message则支持更多丰富的特性。本节以python-message为例，讲解发布订阅模式的应用场景。

安装python-message相当简单，通过pip安装就可以了。
    pip install message

然后简单验证一下:
```
import message
def hello(name):
    print("hello, %s"%name)

message.sub("greet", hello)
message.pub("greet", "lai")
```

成功输出:
```
hello, lai
```

接下来用它解决一些实际问题。
假定项目组开发了一个程序库foo， 里面有一个非常重要的函数--bar
```
def bar():
    print("Haha, Calling bar()")
    do_sth()
```

这个函数如此重要，所以你给它加上了一行输出代码，用以输出日志。后来你的这个程序库foo被大量使用了，一直运行的很好，知道一个新项目拖你过去救火，因为出现bug无法查出原因，怀疑是foo出现的问题。你查看了很久的日志，都没有发现他们调用bar()痕迹，一问，原来他们是用logging的，标准输出在做Dacmon的时候被重定向到了/dev/null在临时修改了输出重定向以后，找到了bug所在，并解决了，然后你开始着手解决这个问题。一开始你想在你的foo库中引入logging, 但原来的项目又不用logging，你在程序库里引入logging， 但谁来初始化它呢？

就算你引入logging，则你们的项目可能是用logging.getLogger('prjA')获取logger,另一个项目可能是用logging.getLogger('prjB'), 日后还有新项目呢？

解决：轻松更改以下bar()函数
```
import message
LOG_MSG = ('log', 'foo')
def bar():
    message.pub(LOG_MSG, 'Haha, Calling bar().')
    do_sth()
```

在已有的项目中，只需要在项目开始处加上这样的代码，继续把日志放到标准输出:
```
import message
import foo
def handle_foo_log_msg(txt):
    print(txt)

message.sub(foo.LOG_MSG, handle_foo_log_msg)
```

而在那个使用logging的新项目中，则可以这样修改:
```
def hangle_foo_log_msg(txt):
    import logging
    logging.debug(txt)
```

甚至在一些不关注底层库的日志项目中， 直接无视就可以了。
通过message，可以轻松的获得库与应用之间的解耦，因为库关注的是要有日志，而不关注日志输出到哪里，应用关注的是日志要统一放置，但不关注谁往日志文件中输出内容，这正与发布订阅模式的应用场景不谋而合。

除了sub()/pub()之外，python-message还支持取消订阅(unsub())和中止消息传递。
```
import message

def hello(name):
    print("hello , %s" % name)
    ctx = message.Context()
    ctx.discontinued = True
    return ctx

def hi(name):
    print("you can't call me.")

message.sub('greet', hello)
message.sub('greet', hi)
message.pub('greet', 'lai')
```
在上面这个例子中是看不到"you  can't call me"的， 因为在调用hello()后就中止了传递了(Broker使用list对象存储回调就是为了保证次序)

python-message是同步调用回调函数的，也就是说谁先sub谁就先被调用。

订阅/发布模式是观察者模式的超集，它不关注消息是随发布的，也不关注消息是由谁处理的。

但有时候我们也希望某个自己的类也能够更方便的订阅/发布消息， 也就是退化为观察者模式，python-message提供了如下的支持:
```
from message import observable
def greet(people):
    print("hello, %s"%people.name)

@observable
class Foo(object):
    def __init__(self, name):
        print("Foo")
        self.name = name
        self.sub("greet", greet)

    def pub_greet(self):
        self.pub("greet", self)

foo = Foo('lai')
foo.pub_greet()
```


### 53. 用状态模式美化代码

状态模式: 

就是当一个对象的内在状态改变时，允许改变其行为，但这个对象看起来像是改变了其类。

应用场景：

一个对象的行为取决于它的状态，即它必须在运行时刻根据状态改变它的行为。如果控制状态转换的条件表达式过于复杂，就可以考虑使用状态模式。

关键点：

把状态的判断逻辑转移到表示不同状态的一系列类当中，这样就可以简化复杂的逻辑判断了。

优点：

将与特定状态相关的行为局部化，并且将不同状态的行为分割开来。

```
#encoding=utf-8
#
#by panda
#状态模式


def printInfo(info):
    print unicode(info, 'utf-8').encode('gbk')

#State：上班状态基类
class State():
    def WriteProgram():
        pass

#上午工作状态类
class ForenoonState(State):
    def WriteProgram(self,w):
        if (w.Hour < 12):
            printInfo("当前时间：%d点 工作状态：上午工作，精神百倍" % w.Hour)
        else:
            w.SetState(noonState())
            w.WriteProgram()            

#中午工作状态类
class noonState(State):
    def WriteProgram(self,w):
        if (w.Hour < 13):
            printInfo("当前时间：%d点 午饭；午休" % w.Hour)
        else:
            w.SetState(AfternoonState())
            w.WriteProgram();
            
#下午工作状态类
class AfternoonState(State):
    def WriteProgram(self,w):
        if (w.Hour < 18):
            printInfo("当前时间：%d点 下午状态还不错，继续努力" % w.Hour)
        else:
            w.SetState(EveningState())
            w.WriteProgram();

#晚上工作状态类
class EveningState(State):
    def WriteProgram(self,w):
        if(w.TaskFinished):
            w.SetState(RestState())
            w.WriteProgram()
            return
            
        if (w.Hour < 21):
            printInfo("当前时间：%d点 加班哦，好累！" % w.Hour)
        else:
            w.SetState(SleepingState())
            w.WriteProgram();

#睡眠状态
class SleepingState(State):
    def WriteProgram(self,w):
        printInfo("当前时间：%d点 睡觉了" % w.Hour)


#下班工作状态
class RestState(State):
    def WriteProgram(self,w):
        printInfo("当前时间：%d点 下班回家了" % w.Hour)
            

#Context：上班
class Work():
    state = ForenoonState();
    TaskFinished = False
    Hour = 8.0
    
    def SetState(self, state):
        self.state = state
        
    def WriteProgram(self):
        self.state.WriteProgram(self)


def clientUI():
    work = Work()    
    for i in range(9,23,1):
        work.Hour = i
        if(i > 19):
            work.TaskFinished = True
        work.WriteProgram()
    return

if __name__ == '__main__':
    clientUI();

```

运行结果：
```
当前时间：9点 工作状态：上午工作，精神百倍
当前时间：10点 工作状态：上午工作，精神百倍
当前时间：11点 工作状态：上午工作，精神百倍
当前时间：12点 午饭；午休
当前时间：13点 下午状态还不错，继续努力
当前时间：14点 下午状态还不错，继续努力
当前时间：15点 下午状态还不错，继续努力
当前时间：16点 下午状态还不错，继续努力
当前时间：17点 下午状态还不错，继续努力
当前时间：18点 加班哦，好累！
当前时间：19点 加班哦，好累！
当前时间：20点 下班回家了
当前时间：21点 下班回家了
当前时间：22点 下班回家了
```


![类图](http://7xorah.com1.z0.glb.clouddn.com/%E6%B7%B1%E5%BA%A6%E6%88%AA%E5%9B%BE20161031225014.png)

这种状态模式，逻辑控制部分和状态转换控制都放在了不同的状态类中，但是如果我们希望将所有的逻辑控制和状态转换都放在同一个地方，而状态类只需要关注自己要做的事情即可，就出现了书中的示例代码：
```
def workday():
    print 'work hard!'

def weekday():
    print 'play harder!'

class People(object):pass

people = People()

for i in xrange(1,8):
    if i == 6:
        people.day = weekday
    if i == 1:
        people.day =workday
    people.day()

```

解释：当我第一眼看最后一行代码的时候，觉得people.day()没定义啊，当我从for开始往下看的时候，才醒悟，汗！。当i=1，day的状态为workday，然后直到i=6才会改变状态为weekday，也就是说，i的值在1~5时，状态一直是workday，到了6才是weekday，当然7也是weekday。

好了，现在所有的逻辑控制部分都在for里面，两个状态类不用关心状态怎么转换，但是仍然还有以下缺陷（基本摘自书中）：
    
1. 查询对象的当前状态很麻烦

2. 状态切换时如果需要对原状态做一些清理工作，对新的状态做一些初始化工作，那把这个清理和初始化工作都都写在for里面或者原来的状态类里，必然有重复，因为每个状态都要进行初始化和清理，那我几个状态转换下来，这个for循环已经没法保持好看的身材了。我们需要一个机制来简化这个问题。
    
ＰＳ：其实这些问题只是在状态类较多的情况下更加明显，如果只是两到三个状态类，个人意见是随便写，重复两三条没啥问题（也许是自己要求太低。。）
    
好了，言归正传，如果状态类很多，多到要写状态初始化和清理都很烦的时候，那我们急需一个辅助工具来做这个重复又头疼的事情，python-state工具通过几个辅助函数和修饰函数解决了这个问题，并定义了一个简明状态机框架（这个真没看出来，汗！）。
 地址：https://pypi.python.org/pypi/state/0.1.2dev-r2可以下载，也可以通过pip install state直接安装。

 ```
 # -*- coding:utf-8 -*-
import inspect
import functools

class State(object):
    @staticmethod
    def __begin__(host):
        pass

    @staticmethod
    def __end__(host):
        pass

def stateful(cls):
    defaults = []
    for i in cls.__dict__.itervalues():
        if inspect.isclass(i) and issubclass(i, State) and hasattr(i, 'default') and i.default:
            defaults.append(i)
    if not defaults:
        raise Error('%s\'s default state is not found.' % cls.__name__)
    if len(defaults) > 1:
        raise Error('%s\'s has too much default state.%s' % (cls.__name__, defaults))
    default = defaults[0]

    old__init__ = cls.__init__
    if hasattr(cls, '__getattr__'):
        old__getattr__ = getattr(cls, '__getattr__')
    else:
        old__getattr__ = getattr(cls, '__getattribute__')

    def __init__(self, *a, **kw):
        self.__state__ = default
        self.__state__.__begin__(self)
        return old__init__(self, *a, **kw)

    def __getattr__(self, name):
        try:
            old__getattr__(self, name)
        except AttributeError, e:
            pass
        try:
            f = getattr(curr(self), name)
        except AttributeError:
            raise e
        if not callable(f):
            raise e
        return functools.partial(f, self)

    cls.__init__ = __init__
    cls.__getattr__ = __getattr__
    return cls

def curr(host):
    return host.__state__

def switch(host, new_state):
    host.__state__.__end__(host)
    host.__state__ = new_state
    new_state.__begin__(host)

behavior = staticmethod
#上面是state工具的代码，下面是书中的使用示例
@stateful
class People(object):
        class Workday(State):
                default = True
                @behavior
                def day(self):
                        print 'word hard!'
        class Weekday(State):
                @behavior
                def day(self):
                        print 'play harder!'
people = People()
for i in xrange(1,8):
        if i == 6:
                switch(people,People.Weekday)
        if i == 1:
                switch(people,People.Workday)
        people.day()

 ```

运行结果：
```
word hard!
word hard!
word hard!
word hard!
word hard!
play harder!
play harder!
```


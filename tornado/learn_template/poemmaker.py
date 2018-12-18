import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default = 8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):#定义了几个RequestHandler子类并把它们传给tornado.web.Application对象
    def get(self):
        self.render('index.html')#这段代码告诉Tornado在templates文件夹下找到一个名为index.html的文件，读取其中的内容，并且发送给浏览器。

class PoemPageHandler(tornado.web.RequestHandler):#定义了几个RequestHandler子类并把它们传给tornado.web.Application对象
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb, difference=noun3)
        #告诉模板使用变量noun1（该变量是从get_argument方法取得的）作为模板中roads的值，noun2作为模板中wood的值，依此类推。

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [(r'/', IndexHandler), (r'/poem', PoemPageHandler)],
        template_path = os.path.join(os.path.dirname(__file__), "templates")
    )
    #template_path参数告诉Tornado在哪里寻找模板文件：模板是一个允许你嵌入Python代码片段的HTML文件。

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

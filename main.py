import tornado.ioloop
import tornado.web
import time
import uimethod as md   ## 对应settings 配置中 可以在 login.html中是直接使用 md 中的方法 tab 返回 uimethod  定义的是方法
import uimodules  ## 其中有类m1  定义的是类  可以自定义css  js等
from session import Session

## 记得在application 中传入，不传怎么生效
settings = {
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'template_path': 'templates',
    'ui_methods': md,
    'ui_modules': uimodules


}
## 基类
class BaseHandler(object):
    def initialize(self):
        #获取用户cookie 有就获取，没有就生成
        self.ssss="--4s from BaseHandler"
        self.session = Session(self) ## 记得从文件导入
        super(BaseHandler,self).initialize()


class MainHandler(BaseHandler,tornado.web.RequestHandler):
    def get(self):
        print(self.session.get_value('is_login'))
        if self.session.get_value('is_login'):
            print("is_login exists")
            self.write("hello tornado"+str(self.ssss))
        else:
            print("index redirect to login")
            self.redirect('/login/')

class LoginHandler(BaseHandler,tornado.web.RequestHandler):
    def get(self):
        # self.write("login get hello tornado")
        # v = self.get_argument('v') ## 获取get post参数
        # print(v)
        v = "test"
        self.set_cookie('k1','v1')
        print('22222')
        self.render('login.html',k1="v1"+str(self.ssss),k2=['1','2'],k3={"key":"value1","k2":"value2"})

    def post(self):
        user = self.get_argument('user')
        print(user)
        if user == "cl":
            self.session.set_value('is_login',True)
            print(self.session.get_value('is_login'))
            print("ssssssssssssssssssssssssssss")
            self.redirect('/index/')
        else:
            self.redirect('/login/')


application = tornado.web.Application([
    (r"/index/", MainHandler),
    (r"/login/", LoginHandler),
    ],**settings)

if __name__=='__main__':
    application.listen((8888))
    tornado.ioloop.IOLoop.instance().start()

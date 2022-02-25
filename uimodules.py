from tornado.web import UIModule
from tornado import escape

class m1(UIModule):
    def embedded_css(self):
        return 'body{color:blue}'   ## 访问 login.html验证颜色
    def embedded_javascript(self):
        return 'document.getElementById("demo").innerHTML = "from uimodule js 的我的第一段 JavaScript";'
    def render(self, *args, **kwargs) -> str:
        print(*args,**kwargs)
        return escape.xhtml_escape('<h1>from_m1_uimodule'+str(*args)+'</h1>')

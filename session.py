import uuid



class Session(object):
    container = {}
    def __init__(self,handler):
        nid = handler.get_cookie('session_id')
        if nid:
            if nid in self.container:
                pass
            else:
                nid = str(uuid.uuid4())
                handler.set_cookie('session_id', nid)
                Session.container[nid] = {}
        else:
            nid = str(uuid.uuid4())
            handler.set_cookie('session_id', nid)
            Session.container[nid] = {}
        # 重新赋值
        self.nid = nid
        self.handler = handler


    def set_value(self,key,value):
        Session.container[self.nid][key] = value

    def get_value(self,key):
        return Session.container[self.nid].get(key)




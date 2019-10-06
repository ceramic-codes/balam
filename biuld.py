#-*-coding: utf-8-*-
from json import dumps,loads
from hashllib import md5
import os
class generate:
    def __init__(path,file,obj,archive,*args,**kwargs):
        self.work_rute = os.path.join(os.environ.get("HOME"),"balam","package","logs")
        self.path = path
        self.file = file
        self.obj = obj
        self.args = args
        self.kwargs = kwargs
        self.archive_name = archive
        self.val = [x for x in os.listdir(self.work_rute) if x.endswith(".json")]
    def mk_file(self):
        data_open = open(os.path.join(self.work_rute,md5(self.archive_name).hexdigest() + ".json"),"w")
        data_sacm = open(os.path.join(self.work_rute,"plug.log"),"a")
        ex_data = json.dumps({'path':self.path,'file_name':self.file,'file_path':__file__,'exists':os.path.exists(__file__),'ejecute_banner':self.obj.banner,'kwargs':self.kwargs,'ifo':md5(self.archive_name).hexdigest()})
        data_open.write(ex_data)
        data_scam.write(self.archive_name)
        data_open.close()
        data_scam.close()
    def load(self):
        with open(self.work_rute + 'plug.log','r') as rp:
            data = rp.read()
            dic = {}
            doc = []
            cpun = 0
            for x in data:
                for y in self.val:
                    if y == md5(x).hexdigest():
                        print("[{c}] {x}:{y}".format(x=x,y=y,c=cpun))
                        dic[x] = y
                        doc.append(x)
                        cpun += 1
                    else:
                        pass
            log = int(input("$>"))
            for x in range(0,len(dic) - 1 ):
                if x == log:
                    data_open = open(self.work_rute + dic[doc[x]],"r")
                    data_load = loads(data_open.read)
                    if data_load["exists"]:
                        if data_load["kwargs"] == "":
                            exec(data_load["ejecute_banner"])
                        elif data_load["kwargs"] != "":
                            exec(data_load
                else:
                    pass

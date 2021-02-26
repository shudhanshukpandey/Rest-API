import googletrans
from info_lan import Info

translator=googletrans.Translator()
obj=Info()

class Utility():
    def __init__(self):
        pass
    def getdata(self,in_data):
        obj.stext=in_data["text"]
        obj.des=in_data["lan"]
        
    def changelan(self):
        obj.dtext=""
        for i in str(obj.stext).split():
            if i.startswith("https://") or i.startswith("www") or i.startswith("http://"):
                obj.dtext+=" "+i
        
            elif i.isalpha():
                obj.dtext+=" "+str(translator.translate(i,dest=obj.des).text)

            elif i.isalnum():
                obj.dtext+=" "+i

        return str(obj.dtext)

    def robj(self):
        obj.robj={"text":obj.dtext,"C_Lan":obj.des.title()}
        return obj.robj

    def All_Languages(self):
        obj.alan=googletrans.LANGUAGES
        return obj.alan

    def nlan(self):
        return str(obj.dtext)
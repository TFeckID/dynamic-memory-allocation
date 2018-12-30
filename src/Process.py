from Table import Table_structure
from Table import Table

class Process(object):
    def __init__(self):
        pass

    def firstfit(self,tab_obj, ap_size):
        tab_obj.frTable.sort(key=lambda x:x.initaddr,reverse=True)
        count=0
        for i in range(len(tab_obj.frTable)):
            if tab_obj.alloct(ap_size,i):
                return True
            else:
                count+=1
        if count==len(tab_obj.frTable):
            return False

    def nextfit(self,tab_obj,ap_size,ls_index):
        count=0
        nextflag=False
        for i in range(ls_index,len(tab_obj.frTable)):
            if tab_obj.alloct(ap_size,i):
                ls_index=i
                return True
            else:
                count+=1
                nextflag=True
        if nextflag:
            for i in range(0,ls_index):
                if tab_obj.alloct(ap_size,i):
                    ls_index=i
                    return True
                else:
                    count+=1
            if count==len(tab_obj.frTable):
                return False

    def bestfit(self,tab_obj,ap_size):
        count=0
        tab_obj.frTable.sort(key=lambda x:x.size,reverse=False)
        for i in range(len(tab_obj.frTable)):
            if tab_obj.alloct(ap_size,i):
                return True
            else:
                count+=1
        if count==len(tab_obj.frTable):
            return False

    def worsefit(self,tab_obj,ap_size):
        count=0
        tab_obj.frTable.sort(key=lambda x:x.size,reverse=True)
        for i in range(len(tab_obj.frTable)):
            if tab_obj.alloct(ap_size,i):
                return True
            else:
                count+=1
        if count==len(tab_obj.frTable):
            return False

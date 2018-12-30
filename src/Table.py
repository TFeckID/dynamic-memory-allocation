class Table_structure(object):
    def __init__(self,size,initaddr,is_alloted):
        self.size=size
        self.initaddr=initaddr
        self.is_alloted=is_alloted


class Table(object):
    def __init__(self):
        self.frTable=[Table_structure(50,85,False),
                      Table_structure(32,155,False),
                      Table_structure(70,275,False),
                      Table_structure(60,532,False)]

        self.alTable=[Table_structure(85,0,True),
                      Table_structure(20,135,True),
                      Table_structure(88,187,True),
                      Table_structure(187,345,True)]

    def printf(self):
        print("Free Table:")
        print("Addr Size Stats")
        for i in self.frTable:
            print(i.initaddr,end="   ")
            print(i.size,end="   ")
            print(i.is_alloted)
        print("Alocation Table:")
        print("Addr Size Stats")
        for i in self.alTable:
            print(i.initaddr,end="   ")
            print(i.size,end="   ")
            print(i.is_alloted)

    def alloct(self,u_size,u_index):
        if self.frTable[u_index].size>=u_size:
            if self.frTable[u_index].size-u_size<=4:
                t_size=self.frTable[u_index].size
                t_addr=self.frTable[u_index].initaddr
                self.alTable.append(Table_structure(t_size,t_addr,True))
                self.frTable.pop(u_index)
                return True
            else:
                t_size=u_size
                t_addr=self.frTable[u_index].initaddr+self.frTable[u_index].size-u_size
                self.alTable.append(Table_structure(t_size,t_addr,True))
                self.frTable[u_index].size=self.frTable[u_index].size-u_size
                return True
        else:
            return False


    def recyc(self,recaddr):
        reflag=False
        upflag=False
        downflag=False
        upindex=0
        downindex=0
        i=len(self.alTable)-1
        while i>=0:
            if self.alTable[i].initaddr==recaddr:
                for j in range(len(self.frTable)):
                    if self.frTable[j].initaddr==(self.alTable[i].initaddr+self.alTable[i].size):
                        downflag=True
                        downindex=j
                    if self.frTable[j].initaddr+self.frTable[j].size==self.alTable[i].initaddr:
                        upflag=True
                        upindex=j
                if upflag==True and downflag==True:
                    self.frTable[upindex].size=self.frTable[upindex].size+self.frTable[downindex].size+self.alTable[i].size
                    self.alTable.pop(i)
                    self.frTable.pop(downindex)
                    reflag = True
                    print("回收成功")
                    self.printf()
                elif upflag==False and downflag ==True:
                    t_size=self.alTable[i].size+self.frTable[downindex].size
                    self.frTable.append(Table_structure(t_size,recaddr,False))
                    self.frTable.pop(downindex)
                    self.alTable.pop(i)
                    reflag = True
                    print("回收成功")
                    self.printf()
                elif upflag==True and downflag == False:
                    self.frTable[upindex].size+=self.alTable[i].size
                    self.alTable.pop(i)
                    reflag = True
                    print("回收成功")
                    self.printf()
                elif upflag==False and downflag==False:
                    t_size=self.alTable[i].size
                    self.frTable.append(Table_structure(t_size,recaddr,False))
                    self.alTable.pop(i)
                    reflag = True
                    print("回收成功")
                    self.printf()
            i=i-1

        if not reflag:
            print("无效地址，回收失败")






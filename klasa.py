class Fifo:
    def __init__(self):
        self.items=[]
    def put(self,data):
        self.items.append(data)
    def get(self):
        try:
            return self.items.pop(0)
        except:
            pass

class Lifo:
    def __init__(self):
        self.items=[]
        self.i=0
    def put(self,data):
        self.items.append(data)
        self.i+=1
    def get(self):
        try:
            self.i -= 1
            return self.items.pop(self.i)
        except:
            pass
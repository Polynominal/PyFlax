def linear(x):
    return x
ease = {
    "linear":linear,
}
def findDistance(x,y):
    if not x or not y:
        return 0
    else:
        return max(x,y)-min(x,y)
class single:
     def __init__(self,time,item,exp,mode="linear"):
         self.progress = 0
         self.rate = time > 0 and 1 / time or 0
         self.start = item
         self.current = item
         self.diff = findDistance(item,exp)
         self.mode = mode
         self.exp = exp
         self.done = False
     def get(self):
         return self.current
     def update(self,dt):
         self.progress = self.progress + self.rate * dt
         p = self.progress
         x = x = p >= 1 and 1 or ease[self.mode](p)
         self.current = self.start + self.diff*x
         if p > 1:
             self.done = True


class _to:
    def __init__(self,time,obj,var,mode="Linear"):
        self.tweens = []
        self.var = var
        self.obj = obj
        #key val
        for i,v in var.items():
            item = single(time,getattr(obj,i),v)
            list.insert(self.tweens,len(self.tweens)+1,item)

    def update(self,dt):
        no = 0
        items = []
        for i,v in self.var.items():
            self.tweens[no].update(dt)
            setattr(self.obj,i,self.tweens[no].get())
            if self.tweens[no].done:
                items.insert(len(items)+1,i)
            no = no +1
        no = 0
        for item in self.tweens:
            if item.done:
                self.tweens.remove(item)
            no = no +1
        for item in items:
             self.var.pop(item, None)
        pass
    def stop(self):
        pass
class Tween():
    def __init__(self):
        self.tweens = []
        pass
    # VAR HAS TO BE DICT WITH STR:EXPVAL
    def to(self,time,obj,var,mode="Linear"):
       t = _to(time,obj,var,mode="Linear")
       list.insert(self.tweens,len(self.tweens)+1,t)
       return

    def update(self,dt):
        for tween in self.tweens:
            tween.update(dt)
        pass

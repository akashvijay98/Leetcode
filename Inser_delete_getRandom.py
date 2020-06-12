class RandomizedSet:

    def __init__(self):
        self.d={}
        
        
        
        
        
        

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        else:
            self.d[val]=len(self.d)
            return True
    def remove(self, val: int) -> bool:
        if val in self.d:
            self.d.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        
        
        return random.choice(list(self.d.keys()))

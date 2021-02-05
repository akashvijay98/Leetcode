class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
        

class MyLinkedList:

    def __init__(self):        
        self.head=None
        self.len=0

        
    
    def get(self, index: int) -> int:
        
        if index>=self.len:
            return -1
        
        
        
        l=self.head
        j=0
        while(j<=index):
            if(j==index):
                #print("element="+str(l.val))
                return l.val
            else:
                j+=1
                l=l.next
        
        
        

    def addAtHead(self, val: int) -> None:
        if self.head==None:
            self.head=Node(val)
            self.len+=1
        else:
            n=Node(val)
            
            n.next=self.head
            self.head=n
            self.len+=1
            

    def addAtTail(self, val: int) -> None:
        n=Node(val)
        p=self.head
        
        if self.head==None:
            self.head=Node(val)
            self.len+=1
            return 
        
        while(p.next!=None):
            p=p.next
        p.next=n
        self.len+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.len:
            return -1
        if index==0:
            self.addAtHead(val)
            
        i=0
        q=self.head
        p=self.head
        
       
        if index>self.len:
            return -1
        while(i<=self.len):
            if i==index:
                n=Node(val)
                q.next=n
                n.next=p
                self.len+=1
                return
                
                
                
                
            else:
                i+=1
                q=p
                p=p.next
        
            

    def deleteAtIndex(self, index: int) -> None:
        i=0
        p=self.head
        q=self.head
        
        if index>=self.len:
            return -1
        
        if index==0:
            q=p.next
            self.head=q
            return 
        
        while(i<=index):
            if(i==index):
                q.next=p.next
                
                self.len-=1
                break
                
            else:
                i+=1
                q=p
                p=p.next
                



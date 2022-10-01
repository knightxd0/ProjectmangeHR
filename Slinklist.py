from msilib.schema import File


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Slinklist:
    def __init__(self):
        self.head = None
        self.index = 0
    
    def printList(self,node):
        if node == None:
            print('None')
        else:
            print(node.data + ' -> ',end='')
            self.printList(node.next)
    
    file = None
    def list_fileproc(self,node,data):
        global file
        if node == None:
            file.close()
            print("Success...")
        else:
            user = node.data + "\n"
            file.write(user)
            print(node.data + ' -> ',end='')
            return self.list_fileproc(node.next,data)
    
    def list_file(self,type):
        global file
        if type == "user":
            data = type + ".txt"
            file = open(data,'w',encoding="utf8")
            self.list_fileproc(self.head,data)
        elif type == "rank":
            data = type + ".txt"
            file = open(data,'w',encoding="utf8")
            self.list_fileproc(self.head,data)
        elif type == "salary":
            data = type + ".txt"
            file = open(data,'w',encoding="utf8")
            self.list_fileproc(self.head,data)
            
    def insertAtEnd_proc(self,node,val):
        if node == None:
            # insert here
            newNode = Node(val)
            node = newNode
        else:
            node.next = self.insertAtEnd_proc(node.next,val)
        return node

    def insertAtEnd(self,val):
        self.head = self.insertAtEnd_proc(self.head,val)
        
    def search_proc(self,node,val):
        if node == None:
            return -1
        elif node.data == val:
            return self.index
        else:
            self.index = self.index + 1
            return self.search_proc(node.next,val)
            

    def search(self,val):
        result = self.search_proc(self.head,val)
        print(result) # true false
        self.index = 0
        return result
    
    def delete_proc(self,node,val):
        if node == None:
            return node
        elif node.data == val:
            tmp = node
            node = node.next
            tmp = None
        elif node.next == None:
            return node
        elif node.next.data == val:
            tmp = node.next
            node.next = node.next.next 
            tmp = None
        else:
            node.next = self.delete_proc(node.next,val)
        return node

    def delete(self,val):
        if self.search(val):
            self.head = self.delete_proc(self.head,val)
        else:
            print('not found')
    
    #ใช้หาจำนวนข้อมูลใน list       
    def len_proc(self,Node):
        if Node == None:
            return self.index_len
        else:
            self.index_len = self.index_len + 1
            return self.len_proc(Node.next)
        
    def len(self):
        l = self.len_proc(self.head)
        return l
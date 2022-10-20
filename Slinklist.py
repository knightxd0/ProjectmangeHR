

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Slinklist:
    def __init__(self):
        self.head = None
        self.index = 0
        self.index_len = 0
        self.count_index = 0
        self.count_listfile = 0
    
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
            data = str(node.data)
            if  data != " " :
                user = str(node.data)
                file.write(user)
                file.write("\n")
                print(user + ' -> ',end='')
                # self.count_listfile = self.count_listfile + 1
                return self.list_fileproc(node.next,data)
            else :
                user = str(node.data)
                file.write(user)
                print(user + ' -> ',end='')
                # self.count_listfile = 0
                return self.list_fileproc(node.next,data)
    
    def list_file(self,type):
        global file
        if type == "user":
            data = "ProjectmangeHR/data/"+type + ".txt"
            file = open(data,'w',encoding="utf8")
            self.list_fileproc(self.head,data)
        elif type == "rank":
            data = "ProjectmangeHR/data/"+type + ".txt"
            file = open(data,'w',encoding="utf8")
            self.list_fileproc(self.head,data)
        elif type == "salary":
            data = "ProjectmangeHR/data/"+type + ".txt"
            file = open(data,'w',encoding="utf8")
            self.list_fileproc(self.head,data)

    def insertAtHead(self,val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        print("newnode = " + str(newNode.data))
                
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
        if self.search(val) >= 0:
            self.head = self.delete_proc(self.head,val)
        else:
            print('not found')
    
    #delete ที่ index        
    def deleteIndex_proc(self,node,index):
        
        if self.count_index == index:
            self.delete(node.data)
            print("count = " + str(self.count_index))
            self.count_index = 0
        else:
            print("count = " + str(self.count_index))
            self.count_index = self.count_index + 1
            return self.deleteIndex_proc(node.next,index)
        
    def delete_index(self,index):
        if index > -1:
            self.deleteIndex_proc(self.head,index)
    
    # check resualt in index
    def index_proc(self,node,index):
        # print("count = " + str(self.count_index))
        if self.count_index == index:
            return node.data
        else:
            self.count_index = self.count_index + 1
            return self.index_proc(node.next,index)
                
    def index_data(self,index):
        len = self.len()
        if index > -1 and index < len:
            r = self.index_proc(self.head,index)
            return r
        else:
            print("Index out of len")
            
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
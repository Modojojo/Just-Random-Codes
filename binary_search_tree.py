class Node:
    def __init__(self, data):
        self.__data = data
        self.left = None
        self.right = None
    def get_data(self):
        return self.__data

class BST:
	'''
    constructs a bst only for unique values
    '''
    depth = 0   #static counter
    def __init__(self):
        self.root = None
        self.bst_visual = {}
        self.parents = []

    def add_node(self, data):
        node = Node(data)
        temp_node = self.root
        if temp_node is None:
            self.root = node
            #print("ADDING ROOT")
            BST.depth+=1
            return
        else:
            prev = temp_node
            current = 0
            while True:
                if node.get_data() < temp_node.get_data(): # check left
                    if temp_node.left is None:             #if leftchild is empty add child else goto next leftchild
                        temp_node.left = node
                        current+=1                         #increase counter bcoz child is added and loop breaks thus cannot go to the counter at line 43
                        #print("Adding LEFT CHILD("+str(node.get_data())+") :: parent :"+str(temp_node.get_data()))
                        self.parents.append(temp_node.get_data())
                        break
                    temp_node = temp_node.left             #goto left child
                elif node.get_data() > temp_node.get_data():    #check right
                    if temp_node.right is None:            #if rightchild is empty add child else goto next rightchild
                        temp_node.right = node
                        current+=1                         #increase counter bcoz child is added and loop breaks thus cannot go to the counter at line 43
                        #print("Adding RIGHT CHILD("+str(node.get_data())+") :: parent :"+str(temp_node.get_data()))
                        self.parents.append(temp_node.get_data())
                        break
                    temp_node = temp_node.right            #goto right child
                current+=1                                 #increase counter(temporary depth) for every child
            if current > BST.depth:
                BST.depth = current

    def get_depth(self):
        print("DEPTH : ", BST.depth)

    def find_element(self, element):
        temp_node = self.root
        temp_depth = 1
        t_str = ""
        while True:
            if temp_node is None:
                print("ELEMENT NOT FOUND")
                return
            elif temp_node.get_data() == element:
                t_str+= str(temp_node.get_data())
                print(t_str)
                break
            if element < temp_node.get_data():
                t_str+=str(temp_node.get_data()) + " [L]--> "
                temp_node = temp_node.left
            elif element > temp_node.get_data():
                t_str+=str(temp_node.get_data()) + " [R]--> "
                temp_node = temp_node.right
            temp_depth+=1

    def visualizer_util(self, temp_node, parent):
        if temp_node is None:
            return
        else:
            self.bst_visual[parent.get_data()].append(temp_node.get_data())
            self.visualizer_util(temp_node.left, temp_node)
            self.visualizer_util(temp_node.right, temp_node)


    def visualize(self):
        for i in self.parents:
            if i not in self.bst_visual:
                self.bst_visual[i] = []
        root = self.root
        left = self.root.left
        right = self.root.right
        self.visualizer_util(left, root)
        self.visualizer_util(right, root)
        print()
        print("{0:<7} :".format("#parent"),"#child")
        for i in self.bst_visual:
            print("{0:<7} :".format(i), self.bst_visual[i])

bst = BST()
lst = [6,21,4,5,10,15,100,0,3,27,200,22,76,26,1,54,7,36,23,67,90,101,12,11]
for i in lst:
    bst.add_node(i)


bst.visualize()
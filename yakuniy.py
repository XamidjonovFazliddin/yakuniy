#1

# data = [[1,2], [3, 4], [5, 6]]
# print(data[1][0]) 
# 3 ni olish usuli ya'ni listni ichida yana 3ta list bor. Ularni indexlari 0, 1, 2. 
# 3soni 1-indexdagi listda yotiibdi. Va shu listni 0-chi indexda yotibdi. Shhuning data[1][0] deb yozganman. 

#2
# binary tree ishlashi boshida ota tugun bo'ladi. Undan 2ta tugun chiqsa, yani child tugunlari chiqsa, birinchi chap keyin o'ngda ishlaydi. 
# Bir so'z bilan aytganda chapdan o'ngga qarab ishlaydi.


#3
def flatten(lst):
    result = []
    for sublist in lst:
        for item in sublist:
            result.append(item)
    return result

nested = [[1, 2], [3, 4], [5, 6]]
tekis = flatten(nested)
print(tekis)


#4
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)
    
    def inorder_traversal(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements
    
    def _inorder_recursive(self, current_node, elements):
        if current_node:
            self._inorder_recursive(current_node.left, elements)
            elements.append(current_node.value)
            self._inorder_recursive(current_node.right, elements)

if __name__ == "__main__":
    tree = BinaryTree()
    
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(18)
    
    print("Daraxt elementlari:", tree.inorder_traversal())
    print("5 daraxtda bormi?", tree.search(5))  
    print("8 daraxtda bormi?", tree.search(8))  
    print("15 daraxtda bormi?", tree.search(15))  
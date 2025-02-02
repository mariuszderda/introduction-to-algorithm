from collections import deque


class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.content = None

    def insert(self, value, content=None):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                self.left.content = content
            else:
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = TreeNode(value)
                self.right.content = content
            else:
                self.right.insert(value, content)

    def insert_loop(self, value):
        while self.left or self.right is not None:
            if value < self.value:
                if self.left is None:
                    break
                self = self.left
                continue
            if value > self.value:
                if self.right is None:
                    break
                self = self.right
                continue

        if value < self.value:
            self.left = TreeNode(value)
        elif value > self.value:
            self.right = TreeNode(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value, sep=",", end=" ")
        if self.right:
            self.right.inorder_traversal()

    def reverse_inorder_traversal(self):
        if self.right:
            self.right.reverse_inorder_traversal()
        if self.value is not None:
            print(self.value, sep=",", end=" ")
        if self.left:
            self.left.reverse_inorder_traversal()

    def preorder_traversal(self):
        print(self.value if self.value is not None else "", sep=",", end=" ")
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value, sep=",", end=" ")

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return self

    def find_key(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return self

    def level_order_traversal(self):
        queue = deque([(self, 0)])  # (węzeł, poziom)
        current_level = 0
        print(f"Level {current_level}:", end=" ")

        while queue:
            node, level = queue.popleft()

            if level > current_level:
                print(f"\nLevel {level}:", end=" ")
                current_level = level

            print(node.value, end=" ")

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        print()

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def rotate_left(self):
        if self.right is None:
            return self

        new_parent = self.right
        new_right_leaf = self.right.right
        new_left_value = self.value
        new_left_leaf = self.left
        new_left_right_leaf = self.right.left

        self.value = new_parent.value
        self.right = new_right_leaf
        self.left = TreeNode(new_left_value)
        self.left.left = new_left_leaf
        self.left.right = new_left_right_leaf

    def rotate_right(self):
        if self.left is None:
            return self

        new_parent = self.left
        new_left_leaf = self.left.left
        new_right_value = self.value
        new_right_leaf = self.right
        new_right_left_leaf = self.left.right

        self.value = new_parent.value
        self.left = new_left_leaf
        self.right = TreeNode(new_right_value)
        self.right.right = new_right_leaf
        self.right.left = new_right_left_leaf

    def straighten_tree(self):
        if self.left is not None:
            self.rotate_right()

            self.straighten_tree()
        if self.left is None:
            if self.right is None:
                return
            self.right.straighten_tree()



if __name__ == "__main__":


    tree = TreeNode(3)
    tree.insert(1)
    tree.insert(0)
    tree.insert(2)
    tree.insert(5)
    tree.insert(6)
    tree.insert(4)

    print(f"{"_"*20} Wyszukiwanie wartości {"_"*20}")
    print(f"liczba 20 {"występuje" if tree.find(20) else "nie występuje"} w drzewie")
    print(f"liczba 5 {"występuje" if tree.find(5) else "nie występuje"} w drzewie")
    print()
    print(f"{"_"*20} Wyświetlanie {"_"*20}")
    print("PreOrder")
    tree.preorder_traversal()
    print()
    print("PostOrder")
    tree.postorder_traversal()
    print()
    print("InOrder")
    tree.inorder_traversal()
    print()
    print("Reverse InOrder")
    tree.reverse_inorder_traversal()
    print()
    print()
    print(f"{"_"*20} Level Order {"_"*20}")
    tree.level_order_traversal()
    print(f"Height: {tree.height()}")
    print("="*50)
    print(f"{"_" * 20} Rotacja w lewo {"_" * 20}")
    tree.rotate_left()
    print("PreOrder")
    tree.preorder_traversal()
    print()
    print("PostOrder")
    tree.postorder_traversal()
    print()
    print("InOrder")
    tree.inorder_traversal()
    print()
    print("Reverse InOrder")
    tree.reverse_inorder_traversal()
    print()
    print()
    print(f"{"_" * 20} Level Order {"_" * 20}")
    print(tree.level_order_traversal())
    print(f"Height: {tree.height()}")
    print("=" * 50)
    print(f"{"_" * 20} Rotacja w lewo {"_" * 20}")
    tree.rotate_right()
    print("PreOrder")
    tree.preorder_traversal()
    print()
    print("PostOrder")
    tree.postorder_traversal()
    print()
    print("InOrder")
    tree.inorder_traversal()
    print()
    print("Reverse InOrder")
    tree.reverse_inorder_traversal()
    print()
    print(f"{"_" * 20} Level Order {"_" * 20}")
    tree.level_order_traversal()
    print(f"Height: {tree.height()}")
    print(f"{"_" * 20} Prostowanie drzewa {"_" * 20}")
    tree.straighten_tree()
    print("PreOrder")
    tree.preorder_traversal()
    print()
    print("PostOrder")
    tree.postorder_traversal()
    print()
    print("InOrder")
    tree.inorder_traversal()
    print()
    print("Reverse InOrder")
    tree.reverse_inorder_traversal()
    print()
    print(f"{"_" * 20} Level Order {"_" * 20}")
    tree.level_order_traversal()
    print(f"Height: {tree.height()}")





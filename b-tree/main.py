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
        print(self.value, sep=",", end=" ")
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

    def rotate_right(self):
        if self.right is None:
            return self

        new_root = self.right
        self.right = new_root.left
        new_root.left = self

        return new_root  # Zwracamy nowy korzeń poddrzewa



tree = TreeNode(3)
tree.insert(1)
tree.insert(0)
tree.insert(2)
tree.insert(5, {"data": "Hello World!"})
tree.insert(6)
tree.insert(4)

tree.inorder_traversal()
print()
print("*" * 10)
tree.reverse_inorder_traversal()
print()
print("*" * 10)
tree.preorder_traversal()
print()
print("*" * 10)
tree.level_order_traversal()
print()
print("*" * 10)
print(tree.height())
tree.rotate_right()
print()
print("*" * 10)
tree.level_order_traversal()

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return "key: {}, height: {}\n".format(self.key, self.height)


class AVL:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is not None:
            return node.height
        else:
            return 0

    def insert(self, key):
        if not self.root:
            print("\nInsert: ", key)
            self.root = Node(key)
            self.print_avl(self.root, "", True, 0)
        else:
            print("\nInsert: ", key)
            self.root = self.insert_rec(key, self.root)
            self.print_avl(self.root, "", True, 0)

    def insert_rec(self, key, node):
        if not node:
            node = Node(key)
        elif key < node.key:
            node.left = self.insert_rec(key, node.left)
        else:
            node.right = self.insert_rec(key, node.right)

        if self.height(node.right) - self.height(node.left) == 2:
            if key < node.right.key:
                node = self.big_l_rotate(node)
            else:
                node = self.small_l_rotate(node)

        if self.height(node.right) - self.height(node.left) == -2:
            if key > node.left.key:
                node = self.big_r_rotate(node)
            else:
                node = self.small_r_rotate(node)
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return node

    def delete(self, key):
        print("\nDelete: ", key)
        self.root = self.delete_rec(key, self.root)
        self.print_avl(self.root, "", True, 0)

    def delete_rec(self, key, node):
        if not node:
            return node
        elif key < node.key:
            node.left = self.delete_rec(key, node.left)
        elif key > node.key:
            node.right = self.delete_rec(key, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            else:
                temp = self.minimum(node.right)
                node.key = temp.key
                node.right = self.delete_rec(temp.key, node.right)

        if self.height(node.right) - self.height(node.left) == 2:
            if self.height(node.right.left) - self.height(node.right.right) > 0:
                node = self.big_l_rotate(node)
            else:
                node = self.small_l_rotate(node)

        if self.height(node.right) - self.height(node.left) == -2:
            if self.height(node.left.left) - self.height(node.left.right) < 0:
                node = self.big_r_rotate(node)
            else:
                node = self.small_r_rotate(node)
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return node

    def minimum(self, node):
        while node.left != None:
            node = node.left
        return node

    def find(self, key, node, a):
        print("\nFind: ", key)
        if node is None:
            a.append("Узел не найден!")
        else:
            if key < node.key:
                print(node.key)
                self.find(key, node.left, a)
            elif key > node.key:
                print(node.key)
                self.find(key, node.right, a)
            else:
                a.append(node)
        return a

    def small_l_rotate(self, node):
        print("\nSmall left rotate")
        b = node.right
        c = b.left
        node.right = c
        b.left = node
        b.height = max(self.height(b.left), self.height(b.right)) + 1
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return b

    def big_l_rotate(self, node):
        print("\nBig left rotate")
        node.right = self.small_r_rotate(node.right)
        self.print_avl(self.root, "", True, 0)
        return self.small_l_rotate(node)

    def small_r_rotate(self, node):
        print("\nSmall right rotate")
        b = node.left
        c = b.right
        node.left = c
        b.right = node
        b.height = max(self.height(b.left), self.height(b.right)) + 1
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return b

    def big_r_rotate(self, node):
        print("\nBig right rotate")
        node.left = self.small_l_rotate(node.left)
        self.print_avl(self.root, "", True, 0)
        return self.small_r_rotate(node)

    def print_avl(self, current, indention, child_r, check):
        if current != None:
            print(indention, end='')
            if not child_r:
                print("L-----", end='')
                indention += "|     "
            else:
                if (current.key == self.root.key and check == 0):
                    print("V-----", end='')
                    check = 1
                else:
                    print("R-----", end='')
                indention += "      "
            print(current.key)
            self.print_avl(current.left, indention, False, check)
            self.print_avl(current.right, indention, True, check)

    def root(self):
        return self.root
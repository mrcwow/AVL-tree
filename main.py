from avl import AVL


if __name__ == '__main__':
    tree_avl = AVL()
    nums = [7, 11, 2, 13, 1]
    for num in nums:
        tree_avl.insert(num)
    tree_avl.insert(5)
    tree_avl.insert(14)
    root1 = tree_avl.root
    a = []
    a = tree_avl.find(111, root1, a)
    for i in a:
        print(i)
    a = []
    a = tree_avl.find(5, root1, a)
    for i in a:
        print(i)
    tree_avl.delete(5)
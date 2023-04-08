from avl import AVL


def top(root, a):
    if root != None:
        a.append(root.key)
        top(root.left, a)
        top(root.right, a)
    return a


def test_bigrightrotate():
    print("\n1")
    tree = AVL()
    nums = [7, 11, 2, 13, 1, 3]
    for num in nums:
        tree.insert(num)
    tree.insert(5)
    tree.delete(13)
    v = top(tree.root, [])
    assert v == [3, 2, 1, 7, 5, 11]


def test_bigleftrotate():
    print("\n2")
    tree = AVL()
    nums = [1, 3, 2]
    for num in nums:
        tree.insert(num)
    v = top(tree.root, [])
    assert v == [2, 1, 3]


def test_delete_all():
    print("\n3")
    tree = AVL()
    nums = [18, 19, 35, 17, 11, 27, 8]
    for num in nums:
        tree.insert(num)
    tree.delete(8)
    tree.delete(27)
    tree.delete(11)
    tree.delete(17)
    tree.delete(35)
    tree.delete(19)
    tree.delete(18)
    v = top(tree.root, [])
    assert v == []


def test_find_all_and_absent():
    print("\n4")
    tree = AVL()
    nums = [5, 7, 8, 1, 15, 17]
    for num in nums:
        tree.insert(num)
    a = []
    tree.find(15, tree.root, a)
    tree.find(1, tree.root, a)
    tree.find(101, tree.root, a)
    tree.find(7, tree.root, a)
    tree.find(17, tree.root, a)
    tree.find(5, tree.root, a)
    tree.find(8, tree.root, a)
    v = []
    for i in a:
        v.append(str(i))
    assert v == ['key: 15, height: 2\n', 'key: 1, height: 1\n', 'Узел не найден!', 'key: 7, height: 3\n', 'key: 17, height: 1\n', 'key: 5, height: 2\n', 'key: 8, height: 1\n']


if __name__ == '__main__':
    test_bigrightrotate()
    test_bigleftrotate()
    test_delete_all()
    test_find_all_and_absent()
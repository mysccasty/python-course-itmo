class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return True
        else:
            if self._insert_recursive(self.root, value):
                return True
            else:
                return False

    def _insert_recursive(self, node, value):
        if value == node.value:
            return False
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
                node.left.parent = node
                return True
            else:
                return self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
                node.right.parent = node
                return True
            else:
                return self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value):
        node = self.search(value)
        if node is None:
            return False
        self._delete_node(node)
        return True

    def _delete_node(self, node):
        if node.left is None:
            self._transplant(node, node.right)
        elif node.right is None:
            self._transplant(node, node.left)
        else:
            successor = self._minimum(node.right)
            if successor.parent != node:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def _minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def print_tree(self):
        self._print_tree_recursive(self.root, "", True)

    def _print_tree_recursive(self, node, indent, last):
        if node is not None:
            print(indent, end="")
            if last:
                print("└─", end="")
                indent += "  "
            else:
                print("├─", end="")
                indent += "| "
            print(node.value)
            last_left = False
            if node.right is None:
                last_left = True
            self._print_tree_recursive(node.left, indent, last_left)
            self._print_tree_recursive(node.right, indent, True)

def main():
    bst = BinarySearchTree()

    while True:
        print("\nБинарное дерево поиска")
        print("1. Вставка элемента")
        print("2. Удаление элемента")
        print("3. Поиск элемента")
        print("4. Вывод дерева")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            value = int(input("Введите число для вставки: "))
            if bst.insert(value):
                print(f"Элемент {value} вставлен")
            else:
                print(f"Элемент {value} уже существует")
        elif choice == "2":
            value = int(input("Введите число для удаления: "))
            if bst.delete(value):
                print(f"Элемент {value} удален.")
            else:
                print(f"Элемент {value} не найден.")
        elif choice == "3":
            value = int(input("Введите число для поиска: "))
            if bst.search(value):
                print(f"Элемент {value} найден.")
            else:
                print(f"Элемент {value} не найден.")
        elif choice == "4":
            print("Бинарное дерево поиска:")
            bst.print_tree()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Повторите ввод:")

if __name__ == "__main__":
    main()
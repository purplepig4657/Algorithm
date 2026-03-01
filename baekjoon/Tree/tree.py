class Node():
    
    def __init__(self):
        self._childs: list[int] = []

    def add_child(self, child_idx: int):
        self._childs.append(child_idx)

    def delete_child(self, child_idx: int):
        self._childs.remove(child_idx)

    def get_child_list(self) -> list[int]:
        return self._childs


class Tree():
    
    def __init__(self, init_node_list_len: int):
        self._node_num: int = init_node_list_len
        self._all_nodes: list[Node | None] = [None for _ in range(init_node_list_len)]
        self._deleted_node_parent_idx: int = -1

    def add_node(self, add_node_idx: int, parent_node_idx: int, idx_to_deleted_node: int) -> bool:
        if add_node_idx < 0 or add_node_idx >= self._node_num or parent_node_idx >= self._node_num:
            raise IndexError("Node index out of range.")


        if parent_node_idx == -1:
            self._all_nodes[add_node_idx] = Node()
            return True
        
        parent_node: Node | None = self._all_nodes[parent_node_idx]

        if parent_node == None:
            return False
        else:
            self._all_nodes[add_node_idx] = Node()
            parent_node.add_child(add_node_idx)
            if add_node_idx == idx_to_deleted_node:
                self._deleted_node_parent_idx = parent_node_idx
            return True

    
    def get_node(self, node_idx: int) -> Node | None:
        if node_idx < 0 or node_idx >= self._node_num:
            raise IndexError("Node index out of range.")
        return self._all_nodes[node_idx]


    def delete_node(self, idx_to_delete: int):
        if idx_to_delete < 0 or idx_to_delete >= self._node_num:
            raise IndexError("Node index out of range.")

        if self._deleted_node_parent_idx == -1:
            return

        deleted_node_parent: Node | None = self._all_nodes[self._deleted_node_parent_idx]

        if deleted_node_parent == None:
            raise IndexError("Not existed parent node index.")

        deleted_node_parent.delete_child(idx_to_delete)

    
    def get_child_node_bool_list(self, node_idx: int, bool_node_list: list[bool]):
        if node_idx < 0 or node_idx >= self._node_num:
            raise IndexError("Node index out of range.")

        node = self.get_node(node_idx)

        if node is None:
            raise IndexError("Node index out of range.")

        node_child_list = node.get_child_list()
        for child_idx in node_child_list:
            bool_node_list[child_idx] = True
            self.get_child_node_bool_list(child_idx, bool_node_list)


def count_leaf_node_recursion(tree: Tree, node: Node, is_visited: list[bool]) -> int:
    child_list = node.get_child_list()
    if len(child_list) == 0:
        return 1
    else:
        count = 0
        for child_idx in child_list:
            if is_visited[child_idx]:
                continue
            child = tree.get_node(child_idx)
            if child is None:
                raise IndexError("Node index out of range.")
            count += count_leaf_node_recursion(tree, child, is_visited)
            is_visited[child_idx] = True
        return count


def count_leaf_node(tree: Tree, node_list_len: int, node_to_deleted: int) -> int:
    count = 0
    is_visited: list[bool] = [False for _ in range(node_list_len)]
    tree.get_child_node_bool_list(node_to_deleted, is_visited)
    is_visited[node_to_deleted] = True
    for idx in range(node_list_len):
        if is_visited[idx]:
            continue
        target_node = tree.get_node(idx)
        if target_node is None:
            raise IndexError("Node index out of range.")
        count += count_leaf_node_recursion(tree, target_node, is_visited)
        is_visited[idx] = True
        
    return count


if __name__ == '__main__':
    N = int(input())
    nodes_info = list(map(int, input().split()))
    node_to_deleted = int(input())

    added_node_checker: list[bool] = [False for _ in range(N)]

    tree = Tree(N)


    while True:
        all_node_added = True
        for idx in range(N):
            if not added_node_checker[idx]:
                all_node_added = False
                child_node_idx = idx
                parent_node_idx = nodes_info[idx]
                if tree.add_node(child_node_idx, parent_node_idx, node_to_deleted):
                    added_node_checker[idx] = True

        if all_node_added:
            break

    
    tree.delete_node(node_to_deleted)


    print(count_leaf_node(tree, N, node_to_deleted))


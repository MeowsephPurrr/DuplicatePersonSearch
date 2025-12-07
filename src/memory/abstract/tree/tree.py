from dataclasses import dataclass

from src.memory.abstract.tree.tree_node import TreeNode


@dataclass
class Tree:
    root: TreeNode

    def __init__(self, root: int | str):
        self.root = TreeNode(root)

    def add_node(self, value: str | int, new_item: int) -> None:
        formatted_value = list(str(value))

        if not self.root:
            self.root = TreeNode(formatted_value[0])

        for char in formatted_value[1:]:
            self.root.add_node(char)

        self.root.add_item(formatted_value[-1], new_item)
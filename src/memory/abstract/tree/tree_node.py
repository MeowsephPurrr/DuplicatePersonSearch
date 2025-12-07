from dataclasses import dataclass


@dataclass
class TreeNode:
    value: int | str
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None
    items: list = None

    def __init__(self, value: int | str) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.items = []

    def add_node(self, new_node: int | str) -> None:
        if new_node < self.value:
            self._add_left(new_node)
            return

        self._add_right(new_node)

    def add_item(self, position_node_value: int | str, new_item: int) -> None:
        if position_node_value == self.value:
            self.items.append(new_item)
            return

        if position_node_value < self.value:
            self.left.add_item(position_node_value, new_item)
            return

        self.right.add_item(position_node_value, new_item)


    def _add_left(self, new_node: int | str) -> None:
        if self.left:
            self.left.add_node(new_node)
            return

        self.left = TreeNode(new_node)

    def _add_right(self, new_node: int | str) -> None:
        if self.right:
            self.right.add_node(new_node)
            return

        self.right = TreeNode(new_node)
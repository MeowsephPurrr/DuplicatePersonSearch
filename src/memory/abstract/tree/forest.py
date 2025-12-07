from dataclasses import dataclass

from src.memory.abstract.tree.tree import Tree


@dataclass
class Forest:
    trees: dict[str, Tree] = None

    def __post_init__(self):
        self.trees = {}

    def build(self, value: str | int, identifier: int) -> None:
        if value not in self.trees:
            self.trees[value] = Tree(value)
            return

        self.trees[value].add_node(value, identifier)

import os
from dataclasses import dataclass

from memory.abstract.abstract import AbstractMemory


@dataclass
class PhoneTree(AbstractMemory):
    db_table = os.environ.get("PHONE_DB_TABLE", "applicant")
    db_field_names = [os.environ.get("PHONE_DB_FIELD", "phone")]

    trees: dict[str, dict] = None

    def __post_init__(self):
        self.trees = {}

    def build(self, record: dict, fields: list[str]) -> None:
        phone_index = fields.index(self.db_field_names[0])
        id_index = fields.index("id")

        phone = record[phone_index]


    def get_indices(self, phone: str) -> list[int]:
        pass
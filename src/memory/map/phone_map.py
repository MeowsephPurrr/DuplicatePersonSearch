import os
from dataclasses import dataclass


@dataclass
class PhoneMap:
    db_table = os.environ.get("PHONE_DB_TABLE", "applicant")
    db_field_names = [os.environ.get("PHONE_DB_FIELD", "phone")]

    map: dict[str, list[int]] = None

    def __post_init__(self):
        self.map = {}

    def build(self, record: dict, fields: list[str]) -> None:
        phone_index = fields.index(self.db_field_names[0])
        id_index = fields.index("id")
        if record[phone_index] not in self.map:
            self.map[record[phone_index]] = []
        self.map[record[phone_index]].append(record[id_index])
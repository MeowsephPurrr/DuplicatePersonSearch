import os
from dataclasses import dataclass

from src.memory.map.phone_map import PhoneMap
from src.db import DB


@dataclass
class SearchMemory:
    """ Defines if the memory is ready to be used """
    ready: bool = False

    name: dict = None
    mail: dict = None
    phone: PhoneMap = None

    def __post_init__(self):
        self.build()

    def _get_memory_map(self) -> dict[str, list[str]]:
        memory_map: dict[str, list[str]] = dict()
        for search_memory in [self.name, self.mail, self.phone]:
            if not search_memory:
                continue
            table_name = search_memory.db_table
            if not table_name in memory_map:
                memory_map[table_name] = ["id"]

            memory_map[table_name].append(*search_memory.db_field_names)

        return memory_map

    def build(self) -> None:
        """
            Builds the search memory. Sets the Memory temporary as not ready.
        """

        memories = list()
        if os.environ.get("USE_PHONE"):
            self.phone = PhoneMap()
            memories.append(self.phone)

        memory_map = self._get_memory_map()
        for table_name, fields in memory_map.items():
            with DB() as db:
                batch = db.get_records_in_batches(table_name, fields)
                for record in batch:
                    [memory.build(record, fields) for memory in memories if memory.db_table == table_name]


        self.ready = True


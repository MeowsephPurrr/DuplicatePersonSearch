from abc import ABC, abstractmethod

class AbstractMemory(ABC):
    db_table: str
    db_field_names: list[str]

    @abstractmethod
    def build(self, record: dict, fields: list[str]) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_indices(self, *args: any, **kwargs: any) -> list[int]:
        raise NotImplementedError()
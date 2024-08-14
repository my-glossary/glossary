import datetime
from datetime import date


class Employee:
    """Employee class."""

    def __init__(self, name: str, birth_date: str) -> None:
        """Construct the employee."""
        self.name = name
        self.birth_date = birth_date

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value.upper()

    @property
    def birth_date(self) -> datetime.date:
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: str) -> None:
        self._birth_date = date.fromisoformat(value)

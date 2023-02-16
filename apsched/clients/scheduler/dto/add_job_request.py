from typing import Any
from pydantic import BaseModel
from .triggers import TriggerDto


class AddJobRequestDto(BaseModel):
    """
    Модель запроса на создание периодической задачи.

    :param func: Классификатор исполняемой задачи в формате <модуль>:<функция модуля>.
    :param trigger: Параметры периодичности запуска задачи.
    :param args: Неключевые аргументы задачи.
    :param kwargs: Ключевые аргументы задачи.
    :param id_on_args: Идентифицировать ли задачу по ее классификатору и аргументам.
    """

    func: str
    name: str
    trigger: TriggerDto
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    id_on_args: bool

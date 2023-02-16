from typing import Any
from datetime import datetime
from pydantic import BaseModel
from .triggers import Trigger


class AddJobRequest(BaseModel):
    """
    Модель запроса на создание периодической задачи.

    :param func: Классификатор исполняемой задачи в формате <модуль>:<функция модуля>.
    :param trigger: Параметры периодичности запуска задачи.
    :param id:
    :param args: Неключевые аргументы задачи.
    :param kwargs: Ключевые аргументы задачи.
    :param id_on_args: Идентифицировать ли задачу по ее классификатору и аргументам.
    :param start_time: Время, с которого начинается планирование задачи на исполнение.
    """

    func: str
    name: str
    id: str | None
    trigger: Trigger
    args: tuple[Any, ...]
    kwargs: dict[str, Any]

from typing import Any
from dramatiq.generic import generic_actor


class BaseTaskMeta(generic_actor):
    """
    Workaround над неспособностью Dramatiq извлекать поля из миксинов к Meta.
    """

    def __new__(mcls, name: str, bases: tuple[type], attrs: dict[str, Any]):
        Meta = attrs.get("Meta")
        if Meta is not None:
            for base in reversed(bases):
                BaseMeta = getattr(base, "Meta", None)
                if BaseMeta is None:
                    continue
                for key in dir(BaseMeta):
                    if hasattr(Meta, key):
                        continue
                    value = getattr(BaseMeta, key)
                    setattr(Meta, key, value)
        return super().__new__(mcls, name, bases, attrs)

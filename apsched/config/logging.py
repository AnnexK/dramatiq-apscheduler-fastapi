import logging
import logging.config
from sys import stdout

_loglevel = logging.DEBUG

logging_settings = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(name)s: %(levelname)s - %(message)s",
            "datefmt": "%d.%m.%y %H:%M:%S",
        },
    },
    "handlers": {
        "stdHandler": {
            "class": "logging.StreamHandler",
            "level": _loglevel,
            "formatter": "default",
            "stream": stdout,
        },
    },
    "loggers": {
        "__main__": {
            "handlers": ["stdHandler"],
        },
    },
    "root": {
        "handlers": ["stdHandler"],
        "level": _loglevel,
    },
}

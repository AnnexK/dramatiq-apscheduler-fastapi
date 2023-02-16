"""
Модуль для запуска Dramatiq.
Связывает Dramatiq с брокером из config и импортирует все классы задач.
"""

import apsched.broker.set_broker

from apsched.tasks.instant import *
from apsched.tasks.periodic import *

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

from apsched.config.app_config import settings

broker = RabbitmqBroker(url=settings.SCHEDULER.BROKER.RMQ.URL)
broker.declare_queue(settings.SCHEDULER.BROKER.QUEUE_NAME)
dramatiq.set_broker(broker)

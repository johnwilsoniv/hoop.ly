from redis import Redis
from rq import Queue, Worker
from hooply.market.pipeline import DEFAULT_QUEUE_NAME


def init_pipeline():
    # Initialize redis queue (if fresh is specified)
    #                         -> queue tasks
    #                          -> schedule periodic jobs
    redis = Redis()
    queue = Queue(DEFAULT_QUEUE_NAME)
    # Load queue with job

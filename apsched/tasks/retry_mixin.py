class RetryMixin:
    max_retries = 5
    min_backoff = 10
    max_backoff = 120

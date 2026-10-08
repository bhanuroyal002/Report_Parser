import os

bind = f"{os.getenv('HOST', '0.0.0.0')}:{os.getenv('PORT', '8080')}"
workers = int(os.getenv('WEB_CONCURRENCY', '2'))
worker_class = "sync"
timeout = int(os.getenv('GUNICORN_TIMEOUT', '900'))
keepalive = 5
accesslog = "-"
errorlog = "-"
loglevel = os.getenv('GUNICORN_LOG_LEVEL', 'info')

# Large certification ZIP uploads can take time to parse.
limit_request_line = 8190

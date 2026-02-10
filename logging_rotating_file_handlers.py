import logging
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# after log file size of app.log crosses threshold of 2000 bytes
# it will roll it over to app.log.1, in this way it will create backup of 5 as mentioned till app.log.5
# app.log + 5 backups (so total 6)
handler=RotatingFileHandler(
    'app.log',maxBytes=2000,backupCount=5
)
stream_handler = logging.StreamHandler() # prints to console

logger.addHandler(handler)
logger.addHandler(stream_handler)

for _ in range(10000):
    logger.info("Hello WORLD!")

#TIMEROTATINGFILEHANDLER

# app.log will be rolled over to app.log.<timestamp> every 5 seconds 5 backups of such will be preserved.
# app.log + 5 backups (so total 6)
handler_timed = TimedRotatingFileHandler(
    'app.log',when='s',interval=5,
    backupCount=5
)
logger.addHandler(handler)
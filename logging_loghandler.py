# LOG_HANDLER: Log handlers are responsbile to send log messages to standard output stream or to a file

import logging
#logging.basicConfig(level=logging.DEBUG)
# will add one more stream handler to logger by default
# thus we should comment it if already are adding one!!
logger = logging.getLogger(__name__)

#EVEN IF WE SET
# log level at handler level as DEBUG we need to set logger level as DEBUG otherwise it wont work!!
# If we set warning here and at handler level set debug and try to log debug then it wont work!
logger.setLevel(logging.DEBUG)

# STREAM HANDLER
stream_h = logging.StreamHandler()

# FILE HANDLER
file_h = logging.FileHandler('file.log')

# SET THE LEVEL and FORMATTER for the log handler
stream_h.setLevel(logging.DEBUG)
file_h.setLevel(logging.WARNING)

# DEFINE A FORMATTER
formatter = logging.Formatter('%(name)s - %(levelname)s -%(message)s')

# SETTING Formatter to handler
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# Add handler to logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.debug("hello world")
logger.warning("I maybe printed in file log")
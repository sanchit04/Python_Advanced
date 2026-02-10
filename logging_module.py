# BUILTIN logging module is available in python

import logging

# We can log 5 different log levels
# logging.debug("I am debug")
# logging.info("I am info")
# logging.warning("I am warning")
# logging.error("I am error")
# logging.critical("I am critical")

# OP: (INFO and DEBUG are not shown since bydefault logging level is set at WARN)
# WARNING:root:I am warning
# ERROR:root:I am error
# CRITICAL:root:I am critical

# In order to change this we need to setup logging configuration:
# Below sets it to highest level that is DEBUG
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("I am debug")
# logging.info("I am info")
# logging.warning("I am warning")
# logging.error("I am error")
# logging.critical("I am critical")

# Changing formatting of logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M')

logging.debug("I am debug")
logging.info("I am info")
logging.warning("I am warning")
logging.error("I am error")
logging.critical("I am critical")

#OP:
# 02/10/2026 06:54 - root - DEBUG - I am debug
# 02/10/2026 06:54 - root - INFO - I am info
# 02/10/2026 06:54 - root - WARNING - I am warning
# 02/10/2026 06:54 - root - ERROR - I am error
# 02/10/2026 06:54 - root - CRITICAL - I am critical

# BY-DEFAULT NAME OF logger will be set as root logger (As a best practise we should have logger name for each module)
import logging_module_helper

#OP:
# 02/10/2026 06:59 - root - DEBUG - I am debug
# 02/10/2026 06:59 - root - INFO - I am info
# 02/10/2026 06:59 - root - WARNING - I am warning
# 02/10/2026 06:59 - root - ERROR - I am error
# 02/10/2026 06:59 - root - CRITICAL - I am critical
# 02/10/2026 06:59 - logging_module_helper - DEBUG - Hello I am logged from the helper

# IF WE WANT TO STOP LOGGING FROM HELPER MODULE
# IN HELPER MODULE add logger.propagate=False (this will block propagation of logs from helper module)
#OP: no more logging from helper even after we have imported logging_module_helper
# 02/10/2026 07:02 - root - DEBUG - I am debug
# 02/10/2026 07:02 - root - INFO - I am info
# 02/10/2026 07:02 - root - WARNING - I am warning
# 02/10/2026 07:02 - root - ERROR - I am error
# 02/10/2026 07:02 - root - CRITICAL - I am critical
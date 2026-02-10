# CAPTURE STACK TRACES with exc_info

import logging

try:
    var1=5/0
except ZeroDivisionError as e:
    logging.error(e)

# OP:
#ERROR:root:division by zero

try:
    var1=5/0
except ZeroDivisionError as e:
    #print(e,exc_info=True) -> ERROR exc_info works only with logging!!
    logging.error(e,exc_info=True)

#OP:
# ERROR:root:division by zero
# Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/PYTHON_ADVANCED/logging_capture_stack_traces.py", line 11, in <module>
#     var1=5/0
# ZeroDivisionError: division by zero
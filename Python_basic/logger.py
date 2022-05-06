import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# console handler
ch = logging.StreamHandler()

# file handler
fh = logging.FileHandler(filename="logfile.log")
fh.setLevel(logging.INFO)
fh.setFormatter(logging.Formatter("%(levelname)s %(asctime)s - %(message)s"))

logger.addHandler(ch)
logger.addHandler(fh)

logger.critical("Our First Log Message")
logger.debug("print console but does not log to file")

try:
    print(1/0)
except Exception as e:
    logger.critical('error occurred', exc_info=e)


# def handle_exception(exc_type, exc_value, exc_traceback):
#     # ignore traceback to auto close app. except keyboard interrupt
#     if issubclass(exc_type, KeyboardInterrupt):
#         sys.__excepthook__(exc_type, exc_value, exc_traceback)
#         return
#
#     logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
#
#
# sys.excepthook = handle_exception
#
# print(1/0)
# try:
#     print(1 / 0)
# except ZeroDivisionError as e:
#     logger.critical('error', exc_info=e)

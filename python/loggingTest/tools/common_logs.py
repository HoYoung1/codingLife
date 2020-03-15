# Logging
import logging
import logging.handlers

_logger = logging.getLogger(__name__)

_formater = logging.Formatter("[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)s] %(message)s")

_streamHandler = logging.StreamHandler()
#_fileHandler = logging.FileHandler("./logs/log.log")
_fileMaxBytes = 1024 * 1024 * 100 # 100mb
_fileHandler = logging.handlers.RotatingFileHandler("./logs/log.log", maxBytes=_fileMaxBytes, backupCount=5)

_streamHandler.setFormatter(_formater)
_fileHandler.setFormatter(_formater)

_logger.addHandler(_streamHandler)
_logger.addHandler(_fileHandler)

_logger.setLevel(level=logging.DEBUG)


import logging
import logging.config

logging.config.fileConfig('conf/logging.conf', defaults={'fileHandlerLog': 'logs/run_script.log'})
logger = logging.getLogger(__name__)

logger.info("__all__ applies to the situation where from foo.bar import *")

__all__ = [
    'logger'
]
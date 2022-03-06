import logging

# setup logging environment
logger = logging.getLogger(__name__)

def specific_func():
    logger.info(f'logger name: {logger.name}')
    logger.info(f'--- starting {__name__} ---')
    logger.warning(f"-- something didn't work out ---")
    logger.error(f'--- run_script complete ---')
    return None
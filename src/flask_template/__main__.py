import logging
import logging.config

if __name__ == "__main__":

    # setup logging environment
    logging.config.fileConfig('conf/logging.conf', defaults={'fileHandlerLog': 'logs/flask_template.log'})
    logger = logging.getLogger(__name__)
    
    logger.info(f'only applies to python -m flask_template')
    print("only applies to python -m flask_template")
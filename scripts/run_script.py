import argparse
import configparser
import logging
import logging.config
from flask_template.funcs import specific_func

# setup logging environment
logging.config.fileConfig('conf/logging.conf', defaults={'fileHandlerLog': 'logs/run_script.log'})
logger = logging.getLogger(__name__)

if __name__ == "__main__":

    # parse arguments
    parser = argparse.ArgumentParser(description='python bioler-plate template')
    parser.add_argument('required_argument', type=str, help='required script argument')
    parser.add_argument('-opt', '--optional', default=None, help='optional script argument')
    args = parser.parse_args()

    # config_parser
    cparser = configparser.ConfigParser()
    cparser.read('conf/pipeline_hidden.conf')
    access_key = cparser.get('aws_boto_credentials', 'access_key')
    secrey_key = cparser.get('aws_boto_credentials', 'secret_key')

    # application logic
    logger.info(f'logger name: {logger.name}')
    logger.info(f'starting main: __name__: {__name__}')
    specific_func()

    


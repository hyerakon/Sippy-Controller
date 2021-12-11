from datetime import date
import logging

import os
THIS_FOLDER = './sippycontroller/logs'
os.makedirs(THIS_FOLDER, exist_ok=True)

info_file = os.path.join(THIS_FOLDER, 'info.log')
warning_file = os.path.join(THIS_FOLDER, 'warning.log')
error_file = os.path.join(THIS_FOLDER, 'error.log')
critical_file = os.path.join(THIS_FOLDER, 'critical.log')

formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

def setup_logger(name, log_file, level):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def command_log(who, what):
    today = date.today().strftime("%d/%m/%Y")
    
    logger = setup_logger('Info_Logger', info_file, level=logging.INFO)
    
    print(f'{today}: {what} - {who}')
    logger.info(f'{what} - {who}')

def warning_log(who, what):
    today = date.today().strftime("%d/%m/%Y")
    
    logger = setup_logger('Warning_Logger', warning_file, level=logging.WARNING)
    
    print(f'{today}: {what} - {who}')
    logger.warning(f'{what} - {who}')

def error_log(who, what):
    today = date.today().strftime("%d/%m/%Y")
    
    logger = setup_logger('Error_Logger', error_file, level=logging.ERROR)
    
    print(f'{today}: {what} - {who}')
    logger.error(f'{what} - {who}')

def critical_log(who, what):
    today = date.today().strftime("%d/%m/%Y")
    
    logger = setup_logger('Critical_Logger', critical_file, level=logging.CRITICAL)
    
    print(f'{today}: {what} - {who}')
    logger.critical(f'{what} - {who}')

def _test():
    command_log('test', 'TEST: Command Log')
    error_log('test', 'TEST: Error Log')
    warning_log('test', 'TEST: Warning Log')
    critical_log('test', 'TEST: Critical Log')

if __name__ == "__main__":
    _test()

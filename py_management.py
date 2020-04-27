import logging.config

# Bootstrap logging framework
logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.info('PyManagement Startup')
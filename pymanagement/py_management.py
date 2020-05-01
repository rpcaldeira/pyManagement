import logging.config
import platform

# Bootstrap logging framework
logging.config.fileConfig(fname='pyManagement/logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.info('PyManagement Startup')

logger.info()
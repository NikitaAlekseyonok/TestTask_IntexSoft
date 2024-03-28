import sys

from loguru import logger


class Logger:
    __logger = logger
    __logger.remove(0)

    __logger.add(sys.stderr, format="<blue>[{level}]</blue> : <green>{message}</green>", colorize=True)


    @staticmethod
    def info(message):
        Logger.__logger.info(message)

    @staticmethod
    def debug(message):
        Logger.__logger.debug(message)

    @staticmethod
    def warning(message):
        Logger.__logger.warning(message)

    @staticmethod
    def error(message):
        Logger.__logger.error(message)

    @staticmethod
    def step(message: str):
        def step_decorator(step_method):
            Logger.__logger.info(f'STEP: {message}')
            return step_method

        return step_decorator


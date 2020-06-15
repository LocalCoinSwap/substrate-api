import inspect
import logging
import sys

from logstash_async.handler import AsynchronousLogstashHandler

from .settings import DEBUG_STATUS
from .settings import LOGSTASH
from .settings import UNIFIED_LOGGING

logger = logging.getLogger(LOGSTASH["name"])
# loglevel threshold (add it as an option to LOGSTASH?)
logger.setLevel(logging.DEBUG)

if UNIFIED_LOGGING:
    logger.addHandler(
        AsynchronousLogstashHandler(
            LOGSTASH["host"], LOGSTASH["port"], database_path=None
        )
    )
else:
    # more verbose formatting for local logs (stdout or uwsgi logs)
    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s] %(message)s")
    stream_handler.setFormatter(stream_formatter)
    logger.addHandler(stream_handler)


class Logger:
    def __init__(
        self, module="", use_module=True, use_class_name=True, use_function_name=True
    ):
        self.logger = logger
        self.module = module
        self.use_module = use_module
        self.use_class_name = use_class_name
        self.use_function_name = use_function_name

    @property
    def class_name(self):
        try:
            return type(inspect.stack()[3].frame.f_locals["self"]).__name__
        except:
            return "None"

    @property
    def func_name(self):
        try:
            return inspect.stack()[3].function
        except:
            return "None"

    @property
    def path(self):
        try:
            return inspect.stack()[3].filename
        except:
            return "None"

    @property
    def extra_params(self):
        ns = []
        if self.use_module:
            ns.append(self.module)
        if self.use_class_name:
            ns.append(self.class_name)
        if self.use_function_name:
            ns.append(self.func_name)

        return {"namespace": ":".join(ns), "path": self.path}

    def error(self, *args, **kwargs):
        self.logger.error(*args, **kwargs, extra=self.extra_params)

    def info(self, *args, **kwargs):
        self.logger.info(*args, **kwargs, extra=self.extra_params)

    def debug(self, *args, **kwargs):
        self.logger.debug(*args, **kwargs, extra=self.extra_params)

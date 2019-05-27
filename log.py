#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


logging.basicConfig(
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.StreamHandler()
    ],
    level=logging.INFO
)


class Log:

    def info(self, message: str):
        logging.info(message)

    def error(self, message: str):
        logging.error(message)

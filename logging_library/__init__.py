""" this is module level logging. """

import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())


def library(*args, **kwargs):
    if len(args) > 2:
        logging.warning("that's a log of args: {}".format(args))
    logging.debug('here are the args: {}\t\there are the kwargs: {}'.format(args, kwargs))

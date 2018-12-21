""" this is root level logging.  i want to see how module level logging works from the root """

import json
import logging
from logging_library import library


class JSONFormatter(logging.Formatter):
    """ convert a log to json.

    Nothing fancy, same input as you are used to except disregard all your nice dashes spaces, semicolons, etc and
    return json data.  Would be pretty standard as far as parsing logs goes.
    """

    def format(self, record):
        return json.dumps({_: record.__dict__[_] for _ in record.__dict__ if record.__dict__[_] is not None})

    @classmethod
    def make_json_formatter(cls, formatter):
        return cls(formatter._fmt)


def main():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        'time:%(asctime)s -process:%(process)s - name:%(name)s - path:%(pathname)s - module:%(module)s - func:%(funcName)s - lineno:%(lineno)d - level:%(levelname)s - message:%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # suppose you have a stream handler, but you want to log json to a file
    fh = logging.FileHandler(filename='logging_root' + '.log')
    fh.setLevel(logging.INFO)
    json_formatter = JSONFormatter.make_json_formatter(formatter)
    fh.setFormatter(json_formatter)
    logger.addHandler(fh)

    logging.info('Started')
    library(1, 2, 3, 4, 5, a=1)
    logging.info('Finished')


if __name__ == '__main__':
    main()

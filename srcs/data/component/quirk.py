from enum import Enum

class QuirkType(Enum):
    PREFIX = "Prefix"
    SUFFIX = "Suffix"
    REPLACE = "Simple Replace"
    REGEXP = "Regexp Replace"
    RANDOM = "Random Replace"
    SPELLING = "Mispeller"

class Quirk:
    source: str     # "from" field
    dest: str       # "to" field
    enabled: bool   # "on" field
    group: str      # "group" field
    type: QuirkType # "type" field

    def __init__(self):
        raise NotImplementedError

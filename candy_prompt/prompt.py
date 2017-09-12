# -*- coding:utf-8 -*-

import prompt_toolkit

from .completer import *
from .validator import *
from enum import Enum
from prompt_toolkit.history import FileHistory
from candy import path
from candy.utils.convertor import str2boo


class Converter(object):
    def __init__(self, convert_func, validator):
        self.convert_func = convert_func
        self.validator = validator

    def convert(self, data):
        return self.convert_func(data)


class PromptType(Enum):
    STR = Converter(str, StrValidator())
    INT = Converter(int, IntValidator())
    BOOL = Converter(str2boo, BoolValidator())
    FLOAT = Converter(float, FloatValidator())
    LIST = Converter(list, ListValidator())
    DICT = Converter(dict, ListValidator())
    DIR = Converter(str, DirValidator())
    FILE = Converter(str, FileValidator())


def prompt(message, type='STR', default=None, multiline=False, history=None):
    if history is None:
        history = FileHistory(os.path.join(path.HOME, '.prompt_history'))
    converter = getattr(PromptType, type)
    completer = WordCompleter(words=[], history=history)
    res = prompt_toolkit.prompt(message, default=default or '', history=history,
                                validator=converter.value.validator, completer=completer, multiline=multiline)
    return converter.value.convert(res)


def prompt_list(message, type='STR', default=None, completions=None, multiline=False, history=None):
    if history is None:
        history = FileHistory(os.path.join(path.HOME, '.prompt_history'))
    converter = getattr(PromptType, type)
    completer = WordCompleter(words=completions, history=history)
    res = prompt_toolkit.prompt(message, default=default or '', history=history,
                                validator=converter.value.validator, completer=completer, multiline=multiline)
    return converter.value.convert(res)


def prompt_path(message, root, type='DIR', recursion=False, default=None):
    converter = getattr(PromptType, type)
    completer = PathCompleter(root, match_type=type, recursion=recursion)
    res = prompt_toolkit.prompt(message, default=default or '', completer=completer,
                                validator=converter.value.validator)
    return converter.value.convert(res)

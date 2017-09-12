# -*- coding:utf-8 -*-

import os
import sys
import ast

# sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import prompt_toolkit

from candy_prompt.completer import *
from candy_prompt.validator import *
from candy_prompt.history import PromptFileHistory as FileHistory
from enum import Enum
from candy import path


class PromptType(Enum):
    STR = StrValidator()
    INT = IntValidator()
    BOOL = BoolValidator()
    FLOAT = FloatValidator()
    LIST = ListValidator()
    DICT = ListValidator()
    DIR = DirValidator()
    FILE = FileValidator()


def prompt(message, type='STR', default=None, multiline=False, history=None):
    history = FileHistory(history or os.path.join(path.HOME, '.prompt_history'))
    converter = getattr(PromptType, type)
    completer = WordCompleter(words=[], history=history)
    res = prompt_toolkit.prompt(message, default=default or '', history=history,
                                validator=converter.value, completer=completer, multiline=multiline)
    return ast.literal_eval(res)


def prompt_list(message, type='STR', default=None, completions=None, multiline=False, history=None):
    history = FileHistory(history or os.path.join(path.HOME, '.prompt_history'))
    converter = getattr(PromptType, type)
    completer = WordCompleter(words=completions, history=history)
    res = prompt_toolkit.prompt(message, default=default or '', history=history,
                                validator=converter.value, completer=completer, multiline=multiline)
    return ast.literal_eval(res)


def prompt_path(message, root, type='DIR', recursion=False, default=None):
    converter = getattr(PromptType, type)
    completer = PathCompleter(root, match_type=type, recursion=recursion)
    res = prompt_toolkit.prompt(message, default=default or '', completer=completer,
                                validator=converter.value)
    return ast.literal_eval(res)

# -*- coding:utf-8 -*-

import os
import json
from prompt_toolkit.validation import Validator, ValidationError


class StrValidator(Validator):
    def validate(self, document):
        pass


class IntValidator(Validator):
    def validate(self, document):
        text = document.text
        for index, char in enumerate(text):
            if not char.isdigit():
                raise ValidationError(message='Input contains non-numeric char', cursor_position=index)


class FloatValidator(Validator):
    def validate(self, document):
        text = document.text
        try:
            float(text)
        except ValueError:
            raise ValidationError(message='Input must be float')


class BoolValidator(Validator):
    def validate(self, document):
        from candy_enums.boolstrs import BoolStrs
        text = document.text
        if text.lower() not in BoolStrs.BOOL.value:
            raise ValidationError('Input must be one of {}'.format(BoolStrs.BOOL.value))


class ListValidator(Validator):
    def validate(self, document):
        text = document.text
        try:
            list(text)
        except ValueError:
            raise ValidationError('Input must be list')


class DictValidator(Validator):
    def validate(self, document):
        text = document.text
        try:
            json.loads(text)
        except ValueError:
            raise ValidationError('Input must be json')


class DirValidator(Validator):
    def validate(self, document):
        text = document.text
        if not (os.path.exists(text) and os.path.isdir(text)):
            raise ValidationError('Input must be valid dir path')


class FileValidator(Validator):
    def validate(self, document):
        text = document.text
        if not (os.path.exists(text) and os.path.isfile(text)):
            raise ValidationError('Input must be valid file path')
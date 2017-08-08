#!/usr/bin/env python
# encoding: utf-8

import pytest
import datetime
from itertools import zip_longest
from tbone.data.fields import *
from tbone.data.models import *


def test_model_repr():
    ''' Test Model repr function '''
    class M(Model):
        pass
    m = M()
    assert repr(m) == '<M instance>'


def test_model_creation_and_export():
    '''
    Simple model creation test
    '''
    class M(Model):
        name = StringField()
        age = IntegerField()
        decimal = FloatField()
        dt = DateTimeField()

    m = M({'name': 'Ron Burgundy', 'age': 45, 'decimal': '34.77', 'dt': '2017-07-25T12:34:14.414471'})

    # convert model to primitive form
    data = m.to_data()
    # check result is dict
    assert isinstance(data, dict)
    # check keys match
    assert all(a == b for a, b in zip_longest(m._fields.keys(), data.keys(), fillvalue=None))


def test_model_import():
    class M(Model):
        first_name = StringField()
        last_name = StringField()

    m = M()
    m.import_data({'first_name': 'Ron', 'last_name': 'Burgundy'})
    data = m.to_data()

    assert data['first_name'] == 'Ron'
    assert data['last_name'] == 'Burgundy'


def test_model_export_decorator():
    class M(Model):
        first_name = StringField()
        last_name = StringField()

        @export
        def full_name(self):
            return '{} {}'.format(self.first_name, self.last_name)

    m = M({'first_name': 'Ron', 'last_name': 'Burgundy'})
    data = m.to_data()

    assert data['first_name'] == 'Ron'
    assert data['last_name'] == 'Burgundy'
    assert 'full_name' in data
    assert data['full_name'] == 'Ron Burgundy'


def test_model_items():
    class M(Model):
        first_name = StringField()
        last_name = StringField()
        dob = DateTimeField()

    data = {'first_name': 'Ron', 'last_name': 'Burgundy', 'dob': datetime.datetime.now()}
    mo = M(data)
    for key, value in mo.items():
        assert value == data[key]


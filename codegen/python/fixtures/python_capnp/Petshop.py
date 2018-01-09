"""
Auto-generated class for Petshop
"""
import capnp
import os
from .Cat import Cat
from six import string_types

from . import client_support

dir = os.path.dirname(os.path.realpath(__file__))


class Petshop(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type cats: list[Cat]
        :type name: str
        :rtype: Petshop
        """

        return Petshop(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Petshop'
        data = json or kwargs

        # set attributes
        data_types = [Cat]
        self.cats = client_support.set_property('cats', data, data_types, False, [], True, True, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

    def to_capnp(self):
        """
        Load the class in capnp schema Petshop.capnp
        :rtype bytes
        """
        template = capnp.load('%s/Petshop.capnp' % dir)
        return template.Petshop.new_message(**self.as_dict()).to_bytes()


class PetshopCollection:
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def new(binary=None):
        """
        Load the binary of Petshop.capnp into class Petshop
        :type binary: bytes. If none creates an empty capnp object.
        rtype: Petshop
        """
        template = capnp.load('%s/Petshop.capnp' % dir)
        struct = template.Petshop.from_bytes(binary) if binary else template.Petshop.new_message()
        return Petshop(**struct.to_dict(verbose=True))
# encoding: utf-8
# module samba.dcerpc.srvsvc
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/srvsvc.so
# by generator 1.143
""" srvsvc DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class NetTransportInfo2(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    addr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    addr_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    net_addr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default




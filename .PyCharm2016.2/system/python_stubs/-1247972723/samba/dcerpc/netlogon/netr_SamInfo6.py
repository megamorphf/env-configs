# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/netlogon.so
# by generator 1.143
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netr_SamInfo6(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dns_domainname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    principle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sidcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unknown4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default




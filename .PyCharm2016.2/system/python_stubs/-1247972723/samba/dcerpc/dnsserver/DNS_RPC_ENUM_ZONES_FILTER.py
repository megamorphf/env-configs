# encoding: utf-8
# module samba.dcerpc.dnsserver
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/dnsserver.so
# by generator 1.143
""" dnsserver DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DNS_RPC_ENUM_ZONES_FILTER(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    dwFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwReserved0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwRpcStructureVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pszPartitionFqdn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pszQueryString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pszReserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default




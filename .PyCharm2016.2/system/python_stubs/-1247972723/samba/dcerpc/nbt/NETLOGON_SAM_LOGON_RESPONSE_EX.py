# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/nbt.so
# by generator 1.143
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class NETLOGON_SAM_LOGON_RESPONSE_EX(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    client_site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dns_domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain_uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lm20_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lmnt_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_closest_site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nt_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pdc_dns_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pdc_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sbz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sockaddr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sockaddr_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default




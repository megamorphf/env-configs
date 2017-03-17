# encoding: utf-8
# module _ldap
# from /usr/local/lib/python2.7/dist-packages/_ldap.so
# by generator 1.143
# no doc

# imports
import ldap as __ldap


# Variables with simple values

API_VERSION = 3001

AUTH_NONE = 0
AUTH_SIMPLE = 128

AVA_BINARY = 2
AVA_NONPRINTABLE = 4
AVA_NULL = 0
AVA_STRING = 1

CONTROL_ASSERT = '1.3.6.1.1.12'
CONTROL_MANAGEDSAIT = '2.16.840.1.113730.3.4.2'
CONTROL_PAGEDRESULTS = '1.2.840.113556.1.4.319'
CONTROL_PASSWORDPOLICYREQUEST = '1.3.6.1.4.1.42.2.27.8.5.1'
CONTROL_PASSWORDPOLICYRESPONSE = '1.3.6.1.4.1.42.2.27.8.5.1'

CONTROL_POST_READ = '1.3.6.1.1.13.2'

CONTROL_PRE_READ = '1.3.6.1.1.13.1'

CONTROL_PROXY_AUTHZ = '2.16.840.1.113730.3.4.18'

CONTROL_RELAX = '1.3.6.1.4.1.4203.666.5.12'
CONTROL_SORTREQUEST = '1.2.840.113556.1.4.473'
CONTROL_SORTRESPONSE = '1.2.840.113556.1.4.474'
CONTROL_SUBENTRIES = '1.3.6.1.4.1.4203.1.10.1'
CONTROL_SYNC = '1.3.6.1.4.1.4203.1.9.1.1'

CONTROL_SYNC_DONE = '1.3.6.1.4.1.4203.1.9.1.3'
CONTROL_SYNC_STATE = '1.3.6.1.4.1.4203.1.9.1.2'

CONTROL_VALUESRETURNFILTER = '1.2.826.0.1.3344810.2.3'

DEREF_ALWAYS = 3
DEREF_FINDING = 2
DEREF_NEVER = 0
DEREF_SEARCHING = 1

DN_FORMAT_AD_CANONICAL = 80

DN_FORMAT_DCE = 48
DN_FORMAT_LDAP = 0
DN_FORMAT_LDAPV2 = 32
DN_FORMAT_LDAPV3 = 16
DN_FORMAT_MASK = 240
DN_FORMAT_UFN = 64

DN_PEDANTIC = 61440
DN_PRETTY = 256

DN_P_NOLEADTRAILSPACES = 4096
DN_P_NOSPACEAFTERRDN = 8192

DN_SKIP = 512

LIBLDAP_R = 1

MOD_ADD = 0
MOD_BVALUES = 128
MOD_DELETE = 1
MOD_INCREMENT = 3
MOD_REPLACE = 2

MSG_ALL = 1
MSG_ONE = 0
MSG_RECEIVED = 2

NO_LIMIT = 0

OPT_API_FEATURE_INFO = 21

OPT_API_INFO = 0

OPT_CLIENT_CONTROLS = 19

OPT_CONNECT_ASYNC = 20496

OPT_DEBUG_LEVEL = 20481

OPT_DEFBASE = 20489
OPT_DEREF = 2
OPT_DESC = 1

OPT_DIAGNOSTIC_MESSAGE = 50

OPT_ERROR_NUMBER = 49
OPT_ERROR_STRING = 50

OPT_HOST_NAME = 48

OPT_MATCHED_DN = 51

OPT_NETWORK_TIMEOUT = 20485

OPT_OFF = 0
OPT_ON = 1

OPT_PROTOCOL_VERSION = 17

OPT_REFERRALS = 8
OPT_REFHOPLIMIT = 20483
OPT_RESTART = 9

OPT_SERVER_CONTROLS = 18

OPT_SIZELIMIT = 3
OPT_SUCCESS = 0
OPT_TIMELIMIT = 4
OPT_TIMEOUT = 20482
OPT_URI = 20486

OPT_X_KEEPALIVE_IDLE = 25344
OPT_X_KEEPALIVE_INTERVAL = 25346
OPT_X_KEEPALIVE_PROBES = 25345

OPT_X_SASL_AUTHCID = 24834
OPT_X_SASL_AUTHZID = 24835
OPT_X_SASL_MECH = 24832
OPT_X_SASL_NOCANON = 24843
OPT_X_SASL_REALM = 24833
OPT_X_SASL_SECPROPS = 24838
OPT_X_SASL_SSF = 24836

OPT_X_SASL_SSF_EXTERNAL = 24837
OPT_X_SASL_SSF_MAX = 24840
OPT_X_SASL_SSF_MIN = 24839

OPT_X_SASL_USERNAME = 24844

OPT_X_TLS = 24576

OPT_X_TLS_ALLOW = 3
OPT_X_TLS_CACERTDIR = 24579
OPT_X_TLS_CACERTFILE = 24578
OPT_X_TLS_CERTFILE = 24580

OPT_X_TLS_CIPHER_SUITE = 24584

OPT_X_TLS_CRLCHECK = 24587
OPT_X_TLS_CRLFILE = 24592

OPT_X_TLS_CRL_ALL = 2
OPT_X_TLS_CRL_NONE = 0
OPT_X_TLS_CRL_PEER = 1

OPT_X_TLS_CTX = 24577
OPT_X_TLS_DEMAND = 2
OPT_X_TLS_DHFILE = 24590
OPT_X_TLS_HARD = 1
OPT_X_TLS_KEYFILE = 24581
OPT_X_TLS_NEVER = 0
OPT_X_TLS_NEWCTX = 24591
OPT_X_TLS_PACKAGE = 24593

OPT_X_TLS_PROTOCOL_MIN = 24583

OPT_X_TLS_RANDOM_FILE = 24585

OPT_X_TLS_REQUIRE_CERT = 24582

OPT_X_TLS_TRY = 4

PORT = 389

REQ_ABANDON = 80
REQ_ADD = 104
REQ_BIND = 96
REQ_COMPARE = 110
REQ_DELETE = 74
REQ_EXTENDED = 119
REQ_MODIFY = 102
REQ_MODRDN = 108
REQ_SEARCH = 99
REQ_UNBIND = 66

RES_ADD = 105
RES_ANY = -1
RES_BIND = 97
RES_COMPARE = 111
RES_DELETE = 107
RES_EXTENDED = 120
RES_INTERMEDIATE = 121
RES_MODIFY = 103
RES_MODRDN = 109

RES_SEARCH_ENTRY = 100
RES_SEARCH_REFERENCE = 115
RES_SEARCH_RESULT = 101

RES_UNSOLICITED = 0

SASL_AUTOMATIC = 0
SASL_AVAIL = 1
SASL_INTERACTIVE = 1
SASL_QUIET = 2

SCOPE_BASE = 0
SCOPE_ONELEVEL = 1
SCOPE_SUBORDINATE = 3
SCOPE_SUBTREE = 2

SYNC_INFO = '1.3.6.1.4.1.4203.1.9.1.4'

TAG_CONTROLS = 160

TAG_EXOP_REQ_OID = 128
TAG_EXOP_REQ_VALUE = 129

TAG_EXOP_RES_OID = 138
TAG_EXOP_RES_VALUE = 139

TAG_LDAPCRED = 4
TAG_LDAPDN = 4
TAG_MESSAGE = 48
TAG_MSGID = 2
TAG_NEWSUPERIOR = 128
TAG_REFERRAL = 163

TAG_SASL_RES_CREDS = 135

TLS_AVAIL = 1

URL_ERR_BADSCOPE = 8
URL_ERR_MEM = 1

VENDOR_VERSION = 20442

VERSION = 2
VERSION1 = 1
VERSION2 = 2
VERSION3 = 3

VERSION_MAX = 3
VERSION_MIN = 2

__author__ = 'python-ldap Project'

__version__ = '2.4.27'

# functions

def decode_page_control(*args, **kwargs): # real signature unknown
    pass

def encode_assertion_control(*args, **kwargs): # real signature unknown
    pass

def encode_page_control(*args, **kwargs): # real signature unknown
    pass

def encode_valuesreturnfilter_control(*args, **kwargs): # real signature unknown
    pass

def get_option(*args, **kwargs): # real signature unknown
    pass

def initialize(*args, **kwargs): # real signature unknown
    pass

def set_option(*args, **kwargs): # real signature unknown
    pass

def str2attributetype(*args, **kwargs): # real signature unknown
    """  """
    pass

def str2dn(*args, **kwargs): # real signature unknown
    pass

def str2matchingrule(*args, **kwargs): # real signature unknown
    """  """
    pass

def str2objectclass(*args, **kwargs): # real signature unknown
    """  """
    pass

def str2syntax(*args, **kwargs): # real signature unknown
    """  """
    pass

# classes

from LDAPError import LDAPError
from error import error
from ADMINLIMIT_EXCEEDED import ADMINLIMIT_EXCEEDED
from AFFECTS_MULTIPLE_DSAS import AFFECTS_MULTIPLE_DSAS
from ALIAS_DEREF_PROBLEM import ALIAS_DEREF_PROBLEM
from ALIAS_PROBLEM import ALIAS_PROBLEM
from ALREADY_EXISTS import ALREADY_EXISTS
from ASSERTION_FAILED import ASSERTION_FAILED
from AUTH_METHOD_NOT_SUPPORTED import AUTH_METHOD_NOT_SUPPORTED
from AUTH_UNKNOWN import AUTH_UNKNOWN
from BUSY import BUSY
from CANCELLED import CANCELLED
from CANNOT_CANCEL import CANNOT_CANCEL
from CLIENT_LOOP import CLIENT_LOOP
from COMPARE_FALSE import COMPARE_FALSE
from COMPARE_TRUE import COMPARE_TRUE
from CONFIDENTIALITY_REQUIRED import CONFIDENTIALITY_REQUIRED
from CONNECT_ERROR import CONNECT_ERROR
from CONSTRAINT_VIOLATION import CONSTRAINT_VIOLATION
from CONTROL_NOT_FOUND import CONTROL_NOT_FOUND
from DECODING_ERROR import DECODING_ERROR
from ENCODING_ERROR import ENCODING_ERROR
from FILTER_ERROR import FILTER_ERROR
from INAPPROPRIATE_AUTH import INAPPROPRIATE_AUTH
from INAPPROPRIATE_MATCHING import INAPPROPRIATE_MATCHING
from INSUFFICIENT_ACCESS import INSUFFICIENT_ACCESS
from INVALID_CREDENTIALS import INVALID_CREDENTIALS
from INVALID_DN_SYNTAX import INVALID_DN_SYNTAX
from INVALID_SYNTAX import INVALID_SYNTAX
from IS_LEAF import IS_LEAF
from LOCAL_ERROR import LOCAL_ERROR
from LOOP_DETECT import LOOP_DETECT
from MORE_RESULTS_TO_RETURN import MORE_RESULTS_TO_RETURN
from NAMING_VIOLATION import NAMING_VIOLATION
from NOT_ALLOWED_ON_NONLEAF import NOT_ALLOWED_ON_NONLEAF
from NOT_ALLOWED_ON_RDN import NOT_ALLOWED_ON_RDN
from NOT_SUPPORTED import NOT_SUPPORTED
from NO_MEMORY import NO_MEMORY
from NO_OBJECT_CLASS_MODS import NO_OBJECT_CLASS_MODS
from NO_RESULTS_RETURNED import NO_RESULTS_RETURNED
from NO_SUCH_ATTRIBUTE import NO_SUCH_ATTRIBUTE
from NO_SUCH_OBJECT import NO_SUCH_OBJECT
from NO_SUCH_OPERATION import NO_SUCH_OPERATION
from OBJECT_CLASS_VIOLATION import OBJECT_CLASS_VIOLATION
from OPERATIONS_ERROR import OPERATIONS_ERROR
from OTHER import OTHER
from PARAM_ERROR import PARAM_ERROR
from PARTIAL_RESULTS import PARTIAL_RESULTS
from PROTOCOL_ERROR import PROTOCOL_ERROR
from PROXIED_AUTHORIZATION_DENIED import PROXIED_AUTHORIZATION_DENIED
from REFERRAL import REFERRAL
from REFERRAL_LIMIT_EXCEEDED import REFERRAL_LIMIT_EXCEEDED
from RESULTS_TOO_LARGE import RESULTS_TOO_LARGE
from SASL_BIND_IN_PROGRESS import SASL_BIND_IN_PROGRESS
from SERVER_DOWN import SERVER_DOWN
from SIZELIMIT_EXCEEDED import SIZELIMIT_EXCEEDED
from STRONG_AUTH_NOT_SUPPORTED import STRONG_AUTH_NOT_SUPPORTED
from STRONG_AUTH_REQUIRED import STRONG_AUTH_REQUIRED
from SUCCESS import SUCCESS
from TIMELIMIT_EXCEEDED import TIMELIMIT_EXCEEDED
from TIMEOUT import TIMEOUT
from TOO_LATE import TOO_LATE
from TYPE_OR_VALUE_EXISTS import TYPE_OR_VALUE_EXISTS
from UNAVAILABLE import UNAVAILABLE
from UNAVAILABLE_CRITICAL_EXTENSION import UNAVAILABLE_CRITICAL_EXTENSION
from UNDEFINED_TYPE import UNDEFINED_TYPE
from UNWILLING_TO_PERFORM import UNWILLING_TO_PERFORM
from USER_CANCELLED import USER_CANCELLED
from VLV_ERROR import VLV_ERROR
from X_PROXY_AUTHZ_FAILURE import X_PROXY_AUTHZ_FAILURE
# variables with complex values

_forward = {}

_reverse = {
    0: None,
}


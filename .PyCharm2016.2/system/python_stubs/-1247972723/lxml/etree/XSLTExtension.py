# encoding: utf-8
# module lxml.etree
# from /usr/lib/python2.7/dist-packages/lxml/etree.so
# by generator 1.143
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

from object import object

class XSLTExtension(object):
    """ Base class of an XSLT extension element. """
    def apply_templates(self, context, node, output_parent=None, elements_only=False, remove_blank_text=False): # real signature unknown; restored from __doc__
        """
        apply_templates(self, context, node, output_parent=None, elements_only=False, remove_blank_text=False)
        
                Call this method to retrieve the result of applying templates
                to an element.
        
                The return value is a list of elements or text strings that
                were generated by the XSLT processor.  If you pass
                ``elements_only=True``, strings will be discarded from the result
                list.  The option ``remove_blank_text=True`` will only discard
                strings that consist entirely of whitespace (e.g. formatting).
                These options do not apply to Elements, only to bare string results.
        
                If you pass an Element as `output_parent` parameter, the result
                will instead be appended to the element (including attributes
                etc.) and the return value will be `None`.  This is a safe way
                to generate content into the output document directly, without
                having to take care of special values like text or attributes.
                Note that the string discarding options will be ignored in this
                case.
        """
        pass

    def execute(self, context, self_node, input_node, output_parent): # real signature unknown; restored from __doc__
        """
        execute(self, context, self_node, input_node, output_parent)
                Execute this extension element.
        
                Subclasses must override this method.  They may append
                elements to the `output_parent` element here, or set its text
                content.  To this end, the `input_node` provides read-only
                access to the current node in the input document, and the
                `self_node` points to the extension element in the stylesheet.
        
                Note that the `output_parent` parameter may be `None` if there
                is no parent element in the current context (e.g. no content
                was added to the output tree yet).
        """
        pass

    def process_children(self, context, output_parent=None, elements_only=False, remove_blank_text=False): # real signature unknown; restored from __doc__
        """
        process_children(self, context, output_parent=None, elements_only=False, remove_blank_text=False)
        
                Call this method to process the XSLT content of the extension
                element itself.
        
                The return value is a list of elements or text strings that
                were generated by the XSLT processor.  If you pass
                ``elements_only=True``, strings will be discarded from the result
                list.  The option ``remove_blank_text=True`` will only discard
                strings that consist entirely of whitespace (e.g. formatting).
                These options do not apply to Elements, only to bare string results.
        
                If you pass an Element as `output_parent` parameter, the result
                will instead be appended to the element (including attributes
                etc.) and the return value will be `None`.  This is a safe way
                to generate content into the output document directly, without
                having to take care of special values like text or attributes.
                Note that the string discarding options will be ignored in this
                case.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''



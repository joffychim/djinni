# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from constants.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyBoxedBool, CPyBoxedF32, CPyBoxedF64, CPyBoxedI16, CPyBoxedI32, CPyBoxedI64, CPyBoxedI8, CPyPrimitive, CPyRecord, CPyString

from abc import ABCMeta, abstractmethod
from constant_record import ConstantRecord
from constant_record_helper import ConstantRecordHelper
from future.utils import with_metaclass
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

class ConstantsInterface(with_metaclass(ABCMeta)):
    """
     Interface containing constants
    Constants
        BOOL_CONSTANT
        I8_CONSTANT
        I16_CONSTANT
        I32_CONSTANT: i32_constant has documentation.
        I64_CONSTANT: i64_constant has long documentation.
             (Second line of multi-line documentation.
               Indented third line of multi-line documentation.)
        F32_CONSTANT
        F64_CONSTANT
        OPT_BOOL_CONSTANT
        OPT_I8_CONSTANT
        OPT_I16_CONSTANT: opt_i16_constant has documentation.
        OPT_I32_CONSTANT
        OPT_I64_CONSTANT
        OPT_F32_CONSTANT: opt_f32_constant has long documentation.
             (Second line of multi-line documentation.
               Indented third line of multi-line documentation.)
        OPT_F64_CONSTANT
        STRING_CONSTANT
        OPT_STRING_CONSTANT
        OBJECT_CONSTANT
    """

    BOOL_CONSTANT = True
    I8_CONSTANT = 1
    I16_CONSTANT = 2
    I32_CONSTANT = 3
    I64_CONSTANT = 4
    F32_CONSTANT = 5.0
    F64_CONSTANT = 5.0
    OPT_BOOL_CONSTANT = True
    OPT_I8_CONSTANT = 1
    OPT_I16_CONSTANT = 2
    OPT_I32_CONSTANT = 3
    OPT_I64_CONSTANT = 4
    OPT_F32_CONSTANT = 5.0
    OPT_F64_CONSTANT = 5.0
    STRING_CONSTANT = "string-constant"
    OPT_STRING_CONSTANT = "string-constant"

    @abstractmethod
    def dummy(self):
        """
         No support for null optional constants
         No support for optional constant records
         No support for constant binary, list, set, map
        """
        raise NotImplementedError


ConstantsInterface.OBJECT_CONSTANT = ConstantRecord(
    ConstantsInterface.I32_CONSTANT,
    ConstantsInterface.STRING_CONSTANT)


class ConstantsInterfaceCppProxy(ConstantsInterface):
    def __init__(self, proxy):
        self._is_cpp_proxy = True
        self._cpp_impl = proxy
    def __del__(self):
        if not lib:
            return
        lib.constants_interface___wrapper_dec_ref(self._cpp_impl)

    def dummy(self):
        lib.cw__constants_interface_dummy(self._cpp_impl)
        CPyException.toPyCheckAndRaise(ffi.NULL)

class ConstantsInterfaceHelper:
    c_data_set = MultiSet()
    @staticmethod
    def toPy(obj):
        if obj == ffi.NULL:
            return None
        return ConstantsInterfaceCppProxy(obj)

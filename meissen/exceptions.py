"""Contains app specific exceptions"""

class MeissenException(Exception):
    """Base class for all app specific exceptions"""
    pass

# FileSystem exceptions
class MeissenFileSystemExceptions(MeissenException):
    """Base class for exceptions during file system operations"""
    pass

class MeissenNotExistingPath(MeissenFileSystemException):
    """Raised if a path does not exist"""
    pass

class MeissenNoReadAccessException(MeissenFileSystemException):
    """Raised if something can not be read"""
    pass

class MeissenNoWriteAccessException(MeissenFileSystemException):
    """Raised if something can not be written"""
    pass

class MeissenNoExecuteAccessException(MeissenFileSystemException):
    """Raised if something can not be executed"""
    pass

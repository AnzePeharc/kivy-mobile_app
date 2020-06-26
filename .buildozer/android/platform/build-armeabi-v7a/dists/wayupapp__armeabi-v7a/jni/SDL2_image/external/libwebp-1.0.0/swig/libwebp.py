# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


from sys import version_info

if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_libwebp', [dirname(__file__)])
        except ImportError:
            import _libwebp
            return _libwebp
        if fp is not None:
            try:
                _mod = imp.load_module('_libwebp', fp, pathname, description)
            finally:
                fp.close()
            return _mod


    _libwebp = swig_import_helper()
    del swig_import_helper
else:
    import _libwebp
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method: return method(self, value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method: return method(self)
    raise AttributeError(name)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass


    _newclass = 0


def WebPGetDecoderVersion():
    """WebPGetDecoderVersion() -> int"""
    return _libwebp.WebPGetDecoderVersion()


def WebPGetInfo(*args):
    """WebPGetInfo(uint8_t data) -> (width, height)"""
    return _libwebp.WebPGetInfo(*args)


def WebPDecodeRGB(*args):
    """WebPDecodeRGB(uint8_t data) -> (rgb, width, height)"""
    return _libwebp.WebPDecodeRGB(*args)


def WebPDecodeRGBA(*args):
    """WebPDecodeRGBA(uint8_t data) -> (rgb, width, height)"""
    return _libwebp.WebPDecodeRGBA(*args)


def WebPDecodeARGB(*args):
    """WebPDecodeARGB(uint8_t data) -> (rgb, width, height)"""
    return _libwebp.WebPDecodeARGB(*args)


def WebPDecodeBGR(*args):
    """WebPDecodeBGR(uint8_t data) -> (rgb, width, height)"""
    return _libwebp.WebPDecodeBGR(*args)


def WebPDecodeBGRA(*args):
    """WebPDecodeBGRA(uint8_t data) -> (rgb, width, height)"""
    return _libwebp.WebPDecodeBGRA(*args)


def WebPGetEncoderVersion():
    """WebPGetEncoderVersion() -> int"""
    return _libwebp.WebPGetEncoderVersion()


def wrap_WebPEncodeRGB(*args):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeRGB(*args)


def wrap_WebPEncodeBGR(*args):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeBGR(*args)


def wrap_WebPEncodeRGBA(*args):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeRGBA(*args)


def wrap_WebPEncodeBGRA(*args):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeBGRA(*args)


def wrap_WebPEncodeLosslessRGB(*args):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeLosslessRGB(*args)


def wrap_WebPEncodeLosslessBGR(*args):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeLosslessBGR(*args)


def wrap_WebPEncodeLosslessRGBA(*args):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeLosslessRGBA(*args)


def wrap_WebPEncodeLosslessBGRA(*args):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeLosslessBGRA(*args)


_UNUSED = 1


def WebPEncodeRGB(rgb, width, height, stride, quality_factor):
    """WebPEncodeRGB(uint8_t rgb, int width, int height, int stride, float quality_factor) -> lossy_webp"""
    webp = wrap_WebPEncodeRGB(
        rgb, _UNUSED, _UNUSED, width, height, stride, quality_factor)
    if len(webp[0]) == 0:
        return None
    return webp[0]


def WebPEncodeRGBA(rgb, width, height, stride, quality_factor):
    """WebPEncodeRGBA(uint8_t rgb, int width, int height, int stride, float quality_factor) -> lossy_webp"""
    webp = wrap_WebPEncodeRGBA(
        rgb, _UNUSED, _UNUSED, width, height, stride, quality_factor)
    if len(webp[0]) == 0:
        return None
    return webp[0]


def WebPEncodeBGR(rgb, width, height, stride, quality_factor):
    """WebPEncodeBGR(uint8_t rgb, int width, int height, int stride, float quality_factor) -> lossy_webp"""
    webp = wrap_WebPEncodeBGR(
        rgb, _UNUSED, _UNUSED, width, height, stride, quality_factor)
    if len(webp[0]) == 0:
        return None
    return webp[0]


def WebPEncodeBGRA(rgb, width, height, stride, quality_factor):
    """WebPEncodeBGRA(uint8_t rgb, int width, int height, int stride, float quality_factor) -> lossy_webp"""
    webp = wrap_WebPEncodeBGRA(
        rgb, _UNUSED, _UNUSED, width, height, stride, quality_factor)
    if len(webp[0]) == 0:
        return None
    return webp[0]


def WebPEncodeLosslessRGB(rgb, width, height, stride):
    """WebPEncodeLosslessRGB(uint8_t rgb, int width, int height, int stride) -> lossless_webp"""
    webp = wrap_WebPEncodeLosslessRGB(rgb, _UNUSED, _UNUSED, width, height, stride)
    if len(webp[0]) == 0:
        return None
    return webp[0]


def WebPEncodeLosslessRGBA(rgb, width, height, stride):
    """WebPEncodeLosslessRGBA(uint8_t rgb, int width, int height, int stride) -> lossless_webp"""
    webp = wrap_WebPEncodeLosslessRGBA(rgb, _UNUSED, _UNUSED, width, height, stride)
    if len(webp[0]) == 0:
        return None
    return webp[0]


def WebPEncodeLosslessBGR(rgb, width, height, stride):
    """WebPEncodeLosslessBGR(uint8_t rgb, int width, int height, int stride) -> lossless_webp"""
    webp = wrap_WebPEncodeLosslessBGR(rgb, _UNUSED, _UNUSED, width, height, stride)
    if len(webp[0]) == 0:
        return None
    return webp[0]


def WebPEncodeLosslessBGRA(rgb, width, height, stride):
    """WebPEncodeLosslessBGRA(uint8_t rgb, int width, int height, int stride) -> lossless_webp"""
    webp = wrap_WebPEncodeLosslessBGRA(rgb, _UNUSED, _UNUSED, width, height, stride)
    if len(webp[0]) == 0:
        return None
    return webp[0]

# This file is compatible with both classic and new-style classes.
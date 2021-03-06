from spack import *

class Tk(Package):
    """Tk is a graphical user interface toolkit that takes developing
       desktop applications to a higher level than conventional
       approaches. Tk is the standard GUI not only for Tcl, but for
       many other dynamic languages, and can produce rich, native
       applications that run unchanged across Windows, Mac OS X, Linux
       and more."""
    homepage = "http://www.tcl.tk"

    def url_for_version(self, version):
        return "http://prdownloads.sourceforge.net/tcl/tk%s-src.tar.gz" % version

    version('8.6.3', '85ca4dbf4dcc19777fd456f6ee5d0221')

    depends_on("tcl")

    def install(self, spec, prefix):
        with working_dir('unix'):
            configure("--prefix=%s" % prefix,
                      "--with-tcl=%s" % spec['tcl'].prefix.lib)
            make()
            make("install")

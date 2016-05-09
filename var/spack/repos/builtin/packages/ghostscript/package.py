from spack import *

class Ghostscript(Package):
    """an interpreter for the PostScript language and for PDF. """
    homepage = "http://ghostscript.com/"
    #url      = "http://downloads.ghostscript.com/public/ghostscript-9.16.tar.gz"
    url      = "https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs919/ghostscript-9.19.tar.gz"
    
    version('9.19', '829319325bbdb83f5c81379a8f86f38f')

    parallel = False

    def install(self, spec, prefix):
        configure("--prefix=%s" %prefix, "--enable-shared")

        make()
        make("install")


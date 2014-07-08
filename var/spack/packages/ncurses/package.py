from spack import *

class Ncurses(Package):
    """The ncurses (new curses) library is a free software emulation of curses
       in System V Release 4.0, and more. It uses terminfo format, supports pads and
       color and multiple highlights and forms characters and function-key mapping,
       and has all the other SYSV-curses enhancements over BSD curses.
    """

    homepage = "http://invisible-island.net/ncurses/ncurses.html"
    url      = "http://invisible-island.net/datafiles/release/ncurses.tar.gz"

    versions = { 'stable' : '8cb9c412e5f2d96bc6f459aa8c6282a1' }

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")

    def url_for_version(self, version):
        return "http://invisible-island.net/datafiles/release/ncurses.tar.gz"
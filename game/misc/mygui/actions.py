#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's/\${OIS_LIBRARIES}/${OIS_LIBRARIES} boost_system/g' Common/CMakeLists.txt")
    shelltools.system("sed -i '71 i set(MYGUI_GCC_VISIBILITY_FLAGS "")' CMakeLists.txt")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DMYGUI_INSTALL_SAMPLES=TRUE \
                          -DMYGUI_INSTALL_TOOLS=TRUE \
                          -DMYGUI_INSTALL_DOCS=TRUE \
                          -DMYGUI_INSTALL_MEDIA=TRUE \
                          -DFREETYPE_INCLUDE_DIR=/usr/include/freetype2/ \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DBUILD_SHARED_LIBS=TRUE", installPrefix="/usr")

def build():
    cmaketools.make()
    cmaketools.make("api-docs")

def install():
    # libMyGUI.OgrePlatform.a ?
    # non-bin files in bin: plugins.cfg, resources.xml? opt?
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.chmod("%s/usr/bin/" % get.installDIR(), 0755)
    
    pisitools.dohtml("Docs/html")

    pisitools.dodoc("ChangeLog.txt", "COPYING.LESSER", "Readme.txt")
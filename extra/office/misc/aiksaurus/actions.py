#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-gtk")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def configure():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % (get.installDIR()))

    pisitools.dodoc("AUTHORS", "COPYING", "README", "ChangeLog")

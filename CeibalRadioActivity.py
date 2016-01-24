#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   CeibalRadio.py por:
#   Flavio Danesse <fdanesse@gmail.com>
#   Ceibal Jam - Uruguay - Plan Ceibal
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import TitleEntry
from sugar3.activity.widgets import StopButton

from gi.repository import Gtk

failure = False
try:
    from VistaReproductor import VistaReproductor
except:
    failure = True

class CeibalRadioActivity(activity.Activity):

    def __init__(self,handle):

        activity.Activity.__init__(self,handle,False)

        self.set_title("Ceibal_Radio")

        barraprincipal = ToolbarBox(self)

        activity_button = ActivityButton(self)
        barraprincipal.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        barraprincipal.toolbar.insert(title_entry, -1)
        title_entry.show()
        
        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        barraprincipal.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        barraprincipal.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(barraprincipal)
        if not failure:
            vistareproductor = VistaReproductor()
            self.set_canvas(vistareproductor)
        else:
            error = Gtk.Label("Sorry, this activity doesn't work on this computer.")
            self.set_canvas(error)

        self.show_all()



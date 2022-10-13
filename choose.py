#!/usr/bin/env python
import sys
import os

print(dir(sys.argv))

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

mime = sys.argv[1] if len(sys.argv) >= 2 else "image/png"
chooser = Gtk.AppChooserDialog.new_for_content_type(None, 0, mime)
print(chooser)
# chooser.connect("response")

def quit_fn(reason):
    def quit(*args):
        print(f"{reason} args={args}")
        Gtk.main_quit()
    return quit

chooser.connect("destroy", quit_fn("destroy"))
chooser.connect("close", quit_fn("close"))

def response(dialog, response_id):
    print(f"response {dialog} {response_id}")
    res = Gtk.ResponseType(response_id)
    print("res", res)
    if res == Gtk.ResponseType.OK:
        print("res ok")
        info = Gtk.AppChooser.get_app_info(dialog)
        print("info", info.get_id(), info.get_name())
    else:
        Gtk.main_quit()

chooser.connect("response", response)


Gtk.Widget.show(chooser)
print("ok")

Gtk.main()
print("end")

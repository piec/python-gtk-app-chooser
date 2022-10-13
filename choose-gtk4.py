#!/usr/bin/env python
import sys
import os

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

app = None

def quit_fn(reason):
    def quit(*args):
        print(f"{reason} args={args}")
        # Gtk.main_quit()
        print("app quit", app.quit)
        app.quit()
    return quit

def response(dialog, response_id):
    print(f"response {dialog} {response_id}")
    res = Gtk.ResponseType(response_id)
    print("res", res)
    if res == Gtk.ResponseType.OK:
        print("res ok")
        info = Gtk.AppChooser.get_app_info(dialog)
        print("info", info)
        print("info", info.get_id(), info.get_name())
    else:
        app.quit()


def create_chooser():
    chooser = Gtk.AppChooserDialog.new_for_content_type(None, 0, "image/png")
    print(chooser)

    chooser.connect("destroy", quit_fn("destroy"))
    chooser.connect("close", quit_fn("close"))

    chooser.connect("response", response)

    print("present")
    chooser.present()

def on_activate(new_app):
    global app
    app = new_app
    win = Gtk.ApplicationWindow(application=app)
    btn = Gtk.Button(label="Hello, World!")
    btn.connect('clicked', lambda x: win.close())
    win.set_child(btn)
    # win.present()

    create_chooser()

app = Gtk.Application(application_id="fr.carru.lol")
app.connect('activate', on_activate)
app.run(None)

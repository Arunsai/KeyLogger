#!/usr/bin/env python
#This program is intended to retrieve the data from a local file and display the contents on the GUI. This program asks for the filename to be displayed and if the requested file exists, it displays the file on a window. 
#This program presents a simple GUI for the client to request a file and read the contents of the file. 
import pygtk
pygtk.require('2.0')
import gtk
textbuffer=''
entry=''


class DisplayKeyLogs:

	def close_app(self, widget):
		gtk.main_quit()

	def __init__(self):

		global textbuffer,entry
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_default_size(300,500)
		window.set_resizable(True)
		window.connect("destroy", self.close_app)
		window.set_title("Key Logger GUI")
		window.set_border_width(0)

 
		box1 = gtk.VBox(False, 0)
		window.add(box1)
		box1.show()

		box2 = gtk.HBox(False, 10)
		box2.set_border_width(10)
		box1.pack_start(box2, False, True, 0)
		box2.show()

	        entry = gtk.Entry()
	        entry.set_max_length(50)
	        entry.set_text("Enter Filename Here")

		box2.pack_start(entry,True,True,0)
		entry.show()
		button = gtk.Button("Show File")
		button.connect("clicked", self.retrieve_file,entry)
		box2.pack_start(button,True, True,0)
		button.set_flags(gtk.CAN_DEFAULT)
		button.grab_default()
		button.show()

		button = gtk.Button("close")
		button.connect("clicked", self.close_app)
		box2.pack_start(button, True, True, 0)
		button.show()

		separator = gtk.HSeparator()
		box1.pack_start(separator, False, True, 0)
		separator.show()


		box2 = gtk.HBox(False, 10)
		box2.set_border_width(10)
		box1.pack_start(box2, True, True, 0)
		box2.show()
		sw = gtk.ScrolledWindow()
		sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		textview = gtk.TextView()
		textbuffer = textview.get_buffer()
		sw.add(textview)
		sw.show()
		textview.show()
		box2.pack_start(sw)

		window.show()

	def retrieve_file(self, widget, data):
		global textbuffer,entry
		data=entry.get_text()
		print "Hello %s " %data
		fd = open( data, "r")
		if fd:
			string = fd.read()
			fd.close()
			textbuffer.set_text(string)

def main():
	gtk.main()
	return 0

DisplayKeyLogs()
main()
import os, sys, ping, time, rrd

host = "www.google.com"
rrdfile = "temp/ping.rrd"
rrdpng = "temp/ping.png"

default_graph_width = 400
default_graph_height = 100

from PyQt4 import QtGui, QtCore, uic

class HelloworldApp(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		
		f = open('resources/darkorange.stylesheet', 'r')
		self.styleData = f.read()
		f.close()
		
		self.ui = uic.loadUi('app.ui')
		self.ui.ms_label.setText("Initializing...")
		self.ui.setStyleSheet(self.styleData)
		self.ui.show()
		# self.ui.showFullScreen() #seems to be troublesome for raspberry pis
		
		
		thread.set_graph_size(self.ui.graph.size().width(), self.ui.graph.size().height())
		
		self.connect(thread, thread.signal, self.updateUI)
		self.connect(self.ui.exitButton, QtCore.SIGNAL("clicked()"), exit)
		
		
	def updateUI(self, value):
		win.ui.ms_label.setText(str(value) + " ms")
		win.ui.graph.setPixmap(QtGui.QPixmap(os.getcwd() + "/" + rrdpng))
	
def exit():
	sys.exit()

class AThread(QtCore.QThread):
	def __init__(self):
		QtCore.QThread.__init__(self, parent=app)
		self.signal = QtCore.SIGNAL("signal")
		self.graph_width = default_graph_width
		self.graph_height = default_graph_height
		
	def run(self):
		rrd_count = 0
		graph_reload_count = 0
		
		while True:
			pingval = ping.ping(host)
			rrd.update_rrd(rrdfile, pingval)
			
			if (rrd_count == 5):
				rrd.update_png(rrdpng, rrdfile, self.graph_width, self.graph_height)
				rrd_count = 0
				graph_reload_count += 1
			
			if(graph_reload_count > 0):
				self.emit( self.signal, str( round( float(pingval['minping']), 2 ) ) )
			
			time.sleep(1)
			rrd_count += 1
			
	def set_graph_size(self, width, height):
		self.graph_width = int(width)
		self.graph_height = int(height)

if __name__ == "__main__":
	
	rrd.remove_png(rrdpng)
	rrd.create_rrd(rrdfile)
	
	app = QtGui.QApplication(sys.argv)
	app.setStyle('plastique')
	thread = AThread()
	win = HelloworldApp()
	thread.start()
	sys.exit(app.exec_())

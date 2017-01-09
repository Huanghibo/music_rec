import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication,QFileDialog, QLineEdit, QInputDialog,QLabel,QVBoxLayout
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer,MicrophoneRecognizer

#from __future__ import super()
print "Name of SQL database : "
db=raw_input()
print "MySQL password : "
password=raw_input()
config = {
	"database": {
	"host": "127.0.0.1",
	"user": "root",
	"passwd":password, 
	"db":db,
	}
}

djv=Dejavu(config)

def micrec(length):
	song=djv.recognize(MicrophoneRecognizer,seconds=length)
	print "doododododododod"

def filerec(fname):
	song=djv.recognize(FileRecognizer,fname)
	print song['song_name']

def getAddress(address):
	print "Fingerprinting files from directory : " + address
	djv.fingerprint_directory(address,['mp3'])

class Example(QMainWindow):
	def __init__(self):
		super(Example,self).__init__()
		self.initUI()
		
	def initUI(self):
	
		self.lbl=QLabel(self)
		self.lbl.move(130,205)
		self.lbl.resize(200,50)
		self.lbl.setText('Enter length of mic<br> sample in seconds :')	

		#self.btn=QPushButton('Dialog',self)
		#self.btn.move(240,110)
		#self.btn.clicked.connect(self.showDialog)
		
		self.le=QLineEdit(self)
		self.le.move(270,216)
		self.le.setText('10')
		self.le.resize(50,30)
		
		btn1=QPushButton("Add folder to database",self)
		btn1.resize(btn1.sizeHint())
		btn1.move(10,5)
		
		btn2=QPushButton("File Input",self)
		btn2.resize(100,100)
		btn2.move(10,110)
		
		btn3=QPushButton("Mic Input",self)
		btn3.resize(100,100)
		btn3.move(130,110)
		
		btn1.clicked.connect(self.buttonClicked)
		btn2.clicked.connect(self.buttonClicked)
		btn3.clicked.connect(self.buttonClicked)
		self.statusBar()
		
		self.setGeometry(300,300,400,350)
		self.setWindowTitle("Audio Recognition")
		self.show()
		
	def showDialog(self):
		text,ok=QInputDialog.getInt(self,'Input Dialog','Enter length')
		if ok:
			self.le.setText(str(text))
		
	def buttonClicked(self):
		
		sender=self.sender()
		if(sender.text()=='Add folder to database'):	
			self.statusBar().showMessage('Adding files. This may take a while.')
			self.address()
			self.statusBar().showMessage('Files added')
		elif(sender.text()=='File Input'):
			fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
			self.statusBar().showMessage('Searching')
			filerec(fname)
			self.statusBar().showMessage(' ')
		elif(sender.text()=='Mic Input'):
			print "yada"
			length=int(self.le.text())
			self.statusBar().showMessage('Listening...')
			micrec(length)	
	
	def address(self):
		getAddress(str(QFileDialog.getExistingDirectory(self,"Select Directory")))

		
if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())

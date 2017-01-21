import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication,QFileDialog, QLineEdit, QInputDialog,QLabel,QVBoxLayout,QMessageBox,QDialog
from PyQt5.QtCore import QCoreApplication
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer,MicrophoneRecognizer


def readDBfromfile():#reads the name of database and password stored in dbconfig file and returns both of them 
	fo=open('dbconfig','a+')
	try:
		text=fo.read().split('\n')
		dbname,dbpassword=text[0],text[1]
	except IndexError:
		dbname,dbpassword="",""
	
	return(dbname,dbpassword)
	fo.close()
	
def writeDBtofile(dbname,dbpassword): #writes new name of database and password to dbconfig file
	fo=open('dbconfig','w+')
	text=fo.write(dbname+'\n'+dbpassword)
	fo.close()

def micrec(length):					#to recognize audio via microphone of 'length' seconds. recognize is a function of dejavu library.  
	song=djv.recognize(MicrophoneRecognizer,seconds=length)
	songname=song['song_name']
	if(song['confidence']>10):		#confidence is determined by recognize function. Better the match, more is the confidences
		return songname
	else:
		return "No match found!!  XD "	

def filerec(fname):					#to recognize audio file of. fname is the directory and name of file
	song=djv.recognize(FileRecognizer,fname)
	if(song['confidence']>10):
		return song['song_name']
	else:
		return "No match found!!  XD "	

def getAddress(address):			#fingerprints all mp3 files in 'address' directory
	print "\n\nFingerprinting files from directory : " + address
	djv.fingerprint_directory(address,['mp3'])



class secondary(QMainWindow):
	#First UI window to appear. Collects name of database and MYSQL password for further processing	
	
	def __init__(self):
		super(secondary,self).__init__()
		self.initUI()
	
	def initUI(self):
		
		lbl1=QLabel('Name of Database',self)	#label 
		lbl1.move(10,10)						#move()=location in (x,y) on UI window. x,y=0,0 at top left corner
		lbl1.resize(200,50)						#resize(horizontal,vertical). dimensions of the item
		
		lbl2=QLabel('MYSQL Password',self)
		lbl2.move(10,60)
		lbl2.resize(200,50)
		
		dbname,dbpassword=readDBfromfile()
		
		self.le1=QLineEdit(self)				# self.le1 and self.le2 are text boxes for name of database and password respectively
		self.le1.move(150,23)
		self.le1.setText(dbname)
		self.le1.resize(130,25)
		
		self.le2=QLineEdit(self)
		self.le2.move(150,73)
		self.le2.setText(dbpassword)
		self.le2.resize(130,25)
		
		btn1=QPushButton("OK",self)				#btn1 and btn2 are buttons on the window
		btn1.resize(btn1.sizeHint())
		btn1.move(10,120)
		btn1.clicked.connect(self.buttonClicked)
			
		btn2=QPushButton('Quit',self)
		btn2.resize(btn2.sizeHint())
		btn2.move(100,120)
		btn2.clicked.connect(self.buttonClicked)
			
		self.setGeometry(300,300,400,150)		#horizontal and vertical location of the window on screen and horizontal and vertical length of the window, respectively
		self.setWindowTitle("Database Configuration")
		self.show()
		
	def buttonClicked(self):					#when one of the two buttons are clicked
		sender=self.sender()
		if(sender.text()=='Quit'):
			sys.exit()
		elif(sender.text()=='OK'):
			writeDBtofile(self.le1.text(),self.le2.text())	
			self.close()
			
			
			
class main(QMainWindow):
	#second UI window to appear(but the main one). Provides buttons to add files to database, take file input for recognition, take mic input for recognition	
	
	def __init__(self):
		super(main,self).__init__()
		self.initUI()
		
	def initUI(self):
	
		lbl1=QLabel('Length of mic<br> sample in seconds :',self)
		lbl1.move(130,205)
		lbl1.resize(200,50)
				
		self.le=QLineEdit(self)		#text box for length of audio sample
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
				
	def buttonClicked(self):#when one of the buttons is clicked
		
		sender=self.sender()
		
		if(sender.text()=='Add folder to database'):	
			self.statusBar().showMessage('Adding files. This may take a while.')
			self.address()
			self.statusBar().showMessage('Files added')
		
		elif(sender.text()=='Add files to database'):
			self.statusBar().showMessage('Adding files. This may take a while.')
			fname=QFileDialog.getOpenFileNames(self,'Select files','/home')[0][0]
			#for item in fname:
				
			print fname	
		
		elif(sender.text()=='File Input'):
			fname=QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
			self.statusBar().showMessage('Searching')
			message=filerec(fname)
			message=QMessageBox.question(self,' ',message,QMessageBox.Ok)
			self.statusBar().showMessage(' ')
		
		elif(sender.text()=='Mic Input'):
			length=int(self.le.text())
			self.statusBar().showMessage('Listening...')
			message=micrec(length)
			message=QMessageBox.question(self,' ',message,QMessageBox.Ok)
			self.statusBar().showMessage('Finished')	
	
	def address(self):
		getAddress(str(QFileDialog.getExistingDirectory(self,"Select Directory")))

		



db=QApplication(sys.argv)	#PyQt5 window 1. Database configuration window
ex=secondary()				
db.exec_()	

dbname,dbpassword=readDBfromfile()

config = {
"database": {
"host": "127.0.0.1",
"user": "root",
"passwd":dbpassword, 
"db":dbname,
	}
}
djv=Dejavu(config)
	
app=QApplication(sys.argv)	#PyQt5 window 2. Main window
ex=main()
sys.exit(app.exec_())

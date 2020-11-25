import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLCDNumber, QGridLayout
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
                             QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider,QLineEdit,QLabel)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5 import Qt

def window():



	app = QApplication(sys.argv)
	
	win = QWidget()


		


	#############################################################
	##############									#############
	##############				Fonctions			#############
	##############									#############
	#############################################################
	def modif1():
		contour_bone.SetValue(0, Slider_1.value())
		iren.ReInitialize()

	def modif6():
		contour_skin.SetValue(0, Slider_6.value())
		iren.ReInitialize()

	def modif2():
		lut_bone.SetHueRange(0.0, Slider_2.value()/100)
		iren.ReInitialize()

	def modif7():
		lut_skin.SetHueRange(0.0, Slider_7.value()/100)
		iren.ReInitialize()

	def modif3():
		lut_bone.SetSaturationRange(0.0, Slider_3.value()/100)
		iren.ReInitialize()

	def modif8():
		lut_skin.SetSaturationRange(0.0, Slider_8.value()/100)
		iren.ReInitialize()

	def modif4():
		lut_bone.SetValueRange(0.0, Slider_4.value()/100)
		iren.ReInitialize()

	def modif9():
		lut_skin.SetValueRange(0.0, Slider_9.value()/100)
		iren.ReInitialize()

	def modif5():
		lut_bone.SetAlphaRange(0.0, Slider_9.value()/100)
		iren.ReInitialize()

	def modif10():
		lut_skin.SetAlphaRange(0.0, Slider_10.value()/100)
		iren.ReInitialize()


	#############################################################
	##############									#############
	##############				Layouts			    #############
	##############									#############
	#############################################################


	main_layout = QtWidgets.QHBoxLayout()
	vertical_bone = QtWidgets.QVBoxLayout()
	vertical_skin = QtWidgets.QVBoxLayout()
	horizontal_grid_bone = QtWidgets.QHBoxLayout()
	horizontal_grid_skin = QtWidgets.QHBoxLayout()



	#############################################################
	##############									#############
	##############				QtWidgets			#############
	##############									#############
	#############################################################


	Display_1 = QLCDNumber(3)
	Display_2 = QLCDNumber(3)
	Display_3 = QLCDNumber(3)
	Display_4 = QLCDNumber(3)
	Display_5 = QLCDNumber(3)
	Display_6 = QLCDNumber(3)
	Display_7 = QLCDNumber(3)
	Display_8 = QLCDNumber(3)
	Display_9 = QLCDNumber(3)
	Display_10 = QLCDNumber(3)

	Display_1.setSegmentStyle(QLCDNumber.Flat)
	Display_2.setSegmentStyle(QLCDNumber.Flat)
	Display_3.setSegmentStyle(QLCDNumber.Flat)
	Display_4.setSegmentStyle(QLCDNumber.Flat)
	Display_5.setSegmentStyle(QLCDNumber.Flat)
	Display_6.setSegmentStyle(QLCDNumber.Flat)
	Display_7.setSegmentStyle(QLCDNumber.Flat)
	Display_8.setSegmentStyle(QLCDNumber.Flat)
	Display_9.setSegmentStyle(QLCDNumber.Flat)
	Display_10.setSegmentStyle(QLCDNumber.Flat)

	Display_1.display(90)
	Display_2.display(50)
	Display_3.display(100)
	Display_4.display(100)
	Display_5.display(100)
	Display_6.display(50)
	Display_7.display(100)
	Display_8.display(100)
	Display_9.display(100)
	Display_10.display(100)

	Slider_1 = QSlider(QtCore.Qt.Horizontal)
	Slider_1.setMinimum(0)
	Slider_1.setMaximum(200)
	Slider_1.setValue(90)
	Slider_1.valueChanged.connect(Display_1.display)
	Slider_1.valueChanged.connect(modif1)


	Slider_2 = QSlider(QtCore.Qt.Horizontal)
	Slider_2.setMinimum(0)
	Slider_2.setMaximum(100)
	Slider_2.setValue(50)
	Slider_2.valueChanged.connect(Display_2.display)
	Slider_2.valueChanged.connect(modif2)


	Slider_3 = QSlider(QtCore.Qt.Horizontal)
	Slider_3.setMinimum(0)
	Slider_3.setMaximum(100)
	Slider_3.setValue(100)
	Slider_3.valueChanged.connect(Display_3.display)
	Slider_3.valueChanged.connect(modif3)

	Slider_4 = QSlider(QtCore.Qt.Horizontal)
	Slider_4.setMinimum(0)
	Slider_4.setMaximum(100)
	Slider_4.setValue(100)
	Slider_4.valueChanged.connect(Display_4.display)
	Slider_4.valueChanged.connect(modif4)

	Slider_5 = QSlider(QtCore.Qt.Horizontal)
	Slider_5.setMinimum(0)
	Slider_5.setMaximum(100)
	Slider_5.setValue(100)
	Slider_5.valueChanged.connect(Display_5.display)
	Slider_5.valueChanged.connect(modif5)

	Slider_6 = QSlider(QtCore.Qt.Horizontal)
	Slider_6.setMinimum(0)
	Slider_6.setMaximum(200)
	Slider_6.setValue(50)
	Slider_6.valueChanged.connect(Display_6.display)
	Slider_6.valueChanged.connect(modif6)

	Slider_7 = QSlider(QtCore.Qt.Horizontal)
	Slider_7.setMinimum(0)
	Slider_7.setMaximum(100)
	Slider_7.setValue(100)
	Slider_7.valueChanged.connect(Display_7.display)
	Slider_7.valueChanged.connect(modif7)

	Slider_8 = QSlider(QtCore.Qt.Horizontal)
	Slider_8.setMinimum(0)
	Slider_8.setMaximum(100)
	Slider_8.setValue(100)
	Slider_8.valueChanged.connect(Display_8.display)
	Slider_8.valueChanged.connect(modif8)

	Slider_9 = QSlider(QtCore.Qt.Horizontal)
	Slider_9.setMinimum(0)
	Slider_9.setMaximum(100)
	Slider_9.setValue(100)
	Slider_9.valueChanged.connect(Display_9.display)
	Slider_9.valueChanged.connect(modif9)

	Slider_10 = QSlider(QtCore.Qt.Horizontal)
	Slider_10.setMinimum(0)
	Slider_10.setMaximum(100)
	Slider_10.setValue(100)
	Slider_10.valueChanged.connect(Display_10.display)
	Slider_10.valueChanged.connect(modif10)


	bone_label = QLabel("Bone")
	bone_label.setAlignment(QtCore.Qt.AlignCenter)

	skin_label = QLabel("Skin")
	skin_label.setAlignment(QtCore.Qt.AlignCenter)

	label_1 = QLabel("Slices")
	label_1.setAlignment(QtCore.Qt.AlignCenter)

	label_2 = QLabel("Nuance (en %)")
	label_2.setAlignment(QtCore.Qt.AlignCenter)

	label_3 = QLabel("Saturation (en %)")
	label_3.setAlignment(QtCore.Qt.AlignCenter)  

	label_4 = QLabel("Contraste (en %)")
	label_4.setAlignment(QtCore.Qt.AlignCenter)

	label_5 = QLabel("Luminosite (en %)")
	label_5.setAlignment(QtCore.Qt.AlignCenter)

	label_6 = QLabel("Slices")
	label_6.setAlignment(QtCore.Qt.AlignCenter)

	label_7 = QLabel("Nuance (en %)")
	label_7.setAlignment(QtCore.Qt.AlignCenter)

	label_8 = QLabel("Saturation (en %)")
	label_8.setAlignment(QtCore.Qt.AlignCenter)

	label_9 = QLabel("Contraste (en %)")
	label_9.setAlignment(QtCore.Qt.AlignCenter)

	label_10 = QLabel("Luminosite (en %)")
	label_10.setAlignment(QtCore.Qt.AlignCenter)


	frame = QtWidgets.QFrame()
	frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
	frame.setFrameShape(QtWidgets.QFrame.StyledPanel) # Application de la forme
	frame.setFrameShadow(QtWidgets.QFrame.Raised) # application d'une ombre
	frame.setObjectName("frame") # Appellation du cadre

	#############################################################
	##############									#############
	##############				Organisation		#############
	##############									#############
	#############################################################


	vtkWidget = QVTKRenderWindowInteractor(frame)
	vl = Qt.QVBoxLayout()
	vl.addWidget(vtkWidget)

	main_layout.addWidget(frame)
	main_layout.addLayout(vertical_bone)
	main_layout.addLayout(vertical_skin)
	#main_layout.addStretch()

	vertical_bone.addWidget(bone_label)
	vertical_bone.addLayout(horizontal_grid_bone)
	#vertical_bone.addStretch()

	vertical_skin.addWidget(skin_label)
	vertical_skin.addLayout(horizontal_grid_skin)
	#vertical_skin.addStretch()

	###### 	Remplissage vertical skin ######

	vertical_skin.addWidget(label_1)
	vertical_skin.addWidget(Display_1)
	vertical_skin.addWidget(Slider_1)

	vertical_skin.addWidget(label_2)
	vertical_skin.addWidget(Display_2)
	vertical_skin.addWidget(Slider_2)

	vertical_skin.addWidget(label_3)
	vertical_skin.addWidget(Display_3)
	vertical_skin.addWidget(Slider_3)

	vertical_skin.addWidget(label_4)
	vertical_skin.addWidget(Display_4)
	vertical_skin.addWidget(Slider_4)

	vertical_skin.addWidget(label_5)
	vertical_skin.addWidget(Display_5)
	vertical_skin.addWidget(Slider_5)



	###### 	Remplissage vertical bone ######


	vertical_bone.addWidget(label_6)
	vertical_bone.addWidget(Display_6)
	vertical_bone.addWidget(Slider_6)

	vertical_bone.addWidget(label_7)
	vertical_bone.addWidget(Display_7)
	vertical_bone.addWidget(Slider_7)

	vertical_bone.addWidget(label_8)
	vertical_bone.addWidget(Display_8)
	vertical_bone.addWidget(Slider_8)

	vertical_bone.addWidget(label_9)
	vertical_bone.addWidget(Display_9)
	vertical_bone.addWidget(Slider_9)

	vertical_bone.addWidget(label_10)
	vertical_bone.addWidget(Display_10)
	vertical_bone.addWidget(Slider_10)


	

	# vertical_bone.addWidget(Bouton_1)
	# vertical_bone.addWidget(Bouton_2)
	# vertical_bone.addWidget(Bouton_3)
	# vertical_bone.addStretch()


	#############################################################
	##############									#############
	##############				vtkWidget			#############
	##############									#############
	#############################################################





	reader=vtk.vtkStructuredPointsReader()
	reader.SetFileName("/Users/Sebastien/Documents/3A/Modelisation/Projet/foot.vtk")





   ##########################                       ################################
   ########################## Creation de la source ################################
   ##########################                       ################################




   # Creation du filtre
	contour_skin=vtk.vtkContourFilter()
	contour_skin.SetInputConnection(reader.GetOutputPort())
	contour_skin.SetNumberOfContours(1)
	contour_skin.SetValue(0,90.0) 

	contour_bone=vtk.vtkContourFilter()
	contour_bone.SetInputConnection(reader.GetOutputPort())
	contour_bone.SetNumberOfContours(1)
	contour_bone.SetValue(0,50.0)


   ##########################               ################################
   ########################## Look Up Table ################################
   ##########################               ################################


   # Look up table bone
	lut_bone=vtk.vtkLookupTable()

	lut_bone.SetNumberOfColors(256)
	lut_bone.SetTableRange(0,255)
	lut_bone.SetHueRange(0.0,0.5)
	lut_bone.SetSaturationRange(0.0,1.0)
	lut_bone.SetValueRange(0.0,1.0)
	lut_bone.SetAlphaRange(0.0,1.0)
	lut_bone.Build()

	# Look up table skin
	lut_skin=vtk.vtkLookupTable()
	lut_skin.SetNumberOfColors(256)
	lut_skin.SetTableRange(0,255) 
	lut_skin.SetHueRange(0.0,1.0) # 0 et 1
	lut_skin.SetSaturationRange(0.0,1.0) # 0 et 1
	lut_skin.SetValueRange(0.0,1.0) # 0 et 1
	lut_skin.SetAlphaRange(0.0,1.0) # 0 et 1
	lut_skin.Build()

	   ##########################                              ################################
		########################## Creation du Mapper et Acteur ################################
		##########################                              ################################


	mapper_bone=vtk.vtkPolyDataMapper() 
	mapper_bone.SetInputConnection(contour_bone.GetOutputPort())   
	mapper_bone.SetLookupTable(lut_bone)

	mapper_skin=vtk.vtkPolyDataMapper() 
	mapper_skin.SetInputConnection(contour_skin.GetOutputPort())
	mapper_skin.SetLookupTable(lut_skin)

	actor_bone=vtk.vtkActor() 
	actor_bone.SetMapper(mapper_bone)

	actor_skin=vtk.vtkActor()
	actor_skin.SetMapper(mapper_skin)

	ren = vtk.vtkRenderer()
	vtkWidget.GetRenderWindow().AddRenderer(ren)
	iren = vtkWidget.GetRenderWindow().GetInteractor()



	ren.AddActor(actor_bone)
	ren.AddActor(actor_skin)
	ren.ResetCamera()
	frame.setLayout(vl)
	#setCentralWidget(self.frame)
	#show()
	iren.Initialize()
	iren.Start()
	iren.ReInitialize()




	win.setLayout(main_layout)
	win.setWindowTitle("PyQt")
	win.resize(1920, 1080)
	win.show()
	sys.exit(app.exec_())



if __name__ == '__main__':
   window()
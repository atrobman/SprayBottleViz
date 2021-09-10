import sys
import random
import matplotlib
from math import sin, cos, sqrt, pi
import numpy as np

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

	def __init__(self, parent=None, width=5, height=4):
		fig = Figure(figsize=(width, height))
		self.axes = fig.add_subplot(111)
		super().__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

	def __init__(self):
		super().__init__()
		#variables
		self.r = 25 #spray radius
		self.v = 60 #spray velocity
		self.h = 0 #spray height
		self.a = 0 #spray angle (from table)
		self.g = 9.8 #gravity		
		
		self.layout = QtWidgets.QVBoxLayout(self)

		self.r_label = QtWidgets.QLabel(f"Spray Radius: {self.r} m")
		self.v_label = QtWidgets.QLabel(f"Spray Velocity: {self.v} m/s")
		self.h_label = QtWidgets.QLabel(f"Spray Height: {self.h} m")
		self.a_label = QtWidgets.QLabel(f"Spray Angle: {self.a} Degrees")

		self.r_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		self.r_slider.setMinimum(1)
		self.r_slider.setMaximum(100)
		self.r_slider.setValue(self.r)
		self.r_slider.setTickInterval(1)

		self.v_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		self.v_slider.setMinimum(0)
		self.v_slider.setMaximum(100)
		self.v_slider.setValue(self.v)
		self.v_slider.setTickInterval(1)

		self.h_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		self.h_slider.setMinimum(0)
		self.h_slider.setMaximum(100)
		self.h_slider.setValue(self.h)
		self.h_slider.setTickInterval(1)

		self.a_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		self.a_slider.setMinimum(-90)
		self.a_slider.setMaximum(90)
		self.a_slider.setValue(self.a)
		self.a_slider.setTickInterval(1)

		self.canvas = MplCanvas(self, width=5, height=4)
		# self.setCentralWidget(self.canvas)

		self.len = 1000
		self.theta = np.linspace(0, 2*np.pi, self.len)
		self.xdata = None
		self.ydata = None
		self.update_plot()
		
		self.r_slider.valueChanged.connect(self.update_r_label)
		self.v_slider.valueChanged.connect(self.update_v_label)
		self.h_slider.valueChanged.connect(self.update_h_label)
		self.a_slider.valueChanged.connect(self.update_a_label)

		spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
		spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
		spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)

		self.layout.addWidget(self.r_label)
		self.layout.addWidget(self.r_slider)
		self.layout.addItem(spacerItem1)
		self.layout.addWidget(self.v_label)
		self.layout.addWidget(self.v_slider)
		self.layout.addItem(spacerItem2)
		self.layout.addWidget(self.h_label)
		self.layout.addWidget(self.h_slider)
		self.layout.addItem(spacerItem3)
		self.layout.addWidget(self.a_label)
		self.layout.addWidget(self.a_slider)
		self.layout.addWidget(self.canvas)

		self.main_widget = QtWidgets.QWidget(self)
		self.main_widget.setLayout(self.layout)
		self.setCentralWidget(self.main_widget)

	def update_plot(self):
		self.xdata = self.r * np.cos(self.theta)
		self.ydata = self.r * np.sin(self.theta)

		for i in range(self.len):
			point_height = self.ydata[i] + self.r + self.h

			v_x = self.v * cos(self.a * pi / 180)
			v_y = self.v * sin(self.a * pi / 180)

			#y = v_y0*t+0.5*g*t^2
			#t = (sqrt(2*g*y + v_y0^2) - v_y0) / g
			time_taken = (sqrt(2*self.g*point_height + v_y ** 2) - v_y) / self.g

			#x = v * t
			x_landed = v_x * time_taken

			self.ydata[i] = x_landed

		self.canvas.axes.cla()  # Clear the canvas.
		self.canvas.axes.plot(self.xdata, self.ydata, 'r')
		self.canvas.draw()

	def update_r_label(self, value):
		self.r_label.setText(f"Spray Radius: {value} m")
		self.r = value
		self.update_plot()

	def update_v_label(self, value):
		self.v_label.setText(f"Spray Velocity: {value} m/s")
		self.v = value
		self.update_plot()

	def update_h_label(self, value):
		self.h_label.setText(f"Spray Height: {value} m")
		self.h = value
		self.update_plot()

	def update_a_label(self, value):
		self.a_label.setText(f"Spray Angle: {value} Degrees")
		self.a = value
		self.update_plot()

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()

sys.exit(app.exec_())

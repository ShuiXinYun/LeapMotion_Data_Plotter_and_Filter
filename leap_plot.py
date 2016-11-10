import Leap
from pyqtgraph.Qt import QtGui, QtCore
from collections import deque
import pyqtgraph as pg
import math
import scipy.ndimage as fd


controller = Leap.Controller()
pen_width=2
rad2deg=180.0/math.pi
framenum=500
x_label=range(1,framenum+1)
leap_x_deque=deque(maxlen=framenum)
leap_y_deque=deque(maxlen=framenum)
leap_z_deque=deque(maxlen=framenum)
leap_pitch_deque=deque(maxlen=framenum)
leap_roll_deque=deque(maxlen=framenum)
leap_yaw_deque=deque(maxlen=framenum)
for i in xrange(framenum):
    leap_x_deque.append(0.0)
    leap_y_deque.append(0.0)
    leap_z_deque.append(0.0)
    leap_pitch_deque.append(0.0)
    leap_roll_deque.append(0.0)
    leap_yaw_deque.append(0.0)
win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,1000)
win.setWindowTitle('Leap Motion Data Plotter')
pg.setConfigOptions(antialias=True)

leap_x_plotter = win.addPlot(title="Leap_X_Plotter")
leap_x_plotter.showGrid(x=True,y=True)
leap_x_plotter.setLabel('left', "X Displacement", units='mm')
leap_x_plotter.setLabel('bottom', "FrameNum")
leap_x_plotter.setYRange(-200,200)
curve_leap_x=leap_x_plotter.plot(pen=pg.mkPen(color=(255, 99, 71),width=pen_width))

leap_y_plotter = win.addPlot(title="Leap_Y_Plotter")
leap_y_plotter.showGrid(x=True,y=True)
leap_y_plotter.setLabel('left', "Y Displacement", units='mm')
leap_y_plotter.setLabel('bottom', "FrameNum")
leap_y_plotter.setYRange(-200,200)
curve_leap_y=leap_y_plotter.plot(pen=pg.mkPen(color=(60, 179, 113),width=pen_width))

leap_z_plotter = win.addPlot(title="Leap_Z_Plotter")
leap_z_plotter.showGrid(x=True,y=True)
leap_z_plotter.setLabel('left', "Z Displacement", units='mm')
leap_z_plotter.setLabel('bottom', "FrameNum")
leap_z_plotter.setYRange(0,500)
curve_leap_z=leap_z_plotter.plot(pen=pg.mkPen(color=(30, 144, 255),width=pen_width))

win.nextRow()

leap_pitch_plotter=win.addPlot(title='Leap_Pitch_Plotter')
leap_pitch_plotter.showGrid(x=True,y=True)
leap_pitch_plotter.setLabel('left', "Pitch Value", units='Deg')
leap_pitch_plotter.setLabel('bottom', "FrameNum")
leap_pitch_plotter.setYRange(-90,90)
curve_leap_pitch=leap_pitch_plotter.plot(pen=pg.mkPen(color=(255,0,255),width=pen_width))

leap_roll_plotter=win.addPlot(title='Leap_Roll_Plotter')
leap_roll_plotter.showGrid(x=True,y=True)
leap_roll_plotter.setLabel('left', "Roll Value", units='Deg')
leap_roll_plotter.setLabel('bottom', "FrameNum")
leap_roll_plotter.setYRange(-90,90)
curve_leap_roll=leap_roll_plotter.plot(pen=pg.mkPen(color=(0, 255, 127),width=pen_width))

leap_yaw_plotter=win.addPlot(title='Leap_Yaw_Plotter')
leap_yaw_plotter.showGrid(x=True,y=True)
leap_yaw_plotter.setLabel('left', "Yaw Value", units='Deg')
leap_yaw_plotter.setLabel('bottom', "FrameNum")
leap_yaw_plotter.setYRange(-90,90)
curve_leap_yaw=leap_yaw_plotter.plot(pen=pg.mkPen(color=(0,245,255),width=pen_width))

win.nextRow()

leap_x_filter_plotter = win.addPlot(title="Leap_X_Filter_Plotter")
leap_x_filter_plotter.showGrid(x=True,y=True)
leap_x_filter_plotter.setLabel('left', "X Displacement", units='mm')
leap_x_filter_plotter.setLabel('bottom', "FrameNum")
leap_x_filter_plotter.setYRange(-200,200)
curve_leap_x_filterd =leap_x_filter_plotter.plot(pen=pg.mkPen(color=(255, 99, 71),width=pen_width))

leap_y_filter_plotter = win.addPlot(title="Leap_Y_Filter_Plotter")
leap_y_filter_plotter.showGrid(x=True,y=True)
leap_y_filter_plotter.setLabel('left', "Y Displacement", units='mm')
leap_y_filter_plotter.setLabel('bottom', "FrameNum")
leap_y_filter_plotter.setYRange(-200,200)
curve_leap_y_filterd=leap_y_filter_plotter.plot(pen=pg.mkPen(color=(60, 179, 113),width=pen_width))

leap_z_filter_plotter = win.addPlot(title="Leap_Z_Filter_Plotter")
leap_z_filter_plotter.showGrid(x=True,y=True)
leap_z_filter_plotter.setLabel('left', "Z Displacement", units='mm')
leap_z_filter_plotter.setLabel('bottom', "FrameNum")
leap_z_filter_plotter.setYRange(0,500)
curve_leap_z_filterd=leap_z_filter_plotter.plot(pen=pg.mkPen(color=(30, 144, 255),width=pen_width))

win.nextRow()

leap_pitch_filter_plotter=win.addPlot(title='Leap_Pitch_Filter_Plotter')
leap_pitch_filter_plotter.showGrid(x=True,y=True)
leap_pitch_filter_plotter.setLabel('left', "Pitch Value", units='Deg')
leap_pitch_filter_plotter.setLabel('bottom', "FrameNum")
leap_pitch_filter_plotter.setYRange(-90,90)
curve_leap_pitch_filterd=leap_pitch_filter_plotter.plot(pen=pg.mkPen(color=(255,0,255),width=pen_width))

leap_roll_filter_plotter=win.addPlot(title='Leap_Roll_Filter_Plotter')
leap_roll_filter_plotter.showGrid(x=True,y=True)
leap_roll_filter_plotter.setLabel('left', "Roll Value", units='Deg')
leap_roll_filter_plotter.setLabel('bottom', "FrameNum")
leap_roll_filter_plotter.setYRange(-90,90)
curve_leap_roll_filterd=leap_roll_filter_plotter.plot(pen=pg.mkPen(color=(0, 255, 127),width=pen_width))

leap_yaw_filter_plotter=win.addPlot(title='Leap_Yaw_Filter_Plotter')
leap_yaw_filter_plotter.showGrid(x=True,y=True)
leap_yaw_filter_plotter.setLabel('left', "Yaw Value", units='Deg')
leap_yaw_filter_plotter.setLabel('bottom', "FrameNum")
leap_yaw_filter_plotter.setYRange(-90,90)
curve_leap_yaw_filterd=leap_yaw_filter_plotter.plot(pen=pg.mkPen(color=(0,245,255),width=pen_width))

def update():
    global curve, leap_x_deque
    frame = controller.frame()
    hand = frame.hands[0]
    direction = hand.direction
    normal = hand.palm_normal
    leap_x_deque.append(round(hand.palm_position[2], 4))
    leap_y_deque.append(round(hand.palm_position[0], 4))
    leap_z_deque.append(round(hand.palm_position[1], 4))
    leap_x_filterd= list(fd.filters.gaussian_filter(list(leap_x_deque),5))
    leap_y_filterd = list(fd.filters.gaussian_filter(list(leap_y_deque), 5))
    leap_z_filterd = list(fd.filters.gaussian_filter(list(leap_z_deque), 5))
    leap_pitch_deque.append(round(direction.pitch*rad2deg, 4))
    leap_roll_deque.append(round(normal.roll * rad2deg, 4))
    leap_yaw_deque.append(round(direction.yaw * rad2deg, 4))
    leap_pitch_filtered= list(fd.filters.gaussian_filter(list(leap_pitch_deque),5))
    leap_roll_filtered = list(fd.filters.gaussian_filter(list(leap_roll_deque), 5))
    leap_yaw_filtered = list(fd.filters.gaussian_filter(list(leap_yaw_deque), 5))
    curve_leap_x.setData(x_label, list(leap_x_deque))
    curve_leap_y.setData(x_label, list(leap_y_deque))
    curve_leap_z.setData(x_label, list(leap_z_deque))
    curve_leap_pitch.setData(x_label, list(leap_pitch_deque))
    curve_leap_roll.setData(x_label, list(leap_roll_deque))
    curve_leap_yaw.setData(x_label, list(leap_yaw_deque))
    curve_leap_x_filterd.setData(x_label,leap_x_filterd)
    curve_leap_y_filterd.setData(x_label, leap_y_filterd)
    curve_leap_z_filterd.setData(x_label, leap_z_filterd)
    curve_leap_pitch_filterd.setData(x_label,leap_pitch_filtered)
    curve_leap_roll_filterd.setData(x_label, leap_roll_filtered)
    curve_leap_yaw_filterd.setData(x_label, leap_yaw_filtered)
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(5)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
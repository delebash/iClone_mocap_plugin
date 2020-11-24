#!/usr/bin/env python3
# main.py

# debug setup for vs code
# ptvsd has to be at top
# import ptvsd
# ptvsd.enable_attach(address=("localhost", 5678), redirect_output=True)
# ptvsd.wait_for_attach()

# PyCharm
import pydevd_pycharm
pydevd_pycharm.settrace('127.0.0.1', port=12345, stdoutToServer=False,
                        stderrToServer=False)

import RLPy
from PySide2.shiboken2 import wrapInstance
from PySide2.QtCore import QThread
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import *
from PySide2 import *
from PySide2.QtCore import *

from BoneData import *
from testing_with_file.generate_iclone_from_left_hand_stream import *
import python_websocket_client

mocap_manager = RLPy.RGlobal.GetMocapManager()
avatar = None
hand_device_ID = "HandDevice"
hand_device = mocap_manager.AddHandDevice(hand_device_ID)
new_pose = None
closefist_frame_data = [
0.0,
105.0,
0.0,
0.0,
0.0,
0.0,
-11.0,
105.0,
0.0,
0.0,
0.0,
0.0,
-11.0,
56.0,
0.0,
0.0,
0.0,
0.0,
-11.0,
8.0,
0.0,
0.0,
0.0,
0.0,
11.0,
105.0,
0.0,
0.0,
0.0,
0.0,
11.0,
56.0,
0.0,
0.0,
0.0,
0.0,
11.0,
8.0,
0.0,
0.0,
0.0,
0.0,
0.0,
118.0,
0.0,
0.0,
0.0,
0.0,
0.0,
129.0,
0.0,
0.0,
0.0,
0.0,
0.0,
141.0,
0.0,
0.0,
0.0,
0.0,
0.0,
152.0,
0.0,
0.0,
0.0,
0.0,
0.0,
164.0,
0.0,
0.0,
0.0,
0.0,
0.0,
173.0,
0.0,
0.0,
0.0,
0.0,
-3.0,
160.0,
0.0,
0.0,
0.0,
0.0,
-17.0,
160.0,
0.0,
0.0,
0.0,
0.0,
-46.0,
160.0,
0.0,
0.0,
0.0,
0.0,
-74.0,
160.0,
0.0,
0.0,
0.0,
0.0,
-77.0,
161.0,
3.0,
0.0,
30.0,
0.0,
-81.0,
161.0,
3.0,
0.0,
0.0,
0.0,
-83.0,
161.0,
3.0,
0.0,
0.0,
0.0,
-78.0,
161.0,
2.0,
0.0,
0.0,
0.0,
-83.0,
161.0,
3.0,
0.0,
0.0,
0.0,
-87.0,
161.0,
3.0,
0.0,
0.0,
0.0,
-89.0,
161.0,
3.0,
0.0,
0.0,
0.0,
-78.0,
161.0,
0.0,
0.0,
0.0,
0.0,
-83.0,
161.0,
1.0,
0.0,
0.0,
0.0,
-88.0,
161.0,
1.0,
0.0,
0.0,
0.0,
-90.0,
161.0,
1.0,
0.0,
0.0,
0.0,
-78.0,
161.0,
0.0,
0.0,
0.0,
0.0,
-83.0,
161.0,
0.0,
0.0,
0.0,
0.0,
-86.0,
161.0,
0.0,
0.0,
0.0,
0.0,
-89.0,
161.0,
0.0,
0.0,
0.0,
0.0,
-77.0,
161.0,
-1.0,
0.0,
0.0,
0.0,
-82.0,
161.0,
-2.0,
0.0,
0.0,
0.0,
-85.0,
161.0,
-2.0,
0.0,
0.0,
0.0,
-87.0,
161.0,
-2.0,
0.0,
0.0,
0.0,
3.0,
160.0,
0.0,
0.0,
0.0,
0.0,
17.0,
160.0,
0.0,
0.0,
0.0,
0.0,
46.0,
160.0,
0.0,
0.0,
0.0,
0.0,
74.0,
160.0,
0.0,
0.0,
0.0,
0.0,
77.0,
161.0,
3.0,
0.0,
-36.53785558892015,
0.0,
81.0,
161.0,
3.0,
0.0,
-5.9215987580693294,
0.0,
83.0,
161.0,
3.0,
0.0,
-7.382070069313884,
0.0,
78.0,
161.0,
2.0,
0.0,
0.0,
-6.5378555889201495,
83.0,
161.0,
3.0,
0.0,
0.0,
0.0,
87.0,
161.0,
3.0,
0.0,
0.0,
-5.9215987580693294,
89.0,
161.0,
3.0,
0.0,
0.0,
-7.382070069313884,
78.0,
161.0,
0.0,
0.0,
0.0,
-6.5378555889201495,
83.0,
161.0,
1.0,
0.0,
0.0,
0.0,
88.0,
161.0,
1.0,
0.0,
0.0,
-5.9215987580693294,
90.0,
161.0,
1.0,
0.0,
0.0,
-7.382070069313884,
78.0,
161.0,
0.0,
0.0,
0.0,
-6.5378555889201495,
83.0,
161.0,
0.0,
0.0,
0.0,
0.0,
86.0,
161.0,
0.0,
0.0,
0.0,
-5.9215987580693294,
89.0,
161.0,
0.0,
0.0,
0.0,
-7.382070069313884,
77.0,
161.0,
-1.0,
0.0,
0.0,
-6.5378555889201495,
82.0,
161.0,
-2.0,
0.0,
0.0,
0.0,
85.0,
161.0,
-2.0,
0.0,
0.0,
-5.9215987580693294,
87.0,
161.0,
-2.0,
0.0,
0.0,
-7.382070069313884,
]

class App:
    """GUI Application using PySide2 widgets"""

    def __init__(self):
        super().__init__()
        # 1 - create Worker and Thread inside the Form
        self.obj = python_websocket_client.Worker()  # no parent!
        self.thread = QThread()  # no parent!

        # 2 - Connect Worker`s Signals to Form method slots to post data.
        self.obj.message.connect(self.onMessage)
        self.obj.data.connect(self.onData)

        # 3 - Move the Worker object to the Thread object
        self.obj.moveToThread(self.thread)

        # 4 - Connect Worker Signals to the Thread slots
        # self.obj.stop.connect(self.obj.stopclient)
        # self.obj.start.connect(self.obj.startclient)

        # 5 - Connect Thread started signal to Worker operational slot method
        # self.thread.started.connect(self.obj.startclient)

        # * - Thread finished signal will close the app if you want!
        # self.thread.stop.connect(self.obj.stopclient)

        # 6 - Start the thread
        self.thread.start()

        # 7 - Start the form
        self.initUI()

    def initUI(self):
        self.mocap_manager_dialog = RLPy.RUi.CreateRDialog()
        self.mocap_manager_dialog.SetWindowTitle("Mocap Manager")
        # -- Create Pyside layout for RDialog --#
        self.pyside_dialog = wrapInstance(int(self.mocap_manager_dialog.GetWindow()), QtWidgets.QDialog)
        self.pyside_dialog.setFixedWidth(300)
        self.mocap_layout = self.pyside_dialog.layout()

        # -- Add UI Elements --#
        self.info = QtWidgets.QTextEdit()
        self.mocap_layout.addWidget(self.info)

        self.connect_button = QtWidgets.QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect)
        self.mocap_layout.addWidget(self.connect_button)

        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.clicked.connect(self.start)
        self.mocap_layout.addWidget(self.start_button)

        self.stop_button = QtWidgets.QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop)
        self.mocap_layout.addWidget(self.stop_button)

        return

    def connect(self):
        self.obj.connectclient()

    def start(self):
        self.startmocap()

    def stop(self):
        mocap_manager.Stop()

    def onMessage(self, msg):
        self.info.append(msg)

    def onData(self, data):
        new_pose = json2iclon(tpose, data)
        pose_data = np.array([])
        for array in new_pose:
            pose_data = np.concatenate([pose_data, array])
        # self.info.append(data)
        self.proccessmocapdata(pose_data)

    def onStop(self, msg):
        self.info.append('I am Diconnected')

    def show_dialog(self):
        self.mocap_manager_dialog.Show()

    def startmocap(self):
        global hand_device
        global avatar

        if avatar:
            hand_device.RemoveAvatar(avatar)
            avatar = None

        selection_list = RLPy.RScene.GetSelectedObjects()
        if len(selection_list) > 0:
            for object in selection_list:  # find first avatar
                object_type = object.GetType()
                if object_type == RLPy.EObjectType_Avatar:
                    avatar = object

        if avatar is None:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Please click on an avatar")
            msgBox.exec()
            return

        if hand_device is not None:
            hand_device.AddAvatar(avatar)
            hand_device.SetEnable(avatar, True)
            hand_device.SetProcessDataIndex(avatar, 0)

        # hand_device.AddAvatar(avatar)

        hand_setting = hand_device.GetHandSetting(avatar)

        hand_setting.SetRightHandJoin(RLPy.EHandJoin_Wrist)
        hand_setting.SetLeftHandJoin(RLPy.EHandJoin_Wrist)
        hand_setting.SetHandJoinType(RLPy.EHandJoinType_UseParentBone)
        hand_setting.SetRightHandDataSource(RLPy.EHandDataSource_LeftHand)
        hand_setting.SetLeftHandDataSource(RLPy.EHandDataSource_LeftHand)
        hand_setting.SetActivePart(RLPy.EBodyActivePart_Hand_R | RLPy.EBodyActivePart_Finger_R |
                                   RLPy.EBodyActivePart_Hand_L | RLPy.EBodyActivePart_Finger_L)

        device_setting = hand_device.GetDeviceSetting()
        device_setting.SetMocapCoordinate(RLPy.ECoordinateAxis_Y, RLPy.ECoordinateAxes_Z,
                                          RLPy.ECoordinateSystem_RightHand)
        device_setting.SetCoordinateOffset(0, [0, 0, 0])

        position_setting = device_setting.GetPositionSetting()
        rotation_setting = device_setting.GetRotationSetting()
        rotation_setting.SetType(RLPy.ERotationType_Euler)
        rotation_setting.SetUnit(RLPy.ERotationUnit_Degrees)
        rotation_setting.SetEulerOrder(RLPy.EEulerOrder_ZXY)
        rotation_setting.SetCoordinateSpace(RLPy.ECoordinateSpace_Local)
        position_setting.SetUnit(RLPy.EPositionUnit_Centimeters)
        position_setting.SetCoordinateSpace(RLPy.ECoordinateSpace_Local)

        hand_device.Initialize(hik_bone_list)
        hand_device.SetTPoseData(avatar, tpose)

        if hand_device.IsTPoseReady(avatar) == True:
            mocap_manager.Start(RLPy.EMocapState_Preview)

    def proccessmocapdata(self, pose_data):
        hand_device.ProcessData(0, pose_data, -1)


x = App()
x.show_dialog()

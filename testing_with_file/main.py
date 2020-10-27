#!/usr/bin/env python3
# main.py

# debug setup for vs code
# ptvsd has to be at top
# import ptvsd
# ptvsd.enable_attach(address=("localhost", 5678), redirect_output=True)
# ptvsd.wait_for_attach()



import RLPy
from PySide2.shiboken2 import wrapInstance
from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QPushButton, QTextEdit, QMessageBox
from PySide2.QtWidgets import *
from PySide2 import *
from PySide2.QtCore import *

from BoneData import *
from generate_iclone_from_left_hand_json_file import *

mocap_manager = RLPy.RGlobal.GetMocapManager()
avatar = None
hand_device_ID = "HandDevice"
hand_device = mocap_manager.AddHandDevice(hand_device_ID)



new_pose = None

test_hand_data =[
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
-15.228669039374056,
-47.95929868594737,
-23.51199985060732,
0.0,
0.0,
0.0,
-15.228669039374056,
-47.95929868594737,
-23.51199985060732,
0.0,
0.0,
0.0,
-15.228669039374056,
-47.95929868594737,
-23.51199985060732,
0.0,
0.0,
0.0,
-1.136476616468273,
-1.4619874983193384,
-7.877352325442109,
0.0,
0.0,
0.0,
-1.136476616468273,
-1.4619874983193384,
-7.877352325442109,
0.0,
0.0,
0.0,
-1.136476616468273,
-1.4619874983193384,
-7.877352325442109,
0.0,
0.0,
0.0,
89.0,
161.0,
3.0,
0.0,
0.0,
0.0,
-9.29858492486176,
-8.217442275384794,
-2.321560392449365,
0.0,
0.0,
0.0,
-9.29858492486176,
-8.217442275384794,
-2.321560392449365,
0.0,
0.0,
0.0,
-9.29858492486176,
-8.217442275384794,
-2.321560392449365,
0.0,
0.0,
0.0,
90.0,
161.0,
1.0,
0.0,
0.0,
0.0,
-20.799489923066144,
-124.47699509303503,
-41.99680129865608,
0.0,
0.0,
0.0,
-20.799489923066144,
-124.47699509303503,
-41.99680129865608,
0.0,
0.0,
0.0,
-20.799489923066144,
-124.47699509303503,
-41.99680129865608,
0.0,
0.0,
0.0,
89.0,
161.0,
0.0,
0.0,
0.0,
0.0,
-31.82706147543275,
-109.84965358203922,
-5.682761379287413,
0.0,
0.0,
0.0,
-31.82706147543275,
-109.84965358203922,
-5.682761379287413,
0.0,
0.0,
0.0,
-31.82706147543275,
-109.84965358203922,
-5.682761379287413,
0.0,
0.0,
0.0,
87.0,
161.0,
-2.0,
0.0,
0.0,
0.0,
]
class App:
    """GUI Application using PySide2 widgets"""

    def __init__(self):
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

        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.clicked.connect(self.start)
        self.mocap_layout.addWidget(self.start_button)

        self.stop_button = QtWidgets.QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop)
        self.mocap_layout.addWidget(self.stop_button)

        return


    def start(self):
        self.startmocap()
        self.proccessmocapdata()

    def stop(self):
        mocap_manager.Stop()

    def onMessage(self, msg):
        self.info.append(msg)

    def onData(self, data):
        new_pose = json2iclon(tpose, data)
        self.proccessmocapdata(new_pose)

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

    def proccessmocapdata(self):
        hand_device.ProcessData(0, test_hand_data, -1)


x = App()
x.show_dialog()

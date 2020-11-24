from generate_iclone_from_left_hand_json import *

#main function
new_pose = json2iclon(tpose, './data/testy.json')

#output new pose to txt file
f = open("new_pose.txt", 'a')
f.write('closefist_frame_data = [ \n')
arr_num = len(new_pose)
for k in range(arr_num):
    pts = new_pose[k]
    for n in range(6):
        strval = str(pts[n])+"," + '\n'
        f.write(strval)
f.write(']')
f.close()



import math
import showError_file
PI = math.pi

'''Returns the radius of the ei node taking e0 as origin(0,0)'''
def get_radius(e0, ei):
    return math.sqrt((float(ei[1]) - float(e0[1]))*(float(ei[1]) - float(e0[1])) + (float(ei[2]) - float(e0[2]))*(float(ei[2]) - float(e0[2])))

'''Returns the angle that line (x1,y1)-(x2,y2) does with X=x1 line.'''
def get_angle(e, x1, x2, y1, y2): #1st quadrant: x1 > x2 & y1 > y2
    angle = 0
    if x1 == x2:
            if y2 < y1:
                angle = 90
            elif y1 < y2:
                angle = -90
            angle = math.radians(angle)
    elif y1 == y2:
            angle = 0
    else:
        angle = math.atan(abs(y1 - y2)/abs(x1 - x2))
        if x2 < x1 and y1 < y2:
            angle = 0 - angle
        elif x1 < x2 and y1 < y2:
            angle = PI + angle
        elif x1 < x2 and y2 < y1:
            angle = PI - angle
    return angle

'''Returns an array of recalculated radius for each node and using last node as center of space.'''
def redo_radius(elec_data, model_data):
    lim = len(elec_data) - 1
    model_data_new_radius = []
    for i in model_data:
        k = 1
        aux = []
        for j in range(0, len(i)):
            if elec_data[k][0] < j:
                if k < lim:
                    k = k + 1
                else:
                    showError_file.show_error()
                    return None
            aux.append([(i[j][0] - elec_data[k - 1][4])*(get_radius(elec_data[k - 1], elec_data[k]) / (elec_data[k][4] - elec_data[k - 1][4])), i[j][1], i[j][2], i[j][3]])
        model_data_new_radius.append(aux)
    return model_data_new_radius
                
'''Given UTM coordinates from elec_data it returns an array of the ETRS-89, UTM-31 N coordinates of the model.'''
def calculate_UTM(elec_data, model_data):
    model_data_new_radius = redo_radius(elec_data, model_data)
    new_model_data = []
    lim = len(elec_data)
    for i in model_data_new_radius:
        aux = []
        k = 1
        angle = get_angle(elec_data[k][0], elec_data[k][1], elec_data[k - 1][1], elec_data[k][2], elec_data[k - 1][2])
        for j in range(len(i)):
            if elec_data[k][0] < j:
                if k < lim:
                    k = k + 1
                else:
                    showError_file.show_error()
                    return None
                angle = get_angle(elec_data[k][0], elec_data[k][1], elec_data[0][1], elec_data[k][2], elec_data[0][2])
            aux.append([i[j][0]*math.cos(angle) + elec_data[k - 1][1], i[j][0]*math.sin(angle) + elec_data[k - 1][2], i[j][2], i[j][3]])
        new_model_data.append(aux)
    return new_model_data

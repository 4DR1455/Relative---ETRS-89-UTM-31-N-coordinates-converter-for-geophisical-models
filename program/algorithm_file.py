import csv
import UTMcalculator_file

'''Deletes useless data, for the geophisics model.'''
def purify(model_data):
    aux = []
    for i in model_data:
        aux2 = []
        mid = int(len(i)/2) + 1
        k = 0
        while k < mid:
            while k < mid and i[k][3] == i[k + 1][3]:
                k = k + 1
            aux2.append(i[k])
            k = k + 1
        k = mid
        mid = mid - 1
        for k in range(mid,len(i) - 1):
            if i[k][3] != i[k + 1][3]:
                aux2.append(i[k])
        if (i[len(i) - 1][3] != i[len(i) - 2][3]):
            aux2.append(i[len(i) - 1])
        aux.append(aux2)
    return aux

'''Flips the array.'''
def flip(array):
    aux = []
    for i in range(len(array)):
        aux.append(array[len(array) - i - 1])
    return aux

'''Converts identificators into numbers.'''
def numerize(elec_data):
    aux = []
    for i in range(len(elec_data)):
        aux.append([int(elec_data[i][0].replace('e','')), float(elec_data[i][1]), float(elec_data[i][2]), float(elec_data[i][3]), UTMcalculator_file.get_radius(elec_data[0], elec_data[i])])
        #               [0] (nº electrode)                     [1] (x)                      [2] (y)                  [3] (z)                  [4] (Polar coordinate from node 0)
    return aux

'''Process data from arrays that show document's data.'''
def processar(ruta_elecs, ruta_model, nelements):
    elec_data = []
    model_data = []
    # Read CSV file
    with open(ruta_elecs, mode='r', newline='', encoding='utf-8') as elecs_csv:
        lector_csv = csv.reader(elecs_csv)
    
        # Converting file's data into a list
        aux = list(lector_csv)

        for i in aux:
            aux2 = i[0].split(';')
            elec_data.append(aux2)

        if (elec_data[0][0] != 'e1'):
            elec_data = flip(elec_data)

        elec_data = numerize(elec_data)
        
    with open(ruta_model, mode='r', newline='', encoding='utf-8') as model_csv:
        lector_csv = csv.reader(model_csv)

        aux = list(lector_csv)
        aux3 = []
        j = 0
        for i in range(1, len(aux)):
            aux2 = aux[i][0].split(';')
            aux3.append([float(aux2[0]), 0, float(aux2[1]), float(aux2[2])])
            #               [0](radius) [1]     [2](Z)        [3](Resistivity)
            if (i - j) == nelements:
                model_data.append(aux3)
                aux3 = []
                j = i

    #Calculating the ETRS-89, UTM-31 N coordinates.
    new_model_data = UTMcalculator_file.calculate_UTM(elec_data, model_data)

    new_model_data = purify(new_model_data)

    new_model_data_file = []
    new_model_data_file.append(["X UTM", "Y UTM", "Z", "Resistivitat"])
    for i in new_model_data:
        for j in i:
            new_model_data_file.append(j)
        
    straux1 = ""
    for i in ruta_model:
        if i == '/':
            straux1 = ""
        else:
            straux1 += i
        
    ruta_new_model = "new_" + straux1

    straux1 = ""
    straux2 = ""
    for i  in ruta_model:
        straux1 += i
        if (i == '/'):
            straux2 += straux1
            straux1 = ""

    ruta_new_model = straux2 + ruta_new_model


    #Data arays from files
    with open(ruta_new_model, mode='w', newline='', encoding='utf-8') as fitxer_csv:
        escriptor_csv = csv.writer(fitxer_csv)
        escriptor_csv.writerows(new_model_data_file)



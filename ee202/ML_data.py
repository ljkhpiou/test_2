gyro_x = []
gyro_y = []
gyro_z = []
rms = []
row = []
pitch = []
time = []
scroll = []

with open('data_scroll_down.txt', encoding = "ISO-8859-1") as file:
    for line in file:
        line_data = line.split()
        
        if (len(line_data) == 15):
            gyro_x.append(float(line_data[2]))
            gyro_y.append(float(line_data[4]))
            gyro_z.append(float(line_data[6]))
            rms.append(float(line_data[8]))
            row.append(float(line_data[10]))
            pitch.append(float(line_data[12]))
            time.append(float(line_data[14]))
           
            if(gyro_x[len(gyro_x) - 1] < 0 and len(row) > 1 and (row[len(row) - 2] - row[len(row) - 1]) > 10 and row[len(row) - 2] < 0 and row[len(row) - 1] < 0):
                scroll.append(1)
            else:
                scroll.append(0)

data = [[]]

data[0].extend(gyro_x[0:len(gyro_x)-2])
data.append([])
data[1].extend(gyro_y[0:len(gyro_y)-2])
data.append([])
data[2].extend(gyro_z[0:len(gyro_z)-2])
data.append([])
data[3].extend(row[0:len(row)-2])
data.append([])
data[4].extend(gyro_x[1:len(gyro_x)-1])
data.append([])
data[5].extend(gyro_y[1:len(gyro_y)-1])
data.append([])
data[6].extend(gyro_z[1:len(gyro_x)-1])
data.append([])
data[7].extend(row[1:len(gyro_x)-1])

target = []
target.extend(scroll[0:len(gyro_x)-2])
file.close()
print(scroll[0:len(gyro_x)-2])
import numpy
data = numpy.transpose(data)
target = numpy.transpose(target)

from sklearn.svm import SVC
classifier = SVC(kernel='linear')
classifier.fit(data, target)
predict = classifier.predict(data)

print(classifier.coef_)
print(classifier.intercept_)
print(predict[0:len(predict) -1])

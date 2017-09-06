import csv
from resampler import resampler

X = []
Y = []
T = []

fileName = input('Enter original file name: ')
#fileName = 'foo.csv'
print('Resampling in progress...')

#we read the original signal
with open(fileName, newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter=' ')
    for row in reader:
        X.append(float(row[0]))
        Y.append(float(row[1]))
        T.append(float(row[2]))

#we resample the x axis signal
new_sampling_rate = 40
R = resampler(X, T, new_sampling_rate)
X_new = R.resample()

#we resample the y axis signal
R = resampler(Y, T, new_sampling_rate)
Y_new = R.resample()

#we save to a file the resampled signal
fileName = input('Save resampled file as: ')
with open(fileName, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    #we save the x, y signals (either signal has the same time stamps)
    for i in range(0,len(X_new[0])):
        writer.writerow([X_new[1][i], Y_new[1][i], X_new[0][i]])



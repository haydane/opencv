import numpy as np
from numpy import genfromtxt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix, classification_report
from keras.models import load_model

data = genfromtxt(
    '../Document/Computer-Vision-with-Python/DATA/bank_note_data.txt', delimiter=',')

lables = data[:, 4]

features = data[:, 0:4]

X = features

y = lables


# create trained data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

scalar_object = MinMaxScaler()

scalar_object.fit(X_train)

scaled_X_train = scalar_object.transform(X_train)
scaled_X_test = scalar_object.transform(X_test)

model = Sequential()
model.add(Dense(4, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])
model.fit(scaled_X_train, y_train, epochs=50, verbose=2)

predictions = model.predict_classes(scaled_X_test)

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

model.save('mysupermodel.h5')

newmodel = load_model('mysupermodel.h5')

print(newmodel.predict_classes(scaled_X_test))

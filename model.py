import numpy as np
from keras import regularizers
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.optimizers import SGD, Adam, RMSprop

train_data = np.load('D:/proj1/train_data.npy')
test_data = np.load('D:/proj1/test_data.npy')

train_data_X = np.array([i[0] for i in train_data]).reshape(-1,70,70,1)
train_data_Y = np.array([i[1] for i in train_data])
test_data_X = np.array([i[0] for i in test_data]).reshape(-1,70,70,1)
test_data_Y = np.array([i[1] for i in test_data])


model = Sequential()

model.add(Conv2D(32, (3, 3), border_mode='same', input_shape=(70,70,1), activation='relu'))
model.add(Conv2D(32, (3, 3), border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), border_mode='same', activation='relu'))
model.add(Conv2D(64, (3, 3), border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3), border_mode='same', activation='relu'))
model.add(Conv2D(128, (3, 3), border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3), border_mode='same', activation='relu'))
model.add(Conv2D(256, (3, 3), border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(1))
model.add(Activation('sigmoid'))


#model.summary()

model.compile(loss='binary_crossentropy', optimizer=RMSprop(lr=0.0001), metrics=['accuracy'])
model.fit(train_data_X, train_data_Y, batch_size = 64, epochs=20, validation_split = 0.25, verbose=1)
score = model.evaluate(test_data_X, test_data_Y, batch_size = 64, verbose=1)

model_json = model.to_json()
open('cat_and_dog1.json', 'w').write(model_json)
model.save_weights('cat_and_dog1.h5', overwrite=True)

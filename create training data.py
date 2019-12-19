import os
import cv2
from tqdm import tqdm
import numpy as np

def label_img(img):
    label = img.split('.')[0]
    if label=='cat':
        return [0]
    else:
        return [1]

def create_training_data():
    training_data = np.empty(shape=[0,2])
    size = (70,70)
    for img in tqdm(os.listdir('D:/proj1/Train/')):
        try:            
            label = label_img(img)
            path = os.path.join('D:/proj1/Train/', img)
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, size)
            training_data = np.append(training_data, [[np.array(img)/255, np.array(label)]], axis=0)
        except Exception as e:
            print(str(e))
    np.random.shuffle(training_data)
    np.save('train_data1.npy', training_data)

def create_test_data():
    test_data = np.empty(shape=[0,2])
    size = (70,70)
    for img in tqdm(os.listdir('D:/proj1/Test/')):
        try:            
            label = label_img(img)
            path = os.path.join('D:/proj1/Test/', img)
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, size)
            test_data = np.append(test_data, [[np.array(img)/255, np.array(label)]], axis=0)
        except Exception as e:
            print(str(e))
    np.random.shuffle(test_data)
    np.save('test_data1.npy', test_data)

create_training_data()
create_test_data()

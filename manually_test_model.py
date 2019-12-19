from keras.models import load_model
import numpy as np
import cv2

from keras.models import model_from_json

model = model_from_json(open('cat_and_dog1.json').read())
model.load_weights('cat_and_dog1.h5')

img_name = 'c4.jpg'

size = (70,70)
im = cv2.imread(img_name)
cv2.imshow("Image", im)
img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, size)
img_arr = np.array(img).reshape(-1,70,70,1)
img_arr = img_arr/255
ans = model.predict(img_arr)
ans = ans[0][0]
if ans<0.5:
    #ans = ((0.5-ans)/0.5)*100
    #print("Cat: %4.2f"%(ans)+'%')
    print("Cat")
else:
    #ans = (ans)*100
    #print("Dog: %4.2f"%(ans)+'%')
    print("Dog")

cv2.waitKey()
cv2.destroyAllWindows

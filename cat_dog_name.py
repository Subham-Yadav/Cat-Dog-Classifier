import shutil, os

for i in range(0,10000):
                    src = 'D:/proj1/Dog/dog.' + str(i)+'.jpg'
                    src1 = 'D:/proj1/Cat/cat.' + str(i)+'.jpg'
                    dst = 'D:/proj1/Train/dog.' + str(i)+'.jpg'
                    dst1 = 'D:/proj1/Train/cat.' + str(i)+'.jpg'                    
                    shutil.move(src, dst)
                    shutil.move(src1, dst1)


for i in range(10000,12500):
                    src = 'D:/proj1/Dog/dog.' + str(i)+'.jpg'
                    src1 = 'D:/proj1/Cat/cat.' + str(i)+'.jpg'
                    dst = 'D:/proj1/Test/dog.' + str(i)+'.jpg'
                    dst1 = 'D:/proj1/Test/cat.' + str(i)+'.jpg'
                    shutil.move(src, dst)
                    shutil.move(src1, dst1)

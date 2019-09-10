import csv
import cv2
import os

def image2csv(input_file, output_path):
    img = cv2.imread(input_file, cv2.IMREAD_ANYDEPTH|cv2.IMREAD_ANYCOLOR)
    height, width = img.shape

    img_array = img.flatten()
    img_array = img.reshape(480,640)

    name = os.path.basename(input_file)
    name = os.path.splitext(name)[0]

    output_file = open(output_path+name+'.csv', "w", newline='')
    writer = csv.writer(output_file)

    writer.writerows(img_array)
    output_file.close()


if __name__ == "__main__":
    input = os.sys.argv[1]
    output_path = os.sys.argv[2]

    image2csv(input, output_path)
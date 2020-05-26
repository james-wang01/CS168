import pydicom as dicom
import matplotlib.pyplot as plt
import os
import cv2
import PIL
import pandas as pd
import csv

def convert(image, newImage):
    ds = dicom.dcmread(image)
    pixel_array_numpy = ds.pixel_array
    cv2.imwrite(newImage, pixel_array_numpy)

def extract(image, info):
    dicom_image_description = pd.read_csv("dicom_img_description.csv")
    ds = dicom.dcmread(image)
    with open(info, 'w', newline ='') as csvfile:
        fieldnames = list(dicom_image_description["Description"])
        writer = csv.writer(csvfile, delimiter=',')
        rowDescription = []
        rowData = []
        for field in fieldnames:
            try:
                elem = ds.data_element(field)
                rowDescription.append(field)
            except:
                print("This data element was not found %s," % field)

            if elem is None:
                rowData.append('')
            else:
                x = str(elem).replace("'","")
                y = x.find(":")
                x = x[y+2:]
                rowData.append(x)
        writer.writerow(rowDescription)
        writer.writerow(rowData)

def dcm2jpg(image, newImage, info):
    convert(image, newImage)
    extract(image, info)

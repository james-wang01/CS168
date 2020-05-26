import pydicom as dicom
import matplotlib.pyplot as plt
import os
import cv2
import PIL
import pandas as pd
import csv

def convert(image, newImage):
    dicom_image_description = pd.read_csv("dicom_img_description.csv")
    ds = dicom.dcmread(image)
    pixel_array_numpy = ds.pixel_array
    cv2.imwrite(newImage, pixel_array_numpy)

def extract(image, info):
    dicom_image_description = pd.read_csv("dicom_img_description.csv")
    ds = dicom.dcmread(image)
    with open(info, 'w', newline ='') as csvfile:
        fieldnames = list(dicom_image_description["Description"])
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(fieldnames)
        rows = []
        for field in fieldnames:
            if ds.data_element(field) is None:
                rows.append('')
            else:
                x = str(ds.data_element(field)).replace("'", "")
                y = x.find(":")
                x = x[y+2:]
                rows.append(x)
        writer.writerow(rows)

def dcm2jpg(image, newImage, info):
    convert(image, newImage)
    extract(image, info)
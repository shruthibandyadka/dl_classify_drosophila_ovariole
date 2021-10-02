import numpy as np
from skimage import morphology, filters, measure
import matplotlib.pyplot as plt
import h5py
import glob
import path
import cv2
import scipy

def read_segmaps(filename):
    with h5py.File(filename, "r") as f:
        #print("Keys: %s" % f.keys())
        a_group_key = list(f.keys())[0]
        segmap = np.array(f[a_group_key])

        #plt.figure(figsize=(10, 10))
        #plt.imshow(segmap)
    return segmap

def find_small_object_removal_threshold(segmap): 
    labels = measure.label(segmap)
    props = measure.regionprops(labels, segmap)
    properties = ['area']   
    all_object_areas = []
    for index in range(1, labels.max()):
        for prop_name in properties:
            object_area = getattr(props[index], prop_name)
            all_object_areas.append(object_area)
    all_object_areas = sorted(all_object_areas)
    #print(all_object_areas)
    #return min(all_object_areas[-5:])
    return all_object_areas
import numpy as np
import os
import cv2


def Process(k, image, size):
    processed_data = np.memmap(image, dtype=np.uint8, shape = size)
    criteria = (cv2.TERM_CRITERIA_EPS, 1000, 1.0)
    Z = np.float32(processed_data)
    compactness, labels, (centers) = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_PP_CENTERS)
    centers = np.uint8(centers)
    labels = labels.flatten()
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(size)
    print(compactness)
    return segmented_image

current_dir = os.getcwd()
KU_path = current_dir + '/K_means/KU.raw'
Golf_path = current_dir + '/K_means/Golf.raw'
Gun_path = current_dir + '/K_means/Gundam.raw'

cv2.imwrite('KU_out.jpg', Process(2,KU_path,(560,720)))
cv2.imwrite('Golf_out.jpg',Process(4,Golf_path,(540,800)))
cv2.imwrite('Gun_out.jpg',Process(8,Gun_path,(600,600)))

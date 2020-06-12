# K-Means-Clustering-of-input-images
Implementation of K-Means clustering of input images, using OpenCV library and Python
</br>
</br>
 K-means algorithm to cluster 1-dimensional pixel values.</br>
After clustering, each cluster is assigned with the average gray level (centroid gray level). 
There are three input images in the main directory:</br>

* KU.raw (720x560 image, each pixel is an 8-bit number)
* Gundam.raw (600x600 image, each pixel is an 8-bit number)
* Golf.raw (800x540 image, each pixel is an 8-bit number)

</br>
K-means is applied to each image with the number of clusters = 2, 4, and 8 respectively. </br>
At each iteration, the compactness is observed.

</br>
The library used are:

* OpenCV
* numpy
* os

As files from local directories are used, os library was used to get the path of the files. </br>
The K-means clustering was applied using the opencv library functions, after the raw data was processed using numpy.

import cv2 as cv
import os
import shutil
import sys
sys.path.append(r'F:\My_Knowledge_and_Portfolio\Python\OpenCv\OpenCV_OOP_image_operations')

import pandas as pd
from math import radians, sin, cos, sqrt, atan2

from imageoperations import ImageOperations

def list_input_images(directory):
  # Create an empty list to store the file paths
  image_paths = []

  # Loop through all files in the directory
  for filename in os.listdir(directory):
      # Check if the file is an image
      if filename.endswith('.jpg') or filename.endswith('.JPG'):
          # Add the full file path to the list
          image_paths.append(os.path.join(directory, filename))

  # Return the list of image file paths
  return image_paths


# Define a function to calculate the distance between two coordinates using the Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the earth in km
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    a = sin(dLat / 2) * sin(dLat / 2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dLon / 2) * sin(dLon / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c  # Distance in km
    return distance

if __name__ =="__main__":

  cwd = os.getcwd()

  WP = pd.read_csv(os.path.join(cwd, r'input\DroneDeployDownload_2023_04_21_090413.csv'))
  WP = WP.loc[:, ['AnnotationDescription','AnnotationLatAndLong']]
  WP[['latitude', 'longitude']] = WP['AnnotationLatAndLong'].str.split(', ', expand=True)
  WP = WP.loc[:,['AnnotationDescription','latitude', 'longitude']]
  # Convert the latitude and longitude columns from str to float
  WP['latitude'] = WP['latitude'].astype(float)
  WP['longitude'] = WP['longitude'].astype(float)

  image_paths = list_input_images(os.path.join(cwd, r'input\DJI'))

  for image in image_paths:
    photo = ImageOperations(image)
    gps_loc = photo.print_exif_GPS()
    print(gps_loc)

    # Calculate the distance between each point in the dataframe and the dictionary coordinates
    WP['distance'] = WP.apply(lambda row: haversine(row['latitude'], row['longitude'], gps_loc['latitude'], gps_loc['longitude']), axis=1)

    # Get the top 3 rows with the minimum distances
    closest_points = WP.sort_values('distance').head(1)

    to_folder = closest_points.values[0,0]
    print(to_folder)
    destination = os.path.join(cwd, 'results', to_folder)
    print(destination)


    if not os.path.isdir(destination):
      os.makedirs(destination)
    
    image_name = os.path.basename(image)
    shutil.copyfile(image, os.path.join(destination, image_name))


    print(closest_points)
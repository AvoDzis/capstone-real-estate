from math import radians, cos, sin, asin, sqrt
import os
import googlemaps
from datetime import datetime
from geopy.geocoders import Nominatim
import random

geolocator = Nominatim(user_agent="my_application")


def get_district(lat, lng):
    """
    Reverse geocode the coordinates to get the district.

    :param lat: latitude of the location
    :param lng: longitude of the location
    :return: the district of the location
    """

    # Reverse geocode the coordinates to get the address
    location = geolocator.reverse(f"{lat}, {lng}", timeout=None)

    # Extract the district information from the address
    address = location.raw['address']
    district_estim = address.get('suburb', address.get('city_district'))

    return district_estim


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)

    :param lon1: longitude of the first point
    :param lat1: latitude of the first point
    :param lon2: longitude of the second point
    :param lat2: latitude of the second point
    :return: the distance between the two points in kilometers
    """
    # Convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def read_api_key():
    """
    Read the Google Maps API key from a file. This file should be one directory back from the script.
    This is done for security purposes and to avoid sharing the API key with others.
    File is not passed to git, by gitignore file.

    :return: the API key
    """
    # Construct the path to the file containing the API key
    parent_dir = os.path.dirname(os.getcwd())
    api_key_file = os.path.join(parent_dir, 'maps_api.txt')

    # Read the API key from the file
    with open(api_key_file, 'r') as f:
        api_key = f.read().strip()
    return api_key
      

def get_walking_distance(start_lon, start_lat, end_lon, end_lat):
    """
    Calculate the walking distance between two points using the Google Maps API.

    :param start_lon: longitude of the start point
    :param start_lat: latitude of the start point
    :param end_lon: longitude of the end point
    :param end_lat: latitude of the end point
    :return: the distance between the two points in meters
    """
    # Set up the Google Maps API client
    api_key = read_api_key()

    gmaps = googlemaps.Client(key=api_key)

    # Define the start and end coordinates
    start = (start_lat, start_lon)
    end = (end_lat, end_lon)

    # Make the API request
    now = datetime.now()
    directions = gmaps.directions(start, end, mode='walking', departure_time=now)

    # Extract the distance from the response
    distance_estim = directions[0]['legs'][0]['distance']['value']

    # Return the distance in meters
    return distance_estim


def remove_outliers(df, col, lower_bound):
    """
    Removes outliers from a dataframe based on the IQR method. 
    Data is grouped by district, the outliers are detected for each district.

    :param df: The dataframe to remove outliers from
    :param col: The column to remove outliers from
    :param lower_bound: The lower bound for the IQR method
    :return: The dataframe with outliers removed
    """
    grouped_data = df.groupby('district')
    for name, group in grouped_data:
        # Calculate the IQR
        q1 = group[col].quantile(0.25)
        q3 = group[col].quantile(0.75)
        iqr = q3 - q1
        # Setting a lower bound to follow incase lower bound is negative
        lower_bound = max(q1 - 1.5 * iqr, lower_bound)
        upper_bound = q3 + 1.5 * iqr
        outliers = group[(group[col] < lower_bound) | (group[col] > upper_bound)]
        num_outliers = len(outliers)
        print(f"District {name} has {num_outliers} outliers")
        df = df.drop(outliers.index)
    return df


def apply_jitter(coord, distance):
    """
    Apply jitter to a coordinate (latitude and longitude).

    :param coord: Input coordinate (float)
    :param distance: Maximum distance to apply jitter (float)
    :return: jittered_coord: Jittered coordinate (float)
    """
    jittered_coord = coord + (distance * random.uniform(-1, 1))
    return jittered_coord

import math
from aiogram import types
from utils.misc import show_on_gmapsUz, show_on_gmapsRu
from data.locationsRuUz import *

def calc_distanceUz(lat1, lon1, lat2, lon2):
    R = 6371000
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + \
        math.cos(phi_1) * math.cos(phi_2) * \
        math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c  # output distance in meters
    return meters / 1000.0  # output distance in kilometers


def choose_shortestUz(location: types.Location):
    distancesUz = list()
    for shop_nameUz, shop_locationUz in locationsUz:
        distancesUz.append((shop_nameUz,
                          calc_distanceUz(location.latitude, location.longitude,
                                        shop_locationUz["lat"], shop_locationUz["lon"]),
                          show_on_gmapsUz.show(**shop_locationUz),
                          shop_locationUz
                          ))
    return sorted(distancesUz, key=lambda x: x[1])

def calc_distanceRu(lat1, lon1, lat2, lon2):
    R = 6371000
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + \
        math.cos(phi_1) * math.cos(phi_2) * \
        math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c  # output distance in meters
    return meters / 1000.0  # output distance in kilometers


def choose_shortestRu(location: types.Location):
    distancesRu = list()
    for shop_nameRu, shop_locationRu in LocationsRu:
        distancesRu.append((shop_nameRu,
                          calc_distanceRu(location.latitude, location.longitude,
                                        shop_locationRu["lat"], shop_locationRu["lon"]),
                          show_on_gmapsRu.show(**shop_locationRu),
                          shop_locationRu
                          ))
    return sorted(distancesRu, key=lambda x: x[1])
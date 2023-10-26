import math
def get_shipping_cost_per_package(distance_in_radius, package_weight):

    __shipping_cost = 0

    if(distance_in_radius <= 20):

        # zone 1
        if(package_weight < 5):

            __shipping_cost = 4500
        elif(package_weight >= 5 and package_weight <= 10):

            __shipping_cost = 9000

        elif(package_weight > 10):

            __shipping_cost = 18000

    elif(distance_in_radius > 20 and distance_in_radius <= 50):

        # zone 2
        if(package_weight < 5):

            __shipping_cost = 7500

        elif(package_weight >= 5 and package_weight <= 10):

            __shipping_cost = 12000

        elif(package_weight > 10):

            __shipping_cost = 20000

    elif(distance_in_radius > 50):
        # zone 3
        if(package_weight < 5):

            __shipping_cost = 9000

        elif(package_weight >= 5 and package_weight <= 10):

            __shipping_cost = 20000

        elif(package_weight > 10):

            __shipping_cost = 30000

    # extra kilos to the weight
    if(package_weight > 30):

        theextraweights = package_weight-30
        theextraAmount = 1000

        if(theextraweights >= 1):
            __shipping_cost = __shipping_cost + \
                (theextraAmount*theextraweights)

    return __shipping_cost


def convert_degrees_to_radius(degrees):
    return degrees * (math.pi/180)


def get_distance_in_radius(destination_latitude, destination_longitude):
    origin_latitude = 0.3133807
    origin_longitude = 32.5789327

    Radius_of_the_earth = 6371  # Radius of the earth in km
    latitudinal_distance_in_radius = convert_degrees_to_radius(destination_latitude - origin_latitude)  # convert_degrees_to_radius below
    longtudinal_distance_in_radius = convert_degrees_to_radius(destination_longitude - origin_longitude)
    a = math.sin(latitudinal_distance_in_radius/2) * math.sin(latitudinal_distance_in_radius/2) + math.cos(convert_degrees_to_radius(origin_latitude)) * \
        math.cos(convert_degrees_to_radius(destination_latitude)) * math.sin(longtudinal_distance_in_radius/2) * math.sin(longtudinal_distance_in_radius/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = Radius_of_the_earth * c  # Distance in km
    __distance_in_radius = round(d, 2)

    return __distance_in_radius


def calculate_delivery_cost(latitude, longitude, weight):
    __latitude = latitude
    __longitude = longitude

    _distance_in_radius = get_distance_in_radius(__latitude, __longitude)
    __delivery_cost = get_shipping_cost_per_package(_distance_in_radius/2, weight)
    return __delivery_cost


# calculate_delivery_cost(latitude, longitude, weight)
# get_shipping_cost_per_package(distance_in_radius, package_weight)

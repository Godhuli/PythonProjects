# Normal ground shipping
def ground_shipping_cost(weight):
    if weight <= 2:
        price_per_pound = 1.50
    elif (weight > 2) and (weight <= 6):
        price_per_pound = 3.00
    elif (weight > 6) and (weight <= 10):
        price_per_pound = 4.00
    else:
        price_per_pound = 4.75

    cost = weight * price_per_pound + 20.00
    return cost


print(ground_shipping_cost(8.4))

premium_shipping_cost = 125


# Drone shipping

def drone_shipping_cost(weight):
    if weight <= 2:
        price_per_pound = 4.50
    elif (weight > 2) and (weight <= 6):
        price_per_pound = 9.00
    elif (weight > 6) and (weight <= 10):
        price_per_pound = 12.00
    else:
        price_per_pound = 14.25
    cost = weight * price_per_pound
    return cost


print(drone_shipping_cost(1.5))

'''def cheap_shipment(weight):
    if ((ground_shipping_cost(weight)) < (drone_shipping_cost(weight))) and ((ground_shipping_cost(weight)) < premium_shipping_cost):
        return "Ground shipping is cheapest."
    elif ((drone_shipping_cost(weight)) < (ground_shipping_cost(weight))) and ((drone_shipping_cost(weight)) < premium_shipping_cost):
        return "Drone shipping is cheapest."
    else:
        return "premium shipping is cheap."


print(cheap_shipment(2))'''


def cheap_shipment_method(weight):
    ground = ground_shipping_cost(weight)
    premium = premium_shipping_cost
    drone = drone_shipping_cost(weight)
    if ground < premium and ground < drone:
        cost = ground
        method = "ground"
    elif premium < ground and premium < drone:
        cost = premium
        method = "premium"
    else:
        cost = drone
        method = "drone"

    print("The cheapest way to ship " + str(weight) + " pound is " + method +". It will cost $" + str(cost) )


print(cheap_shipment_method(4.8))
print(cheap_shipment_method(41.5))





from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    hummer_car = SilverServiceTaxi("Hummer", 100, 2)

    print("for an {} km trip with fanciness of {}, the fare should be ${}".format(hummer_car.drive(18),
                                                                                  hummer_car.fanciness,
                                                                                  hummer_car.get_fare()))
    print(hummer_car)


main()

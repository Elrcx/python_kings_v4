class Car:
    def __init__(self, cars):
        self._cars = cars
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= len(self._cars):
            raise StopIteration

        result = self._cars[self._idx]
        self._idx += 1
        return result


# for car in Car(["tico", "bmw", "fiat"]):
#     print(car)
#
# carsy = Car(["tico", "bmw", "fiat"])
#
# print(next(carsy))
# print(next(carsy))
# print(next(carsy))

continents = {
    "africa": {
        "egypt": "cairo",
        "libya": "trypolis",
        "nigeria": "abuja",
        "kenya": "nairobi",
        "south_africa": "pretoria",
        "morocco": "rabat"
    },
    "europe": {
        "germany": "berlin",
        "poland": "warsaw",
        "france": "paris",
        "italy": "rome",
        "spain": "madrid",
        "netherlands": "amsterdam",
        "greece": "athens"
    },
    "asia": {
        "china": "beijing",
        "japan": "tokyo",
        "india": "new delhi",
        "south_korea": "seoul",
        "thailand": "bangkok",
        "vietnam": "hanoi"
    },
    "north_america": {
        "usa": "washington, d.c.",
        "canada": "ottawa",
        "mexico": "mexico city",
        "cuba": "havana",
        "guatemala": "guatemala city",
        "panama": "panama city"
    },
    "south_america": {
        "brazil": "brasilia",
        "argentina": "buenos aires",
        "colombia": "bogotá",
        "chile": "santiago",
        "peru": "lima",
        "venezuela": "caracas"
    },
    "australia": {
        "australia": "canberra",
        "new_zealand": "wellington",
        "fiji": "suva",
        "papua_new_guinea": "port moresby",
        "samoa": "apia"
    },
    "antarctica": {
    }
}

class CapitalsIterator:
    def __init__(self, capitals):
        self._capitals = capitals
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= len(self._capitals):
            raise StopIteration

        capital = self._capitals[self._idx]
        self._idx += 1
        return capital


class Capitals:
    def __init__(self, capitals_):
        self._capitals = capitals_

    def __iter__(self):
        capitals = []
        for countries in self._capitals.values():
            capitals.extend(countries.values())

        capitals.sort()
        return CapitalsIterator(capitals)


capitals = Capitals(continents)

for capital in capitals:
    print(capital)

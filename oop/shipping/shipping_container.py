from oop.shipping import iso6346


class ShippingContainer:
    HEIGHT_FT = 8.6
    WIDTH_FT = 8.0
    next_serial = 42

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), **kwargs)

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.length_ft = length_ft
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )

    @property
    def volume_ft3(self):
        return self._calc_volume()

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft



class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents, **kwargs)
        self.celsius = celsius

    @property
    def celsius(self):
        return f"{self._celsius}°C"

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too high!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return f"{self._celsius * 9 / 5 + 32}°F"

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )

    def _calc_volume(self):
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20

    def _set_celsius(self, value):
        if not (HeatedRefrigeratedShippingContainer.MIN_CELSIUS  < value):
            raise ValueError("Temperature is too low!")
        super()._set_celsius(value)


# ISO:6346
# code = 'CDQU3054383'
#
# s0 = ShippingContainer("MAE", 20, ["pengun", "ice cube", "dead body"], celsius=-10.0)
# r1 = RefrigeratedShippingContainer.create_empty('YML', 20, celsius=2.0)
r2 = RefrigeratedShippingContainer.create_with_items('YML', 20, ['ice', 'snow'], celsius=-20.0)
h3 = HeatedRefrigeratedShippingContainer.create_empty('YML', 20, celsius=-20.0)
#
# print(s0.celsius)
# print(s0.fahrenheit)
# print(r1.celsius)
# print(r1.fahrenheit)
print(r2.celsius)
print(r2.fahrenheit)
print(h3.celsius)
print(h3.fahrenheit)
#
# print(r0.volume_ft3)


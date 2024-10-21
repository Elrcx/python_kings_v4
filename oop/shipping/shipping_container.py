class ShippingContainer:
    next_serial = 42

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = type(self).next_serial
        type(self).next_serial += 1

# ISO:6346
code = 'CDQU3054383'

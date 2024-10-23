def sentence(name):
    def full_sentence(city):
        return f"My name is {name} and city is {city}."

    return full_sentence

message = sentence("Jacek")

print(message("Warszawa"))
print(message.__closure__[0].cell_contents)


def power_factory(exponent):
    def power(base):
        return base ** exponent

    return power


power10 = power_factory(10)
power5 = power_factory(5)


print(power10(2))
print(power5(2))

def gen_id(idx=0):
    def next_id(new_value=None):
        nonlocal idx
        if new_value is not None:
            idx = new_value
        result = idx
        idx += 1
        return result
    return next_id

""" to będzie działało i nie wymaga nonlocal
def gen_id():
    def next_id():
        result = next_id.idx
        next_id.idx += 1
        return result
    
    next_id.idx = 0
    return next_id
"""

next_id_ = gen_id(6)
print(next_id_())
print(next_id_())
print(next_id_())
print(next_id_(5))
print(next_id_())
print(next_id_())
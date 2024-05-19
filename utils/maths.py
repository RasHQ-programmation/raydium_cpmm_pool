class U128:
    def __init__(self, value=0):
        if not (0 <= value < 2**128):
            raise ValueError("Value out of range for U128")
        self.value = value

    def __repr__(self):
        return f"U128({self.value})"

    def __add__(self, other):
        return U128((self.value + other.value) % 2**128)

    def __sub__(self, other):
        return U128((self.value - other.value) % 2**128)

    def __mul__(self, other):
        return U128((self.value * other.value) % 2**128)

    def __floordiv__(self, other):
        return U128(self.value // other.value)

    def __mod__(self, other):
        return U128(self.value % other.value)

    def checked_div(self, other):
        if other.value == 0:
            return None
        return U128(self.value // other.value)

    def checked_rem(self, other):
        if other.value == 0:
            return None
        return U128(self.value % other.value)

    def checked_add(self, other):
        return U128((self.value + other.value) % 2**128)

    def checked_mul(self, other):
        return U128((self.value * other.value) % 2**128)


class U256:
    def __init__(self, value=0):
        if not (0 <= value < 2**256):
            raise ValueError("Value out of range for U256")
        self.value = value

    def __repr__(self):
        return f"U256({self.value})"

    def __add__(self, other):
        return U256((self.value + other.value) % 2**256)

    def __sub__(self, other):
        return U256((self.value - other.value) % 2**256)

    def __mul__(self, other):
        return U256((self.value * other.value) % 2**256)

    def __floordiv__(self, other):
        return U256(self.value // other.value)

    def __mod__(self, other):
        return U256(self.value % other.value)

    def checked_div(self, other):
        if other.value == 0:
            return None
        return U256(self.value // other.value)

    def checked_rem(self, other):
        if other.value == 0:
            return None
        return U256(self.value % other.value)

    def checked_add(self, other):
        return U256((self.value + other.value) % 2**256)

    def checked_mul(self, other):
        return U256((self.value * other.value) % 2**256)


class CheckedCeilDivMixin:
    @staticmethod
    def checked_ceil_div(a, b):
        if b == 0:
            return None

        quotient = a // b
        if quotient == 0:
            if a * 2 >= b:
                return 1, 0
            else:
                return 0, 0

        remainder = a % b
        if remainder > 0:
            quotient += 1
            min_amount_needed = a // quotient
            remainder = a % quotient
            if remainder > 0:
                min_amount_needed += 1

            return quotient, min_amount_needed

        return quotient, b


# # Example usage:
# u128_a = U128(500)
# u128_b = U128(50)
# result = CheckedCeilDivMixin.checked_ceil_div(u128_a.value, u128_b.value)
# print(result)

# u256_a = U256(500)
# u256_b = U256(50)
# result = CheckedCeilDivMixin.checked_ceil_div(u256_a.value, u256_b.value)
# print(result)

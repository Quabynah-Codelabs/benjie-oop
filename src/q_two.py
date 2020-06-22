"""Question 2"""


class Groups:
    # constructor
    def __init__(self, z: int, s: int):
        self.z = z
        self.s = s
        self.membermult = 1

    # sums up the attributes
    def sum(self):
        result = self.z + self.s
        print("Result of summation -> " + str(result))

    # multiplication of `membermult` and `b`
    def multiplication(self, b: int):
        result = self.membermult * b
        print("Result of multiplication -> " + str(result))

    # static method that deducts `c` from `b`
    @staticmethod
    def deduct(b: int, c: int):
        result = b - c
        print("Result of deduction -> " + str(result))

    # a tuple of `z` & `s`
    def _value(self):
        return self.z, self.s

    # deleter
    def delete_value(self):
        self.z = 0
        self.s = 0

    # setter
    def set_value(self, z: int, s: int):
        self.z = z
        self.s = s


# Inherited group
class InheritedGroup(Groups):

    # new constructor with third parameter
    def __init__(self, s: int, z: int, y: int):
        # override parent's constructor
        super().__init__(z, s)
        self.y = y

    # overriding the parent's sum method
    def sum(self):
        result = self.z + self.s + self.y
        print("Result of summation -> " + str(result))

# todo: uncomment to see results
# if __name__ == '__main__':
#     new_group = Groups(3, 2)
#     new_group.sum()
#     new_group.multiplication(5)
#     new_group.delete_value()
#     new_group.set_value(14, 12)
#     print(new_group.s, new_group.z)
#     Groups.deduct(6, 2)
#
#     inherited = InheritedGroup(5, 12, 9)
#     inherited.sum()

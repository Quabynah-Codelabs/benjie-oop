"""Question 3b"""


class Person:
    # ununsed property
    titles: ["Dr", "Mr", "Mrs", "Ms"]

    # constructor
    def __init__(self, title: str, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title

    # Full name property
    def fullName(self):
        if self.first_name == "" or self.last_name == "":
            print("No name defined")
        else:
            print(self.title + ". " + self.first_name + " " + self.last_name)

    # Full name setter
    def fullNameSetter(self, full_name: str):
        # split into first name and last name
        spliced_name = full_name.split()
        # first name
        self.first_name = spliced_name[0]
        # last name
        self.last_name = spliced_name[1]
        # print full name
        self.fullName()

    # Full name deleter
    def fullNameDeleter(self):
        # split into first name and last name
        # first name
        self.first_name = ""
        # last name
        self.last_name = ""
        # print full name
        self.fullName()

# todo: uncomment to test results
# if __name__ == '__main__':
#     user = Person("Mr", "John", "Doe")
#     user.fullName()
#     user.fullNameSetter("Eric Doe")
#     user.fullNameDeleter()

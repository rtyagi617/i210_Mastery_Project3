class Person:
    """Creates an person object"""

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def __str__(self):
        reply = "\nName: " + self.__name + "\n"
        reply += "Email: " + self.__email + "\n"
        return reply

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email

    def set_name(self, name):
        self.__name = name
    
    def set_email(self, email):
        self.__email = email 

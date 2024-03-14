class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    # function for get a name and set your name of a User
    def get_name(self):
        # i get name
        return self.__name

    def set_name(self, new_name: str):
        # i change the name to a new email
        self.__name = new_name

    def get_email(self):
        # i get email
        return self.__email

    def set_email(self, new_email):
        # i verify that new_email contains @ and .
        if '@' in new_email and '.' in new_email:
            # I change the email to a new email
            self.__email = new_email
        else:
            raise ValueError('Email is not valid')

    def __str__(self):
        # Devuelve una representación de cadena del objeto User
        return f"User: {self.__name} ({self.__email})"

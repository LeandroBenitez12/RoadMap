class User():
    def __init__(self, name : str, username : str, password : str, email : str, age : int):
        self.__name = name
        self.__username = username
        self.__password = password
        self.__email = email
        self.__age = age

    def __del__(self):
        print(' Instantiated Object has been deleted successfully ')

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    
    def get_username(self):
        return self.__username
    def set_username(self, new_username):
        self.__username = new_username
    
    def get_password(self):
        return self.__password
    def set_password(self, new_password):
        self.__password = new_password
    
    def get_email(self):
        return self.__email
    def set_email(self, new_email):
        self.__email = new_email
    
    def get_age(self):
        return self.__age
    def set_email(self, new_email):
        self.__email = new_email

if __name__ == '__main__':
    User_Leandro = User('Leandro', 'Leancabj.2004', 'Bokitapasion2004', 'Leanbenitz2004@gmail.com', 19)
    
    print(User_Leandro.__dict__)
    print(User_Leandro.get_email())
    print(User_Leandro.set_name('Leo'))
    print(User_Leandro.__dict__)
    del User_Leandro

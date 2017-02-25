class User():

    def __init__(self,name,surname,email,password,age,gender,profession,education):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.age = age
        self.gender = gender
        self.profession = profession
        self.education = education
        self.preferences = []

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getSurname(self):
        return self.surname

    def setSurname(self,surname):
        self.surname = surname

    def getEmail(self):
        return self.email

    def setEmail(self,email):
        self.email = email

    def getPassword(self):
        return self.password

    def setPassword(self,password):
        self.password = password

    def getAge(self):
        return self.age

    def setAge(self,age):
        self.age = age

    def getGender(self):
        return self.gender

    def setGender(self,gender):
        self.gender = gender

    def getProfession(self):
        return self.profession

    def setProfession(self,profession):
        self.profession = profession

    def getEducation(self):
        return self.education

    def setEducation(self,education):
        self.education = education

    def setPreferences(self,preferences):
        self.preferences = preferences

    def serialize(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password,
            'age': self.age,
            'gender': self.gender,
            'profession': self.profession,
            'education': self.education,
            'preferences': self.preferences,
        }
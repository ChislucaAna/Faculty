from utils import get_padding

class Course:
    entities=0
    def __init__(self,name,professor):
        self.__id=Course.entities
        self.__name=name
        self.__professor=professor
        Course.entities+=1
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def professor(self):
        return self.__professor

    def __get_class_fields_as_collumns(self):
        return (
            "|" + get_padding(self.__id) + "Id" + get_padding(self.__id) +
            "|" + get_padding(self.__name) + "Name" + get_padding(self.__name) +
            "|" + get_padding(self.__professor) + "Professor" + get_padding(self.__professor) +
            "|" + "\n")
    
    def __get_object_field_values(self):
        return (
            "|" + get_padding(self.__id) + str(self.__id) + get_padding(self.__id) +
            "|" + get_padding(self.__name) + str(self.__name) + get_padding(self.__name) +
            "|" + get_padding(self.__professor) + str(self.__professor) + get_padding(self.__professor) +
            "|" + "\n"
        )
    
    def __str__(self):
        return (
            self.__get_class_fields_as_collumns() +
            50 * "-" + "\n" +
            self.__get_object_field_values()+
            50 * "-" + "\n"
        )
    
    def __repr__(self):
        return ("Id: "+ str(self.id) +" Name: "+ str(self.name) + " Professor: " +str(self.professor)+"\n")
    
    @staticmethod
    def courselist_as_table(list_of_courses : list['Course'], header)->str:
        table = ""
        table += header + "\n"
        table+=50 * "-" + "\n"
        for course in list_of_courses:
            table+=course.__get_object_field_values()
            table+=50 * "-" + "\n"
        return table

from utils import get_padding

class Student:
    entities=0
    def __init__(self,name):
        self.__id=Student.entities
        self.__name=name
        Student.entities+=1
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name

    def __get_class_fields_as_collumns(self):
        return (
            "|" + get_padding(self.__id) + "Id" + get_padding(self.__id) +
            "|" + get_padding(self.__name) + "Name" + get_padding(self.__name) +
            "|" + "\n")
    
    def __get_object_field_values(self):
        return (
            "|" + get_padding(self.__id) + str(self.__id) + get_padding(self.__id) +
            "|" + get_padding(self.__name) + str(self.__name) + get_padding(self.__name) +
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
        return ("Id: "+ str(self.id) +" Name: "+ str(self.name) +"\n")
    
    @staticmethod
    def studentlist_as_table(list_of_students : list['Student'], header)->str:
        table = ""
        table += header + "\n"
        table+=50 * "-" + "\n"
        for Student in list_of_students:
            table+=Student.__get_object_field_values()
            table+=50 * "-" + "\n"
        return table
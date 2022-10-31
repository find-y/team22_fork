#!/usr/local/bin/python
# coding: utf-8
"""
Модуль описывает абстрактный интерфейс элемента списка дел AbstractTaskListElement и его реализацию TaskListElement
"""
# для того, чтобы создавать НАСТОЯЩИЕ абстрактные классы, нужно наследовать их от abc.ABC
from abc import ABCMeta, abstractmethod
class AbstractTaskListElement():
    """
    попробую проверить методологию создания абстрактного интерфейса и отдельно её реализации
    Данный класс определяет, как должно обеспечиваться взаимодействие одного элемента 
    списка дел (то есть, тройки [Название/дата по плану/ дата готовности]) с внешним миром.
    делать оно это конечно будет через соответствующие методы;
    наконец ещё выяснил что наше дело корректно называть task. это было очевидно с самого начала, но что-то мешало
    использовать это слово.
    https://docs-python.ru/tutorial/klassy-jazyke-python/abstraktnye-klassy/ - первая ссылка в яндексе по теме.
    https://habr.com/ru/post/72757/ третья ссылка в яндексе.
    пример из первой ссылки не работает.
    также видно что есть много способов делать одно и то же.
    """
    #AbstractTaskListElement(ABCMeta) тоже работает. достаточно чего-то одно или можно оба?
    __metaclass__=ABCMeta # можно указать тут метакласс, а можно наверное от него наследовать. это одно и то же?
    
    #преобразовать данные в список 
    @abstractmethod
    def as_list(self): # кто-то определяет список параметров прямо тут в абстракте, кто-то этого не делает.
        pass
    
    #взять из списка, состоящего из трех строчек
    @abstractmethod
    def from_list(self, list_of_three_strings): #как указать, что я хочу тут именн лист а не что-то ещё?
        pass
    
    #вывести результат как строку
    @abstractmethod
    def as_string(self):
        pass
    
    pass # закончили
    
    
class TaskListElement(AbstractTaskListElement):
    """
    это реализация интерфейса взаимодействия списка дел с миром
    """
    #пустой конструктор
    #def __init__(self):
    #    self.__task = u""
    #    self.__date_planned = u""
    #    self.__date_completed = u""   # забыл что тут нельзя несколько конструкторов
        
    def __init__(self,list_of_three_strings=[u"",u"",u""]):
        #self.__init__(self)  # вот так вообще нормально делать? я как-то напарывался на приколы, но не помню уже о чем там шла речь
        self.__task = u""
        self.__date_planned = u""
        self.__date_completed = u""
        self.from_list(list_of_three_strings)
    def __str__(self):
        return unicode(u"|" + unicode(self.__task) + u"|" + self.__date_planned + u"|" + self.__date_completed+ u"|").encode("UTF-8")
    def __repr__(self):
        return unicode(unicode(id(self)) + u"|" + self.__task + u"|" + self.__date_planned + u"|" + self.__date_completed+ u"|").encode("UTF-8")
    #НАПИСАТЬ КОММЕНТАРИЙ        
    def __is_input_list_correct(self, list_of_three_strings):
        correct_data = True
        if((type(list_of_three_strings) != type(list()))and (len(list_of_three_strings) != 3)):
            correct_data = False
        else:            
            for element in list_of_three_strings:
                if(type(element) != type(unicode())):
                    correct_data = False
        return correct_data
    #вынужден определить as_list
      
    def as_list(self):
        return [self.__task,self.__date_planned,self.__date_completed]
    def from_list(self, list_of_three_strings):
        if(self.__is_input_list_correct(list_of_three_strings)):        
            self.__task = list_of_three_strings[0]
            self.__date_planned = list_of_three_strings[1]
            self.__date_completed = list_of_three_strings[2]
        else:
            print(u'incorrect input, list of three strings is required, but' )
            print(list_of_three_strings)
            print(u'given. class data initialized with empty strings')
            self.__task = u""
            self.__date_planned = u""
            self.__date_completed = u""
            
    def as_string(self):
        return self.__str__()

    def as_hiu(self): # проверяю контроль интерфейса
        return "}{yU"
    pass

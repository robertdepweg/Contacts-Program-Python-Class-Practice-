# MODULE:  contact_module                   used by PROJECT:  ContactsProgram
#          contains Contact CLASS
# AUTHOR:  Robert Depweg                                 DESIGNER:  Dr. Kaminski
# MODIFICATION: CLC f-strings, conditional call to main, KVCC refs
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Contact:
    # ----------------------------------------------------- INSTANCE VARIABLES
    # TODO:  show the 2 variables as comments here to remind yourself of their
    #       names and make them PRIVATE.
    # __name
    # __phone
    # ------------------------------------------- ATTRIBUTE INITIALIZER METHOD
    def __init__(self, name = '', phone = ''):  # uses default values if
                                              # "caller" not provide parameters
    # TODO:  finish this method
        self.__name: str = name
        self.__phone: str = phone


        print('OK, added a new Contact instance (without data values)')

    # -------------------------------------------- STATE REPRESENTATION METHOD
    def __str__(self):

        state: str = (f'Contact:  {self.__name}{"  /  "}{self.__phone}')
        return state

    # --------------------------------------------------------- SETTER METHODS
    # TODO:  write the 2 setters
    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    # --------------------------------------------------------- GETTER METHODS
    # TODO:  write the 2 getters
    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    # ---------------------------------------------------------- OTHER METHODS
    # TODO:  finish the 7 methods - replace the dummy return values with
    #       the correct code.
    #       Implement the following class methods using string slicing
    #       Phone #:  (269) 488-1000
    #          269            488-1000            488         1000
    #       area code       local number     local prefix    ending
    #
    def get_initial(self):
        ''' Extract initial of first name. '''
        self.__first_initial: str = self.__name[0:1]
        return self.__first_initial

    def get_area_code(self):
        ''' gets area code: 269 '''
        self.__area_code: str = self.__phone[0:3]
        return self.__area_code

    def get_local_num(self):
        ''' local number: 488-1000 '''
        self.__local_num: str = (f'{self.__phone[3:6]}{"-"}{self.__phone[6:10]}')
        return self.__local_num

    def local_prefix(self):
        ''' grabs middle part of number: 488 '''
        self.__prefix: str = self.__phone[3:6]
        return self.__prefix

    def is_sw_michigan(self):
        ''' Determines if area code is in SW michigan area '''
        if self.__area_code == '269':
            return True
        else:
            return False

    def is_kvcc(self):
        ''' Determines if area code/prefix is in range of KVCC '''
        if (self.__area_code == '269') and (self.__prefix == '488' or self.__prefix == '373'):
            return True
        else:
            return False

    def make_nice_phone(self):
        ''' adds formatting of the number '''
        self.__nice_phone: str = (f'{"("}{self.__phone[0:3]}'
        f'{") "}{self.__phone[3:6]}{"-"}{self.__phone[6:10]}')
        return self.__nice_phone

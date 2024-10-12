# PROJECT:  ContactsProgram                 uses MODULE:  contact_module
#                                                   contains Contact CLASS
# AUTHOR:   Robert Depweg                                DESIGNER:  Dr. Kaminski
# MODIFICATION: CLC f-strings, conditional call to main, KVCC refs
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import contact_module as con

def main():
    print('STARTING THE PROGRAM\n')

    # TODO:  Declare 2 objects:  person1 & person2    of Contact class type.
    #   (Don't include parameter values here since you don't yet have values)
    person1 = con.Contact()
    person2 = con.Contact()

    name: str = 'John Smith'             # hardcoded instead of user input
    phone: str = '2694881000'            # hardcoded instead of user_input
    # TODO:  store this data in person1 object (using the setters)
    person1.set_name(name)
    person1.set_phone(phone)


    name = 'Latisha Brown'          # hardcoded instead of user input
    phone = '6163871000'              # hardcoded instead of user_input
    # TODO:  store this data in person2 object (using the setters)
    person2.set_name(name)
    person2.set_phone(phone)


    # Test some class methods on the 2 objects.
    test_methods(person1)            # TODO:  uncomment this when ready
    test_methods(person2)            # TODO:  uncomment this when ready

    print('\nTHE END')


def test_methods(person):
    print('\nTESTING')
    print(person)

    # Call the methods to get the data needed from the object to print the
    #       test results below (once you've written the class's methods).
    # TODO:  REPLACE 'X's and False's with the method call.

    # obtains name of person
    name = con.Contact.get_name(person) 

    # obtains first character of name
    initial: str = con.Contact.get_initial(person) 

    # obtains phone # of person
    phone = con.Contact.get_phone(person) 

    # gets area code
    area_code: str = con.Contact.get_area_code(person) 

    # gets local #
    local_number: str = con.Contact.get_local_num(person) 

    # grabs middle part of #
    local_prefix: str = con.Contact.local_prefix(person) 

    # adds formatting to phone #
    nice_phone: str = con.Contact.make_nice_phone(person) 

    # determines if # is from sw michigan
    is_sw_michigan: bool = con.Contact.is_sw_michigan(person) 

    # determines if # is from kvcc area
    is_kvcc_ttc: bool = con.Contact.is_kvcc(person) 

    # print test results
    print(f'{name} (starts with {initial}) has phone number: {phone}')

    print(f'\tarea code: {area_code}, local number: {local_number}, (local prefix: {local_prefix})')

    print(f'\tphone number {nice_phone}', end='')
    
    # determines what text to print based on is_sw_michigan's response
    if is_sw_michigan:
        print(f' IS from SW Michigan')
    else:
        print(f' is NOT from SW Michigan')

    # determines what text to print based on is_kvcc_ttc's response
    print(f'\tand the number', end='')
    if is_kvcc_ttc:
        print(f' IS a KVCC number')
    else:
        print(f' is NOT a KVCC number')


main()

user_data = {}


def input_error(func):
    def inner(string):
        try:
            result = func(string)
        except (ValueError,KeyError,IndexError) as error:
            return str(error)
        else:
            return result
    return inner


@input_error
def command_hello(string):
    return "How can I help you?"


@input_error
def command_add(string):
    if len(string.split())<3:
        raise IndexError(f"Give me name and phone please")
    if not str(string.split()[2]).isdigit() :
        raise ValueError(f"Write your phone number correctly")
    data = {string.split()[1]: string.split()[2]}
    user_data.update(data)
    return f'You have added a user {string.split()[1]} with a phone number {string.split()[2]}'


@input_error
def command_change(string):
    if len(string.split())<3:
        raise IndexError(f"Give me name and phone please")
    if not str(string.split()[2]).isdigit() :
        raise ValueError(f"Write your phone number correctly")
    data = {string.split()[1]: string.split()[2]}
    user_data.update(data)
    return f'You have changed {string.split()[1]} phone number to {string.split()[2]}'

@input_error
def command_phone(string):
    if string.split()[1] not in user_data or len(string.split())<2:
        raise IndexError(f"User with name {string.split()[1]} does not exist")
    phone = user_data.get(string.split()[2])
    return phone

@input_error
def command_show_all(string):
    return user_data

@input_error
def command_exit(string):
    return "Good bye!"


OPERATIONS = {
                'hello': command_hello,
                'add': command_add,
                'change': command_change,
                'phone': command_phone,
                'show all': command_show_all,
                'exit': command_exit
              }


def answers(operation):
    if 'hello' in operation:
        return OPERATIONS.get(operation, command_hello)
    elif 'add' in operation:
        return OPERATIONS.get(operation, command_add)
    elif 'change' in operation:
        return OPERATIONS.get(operation, command_change)
    elif 'phone' in operation:
        return OPERATIONS.get(operation, command_phone)
    elif 'show all' in operation:
        return OPERATIONS.get(operation, command_show_all)
    elif 'exit' in operation:
        return OPERATIONS.get(operation, command_exit)

def main():
    while True:
        operation = input('Enter command (hello, add, change, phone, show all, exit): ')
        operation = str(operation.split()[0].lower()) + ' ' + ' '.join(operation.split()[1:])
        hello_func = answers(operation)
        hello_func(operation)
        if hello_func(operation) == "Good bye!":
            print(hello_func(operation))
            break
        elif 'add' in operation:
            print(hello_func(operation))
        elif 'change' in operation:
            print(hello_func(operation))
        elif "hello" in operation:
            print(hello_func(operation))
        elif 'phone' in operation:
            print(hello_func(operation))
        elif 'show all' in operation:
            print(hello_func(operation))


if __name__ == '__main__':
    main()






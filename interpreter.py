import sys


def interpret(source):

    data = [0] * 30000
    data_ptr = 0
    source_ptr = 0
    output = ''

    while source_ptr < len(source):

        command = source[source_ptr]

        if command == '>':
            data_ptr += 1

        elif command == '<':
            data_ptr -= 1

        elif command == '+':
            data[data_ptr] += 1

        elif command == '-':
            data[data_ptr] -= 1

        elif command == '.':
            # sys.stdout.write(chr(data[data_ptr]))
            output += chr(data[data_ptr])

        elif command == ',':
            data[data_ptr] = sys.stdin.read(1)

        elif command == '[' and data[data_ptr] == 0:
            loop = 1

            while loop > 0:
                source_ptr += 1
                temp_command = source[source_ptr]
                if temp_command == '[':
                    loop += 1
                elif temp_command == ']':
                    loop -= 1

        elif command == ']' and data[data_ptr] != 0:
            loop = 1

            while loop > 0:
                source_ptr -= 1
                temp_command = source[source_ptr]
                if temp_command == '[':
                    loop -= 1
                elif temp_command == ']':
                    loop += 1

        source_ptr += 1  # move to next command

    return output


if __name__ == "__main__":

    hello_world_source = '''
        ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.
        +++++++..+++.>++.<<+++++++++++++++.>.+++.------.
        --------.>+.>.
    '''

    result = interpret(hello_world_source)

    print result

    assert result == 'Hello World!\n', 'something went wrong!'

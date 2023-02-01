try:
    file = open('text.txt', 'r')
    print('File is found')
except FileNotFoundError:
    print('File not found or path is incorrect')
finally:
    print('exit')

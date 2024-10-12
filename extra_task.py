import os
import time

offset = ' '
end = '\u001b[0m'
yellow = '\u001b[43;1m'
black = '\u001b[40;1m'

def sleep_and_clear():
    time.sleep(1)
    os.system("cls")
    print('\n')

while True:
    print(offset * 4, f'{yellow} ' * 8, end)
    print(offset * 2, f'{yellow} ' * 2, f'{black} ' * 2, f'{yellow}' * 1, f'{black} ' * 2, f'{yellow} ' * 2,  end)
    print(offset * 1, f'{yellow} ' * 14, end)
    print(offset * 2, f'{yellow} ' * 12, end)
    print(offset * 4, f'{yellow} ' * 8, end)

    sleep_and_clear()

    print(offset * 4, f'{yellow} ' * 8, end)
    print(offset * 2, f'{yellow} ' * 2, f'{black} ' * 2, f'{yellow}' * 1, f'{black} ' * 2, f'{yellow} ' * 2, end)
    print(offset * 1, f'{yellow} ' * 14, end)
    print(offset * 2, f'{yellow} ' * 3, f'{black} ' * 4, f'{yellow} ' * 3, end)
    print(offset * 4, f'{yellow} ' * 8, end)

    sleep_and_clear()
x_axis = [str(i) + '  ' for i in range(10)]
y_axis = [str(round(i / 3, 2)) for i in range(10)]
for current_string in range(9, -1, -1):
    print(y_axis[current_string] + ' \t' * (current_string + 1) + "!!")
print('\n', ' ' * 6, *x_axis)
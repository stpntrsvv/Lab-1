file = open('sequence.txt').readlines()
sequence = [float(file[i][:-1]) for i in range(len(file))]

first_condition_nums = []
second_condition_nums = []

for i in sequence:
    if (i >= -3) and (i <= 3):
        first_condition_nums.append(i)
    else:
        second_condition_nums.append(i)

print('\x1b[44m   ' * 3, '\x1b[m', str((len(first_condition_nums)/len(sequence))*100) + '%')
print('\x1b[45m   ' * 7, '\x1b[m', str((len(second_condition_nums)/len(sequence))*100) + '%')

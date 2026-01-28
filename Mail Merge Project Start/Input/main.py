with open('Input/Names/invited_names.txt') as file1:
    names  = file1.readlines()

with open('Input/Letters/starting_letter.txt') as file2:
    content = file2.read()

for i in range(len(names)):
    new_letter = content.replace('[name]', names[i].strip())
    with open(f'Output/ReadyToSend/letter_for_{names[i]}.txt','w') as file3:
        file3.write(new_letter)



from Group import Group

harris = 'Harris Jessica'
ivanov = 'Ivanov Ivan'
adamson = 'Adamson Samuel'
evans = 'Evans Joseph'
smith = 'Smith Olivia'
walker = 'Walker Emily'
davies = 'Davies Thomas'
wilson = 'Wilson George'
king = 'King Lily'

group = [harris, ivanov, adamson, evans, smith, walker, davies, wilson, king]
group = Group(group)
print(group)
lewis = 'Lewis Isabella'
group.add_student(lewis)
print(group)
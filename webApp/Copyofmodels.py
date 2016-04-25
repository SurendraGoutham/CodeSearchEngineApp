from sets import Set
engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
engineers3 = Set(['John', 'Jane', 'Jack', 'Janice'])
engineers2 = Set(['Jane', 'Jack', 'Janice'])
programmers = Set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = Set(['Jane', 'Jack', 'Susan', 'Zack'])
employees = engineers | programmers | managers# union
engineering_management = engineers & managers# intersection
fulltime_management = managers - engineers - programmers# difference
engineers.add('Marvin')# add element
#print engineers
#print employees.issuperset(engineers)# superset test
#print employees.update(engineers)# update from another set
#print employees.issuperset(engineers)
#print engineers3.issubset(engineers)
for group in [engineers, programmers, managers, employees]:
    group.discard('Susan')# unconditionally remove element
#print group
listitems = ['John', 'Jane', 'Jack', 'Janice']
words = Set(['Jack', 'Samt', 'Susant', 'Janicet'])

words |= Set(listitems)
print words
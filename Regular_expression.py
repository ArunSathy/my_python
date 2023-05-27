import re

# pat=r"arun"

#------match-----------

# if re.match(pat,'arun sathyan, how are you doing'):
#     print('present')
# else:
#     print('absent')

#--------search----------

# if re.search(pat,'hello arun sathyan'):
#     print('present')
# else:
#     print('absent')

#---------findall---------------

# print(re.findall(pat,'arun sathyan hello arun where are you arun'))

#------find&replace-------------

# strg="I'm arun Sathyan, I'm an amazonian"
# new=re.sub('arun','Arun',strg) # first element is the pattern 'arun' & second one is the replacement'Arun'
# print(new)

#---------.match------------------

# pat=r'a..n'
#
# if re.match(pat,'arun'):
#     print('present')
# else:
#     print('absent')

#--------------character class----------------------

pat=r'[A-Z][a-z][0-9]'

if re.search(pat,'Bi8'):
    print('preset')
else:
    print('absent')







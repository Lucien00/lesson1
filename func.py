def get_summ(one, two, delimiter='&'):
   return f'{one}{delimiter}{two}'

lp = get_summ('Learn', 'python')
print(lp.upper())

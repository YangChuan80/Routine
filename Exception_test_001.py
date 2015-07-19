class M(Exception):
    pass

s='What a wonderful world!'

try:
    raise M()
except M:
    print('I got the raised exception!')


try:
    s[100]
finally:
    print('Have finalized!')

print('Continue?')

#abcfdsafdsafsdf
    

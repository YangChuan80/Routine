try:
    def divide(x,y):
        x/y

    r=divide(1, 1)
    print(r)

except ZeroDivisionError:
    print('The divide num is not supposed to be zero')

else:
    print('Correct!!!!!!!!!!')

finally:
    print('Termination Action Reached!')

print('Continuing...')

class NewException(Exception):
    pass

ExceptionInstance=NewException()

try:
    raise ExceptionInstance

except NewException:
    print('Class Exception caught!')
    


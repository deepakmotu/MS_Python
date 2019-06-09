import logging

logging.basicConfig(level=logging.DEBUG,  filename='logging.log', format='%(asctime)s, %(levelname)s, %(message)s, %(relativeCreated)s, %(processName)s,%(threadName)s, %(thread)s')

def add(num1,num2):
    return num1+num2

def subs(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

num1=5
num2=15

add_result=add(num1,num2)
logging.debug('Adding Result is {add_result}')

subs_result=subs(num1,num2)
logging.debug(f'Substracting result is {subs_result}')

multiply_result=multiply(num1,num2)
logging.debug(f'Multiply result is {multiply_result}')

div_result=div(num1,num2)
logging.debug(f'Divide result is {div_result}')


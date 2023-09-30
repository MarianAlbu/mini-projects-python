#add
def add(n1,n2):
  return n1+n2

#Subtract
def subtract(n1,n2):
  return n1-n2

#Multiply
def multiply(n1,n2):
  return n1*n2

#Divide
def divide(n1,n2):
  return n1/n2
operations={
  '+':add, 
  '-':subtract,
  '*':multiply,
  '/':divide
}

def calculator():
  num1=float(input('what is the first number?'))
  for operation in operations:
    print(operation)
  should_continue= True
  while should_continue:
    operation_symbol = input('Pick an operation: ')
    num2=float(input('what is the next number?'))
    calculation_function=operations[operation_symbol]
    answer=calculation_function(num1,num2)

    print(f'{num1} {operation_symbol} {num2} = {answer}')

    if input(f"Type 'y' to continue calculating with {answer} or 'n' to start new calculation") == 'y':
      num1=answer
    else:
      should_continue=False
      calculator()
calculator()

'''''operation_symbol = input('Pick another operation: ')
num3=int(input('what is the next number?'))
calculation_function=operations[operation_symbol]
second_answer=calculation_function(first_answer,num3)

print(f'{first_answer} {operation_symbol} {num3} ={second_answer}')'''''
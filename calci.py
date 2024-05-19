from art import logo
def add(num1,num2):
  return num1+num2
def sub(num1,num2):
  return num1-num2
def prod(num1,num2):
  return num1*num2
def div(num1,num2):
  return num1/num2
operations = {
  "+": add,
  "-":sub,
  "*":prod,
  "/":div
  
}
def calculator():
  print(logo)
  should_continue = True
  while(should_continue):
    num1 = int(input("what is the first number"))
    for symbol in operations:
      print(symbol)
    operation_symbol = input("pick an operation from an line above")
    num2 = int(input("what is the second number"))  
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if(input("enter y to continue with the same answer or n to continue with the wrong answer"))=="y":
      num1 =answer
    else:
      should_continue = False
      calculator()
calculator()      

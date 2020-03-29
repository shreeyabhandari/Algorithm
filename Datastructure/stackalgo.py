
def create_stack():   # create a stack
  return []


def is_empty(q):   #check whether the stack is empty 
  return q == []


def peek(q):   # return the first item of the stack
  if is_empty(q):
    print('Error, the stack is empty')
  else:
    return q[0]
  
  
def s_push(s, x):   # add an element to the stack
  if is_empty(s):
    s.append(x)
  else:
    s = [x]+s
  return s


def s_stack(s):   # remove an element of the stack
  s.pop(0)
  return s

def create_queue(): # create a queue
  return []



def is_empty(q): #check whether queue is empty
  return q == []




def peek(q):  # returns the first item of the queue
  if is_empty(q):
    print('Error, the queue is empty')
  else:
    return q[0]
  
  
  
def enqueue(q, x): # add an element to the queue
  q.append(x)
  return q


def de_queue(q):  #remove an element of the queue
  q.pop(0)
  return q


  
  
  
 



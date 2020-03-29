def bubble_sort(tab):
  swap = true
  n = len(tab)
  while swap:
    swap = false
    for i in range(n-1):
      if tab[i] > tab[i + 1]:
        tab[i], tab[i + 1] = tab[i + 1], tab[i]
        swap = true
    n = n - 1
  return tab
        
  

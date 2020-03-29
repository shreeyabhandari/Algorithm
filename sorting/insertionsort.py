def insertion_sort(tab):
  n = len(tab)
  for i in range(l, n):
    j = i
    while (j > 0) and (tab[j] < tab[j - 1]):
      tab[j], tab[j-1] =tab[j - 1], tab[j]
      j -= 1
  return tab
 

def selection_sort(tab):
  n = len(tab)
  for i in range(n):
    min_pos = i
    for j in range(i + 1, n):
      if tab[j] < tab[min_pos]:
        min_pos = j
    tab[i], tab[min_pos] = tab[min_pos], tab[i]
  return tab  


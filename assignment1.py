Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> x=[0,1,2,3,4,5,6,7,8,9]
>>> 
>>> #applying all lists
>>> 
>>> x.append(3)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
>>> 
>>> x.extend([10,11])
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 10, 11]
>>> 
>>> x.pop()
11
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 10]
>>> 
>>> x.copy()
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 10]
>>> 
>>> x.sort()
>>> 
>>> x
[0, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> x.reverse()
>>> x
[10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 0]
>>> 
>>> x.remove(3)
>>> x
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
>>> x.insert(7,4)
>>> x
[10, 9, 8, 7, 6, 5, 4, 4, 3, 2, 1, 0]
>>> 
>>> #part 2
>>> 
>>> y=[p*10 for p in x]
>>> y
[100, 90, 80, 70, 60, 50, 40, 40, 30, 20, 10, 0]
>>> 
>>> #part 3
>>> 
>>> for p in x:
	print(p*10)

	
100
90
80
70
60
50
40
40
30
20
10
0
>>> 
>>> k=x[:5]
>>> k
[10, 9, 8, 7, 6]
>>> 
>>> v=x[5:10]
>>> v
[5, 4, 4, 3, 2]
>>> 
>>> 
>>> #Question 2
>>> 
>>> n=[[1,2,3],[4,5,6],[7,8,9]]
>>> 
>>> for sublists in n
SyntaxError: invalid syntax
>>> for sublists in n:
	for y in sublist:
		m.append(y)

		
Traceback (most recent call last):
  File "<pyshell#55>", line 2, in <module>
    for y in sublist:
NameError: name 'sublist' is not defined

>>> #repeats the above step
>>> 
>>> m=[]
>>> n[[1,2,3],[4,5,6],[7,8,9]]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    n[[1,2,3],[4,5,6],[7,8,9]]
TypeError: list indices must be integers or slices, not tuple
>>> n=[[1,2,3],[4,5,6],[7,8,9]]
>>>  for sublists in n:
	for y in sublist:
		m.append(y)
		
SyntaxError: unexpected indent
>>> m
[]
>>> 



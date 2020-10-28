import collections
de=collections.deque([1,2,3,3,4,3])
#using append() to insert element at right side
de.append(5)
print('de after append 5 :----------\n',de)

#using appendleft() to insert element at left side
de.appendleft(6)
print('de after appendleft 6 :----------\n',de)

#using pop() to remove element from right side
de.pop()
print('de after pop right element :----------\n',de)

#using popleft() to remove element from left side
de.popleft()
print('de after pop left element :----------\n',de)

#inset(i,a)...'i' is index value and 'a' is value to be inserted
#it insert 7 at 3rd position
de.insert(2,7)
print('de after insert 7 at 3rd position :----------\n',de)

#using count() to count ocurrences of number
print('de after count of no. 3 :----------\n',de.count(3))

#using remove() to remove the 1sr occurence of number passed
de.remove(3)
print('de after remove 1st occurence of 3 :----------\n',de)

#using index(a,i,j) to find position of 1st occurence 'a' from index 'i' to 'j'
print('de after finding position of 1st occurence of 3 :----------\n',de.index(4,1,5))

#using extend() to add multiple elements at right side
de.extend([8,9,10])
print('de after extend of values 8,9,10 :----------\n',de)

#using extendleft() to add multiple elements at left side
de.extendleft([11,12,13])
print('de after extendleft of vales 11,12,13 :----------\n',de)

#using rotate() to rotate deque
#using '-3' we can rotate to left and using '3' we can rotate to right
de.rotate(-3)
print('de after rotating deque to left by 3 :----------\n',de)

#using reverse() to reverse a deque
de.reverse()
print('de after reverse :----------\n',de)

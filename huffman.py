
######################## Priteh Borad ##################################
import numpy as np
import cv2
import operator
from heapq import heappush,heappop,heapify
from bitarray import bitarray

message = ['A','C','D','E','C','A','A','C','B','B']
charac = ['A','B','C','D','E']
x = {}
for i in charac:
    x.update( {i : message.count(i)/len(message)} )
x=dict(sorted(x.items(), key=operator.itemgetter(1)))
print(x)
heap = [[fq, [sym, ""]] for sym, fq in x.items()]  # '' is for entering the huffman code later\
heapify(heap) # transform the list into a heap tree structure
while len(heap) > 1:
    right = heappop(heap)  # heappop - Pop and return the smallest item from the heap
    print('right = ', right)
    left = heappop(heap)
    print('left = ', left)

    for pair in right[1:]:  
        pair[1] = '0' + pair[1]   # add zero to all the right note
    for pair in left[1:]:  
        pair[1] = '1' + pair[1]   # add one to all the left note
    heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])  # add values onto the heap. Eg. h = []; heappush(h, (5, 'write code')) --> h = [(5, 'write code')]
huffman_list = right[1:] + left[1:]
print(huffman_list)
huffman_dict = {a[0]:bitarray(str(a[1])) for a in huffman_list}
print(huffman_dict)
encoded_text = bitarray()
encoded_text.encode(huffman_dict, message)
print(encoded_text)
######################## Priteh Borad ##################################
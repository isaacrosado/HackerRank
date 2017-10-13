#!/bin/python3

import sys


def getLeft(i):
    return int(2 * i + 1)


def getRight(i):
    return int(2 * i + 2)


def getParent(i):
    if i % 2 == 0:
        return int(i / 2 - 1)
    return int((i + 1) / 2 - 1)


def maxHeapify(maxHeap, i):
    left = getLeft(i)
    right = getRight(i)
    largest = i
    if left < len(maxHeap) and maxHeap[left] > maxHeap[i]:
        largest = left
    if right < len(maxHeap) and maxHeap[right] > maxHeap[largest]:
        largest = right
    if largest != i:
        maxHeap[i], maxHeap[largest] = maxHeap[largest], maxHeap[i]
        maxHeapify(maxHeap, largest)


def extractMax(maxHeap):
    maximum = maxHeap[0]
    maxHeap[0] = maxHeap[-1]
    del maxHeap[-1]
    maxHeapify(maxHeap, 0)
    return maximum


def heapIncreaseKey(maxHeap, i, key):
    maxHeap[i] = key
    parent = getParent(i)
    while i > 0 and key > maxHeap[parent]:
        maxHeap[i], maxHeap[parent] = maxHeap[parent], maxHeap[i]
        i = parent
        parent = getParent(i)


def maxHeapInsert(maxHeap, key):
    maxHeap.append(-float("inf"))
    heapIncreaseKey(maxHeap, len(maxHeap) - 1, key)


def minHeapify(minHeap, i):
    left = getLeft(i)
    right = getRight(i)
    smallest = i
    if left < len(minHeap) and minHeap[left] < minHeap[i]:
        smallest = left
    if right < len(minHeap) and minHeap[right] < minHeap[smallest]:
        smallest = right
    if smallest != i:
        minHeap[i], minHeap[smallest] = minHeap[smallest], minHeap[i]
        minHeapify(minHeap, smallest)


def extractMin(minHeap):
    minimum = minHeap[0]
    minHeap[0] = minHeap[-1]
    del minHeap[-1]
    minHeapify(minHeap, 0)
    return minimum


def heapDecreaseKey(minHeap, i, key):
    minHeap[i] = key
    parent = getParent(i)
    while i > 0 and key < minHeap[parent]:
        minHeap[i], minHeap[parent] = minHeap[parent], minHeap[i]
        i = parent
        parent = getParent(i)


def minHeapInsert(minHeap, key):
    minHeap.append(float("inf"))
    heapDecreaseKey(minHeap, len(minHeap) - 1, key)


n = int(input().strip())
a = []
aLength = 0
a_i = 0
maxHeap = []
minHeap = []
maxHeapSize = 0
minHeapSize = 0
median = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
    aLength += 1
    if aLength == 1:
        median = a_t
        print("%.1f" % median)
    else:
        if a_t > median:
            minHeapInsert(minHeap, a_t)
            minHeapSize += 1
        else:
            maxHeapInsert(maxHeap, a_t)
            maxHeapSize += 1
        if minHeapSize > maxHeapSize + 1:
            maxHeapInsert(maxHeap, median)
            maxHeapSize += 1
            median = extractMin(minHeap)
            minHeapSize -= 1
        elif maxHeapSize > minHeapSize + 1:
            minHeapInsert(minHeap, median)
            minHeapSize += 1
            median = extractMax(maxHeap)
            maxHeapSize -= 1
        if maxHeapSize > minHeapSize:
            calculatedMedian = (median + maxHeap[0]) / 2
            print("%.1f" % calculatedMedian)
        elif minHeapSize > maxHeapSize:
            calculatedMedian = (median + minHeap[0]) / 2
            print("%.1f" % calculatedMedian)
        else:
            print("%.1f" % median)
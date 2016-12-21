# -*- coding: utf-8 -*-
import time
import random
import resource
import math


def get_randomarray(size):

    """ Returnerar en osorterad lista med slumpad data av längden size
    """

    return [random.randint(1,10000) for _ in xrange(size)]


def insertion_sort(numlist):

    """ Implementation av insertionsort som arbetar på listan numlist Går igenom alla elleent listan (utom det första)
    från början och sedan jämförs det med alla föregående tills ett lika stort eller större hittas. Då flyttas
    elementet till possitionen före det som hittats.
    """

    for index in xrange(1,len(numlist)):

        currentvalue = numlist[index]
        position = index

        while position>0 and numlist[position-1]>currentvalue:
            numlist[position]=numlist[position-1]
            position = position-1

        numlist[position]=currentvalue


def insertion_sort_binary(numlist):

    """ Implementation av binary insertionsort som arbetar på listan numlist. Fungerar likt insertionsort fast istället
    för att jämföra elementen med alla föregående så gämför man med det dellersta elementet bland de föregående i
    listan och sedan fortsätter man så (fast frammåt till förra kontrollerade element-1 om det ska sorteras in efter)
    tills rätt possition hittas.
    """

    for index in xrange(1, len(numlist)):

        currentvalue = numlist[index]
        bottom, top = 0, index

        while bottom < top:
            middle = (bottom + top) // 2
            if numlist[middle] < currentvalue:
                bottom = middle + 1
            else:
                top = middle

        numlist[:] = numlist[:bottom] + [currentvalue] + numlist[bottom:index] + numlist[index + 1:]


def merge_sort_insert(numlist, minlength):

    """ Den variant av mergesort som delar upp listan tills sublistorna når ett satt värde (minlength) eller mindre, kör
    insertionsort på varje sublista och sedan använder sätter ihop dem som mergsort vanligtvis gör.
    """

    if len(numlist)>minlength:

        middle = len(numlist) // 2
        lefthalf, righthalf = numlist[:middle], numlist[middle:]

        merge_sort_insert(lefthalf, minlength)
        merge_sort_insert(righthalf, minlength)

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numlist[k]=lefthalf[i]
                i=i+1
            else:
                numlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            numlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            numlist[k]=righthalf[j]
            j=j+1
            k=k+1
    else:
        insertion_sort(numlist)


def merge_sort_binary(numlist, minlength):

    """ Den variant av mergesort som delar upp listan tills sublistorna når ett satt värde (length) eller mindre, kör
    binary insertionsort på varje sublista och sedan använder sätter ihop dem som mergsort vanligtvis gör.
    """

    if len(numlist)>minlength:

        middle = len(numlist) // 2
        lefthalf, righthalf = numlist[:middle], numlist[middle:]

        merge_sort_binary(lefthalf, minlength)
        merge_sort_binary(righthalf, minlength)

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numlist[k]=lefthalf[i]
                i=i+1
            else:
                numlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            numlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            numlist[k]=righthalf[j]
            j=j+1
            k=k+1
    else:
        insertion_sort_binary(numlist)

def merge_sort(numlist):

    """Vanlig mergesort. Delar upp listan i halvor rekursivt tills listlängden är 1. Sedan sätts de ihop men i sorterad
    ordning där man letar efter sorterade block, inte enbart individuella ellement när 2 listor slås ihop (vid korta
    listor eller få möjliga värden så kanske det dock alldrig blir block längre än 1).
    """

    if(len(numlist) > 1):

        middle = len(numlist) // 2
        lefthalf, righthalf = numlist[:middle], numlist[middle:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numlist[k]=lefthalf[i]
                i=i+1
            else:
                numlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            numlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            numlist[k]=righthalf[j]
            j=j+1
            k=k+1
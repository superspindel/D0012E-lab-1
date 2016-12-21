# -*- coding: utf-8 -*-
import lab1
import time


def kVarLnGraphLaTEX(avrgRuns, kRange, arrayLength):

    """ Skriver tiderna (genomsnitt av avrgRuns körningar) som de olika algoritmerna tar vid olika k värden
    (som stiger med *2) och fast listlängd till en fil formaterat som en LaTEX graf.
    """

    return_file_ins = open("insert_"+str(arrayLength)+".tex", "w")
    return_file_ins.write("    \\addplot[color=blue]\n    coordinates {\n")
    return_file_bin = open("binary_"+str(arrayLength)+".tex", "w")
    return_file_bin.write("    \\addplot[color=red]\n    coordinates {\n")
    return_file_mer = open("merge_"+str(arrayLength)+".tex", "w")
    return_file_mer.write("    \\addplot[color=green]{")


    divider = 1
    i = 1
    while divider <= kRange:
        mergeSortIns_time = 0
        mergeSortBin_time = 0
        mergeSort_time = 0

        for n in range(0,avrgRuns-1):
            tmp = lab1.get_randomarray(arrayLength)
            start = time.time()
            lab1.merge_sort_insert(tmp, divider)
            mergeSortIns_time += (time.time() - start)
        mergeSortIns_time /= avrgRuns
        return_file_ins.write("        ("+str(divider)+", "+str(mergeSortIns_time)+")\n")

        for n in range(0,avrgRuns-1):
            tmp = lab1.get_randomarray(arrayLength)
            start = time.time()
            lab1.merge_sort_binary(tmp, divider)
            mergeSortBin_time += (time.time() - start)
        mergeSortBin_time /= avrgRuns
        return_file_bin.write("        ("+str(divider)+", "+str(mergeSortBin_time)+")\n")

        print str(divider)

        divider = 2 ** i
        i += 1

    for n in range(0,avrgRuns-1):
        tmp = lab1.get_randomarray(arrayLength)
        start = time.time()
        lab1.merge_sort(tmp)
        mergeSort_time += (time.time() - start)
    mergeSort_time /= avrgRuns
    return_file_mer.write(str(mergeSort_time))

    return_file_ins.write("    };\n\\addlegendentry{Insert Mergesort}\n")
    return_file_ins.close()
    return_file_bin.write("    };\n\\addlegendentry{Binary Mergesort}\n")
    return_file_bin.close()
    return_file_mer.write("    };\n\\addlegendentry{Mergesort}\n")
    return_file_mer.close()


def kVarPrecGraphLaTEX(avrgRuns, kRange, arrayLength):

    """ Skriver tiderna (genomsnitt av avrgRuns körningar) som de olika algoritmerna tar vid olika k värden
    (som stiger med +1) och fast listlängd till en fil formaterat som en LaTEX graf.
     """

    return_file_ins = open("insert_"+str(arrayLength)+"-"+str(kRange) + ".tex", "w")
    return_file_ins.write("    \\addplot[color=blue]\n    coordinates {\n")
    return_file_bin = open("binary_"+str(arrayLength)+"-"+str(kRange)+".tex", "w")
    return_file_bin.write("    \\addplot[color=red]\n    coordinates {\n")
    return_file_mer = open("merge_"+str(arrayLength)+"-"+str(kRange)+".tex", "w")
    return_file_mer.write("    \\addplot[color=green]{")

    divider = 1
    while divider <= kRange:
        mergeSortIns_time = 0
        mergeSortBin_time = 0
        mergeSort_time = 0

        for n in range(0,avrgRuns-1):
            tmp = lab1.get_randomarray(arrayLength)
            start = time.time()
            lab1.merge_sort_insert(tmp, divider)
            mergeSortIns_time += (time.time() - start)
        mergeSortIns_time /= avrgRuns
        return_file_ins.write("        ("+str(divider)+", "+str(mergeSortIns_time)+")\n")

        for n in range(0,avrgRuns-1):
            tmp = lab1.get_randomarray(arrayLength)
            start = time.time()
            lab1.merge_sort_binary(tmp, divider)
            mergeSortBin_time += (time.time() - start)
        mergeSortBin_time /= avrgRuns
        return_file_bin.write("        ("+str(divider)+", "+str(mergeSortBin_time)+")\n")

        print str(divider)

        divider += 1

    for n in range(0,avrgRuns-1):
        tmp = lab1.get_randomarray(arrayLength)
        start = time.time()
        lab1.merge_sort(tmp)
        mergeSort_time += (time.time() - start)
    mergeSort_time /= avrgRuns
    return_file_mer.write(str(mergeSort_time))

    return_file_ins.write("    };\n\\addlegendentry{Insert Mergesort}\n")
    return_file_ins.close()
    return_file_bin.write("    };\n\\addlegendentry{Binary Mergesort}\n")
    return_file_bin.close()
    return_file_mer.write("    };\n\\addlegendentry{Mergesort}\n")
    return_file_mer.close()


def lVarLnGraphLaTEX(avrgRuns, lRange, k):

    """ Skriver tiderna (genomsnitt av avrgRuns körningar) som de olika algoritmerna tar vid olika n (lRange)
    värden (som stiger med *2) och fast k till en fil formaterat som en LaTEX graf.
    """

    return_file_ins = open("insert_variable_length.tex", "w")
    return_file_ins.write("    \\addplot[color=blue]\n    coordinates {\n")
    return_file_bin = open("binary_variable_length.tex", "w")
    return_file_bin.write("    \\addplot[color=red]\n    coordinates {\n")
    return_file_mer = open("merge_variable_length.tex", "w")
    return_file_mer.write("    \\addplot[color=green]\n    coordinates {\n")


    l = 1024
    while l <= lRange:
        mergeSortIns_time = 0
        mergeSortBin_time = 0
        mergeSort_time = 0

        for n in range(0,avrgRuns-1):
            tmp = lab1.get_randomarray(l)
            start = time.time()
            lab1.merge_sort_insert(tmp, k)
            mergeSortIns_time += (time.time() - start)
        mergeSortIns_time /= avrgRuns
        return_file_ins.write("        ("+str(l)+", "+str(mergeSortIns_time)+")\n")

        for n in range(0,avrgRuns-1):
            tmp = lab1.get_randomarray(l)
            start = time.time()
            lab1.merge_sort_binary(tmp, k)
            mergeSortBin_time += (time.time() - start)
        mergeSortBin_time /= avrgRuns
        return_file_bin.write("        ("+str(l)+", "+str(mergeSortBin_time)+")\n")

        for n in range(0,avrgRuns-1):
            tmp = lab1.get_randomarray(l)
            start = time.time()
            lab1.merge_sort(tmp)
            mergeSort_time += (time.time() - start)
        mergeSort_time /= avrgRuns
        return_file_mer.write("        ("+str(l)+", "+str(mergeSort_time)+")\n")

        print str(l)

        l *= 2

    return_file_ins.write("    };\n\t\\addlegendentry{Insert Mergesort}\n")
    return_file_ins.close()
    return_file_bin.write("    };\n\t\\addlegendentry{Binary Mergesort}\n")
    return_file_bin.close()
    return_file_mer.write("    };\n\t\\addlegendentry{Mergesort}\n")
    return_file_mer.close()


def kOptimal(b, arrayLength, avrgRuns):

    """ Returnerar det optimala kvärdet för en av algoritmerna (vilken bestäms av b) vid en listlängd (arrayLength)
    under avrgRuns körningar.
    """

    best = 10000.0
    bestK = 0

    k = 2
    while(k <= 65):

        runTime = 0
        for n in range(0,avrgRuns -1):
            rArray = lab1.get_randomarray(arrayLength)

            start = time.time()
            if b == 1:
                lab1.merge_sort_binary(rArray, k)
            else:
                lab1.merge_sort_insert(rArray, k)

            runTime += (time.time() - start)
        runTime /= avrgRuns

        if (runTime < best):
            best = runTime
            bestK = k

        k *= 2

    return bestK


def kOptimalGraphLaTEX(avrgRuns, arrayLengthMax):

    """ Hittar det optimala k värdet för olika listlängder för de båda algoritmerna och skriver resultatet till en LaTEX
    graf.
    """

    return_file_ins = open("insert_optimal-k<="+str(arrayLengthMax)+".tex", "w")
    return_file_ins.write("    \\addplot[\n        color=blue,\n        mark=*,\n    ]\n    coordinates {\n")
    return_file_bin = open("binary_optimal-k<="+str(arrayLengthMax)+".tex", "w")
    return_file_bin.write("    \\addplot[\n        color=red,\n        mark=*,\n    ]\n    coordinates {\n")

    arrayLength = 1024
    while(arrayLength <= arrayLengthMax):
        return_file_ins.write("        ("+str(arrayLength)+", "+str(kOptimal(0, arrayLength, avrgRuns))+")\n")
        return_file_bin.write("        ("+str(arrayLength)+", "+str(kOptimal(1, arrayLength, avrgRuns))+")\n")
        arrayLength *= 2

    print "k_max = " + str(arrayLength)

    return_file_ins.write("    };\n    \\addlegendentry{Insert Mergesort}\n")
    return_file_ins.close()
    return_file_bin.write("    };\n    \\addlegendentry{Binary Mergesort}\n")
    return_file_bin.close()

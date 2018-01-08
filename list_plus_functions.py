def counting_strings(x):
    count = 0

    for count_the_strings in x:
        if count_the_strings == 'boomy':
            count = count + 1
    return count

array_of_boomy = ['boomy', 'brodie', 'boomy', 'bomy', 'boomy', 'boomy']
counting_boomy = counting_strings(array_of_boomy)
print (counting_boomy)
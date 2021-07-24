# Character Frequency Histogram
**This program reads a text file and counts how many times a character is used in the text file**

*for example:*
we have a text file called **text.txt**

text.txt:

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.

the program outputs this to the console:

    b  ->  5 
    e  ->  14
    a  ->  6 
    u  ->  3 
    t  ->  16
    i  ->  12
    f  ->  1 
    l  ->  8 
    s  ->  5 
    r  ->  4 
    h  ->  4 
    n  ->  4 
    g  ->  1 
    y  ->  1 
    x  ->  3 
    p  ->  6 
    c  ->  6 
    m  ->  5 
    o  ->  3 
    d  ->  1

The Output after being sorted:
 
    a  ->  6
    b  ->  5
    c  ->  6
    d  ->  1
    e  ->  14
    f  ->  1
    g  ->  1
    h  ->  4
    i  ->  12
    l  ->  8
    m  ->  5
    n  ->  4
    o  ->  3
    p  ->  6
    r  ->  4
    s  ->  5
    t  ->  16
    u  ->  3
    x  ->  3
    y  ->  1

## Updated Version of Character Frequency Histogram

**This version also reads a text file but outputs the result to a to a text file with the same name but it adds a "hist_" prefix to the name of the file, it also sorts the output using the values instead of the key**

*for example:*
we have a text file called **text.txt**

text.txt:

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.

hist_text.txt:

    t -> 16
    e -> 14
    i -> 12
    l -> 8
    a -> 6
    p -> 6
    c -> 6
    b -> 5
    s -> 5
    m -> 5
    r -> 4
    h -> 4
    n -> 4
    u -> 3
    x -> 3
    o -> 3
    f -> 1
    g -> 1
    y -> 1
    d -> 1
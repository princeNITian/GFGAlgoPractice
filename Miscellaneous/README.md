- Problem Description
    - [Array Element frequency count](arrayCount.py)
        - Given an unsorted array of n integers which can contain integers from 1 to n. Some elements can be repeated multiple times and some other elements can be absent from the array. Count frequency of all elements that are present and print the missing elements.
    
    - [Google SWE Internship Q2](googleswe2.py)
        - There are N-words in a dictionary such that each word is of fixed length M and consists of only lowercase English letters that are (‘a’, ‘b’, ……. ‘z’).

        - A query word denoted by Q. The length of query word in M. These words contain lowercase English letters but at some places instead of a letter between ‘a’, ‘b’, ……. ‘z’ there is ‘?’ .Refer to the Sample input section to understand this case.

        - A match count of Q, denoted by match_count(Q), is the count of words that are is the dictionary and contain the same English letters (excluding a letter that can be in the position of ?) in the same position as the letters are there are in the query word Q.

        - In other words, a word in the dictionary can contain any letters at the position ‘?’ but the remaining alphabets must match with the query word.

        - You are given a query word Q and you are required to compute match_count(Q).

        -  **Sample Input**
        >

            5 3
            cat
            map
            bat
            man
            pen
            4
            ?at
            ma?
            ?a?
            ??n
        - **Sample Output**
        >
            2
            2
            4
            2

    - [Trie Problem](trie2.py)
        - Given a 2D board and a list of words from the dictionary, find all words in the board, Each word must be constructed from letters of sequentially adjacent cell, wherer "adjacent" cellls are those horizonatlly or vertically neighboring.
        The same letter cell may not be used more than once in a word.
        > **Input**
        - board = [<br>
            ['o','a','a','n'],<br>
            ['e','t','a','e'],<br>
            ['i','h','k','r'],<br>
            ['i','f','l','v']<br>
        ]
        <br>
            words = ["oath","pea","eat","rain"]<br>
        > Output:  ["eat","oath"]
    - Next  &#8265;
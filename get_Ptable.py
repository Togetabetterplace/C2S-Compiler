"""
使用非递归的预测分析表做语法分析————预测分析表的生成

"""
from lexer import Word_List, k_list
import sys
import os
import re

sys.path.append(os.pardir)

# 文法
grammars = {
    "Program": ["type M C Pro"],
    "C": ["( cc )"],
    "cc": ["null"],

    "Pro": ["{ Pr }"],
    "Pr": ["P Pr", "null"],
    "P": ["type L ;", "L ;", "printf OUT ;", "Pan", "Fen"],

    "L": ["M LM"],
    "LM": ["= FE", "Size AM", "null"],
    "FE": ["E", "TEXT", "CHAR"],
    "M": ["name"],

    "E": ["T ET"],
    "ET": ["+ T ET", "- T ET", "null"],
    "T": ["F TT"],
    "TT": ["* F TT", "/ F TT", "null"],
    "F": ["number", "BRA", "M MS"],
    "MS": ["Size", "null"],
    "BRA": ["( E )"],

    "OUT": ["( TXT V )"],
    "TXT": ['TEXT'],
    "V": [", E VV", "null"],
    "VV": [", E VV", "null"],

    "Pan": ["Ptype P_block Pro"],
    "Ptype": ["if", "while"],
    "P_block": ["( Pbc )"],
    "Pbc": ["E PM"],
    "PM": ["Cmp E", "null"],

    "Fen": ["Ftype F_block Pro"],
    "Ftype": ["for"],
    "F_block": ["( Lt ; Pbc ; L )"],
    "Lt": ["L"],

    "Size": ["[ E ]"],
    "AM": ["= E", "null"]
}

first_table = {}
follow_table = {}
predict_table = {}
observer = {}

"""
初始化记录者
记录者： 用于求follow集合的过程中特殊情况：
    非终结符的后继非终结符的first集合可能存在null
    eg： A -> BC     C -> D | null   D -> (A) | i
    那么在一次遍历过程中，因为C的first集合存在null，所以需要将follow（A）加入follow（B）
    !但是！此时的follow（A），并不是完整的，它可能在后续的遍历中会继续更新自身的follow集合
    所以此时会出现遗漏的follow
    所以我在这里用到一个记录者模式
    记录者为一个字典，字典键值为产生式左部，字典内容为产生式右部
"""


def init_observer():
    for k in grammars:
        follow_table[k] = []
        observer[k] = []
        for next_grammar in grammars[k]:
            last_k = next_grammar.split()[-1]
            if last_k in grammars and last_k != k:
                observer[k].append(last_k)


def refresh(k):
    """
    This function is used to refresh the follow set of a non-terminal symbol.
    It checks if the follow set of a non-terminal symbol has been updated,
    and if so, it updates the follow set of all non-terminal symbols that have been recorded as observers.
    This process is done recursively.

    Parameters:
    k (str): The non-terminal symbol for which the follow set needs to be refreshed.

    Returns:
    None
    """
    for lk in observer[k]:
        newlk = U(follow_table[k], follow_table[lk])
        if newlk != follow_table[lk]:
            follow_table[lk] = newlk
            refresh(lk)


def U(A, B):
    """
    This function merges two lists and removes duplicates.

    Parameters:
    A (list): The first list to be merged.
    B (list): The second list to be merged.

    Returns:
    list: A new list that contains all unique elements from both input lists.

    Example:
    >>> U([1, 2, 3], [2, 3, 4])
    [1, 2, 3, 4]
    """
    return list(set(A + B))


def find_first(key):
    """
    This function calculates the first set of a non-terminal symbol in a given context-free grammar.

    Parameters:
    key (str): The non-terminal symbol for which the first set needs to be calculated.

    Returns:
    list: A list containing the first set of the non-terminal symbol.

    The first set of a non-terminal symbol is the set of terminal symbols that can appear as the first symbol in any string derived from that non-terminal symbol.
    """
    if key not in grammars:
        # If the key is not in grammars, it is a terminal symbol, so return it as the first set.
        return [key]

    l = []  # Initialize an empty list to store the first set.

    # Iterate over all productions of the non-terminal symbol.
    for next_grammar in grammars[key]:
        # Get the first symbol of the production.
        next_k = next_grammar.split()[0]

        # Recursively calculate the first set of the first symbol and extend the list.
        l.extend(find_first(next_k))

    return l  # Return the calculated first set.


def find_follow():
    """
    This function calculates the follow set of all non-terminal symbols in a given context-free grammar.

    The follow set of a non-terminal symbol is the set of terminal symbols that can appear immediately to the right of that non-terminal symbol in any string derived from the grammar.

    Parameters:
    None

    Returns:
    None

    The function uses the following steps:
    1. Initialize the observer dictionary to keep track of non-terminal symbols that need to be updated when their follow sets change.
    2. Add the '#' symbol to the follow set of the start symbol (Program).
    3. Iterate over all non-terminal symbols in the grammar.
    4. For each non-terminal symbol, iterate over all its productions.
    5. For each production, iterate over all symbols except the last one.
    6. If the current symbol is a non-terminal symbol, check if its first set contains any terminal symbols.
    7. If the first set does not contain any terminal symbols, add the follow set of the current non-terminal symbol to the follow set of the current symbol.
    8. If the first set contains a terminal symbol, add that terminal symbol to the predict table.
    9. If the first set contains the 'null' symbol, add the follow set of the current non-terminal symbol to the predict table.
    10. Add the follow set of the current non-terminal symbol to the follow set of the last symbol of the production.
    11. Remove the 'null' symbol from the follow sets of all non-terminal symbols.
    """
    init_observer()
    follow_table["Program"] = ["#"]  # follow(S)加入#号
    for k in grammars:
        for next_grammar in grammars[k]:
            next_k = next_grammar.split()
            for i in range(0, len(next_k) - 1):
                if next_k[i] in grammars:
                    if next_k[i + 1] not in grammars:
                        """
                        If the subsequent character is not a terminal symbol, add it to the follow set.
                        """
                        new_follow = U([next_k[i + 1]],
                                       follow_table[next_k[i]])
                        if new_follow != follow_table[next_k[i]]:
                            follow_table[next_k[i]] = new_follow
                            refresh(next_k[i])
                    else:
                        new_follow = U(
                            first_table[next_k[i + 1]], follow_table[next_k[i]])
                        """
                        If the first set of the subsequent character contains 'null', notify all observers to update the follow set.
                        """
                        if "null" in first_table[next_k[i + 1]]:
                            new_follow = U(follow_table[k], new_follow)
                            observer[k].append(next_k[i])
                        if new_follow != follow_table[next_k[i]]:
                            follow_table[next_k[i]] = new_follow
                            refresh(next_k[i])
            """
            Add the follow set of the non-terminal symbol to the follow set of the last non-terminal symbol.
            """
            if next_k[-1] in grammars:
                if next_k[-1] not in follow_table:
                    follow_table[next_k[-1]] = []
                if next_k[-1] != k:
                    follow_table[next_k[-1]
                                 ] = U(follow_table[next_k[-1]], follow_table[k])
    for k in follow_table:
        if "null" in follow_table[k]:
            follow_table[k].remove("null")


def get_first_table():
    """
    This function populates the first_table and predict_table dictionaries.

    The first_table dictionary stores the first set of each non-terminal symbol in the grammar.
    The predict_table dictionary stores the predict set of each non-terminal symbol in the grammar.

    Parameters:
    None

    Returns:
    None

    The function iterates over each non-terminal symbol in the grammar.
    For each non-terminal symbol, it initializes an empty dictionary entry in the predict_table.
    Then, it iterates over each production of the non-terminal symbol.
    For each production, it extracts the first symbol and calculates its first set.
    It extends the first set of the non-terminal symbol with the calculated first set.
    Then, it adds each terminal symbol in the first set to the predict_table,
    associating it with the current production.
    """
    for k in grammars:
        # Initialize an empty dictionary for predict set of non-terminal symbol k
        predict_table[k] = {}
        # Initialize an empty list for first set of non-terminal symbol k
        first_table[k] = []
        for next_grammar in grammars[k]:
            # Extract the first symbol of the production
            next_k = next_grammar.split()[0]
            # Calculate the first set of the first symbol
            kl = find_first(next_k)
            # Extend the first set of non-terminal symbol k with the calculated first set
            first_table[k].extend(kl)
            for kk in kl:
                if kk != "null":  # If the terminal symbol is not 'null'
                    # Add the terminal symbol to the predict set of non-terminal symbol k
                    predict_table[k][kk] = next_grammar


def get_predict_table():
    """
    This function populates the predict_table dictionary with the predict set of each non-terminal symbol in the grammar.

    Parameters:
    None

    Returns:
    None

    The function iterates over each non-terminal symbol in the grammar.
    For each non-terminal symbol, it iterates over each production of the non-terminal symbol.
    For each production, it extracts the first symbol and checks if it is a non-terminal symbol with 'null' in its first set or if it is 'null' itself.
    If the condition is met, it adds each terminal symbol in the follow set of the non-terminal symbol to the predict set of the non-terminal symbol,
    associating it with the current production.
    """
    for k in grammars:
        for next_grammar in grammars[k]:
            next_k = next_grammar.split()[0]
            # If the first symbol of the production is a non-terminal symbol with 'null' in its first set or if it is 'null' itself
            if next_k in grammars and "null" in first_table[next_k] or next_k == "null":
                # Add each terminal symbol in the follow set of the non-terminal symbol to the predict set of the non-terminal symbol
                for fk in follow_table[k]:
                    predict_table[k][fk] = next_grammar


def Create_Predict_Table():
    get_first_table()
    find_follow()
    get_predict_table()
    return predict_table


def show_tables():
    get_first_table()
    find_follow()
    get_predict_table()
    print("\nfirst集合:\n")
    for k in first_table:
        print(k, first_table[k])
    print("\nfollow集合:\n")
    for k in follow_table:
        print(k, follow_table[k])
    # print(first_table)
    print("\n预测表:\n")
    for k in predict_table:
        print(k, predict_table[k])
    return first_table, follow_table, predict_table


if __name__ == "__main__":
    first_table, follow_table, predict_table = show_tables()

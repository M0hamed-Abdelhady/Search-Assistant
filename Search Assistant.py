import re
import sys
import webbrowser

exist_sites = ["Google", "YouTube", "YouTube Music", "Link"]


def search(query, site=1):
    """
    take Query and the index of the site in the list and search the query in the site
    """
    if site == 1:
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif site == 2:
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif site == 3:
        webbrowser.open(f"https://music.youtube.com/search?q={query}")
    elif site == 4:
        webbrowser.open(query)


def extract_quoted_words(text):
    """
    find and extract words surrounded by double quotation marks and return list of the words
    """
    words = re.findall(r'"([^"]*)"', text)
    return words


def choose_site():
    """
    print user interface to choose the site he wants and return site index in the list
    """
    while True:
        try:
            print("Choose (integer) site to search?\n")
            for i in range(len(exist_sites)):
                print(f"  [{i + 1}]{exist_sites[i]}")
            print(f"**[{len(exist_sites) + 1}]Cancel")
            site_str = input("\t-> ")
            site = int(site_str)
            if site < 1 or site > len(exist_sites) + 1:
                raise ValueError(
                    "Error! Please input integer that exist in choices")
            if site == len(exist_sites) + 1:
                sys.exit(interface())
            return site
        except ValueError as er:
            print(er)


def choose_site_for_each_element(words):
    """
    choose different search site for each element in the list that user inputted
    """
    for_edit = True
    print("Choose (integer) site to search?\n")
    for i in range(len(exist_sites)):
        print(f"  [{i + 1}]{exist_sites[i]}")
    print(f"**[{len(exist_sites) + 1}]Cancel\n")
    sites = []
    for i in range(len(words)):
        while True:
            try:
                site = int(input(f"[{i + 1}]{words[i]} => "))
                if site < 0 or site > len(exist_sites) + 1:
                    raise ValueError(
                        "Error! Please input integer that exist in choices")
                if site == len(exist_sites) + 1:
                    sys.exit(interface())
                sites.append(site)
                break
            except ValueError as err:
                print(err)

    # -----------------------------`Last Step`----------------------------------
    while True:
        try:
            if for_edit:
                choose_str = input("[1]Confirm  [2]Edit  [3]Cancel\n\t-> ")
                choose = int(choose_str)
            if choose == 1:
                for i in range(len(words)):
                    search(words[i], sites[i])
                sys.exit(interface())
            elif choose == 2:
                # -----------------------------`Edit`----------------------------------
                for_edit = False
                print(
                    "*Edit by setting a value to i and j ~this means the i-th word will be searched in "
                    "the j-th site\n*End editing by inputting 0 0")
                while True:
                    try:
                        i_str = input("i = ")
                        j_str = input("j = ")
                        i = int(i_str)
                        j = int(j_str)
                        if j < 1 or j > len(exist_sites) or i < 1 or i > len(words):
                            raise ValueError(
                                "Error! Please input integer that exist in choices")
                        sites[i - 1] = j
                        print(f"\2{words[i - 1]} => {exist_sites[j - 1]}")
                        break
                    except ValueError as er:
                        print(er)
                choose_str = input("[1]Confirm  [2]Edit  [3]Cancel\n\t-> ")
                choose = int(choose_str)
            elif choose == 3:
                sys.exit(interface())
            if choose < 1 or choose > 3:
                raise ValueError(
                    "Error! Please input integer that exist in choices")
        except ValueError as err:
            print(err)


def choose_site_for_all_elements(words):
    """
    choose one search site for all elements in the list that user inputted
    """
    for_edit = True
    site = choose_site()
    while True:
        try:
            if for_edit:
                choose_str = input(
                    f"You are close to search the previous list in {exist_sites[site - 1]}.\n"
                    f"  [1]Confirm  [2]Edit  [3]Cancel\n\t-> ")
            choose = int(choose_str)
            if choose == 1:
                for i in range(len(words)):
                    search(words[i], site)
                sys.exit(interface())
            elif choose == 2:
                for_edit = False
                site = choose_site()
                choose_str = input("[1]Confirm  [2]Edit  [3]Cancel\n\t-> ")
                choose = int(choose_str)
            elif choose == 3:
                sys.exit(interface())
            if choose < 1 or choose > 3:
                raise ValueError(
                    "Error! Please input integer that exist in choices")
        except ValueError as err:
            print(err)


def edit_list(words):
    """
    taking the user's list and enable him to edit it
    """
    while True:
        try:
            print("Your List is:")
            for i in range(len(words)):
                print(f"\t{i + 1}.{words[i]}")
            choose_str = input(f"  [1]Confirm the List  [2]Add Queries  [3]Remove Queries  [4]Cancel\n\t-> ")
            choose = int(choose_str)
            if choose == 1:
                return words
            elif choose == 2:
                print("Input Queries to Add to the list (input blank line to end inputting)")
                while True:
                    text = input()
                    if text == '':
                        break
                    words.append(text)
            elif choose == 3:
                print("Input Query index to REMOVE from the list (input blank line to end inputting)")
                print("*PLEASE NOTICE* THE ELEMENTS WILL BE REMOVED AFTER FINISH TAKING INPUT!")
                print("  (mean that if your input was many 1's this will delete just the first element)")
                knocked = []
                while True:
                    try:
                        num = input()
                        i = int(num)
                        if i > len(words):
                            print("No such index")
                        else:
                            knocked.append(i - 1)
                    except ValueError:
                        break
                knocked = list(set(knocked))
                knocked.reverse()
                for i in knocked:
                    del words[i]
            elif choose == 4:
                sys.exit(interface())
            if choose < 1 or choose > 4:
                raise ValueError("Error! Please input integer that exist in choices")
        except ValueError as err:
            print(err)


def check_list(words):
    """
    ask the user if he wants to confirm the list of edit something
    """
    while True:
        try:
            choose_str = input(f"  [1]Confirm the List  [2]Edit  [3]Cancel\n\t-> ")
            choose = int(choose_str)
            if choose == 1:
                return words
            elif choose == 2:
                return edit_list(words)
            elif choose == 3:
                sys.exit(interface())
            if choose < 1 or choose > 3:
                raise ValueError(
                    "Error! Please input integer that exist in choices")
        except ValueError as err:
            print(err)


def assistant(text="", in_type=3, words=None):
    """
    take text and in_type and words and make user choose the way of search and call the needed function
    """
    if words is None:
        words = []
    if in_type == 1:
        words = extract_quoted_words(text)
        print("Your List is:")
        for i in range(len(words)):
            print(f"\t{i + 1}.{words[i]}")
    elif in_type == 2:
        print(f"Your Text is: {words[0]}")
    else:
        print("Your List is:")
        for i in range(len(words)):
            print(f"\t{i + 1}.{words[i]}")
    words = check_list(words)
    while True:
        try:
            choose_str = input(
                "[1]Select All\n[2]Select one by one\n[3]Cancel\n\t-> ")
            choose = int(choose_str)
            if choose == 1:
                choose_site_for_all_elements(words)
            elif choose == 2:
                choose_site_for_each_element(words)
            elif choose == 3:
                sys.exit(interface())
            else:
                raise ValueError(
                    "Error! Please input integer that exist in choices")
            break
        except ValueError as err:
            print(err)


def interface():
    lst = []
    while True:
        in_str = input("[1]Input text and extract quoted\n[2]Input just text to search\n[3]Input list\n[4]Exit\n\t-> ")
        try:
            in_type = int(in_str)
            if in_type == 1:
                text = input("Input text and extract quoted to search: ")
                assistant(text, in_type)
                break
            elif in_type == 2:
                text = input("Input text to search: ")
                lst.append(text)
                assistant('', in_type, lst)
                break
            elif in_type == 3:
                print("Input your list (input blank line to end inputting) :")
                while True:
                    text = input()
                    if text == '':
                        break
                    else:
                        lst.append(text)
                assistant('', in_type, lst)
                break
            elif in_type == 4:
                sys.exit()
            if in_type < 1 or in_type > 4:
                raise ValueError(
                    "Error! Please input integer that exist in choices")
        except ValueError as er:
            print(er)


# ----------------------------------------`main`-------------------------------------

interface()

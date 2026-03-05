import re
RED = "\033[31m"
GREEN = "\033[32m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

keywords = ['if', 'elif', 'else', 'def', 'import']
string_pattern = r'(\".*?\"|\'.*?\')'

class highlighter:
    def __init__(self):
        pass

    def highlight(string):
        code, comment, comment_part = string.partition('#')

        if keywords:
            kw_pattern = r'\b(' + '|'.join(map(re.escape, keywords)) + r')\b'
            code = re.sub(kw_pattern, rf"{CYAN}\1{RESET}", code)


        code = re.sub(string_pattern, rf"{GREEN}\1{RESET}", code)

        print(f"{code}{RED}{comment}{comment_part}{RESET}")


highlighter.highlight('if elif else, "This is a string", print')

input()

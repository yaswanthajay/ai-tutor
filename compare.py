import difflib

def compare_user_code(user_code, correct_code):
    user_lines = user_code.strip().splitlines()
    correct_lines = correct_code.strip().splitlines()

    diff = difflib.unified_diff(user_lines, correct_lines, fromfile='User Code', tofile='Correct Code', lineterm='')
    return '\n'.join(diff)

import difflib
import re

def extract_functions(code: str) -> dict:
    """
    Extracts top-level functions from code.
    Returns a dictionary {function_name: full_function_code}
    """
    functions = {}
    lines = code.splitlines()
    i = 0
    while i < len(lines):
        match = re.match(r'^def (\w+)\(', lines[i])
        if match:
            name = match.group(1)
            start = i
            i += 1
            while i < len(lines) and (lines[i].startswith(' ') or lines[i].strip() == ''):
                i += 1
            functions[name] = '\n'.join(lines[start:i])
        else:
            i += 1
    return functions

def remove_functions_from_code(code: str) -> str:
    """
    Removes all top-level function definitions from the code.
    Returns code with only imports and inline code left.
    """
    lines = code.splitlines()
    cleaned_lines = []
    i = 0
    while i < len(lines):
        if re.match(r'^def \w+\(', lines[i]):
            i += 1
            while i < len(lines) and (lines[i].startswith(' ') or lines[i].strip() == ''):
                i += 1
        else:
            cleaned_lines.append(lines[i])
            i += 1
    return '\n'.join(cleaned_lines).strip()

def integrate_code(original_code: str, improved_code: str) -> str:
    """
    Replaces or adds functions from improved_code into original_code.
    """
    original_funcs = extract_functions(original_code)
    improved_funcs = extract_functions(improved_code)

    # Update or add functions
    for name, new_func in improved_funcs.items():
        original_funcs[name] = new_func

    # Clean out old function definitions from original
    base_code = remove_functions_from_code(original_code)

    # Assemble final code
    final_code = base_code + '\n\n' + '\n\n'.join(original_funcs.values())
    return final_code.strip()


def get_code_diff(original_code: str, improved_code: str) -> str:
    original_lines = original_code.strip().splitlines()
    improved_lines = improved_code.strip().splitlines()
    diff = difflib.unified_diff(original_lines, improved_lines, fromfile='Original', tofile='Improved', lineterm='')
    return '\n'.join(diff)
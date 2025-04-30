import difflib

def integrate_code(original_code: str, improved_code: str) -> str:
    """
    Basic integration: just returns the improved code (like applying a patch).
    """
    return improved_code

def get_code_diff(original_code: str, improved_code: str) -> str:
    original_lines = original_code.strip().splitlines()
    improved_lines = improved_code.strip().splitlines()
    diff = difflib.unified_diff(original_lines, improved_lines, fromfile='Original', tofile='Improved', lineterm='')
    return '\n'.join(diff)

import sys
import json

def normalize_name(name):
    """
    Normalizes a person's name to sound natural in a message.
    Example: 'JUAN PEDRO GONZALEZ' -> 'Juan'
    """
    # Logic to be implemented with LLM API
    # For now, a simple heuristic for demonstration
    parts = name.split()
    if not parts:
        return name
    first_name = parts[0].capitalize()
    return first_name

def normalize_company(company):
    """
    Normalizes a company name to sound natural.
    Example: 'ACME SOLUTIONS S.L.U.' -> 'Acme Solutions'
    """
    # Logic to be implemented with LLM API
    # Common suffixes to remove
    suffixes = ['S.L.', 'S.L.U.', 'S.A.', 'Inc.', 'Ltd.', 'Corporation', 'Group']
    normalized = company
    for suffix in suffixes:
        normalized = normalized.replace(suffix, '').strip()
    return normalized

def main():
    if len(sys.argv) < 3:
        print("Usage: python normalize_data.py <type: name|company> <value>")
        sys.exit(1)

    data_type = sys.argv[1]
    value = sys.argv[2]

    if data_type == 'name':
        print(normalize_name(value))
    elif data_type == 'company':
        print(normalize_company(value))
    else:
        print(f"Unknown type: {data_type}")

if __name__ == "__main__":
    main()

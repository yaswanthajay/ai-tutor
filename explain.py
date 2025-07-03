def generate_pseudocode(code):
    lines = code.strip().splitlines()
    pseudo = []

    for line in lines:
        line = line.strip()
        if line.startswith("def"):
            pseudo.append("Define a function")
        elif "for" in line:
            pseudo.append("Repeat over a range or list")
        elif "if" in line:
            pseudo.append("Check a condition")
        elif "=" in line:
            pseudo.append("Assign a value")
        else:
            pseudo.append("Do something")

    return "\n".join(pseudo)

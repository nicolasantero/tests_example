def write_to_file(s, filename):
    with open(filename, 'w') as f:
        f.write(s)

def read_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()
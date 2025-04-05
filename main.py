import sys


def replace(text, findChars, replaceChars):
    tr = dict(zip(findChars, replaceChars))
    return "".join([tr.get(c, c) for c in text])


def main():
    #        012345678
    valid = "oizehsglb"

    for line in sys.stdin.readlines():
        line = line.strip() # remove trailing whitespace
        line = replace(line, "éèêëìîïòôöùûü", "eeeeiiiooouuu")
        result = [c for c in line if c in valid]
        if len(result) != len(line):
            continue
        if len(result) == 1:
            continue
        print(line)

if __name__ == "__main__":
    main()

#156551479
def decode_instruction(data):
    def solve(pos=0):
        result = ''
        multiplier = ''
        while pos < len(data):
            char = data[pos]
            if char.isdigit():
                multiplier += char
            elif char == '[':
                fragment, pos = solve(pos + 1)
                result += fragment * int(multiplier if multiplier else 1)
                multiplier = ''
            elif char == ']':
                return result, pos
            else:
                result += char
            pos += 1
        return result, pos

    return solve()[0]

if __name__ == '__main__':
    print(decode_instruction(input()))


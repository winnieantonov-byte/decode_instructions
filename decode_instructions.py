#156551479
def decode_instruction(data: str) -> str:
    def solve(pos: int = 0) -> tuple[str, int]:
        result: str = ''
        multiplier: str = ''
        while pos < len(data):
            char: str = data[pos]
            if char.isdigit():
                multiplier += char
            elif char == '[':
                fragment, pos = solve(pos + 1)
                count: int = int(multiplier) if multiplier else 1
                result += fragment * count
                multiplier = ''
            elif char == ']':
                return result, pos
            else:
                result += char
            pos += 1
        return result, pos
    final_result, _ = solve()
    return final_result


if __name__ == '__main__':
    commands: str = input()
    print(decode_instruction(commands))



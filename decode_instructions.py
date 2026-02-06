#156502564
def decode_instructions(encrypted_str: str) -> str:
    result = ""
    multiplier = ""
    bracket_balance = 0
    substring = ""

    for char in encrypted_str:
        if char.isdigit() and bracket_balance == 0:
            multiplier += char
        elif char == '[':
            if bracket_balance > 0:
                substring += char
            bracket_balance += 1
        elif char == ']':
            bracket_balance -= 1
            if bracket_balance > 0:
                substring += char
            else:
                count = int(multiplier) if multiplier else 1
                result += count * decode_instructions(substring)
                multiplier = ""
                substring = ""
        elif bracket_balance > 0:
            substring += char
        else:
            result += char

    return result


if __name__ == '__main__':
    comands = input()
	print(decode_instructions(comands))
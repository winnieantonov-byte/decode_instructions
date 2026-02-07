#156529281
def decode_instructions(encrypted_str: str, i=0) -> tuple[str, int]:
    result = ""
    multiplier = 0  
    while i < len(encrypted_str):
        char = encrypted_str[i]
        if char.isdigit():
            multiplier = multiplier * 10 + int(char)
        elif char == '[':
            substring, next_i = decode_instructions(encrypted_str, i + 1)
            result += substring * (multiplier if multiplier > 0 else 1)
            multiplier = 0
            i = next_i
        elif char == ']':
            return result, i
        else:
            result += char
        i += 1
    return result, i

if __name__ == '__main__':
    commands = input()
    decoded_str, _ = decode_instructions(commands)
print(decoded_str)

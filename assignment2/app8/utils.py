def encode_message(message, date):
    odd_encoding = {chr(i + 65): str(i + 1).zfill(2) for i in range(26)}
    even_encoding = {chr(i + 65): str(i + 501) for i in range(26)}

    is_odd_day = date.day % 2 != 0
    encoding = odd_encoding if is_odd_day else even_encoding

    encoded_message = []
    for char in message.upper():
        if char.isalpha():
            encoded_message.append(encoding[char])
        else:
            encoded_message.append(char)

    return ''.join(encoded_message)

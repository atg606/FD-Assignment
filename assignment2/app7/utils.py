def convert_to_words(n):
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Lakh", "Crore"]

    def num_to_words(num, index):
        if num == 0:
            return []
        if num < 10:
            return [units[num]]
        elif num < 20:
            return [teens[num - 11]]
        elif num < 100:
            return [tens[num // 10]] + num_to_words(num % 10, 0)
        elif num < 1000:
            return [units[num // 100]] + ["Hundred"] + (["and"] if num % 100 != 0 else []) + num_to_words(num % 100, 0)
        else:
            return num_to_words(num // 1000, index + 1) + [thousands[index]] + num_to_words(num % 1000, 0)

    words = num_to_words(n, 0)
    return " ".join(words).strip() + " Rupees Only"

def number_to_words(amount):
    integer_part = int(amount)
    decimal_part = int((amount - integer_part) * 100)

    words = convert_to_words(integer_part)
    if decimal_part > 0:
        words += " and " + convert_to_words(decimal_part) + " Paise"

    return words

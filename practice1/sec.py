import random
import string

def random_string(length=3):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def encode_word(word):
    """Encode a single word based on the given rules."""
    if len(word) < 3:
        return word[::-1]
    else:
        encoded_word = word[1:] + word[0]
        random_prefix = random_string()
        random_suffix = random_string()
        return random_prefix + encoded_word + random_suffix

def decode_word(word):
    """Decode a single word based on the given rules."""
    if len(word) < 3:
        return word[::-1]
    else:
        trimmed_word = word[3:-3]
        decoded_word = trimmed_word[-1] + trimmed_word[:-1]
        return decoded_word

def encode_message(message):
    """Encode a full message word by word."""
    words = message.split()
    encoded_words = [encode_word(word) for word in words]
    return ' '.join(encoded_words)

def decode_message(message):
    """Decode a full message word by word."""
    words = message.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

def main():
    action = input("Do you want to code or decode a message? (Enter 'code' or 'decode'): ").strip().lower()
    
    if action not in ['code', 'decode']:
        print("Invalid choice. Please enter 'code' or 'decode'.")
        return

    message = input("Enter the message: ")

    if action == 'code':
        result = encode_message(message)
    elif action == 'decode':
        result = decode_message(message)

    print("Result:", result)

if __name__ == "__main__":
    main()

zero_width_char_map = {"\u200B": "0", "\u200C": "1"}

with open("hidden_message.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
hidden_line = content[-1] 
binary_message = ''.join(zero_width_char_map[c] for c in hidden_line if c in zero_width_char_map)
decoded_message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

print("Hidden message:", decoded_message)

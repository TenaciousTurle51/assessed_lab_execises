def decrypt_cypher_text(encrypted_text, key):
    """
    Decrypts the given encrypted text using the provided key.

    Parameters:
    ----------
    encrypted_text : str
        The text to be decrypted.
    key : int
        A positive integer key used for decryption.
    
    Returns:
    -------
    str:
        The decrypted text as a single string.
    """
    decrypted_text = ""  # Initialize the decrypted text as an empty string
    
    for char in encrypted_text:
        # Step 1: Convert character to ASCII using ord()
        ascii_code = ord(char)
        
        # Step 2: Subtract the key
        new_ascii = (ascii_code - key) % 256  # Step 3: Modulo 256
        
        # Step 4: Convert back to character using chr()
        decrypted_text += chr(new_ascii)
    
    return decrypted_text


# Example usage
encrypted_text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$"
key = 3
decrypted_text = decrypt_cypher_text(encrypted_text, key)
print("Decrypted Text:", decrypted_text)

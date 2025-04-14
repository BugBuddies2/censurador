from bad_words_filter import filter_text

def main():
    """
    Main function to demonstrate the text filtering functionality.
    """
    # Example usage
    text = "This is a sample text with some bad words like bad, horrible, and terrible."
    bad_words = ["bad", "horrible", "terrible"]
    
    filtered_text = filter_text(text, bad_words)
    print("Original text:")
    print(text)
    print("\nFiltered text:")
    print(filtered_text)
    
    # Example with custom replacement
    custom_replacement = "[CENSORED]"
    filtered_text_custom = filter_text(text, bad_words, replacement=custom_replacement)
    print("\nFiltered text with custom replacement:")
    print(filtered_text_custom)

if __name__ == "__main__":
    main()
import re
from typing import List, Optional

def filter_text(text: str, bad_words: List[str], replacement: str = "***") -> str:
    """
    Filter out bad words from the input text and replace them with asterisks.
    
    Args:
        text: The input text to filter
        bad_words: List of bad words to filter out
        replacement: String to replace bad words with (default: '***')
    
    Returns:
        Filtered text with bad words replaced
    
    Raises:
        TypeError: If inputs are not of the expected types
    """
    # Check for invalid inputs
    if text is None:
        raise TypeError("Input text cannot be None")
    
    if bad_words is None:
        raise TypeError("Bad words list cannot be None")
    
    if not isinstance(text, str):
        raise TypeError("Input text must be a string")
    
    if not isinstance(bad_words, list):
        raise TypeError("Bad words must be provided as a list")
    
    # Check if every item in bad_words is a string
    if not all(isinstance(word, str) for word in bad_words):
        raise TypeError("All items in bad words list must be strings")
    
    # Early return for empty text or empty bad_words list
    if not text or not bad_words:
        return text
    
    # Create a pattern that matches whole words only
    # The pattern looks for word boundaries (\b) before and after the word
    pattern_parts = []
    for word in bad_words:
        # Escape any regex special characters in the word
        escaped_word = re.escape(word)
        pattern_parts.append(r'\b' + escaped_word + r'\b')
    
    # Join patterns with | (OR) operator
    pattern = '|'.join(pattern_parts)
    
    # Using re.IGNORECASE flag for case-insensitive matching
    # The lambda function returns the replacement string for each match
    filtered_text = re.sub(pattern, lambda _: replacement, text, flags=re.IGNORECASE)
    
    return filtered_text 
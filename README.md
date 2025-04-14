# Censurador

A text censoring application that filters out bad words from text.

## Description

This project implements a text filtering system that replaces specified "bad words" with asterisks or a custom replacement string. It's designed to be simple to use while handling various edge cases like case sensitivity, punctuation, and partial word matches.

## Features

- Filter out specified bad words from text
- Case-insensitive matching
- Custom replacement string support
- Handles punctuation and special characters
- Preserves spaces, newlines, and tabs
- Only replaces whole words, not parts of words
- Comprehensive error handling

## Usage

### Basic Usage

```python
from bad_words_filter import filter_text

text = "This text contains bad words"
bad_words = ["bad"]

filtered_text = filter_text(text, bad_words)
print(filtered_text)  # Output: "This text contains *** words"
```

### With Custom Replacement

```python
from bad_words_filter import filter_text

text = "This text contains bad words"
bad_words = ["bad"]
replacement = "[CENSORED]"

filtered_text = filter_text(text, bad_words, replacement=replacement)
print(filtered_text)  # Output: "This text contains [CENSORED] words"
```

## Running the Demo

To see the text filtering in action, run:

```
python main.py
```

## Running Tests

To run the test suite:

```
python -m unittest test.py -v
```

## License

See the LICENSE file for details.

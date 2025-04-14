import unittest
from unittest.mock import patch
import io
import sys

# This will test the bad_words_filter module that you'll implement
# Import statement will look like this when you create your implementation:
# from bad_words_filter import filter_text

class BadWordsFilterTests(unittest.TestCase):
    
    def test_basic_filtering(self):
        """Test that basic bad words are filtered correctly."""
        from bad_words_filter import filter_text
        
        text = "This text contains bad and very bad words"
        bad_words = ["bad"]
        
        result = filter_text(text, bad_words)
        expected = "This text contains *** and very *** words"
        
        self.assertEqual(result, expected)
    
    def test_case_insensitive(self):
        """Test that filtering works regardless of case."""
        from bad_words_filter import filter_text
        
        text = "Bad BAD bad bAd words should all be filtered"
        bad_words = ["bad"]
        
        result = filter_text(text, bad_words)
        expected = "*** *** *** *** words should all be filtered"
        
        self.assertEqual(result, expected)
    
    def test_multiple_bad_words(self):
        """Test filtering multiple different bad words."""
        from bad_words_filter import filter_text
        
        text = "This text has multiple bad words like horrible and terrible things"
        bad_words = ["bad", "horrible", "terrible"]
        
        result = filter_text(text, bad_words)
        expected = "This text has multiple *** words like *** and *** things"
        
        self.assertEqual(result, expected)
    
    def test_partial_word_match(self):
        """Test that only whole words are filtered, not parts of words."""
        from bad_words_filter import filter_text
        
        text = "The word 'abandon' contains 'bad' but shouldn't be filtered"
        bad_words = ["bad"]
        
        result = filter_text(text, bad_words)
        expected = "The word 'abandon' contains '***' but shouldn't be filtered"
        
        self.assertEqual(result, expected)
    
    def test_punctuation(self):
        """Test that words with punctuation are properly filtered."""
        from bad_words_filter import filter_text
        
        text = "Bad! bad, bad. bad? bad; bad:"
        bad_words = ["bad"]
        
        result = filter_text(text, bad_words)
        expected = "***! ***, ***. ***? ***; ***:"
        
        self.assertEqual(result, expected)
    
    def test_empty_text(self):
        """Test handling empty text input."""
        from bad_words_filter import filter_text
        
        text = ""
        bad_words = ["bad"]
        
        result = filter_text(text, bad_words)
        expected = ""
        
        self.assertEqual(result, expected)
    
    def test_empty_bad_words_list(self):
        """Test handling empty bad words list."""
        from bad_words_filter import filter_text
        
        text = "This text should remain unchanged"
        bad_words = []
        
        result = filter_text(text, bad_words)
        expected = "This text should remain unchanged"
        
        self.assertEqual(result, expected)
    
    def test_none_inputs(self):
        """Test handling None inputs."""
        from bad_words_filter import filter_text
        
        # None text
        with self.assertRaises(TypeError):
            filter_text(None, ["bad"])
        
        # None bad_words
        with self.assertRaises(TypeError):
            filter_text("Some text", None)
    
    def test_non_string_text(self):
        """Test handling non-string text input."""
        from bad_words_filter import filter_text
        
        with self.assertRaises(TypeError):
            filter_text(123, ["bad"])
    
    def test_non_list_bad_words(self):
        """Test handling non-list bad_words input."""
        from bad_words_filter import filter_text
        
        with self.assertRaises(TypeError):
            filter_text("Some text", "bad")
    
    def test_non_string_bad_words(self):
        """Test handling non-string items in bad_words list."""
        from bad_words_filter import filter_text
        
        with self.assertRaises(TypeError):
            filter_text("Some text", ["bad", 123, "words"])
    
    def test_custom_replacement(self):
        """Test using a custom replacement string instead of '***'."""
        from bad_words_filter import filter_text
        
        text = "This has bad words"
        bad_words = ["bad"]
        replacement = "[CENSORED]"
        
        result = filter_text(text, bad_words, replacement=replacement)
        expected = "This has [CENSORED] words"
        
        self.assertEqual(result, expected)
    
    def test_preserve_spaces(self):
        """Test that spaces are preserved in the filtered text."""
        from bad_words_filter import filter_text
        
        text = "   Multiple   spaces   between   bad   words   "
        bad_words = ["bad"]
        
        result = filter_text(text, bad_words)
        expected = "   Multiple   spaces   between   ***   words   "
        
        self.assertEqual(result, expected)
    
    def test_newlines_and_tabs(self):
        """Test handling of newlines and tabs."""
        from bad_words_filter import filter_text
        
        text = "Line with bad\nAnother line\tWith bad\twords"
        bad_words = ["bad"]
        
        result = filter_text(text, bad_words)
        expected = "Line with ***\nAnother line\tWith ***\twords"
        
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
from lib.diary_entry import DiaryEntry
import pytest

"""
Gien a title and contents
Format returns a formatted entry, like:
"My title: These are the contents
"""

def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "")
    assert str(err.value) == "Diary entries must have a title or content"

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"

    """
    Given a title and a contents
    count_words return the number of words in the title and contents
    
    """

    def test_counts_words_in_both_title_and_contents():
        diary_entry = DiaryEntry("My Title", "Some contents")
        result = diary_entry.count_words()
        assert result == 4

    """
    Given a wpm of 2
    and a text with 2 words
    reading_time returns 1 minute
    """
    def test_reading_time_with_two_wpm_and_two_words():
        diary_entry = DiaryEntry("My Title", "Some contents")
        result = diary_entry.reading_time()
        assert result == 1
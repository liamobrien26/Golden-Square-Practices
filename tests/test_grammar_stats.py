from lib.grammar_stats import GrammarStats

def test_if_check_True():
    gettingclass = GrammarStats()
    result = gettingclass.check("Text returns true")
    assert result == True

def test_if_check_False():
    gettingclass = GrammarStats()
    result = gettingclass.check("text returns true")
    assert result == False

def test_returns_method():
    grammar_stats = GrammarStats()
    assert grammar_stats.percentage_good() == 0

import pytest


PARENS_TABLE = [
    ('', 0),
    ('(', 1),
    (')', -1),
    ('((())))', -1),
    ('(((())))', 0),
    ('((((())))', 1),
    ('aaa', 0),
    ('(aa(a', 1),
    ('(aa(a)', 1),
    (')))(((', -1),
    (')(((', -1),
    ('(((?(a()))???)', 1),
    ('(((?(a()))???))', 0)
]


@pytest.mark.parametrize('parens, output', PARENS_TABLE)
def test_proper_parenthetics(parens, output):
    from proper_parens import proper_parenthetics
    assert proper_parenthetics(parens) == output


@pytest.mark.parametrize('parens, output', PARENS_TABLE)
def test_proper_parenthetics_2(parens, output):
    from proper_parens import proper_parenthetics_2
    assert proper_parenthetics_2(parens) == output

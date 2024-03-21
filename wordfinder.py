"""Word Finder: finds random words from a dictionary."""

from numpy.random import choice, seed
import re

class WordFinder:
    """Generates random words based on lines read from a source text file.

    Parameters
    ----------

    infile : str
        The path to the text file to be read

    Attributes
    ----------

    word_list : list
        List of words read from an input text file

    Methods
    -------
    random(rand_seed=None):
        Returns a random word from the text file. If `rand_seed` is supplied, will use a that seed
        to generate output.

    reload_words(infile=None):
        Reloads the word_list attribute with the option to supply a new source
        text file

    Examples
    --------

    >>> wf = WordFinder('words_list.txt')
    5 words read

    >>> wf.random(2)
    'dog'

    >>> wf.random(6)
    'mango'
    """

    def __init__(self, infile):
        self._infile = infile
        self.reload_words()

    @property
    def infile(self):
        return self._infile

    @property
    def word_list(self):
        return self._word_list

    def reload_words(self, infile=None):
        if infile:
            self._infile = infile
        self._word_list = self._get_words()
        num_words = len(self._word_list)
        print(f'{num_words} words read')

    def _get_words(self):
        with open(self._infile) as f:
            lines = f.readlines()
            return [i.strip() for i in lines]

    def random(self, rand_seed=None):
        if rand_seed:
            seed(rand_seed)
        return choice(self._word_list)


class SpecialWordFinder(WordFinder):
    """Extends WordFinder - input lines that are blank or begin with a `#` (ex. comments)
    are ignored."""

    def __init__(self, infile):
        WordFinder.__init__(self, infile)

    def _get_words(self):
        lines = WordFinder._get_words(self)
        return [i for i in lines if not bool(re.match("^#.*|^$", i))]

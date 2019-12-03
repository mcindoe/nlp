import spacy
import textacy

# Load "en_core_web_sm" NLP. To download, first pip install spacy, then 
# enter in a terminal "python -m spacy download en_core_web_sm"
nlp = spacy.load('en_core_web_sm')

example_str = "Corning announces investment in Versalume LLC"
example_str_2 = 'Startup companies create jobs and support innovation. Hilary supports entrepreneurship.'

# Note that this process is highly case-sensitive: the following string
# will work poorly; the NLP is unable to extract SVO triples
bad_str = 'Corning Announces Investment in Versalume LLC'

# Parse as an spacy.tokens.doc.Doc instance
example = nlp(example_str)
example_2 = nlp(example_str_2)
bad_example = nlp(bad_str)

extraction = textacy.extract.subject_verb_object_triples(example)
extraction_2 = textacy.extract.subject_verb_object_triples(example_2)
bad_extraction = textacy.extract.subject_verb_object_triples(bad_example)

# 'extraction' is a generator object, not a list. So either cast as a
# list or loop through to print them out
print('Example 1', list(extraction))
print('Example 2', list(extraction_2))
print('Bad Example', list(bad_extraction))
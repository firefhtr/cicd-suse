from __future__ import print_function
import random

buzz = ('Continuous Testing', 'Continuous Integration',
    'Continuous Deployment', 'Continuous Improvement', 'DevOps')
adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end')
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly',
    'seriously')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')
noun = ('SUSE')

def sample(l, n = 1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([noun, sample(verbs), sample(adjectives), buzz_terms[0], sample(adverbs), sample(verbs), buzz_terms[1]])
    return phrase

if __name__ == "__main__":
    print(generate_buzz())

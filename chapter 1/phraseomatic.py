import random

verbs = ['Leverage', 'Sync', 'Target'
                             'Gemify', 'Offline', 'Crowd-sourced',
         '24/7', 'Lead-in', '30,000 foot']

adjectives = ['A/B Tested', 'Freemium', 'Hyperlocal',
              'Siloed', 'B-to-B', 'Oriented', 'Cloud-based',
              'API-based']
nouns = ['Early Adopter', 'Low-hanging fruit',
         'Pipeline', 'Splash Page', 'Productivity',
         'Process', 'Tripping point', 'Paradigm']

# Choose one verb, one adjective anf noun from each list

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

phrase = verb + ' ' + adjective + ' ' + noun

print(phrase)

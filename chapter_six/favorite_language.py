    # """
    # This exercise demonstrates how to work with Python dictionaries, including accessing values using keys and the `get()` method.
    # It practices retrieving values directly and safely handling missing keys with default values.
    # """
favorite_languages = {
    'martin' : 'python',
    'fede' : 'ruby',
    'ivo' : 'sql',
}

martin_language = favorite_languages['martin']

print(f"Martin's favorite language is {martin_language}")

ivo_language = favorite_languages.get('ivo', "there's no language specified for ivo")
print(f"ivo's favorite language is {ivo_language}")

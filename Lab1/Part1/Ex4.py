D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
D['food'] # Fetch value of key 'food'
D['quantity'] += 1 # Add 1 to 'quantity' value
D
D = {}
D['name'] = 'Bob' # Create keys by assignment
D['job'] = 'dev'
D['age'] = 40
D
print(D['name'])
bob1 = dict(name='Bob', job='dev', age=40) # Keywords
bob1
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40])) # Zipping
bob2

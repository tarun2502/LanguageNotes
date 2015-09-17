beatles = [['John', 1943], ['Paul', 1942], ['George', 1943],['Rigo', 1940]]
print beatles
print beatles[0]
print beatles[0][1]

# Mutation in the list
p = ['H','E', 'L', 'L', 'O' ]
p[0] = 'Y'
print p
# Aliasing 
q = p # Now q also refers to p
q[-1] = "!" # Now p is also changed.
print q



# variales
message = 'hello python'
print(message)
message = 'hello'
print(message)

sentence = 'My name is Lili'
sentence.upper()
print(sentence.upper())

sentence.lower()
print(sentence.lower())

# formatting
name = 'lili'
country = 'singapore'
print(name.title())
print(country.title())

print(f'my name is {name},i come from {country},nice to meet you')

message = f'my name is {name},i come from {country},nice to meet you'
print(message)

# line break and tab character
print('hello\tworld')
print('hello\nworld')

# remove spaces
sentence = '   python    '
sentence = sentence.strip()
print(sentence)

# calculate
a,b = 3,4
c1 = a + b
c2 = a - b
c3 = a * b
c4 = a / b
print(c1,c2,c3,c4)

# identify the type of data
a = '45'
b = int(a)
print(type(b))


#用*表达式接受不定长度的值


a = (1,2,3,4,5,6,7)

first, *_, last = a
print(first)
print(last)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


for tag, *args in records:
    print(tag)
    print(args)
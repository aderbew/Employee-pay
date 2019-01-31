import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('name is:',sys.argv[1])
print('pay rate:',sys.argv[2])
print('hours:', sys.argv[3])
name = sys.argv[1]
payrate=int(sys.argv[2])
hours=int(sys.argv[3])


if hours <=40:
	pay=payrate*hours
else:
	pay=pay+(hours-40)*1.5*payrate
	
print(pay)







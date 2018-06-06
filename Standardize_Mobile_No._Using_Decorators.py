number = list()
N = int(input())
for i in range(N):
    number.append(str(input()))

def mobile(function):
    def input(number):
            return sorted([function(i) for i in number])
    return input

@mobile
def standardize(number):
	return "+91" + " " + number[-10:-5] + " " + number[-5:]

print ('\n'.join(standardize(number)))
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

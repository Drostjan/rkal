from rkal import *

if __name__ == '__main__':
	rkal = Calendar(28,12,1901)
    
	print(rkal)
	for i in range(7):
		rkal.update()

	print(rkal.getDate())
    

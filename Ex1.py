width=9
space=width//2
star=1
while (space>0):
	    print ((space * " ")+(star * "*")+(space * " "))
	    space -=1
	    star+=2
while (space<=4):
	    print ((space * " ")+(star * "*")+(space * " "))
	    space +=1
	    star-=2

from pickle import FALSE


def arithmetic(arv1:float,tehe:str,arv2:float)->any:
    """
    """
    if tehe=="+":
        vastus=arv1+arv2
    elif tehe=="-":
        vastus=arv1-arv2
    elif tehe=="*":
        vastus=arv1*arv2 
    elif tehe=="/":
        vastus=arv1-arv2 
        if arv2==0:
            vastus="DIVO"
        else:
            vastus=arv1/arv2 
    else:
        vastus="tundmatu tehe"



def is_year_leap(aasta: int)->bool:
    """
    """
    if aasta%4==0:
        t=True 
    else:
        t=FALSE 




def square(a):
	p = 4*a
	s = a*a
	d = (a**2) / 2
	d = d**0.5
	
	k = (p, s, d)
	
	return k
	
print(square(16))

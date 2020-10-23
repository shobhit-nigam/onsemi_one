# try except

varx = 10
vary = 5
varz = 0

try:
    vara = varx/varz
    print(vara)
except ZeroDivisionError:
    print("we went wrong with denominator")
    
print("application contiues")


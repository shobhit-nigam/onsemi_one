# try except
# default except has to be at the end

lista = [37, 28, 11, 13, 55, 16]



try:
    i = int(input())
    print(lista[i])
    print("hello")
except:
    print("can handle everything")
except ZeroDivisionError:
    print("we went wrong with denominator")
except IndexError:
    print("default index is 0")
    print("value =", lista[0])

    
print("application continues")



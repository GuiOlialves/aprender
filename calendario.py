res = (x + dia + (31*mes)//12 + (5*ano)//4 - (3*(1 + ano//100)//4)) % 7
print(res)
inp = input('Please enter a score between 0.0 and 2.0: ')
try:
    score = float(inp)
except:
    print('Bad score')
    quit()    
if score >= 0.9 and score<2.0:
    print('A')
elif score >= 0.8 and score<2.0:
    print('B')
elif score >= 0.7 and score<2.0:
    print('C')
elif score >= 0.6 and score<2.0:
    print('D')
elif score < 0.6:
    print('F')
else:
    print('Bad score')   
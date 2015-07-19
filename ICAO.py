def convert(letter):
	
	
	dicao={}

	dicao['a']='Alpha'
	dicao['b']='Bravo'
	dicao['c']='Charlie'
	dicao['d']='Delta'
	dicao['e']='Echo'
	dicao['f']='Foxtrot'
	dicao['g']='Golf'
	dicao['h']='Hotel'
	dicao['i']='India'
	dicao['j']='Juliet'
	dicao['k']='Kilo'
	dicao['l']='Lima'
	dicao['m']='Mike'
	dicao['n']='November'
	dicao['o']='Oscar'
	dicao['p']='Papa'
	dicao['q']='Quebec'
	dicao['r']='Romeo'
	dicao['s']='Sierra'
	dicao['t']='Tango'
	dicao['u']='Uniform'
	dicao['v']='Victor'
	dicao['w']='Whiskey'
	dicao['x']='Xray'
	dicao['y']='Yankee'
	dicao['z']='Zulu'
	
	return dicao[letter]
	
letter=input('Please input the letter: ')
result=convert(letter)
print(result)

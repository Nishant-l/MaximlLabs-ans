
Nc = 256
 
def maxDistChar(str, n): 

	count = [0] * Nc  
	for i in range(n): 
		count[ord(str[i])] += 1
	
	max_distinct = 0
	for i in range(Nc): 
		if (count[i] != 0): 
			max_distinct += 1	
	return max_distinct 

def smallSubDistinct(str): 

	n = len(str)	 
	max_distinct =maxDistChar(str, n) 
	minl = n	
	
	for i in range(n): 
		for j in range(n): 
			subs = str[i:j] 
			subs_lenght = len(subs) 
			sub_distinct_char = maxDistChar(subs, subs_lenght) 
			
			if (subs_lenght < minl and
				max_distinct == sub_distinct_char): 
				minl = subs_lenght 
	return minl 

	
str = input().strip()
l = smallSubDistinct(str); 
print(l)

# two pointer: 
# outer loop: target string t
# inner loop: source string s
# time complexity: O(n + m)

def canConvert(self, s, t):
	# Write your code here
	if len(t) > len(s):
		return False

	s_ptr = 0

	for t_ptr in range(len(t)):
		while s_ptr < len(s) and t[t_ptr] != s[s_ptr]:
			s_ptr += 1

		if s_ptr == len(s):
			return False

		s_ptr += 1
	return True

#72ms,13.8MB
class Solution:
	def intToRoman(self, num: int) -> str:
		ans = ''
		while num > 0:
			thou = num // 1000
			for i in range(thou):
				ans += 'M'
			num = num % 1000
			if num // 900 == 1:
				ans += 'CM'
				num -= 900
			elif num // 400 == 1 and num % 400 < 100:
				ans += 'CD'
				num -= 400
			else:
				fifH = num // 500
				if fifH == 1:
					ans += 'D'
					num %= 500
				hund = num // 100
				for i in range(hund):
					ans += 'C'
				num %= 100
			if num // 90 == 1:
				ans += 'XC'
				num -= 90
			elif num // 40 == 1 and num % 40 < 10:
				ans += 'XL'
				num -= 40
			else:
				fifT = num // 50
				if fifT == 1:
					ans += 'L'
				num %= 50
				ten = num // 10
				for i in range(ten):
					ans += 'X'
				num %= 10
			if num == 9:
				ans += 'IX'
				return ans
			elif num == 4:
				ans += 'IV'
				return ans
			else:
				fif = num >= 5
				if fif:
					ans += 'V'
					num -= 5
				for i in range(num):
					ans += 'I'
				return ans

#72ms,13.9MB
class Solution2:
	def intToRoman(self, num: int) -> str:
		nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
		ans = ''
		index = 0

		while index < 13:
			while num >= nums[index]:
				ans += roman[index]
				num -= nums[index]
			index += 1

		return ans

print(Solution2().intToRoman(int(input())))

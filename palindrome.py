class Solution:
    def palindrome_of_number(self, num):
        org_num = num
        num_reversed = 0
        while num:
            digit = num % 10
            num_reversed = num_reversed*10 + digit
            num //= 10
        if org_num == num_reversed:
            print('It is Palindrome: ', num_reversed)
        else:
            print('It is not a palindrome: ', num_reversed)
        return

x = int(input('Enter the number: '))
obj = Solution()
obj.palindrome_of_number(x)
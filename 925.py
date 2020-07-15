class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        for i in range(len(typed)):
            if j == len(name) - 1 and name[j] == typed[i]:
                return True
                # print('ok')
            if typed[i] == name[j]:
                j += 1
        # return False
        print('error')


if __name__ == '__main__':
    a = Solution()
    name = 'alex'
    typed = 'aalleeasxx'
    a.isLongPressedName(name, typed)





# def islongname(name, typed):
#     i,j = 0,0
#     for i in range(len(typed)):
#         if j == len(name) -1 and name[j] == typed[i]:
#             return True
#         if typed[j] == name[i]:
#             j += 1
#     return False
#























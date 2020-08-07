class Solution:
    # [1,3,2,6,5]
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if postorder == []:
            return True
        
        root = postorder[-1]
        del postorder[-1]

        index = None

        for i in range(len(postorder)):
            if index == None and postorder[i] > root:
                index = i
            if index != None and postorder[i] < root:
                return False
        if postorder[:index] == []:
             leftret = True
        else:
            leftret = self.verifyPostorder(postorder[:index])
        if postorder[index:] == []:
            rightret = True
        else:
            rightret = self.verifyPostorder(postorder[index:])
        return leftret and rightret
class Solution(object):
    def isValidList(self, input_list):
        #判断输入的九个数合法
        digit_set = set()
        for i in input_list:
            if i != ".":
                if i not in digit_set:
                    digit_set.add(i)
                else:
                    return False
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #判断每行
        for i in range(len(board)):
            if not self.isValidList(board[i]):
                return False
            col_list = []
			#每列
            for j in range(len(board)):
               col_list.append(board[j][i])
            if not self.isValidList(col_list):
                return False

        #9个box
        for i in range(len(board)/3):
            #行索引i*3:i*3+3
            #列索引j*3:j*3+3
            for j in range(len(board)/3):
                box = []
                for k in range(i*3,i*3+3):
                    box.extend(board[k][j*3:j*3+3])
                if not self.isValidList(box):
                    return False
        return True

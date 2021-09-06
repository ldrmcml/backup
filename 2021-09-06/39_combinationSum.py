class Solution(object):
    def backtrace(self, candidates, all_combination, cur_combination, target, index):
        #所有元素遍历完
        if index == len(candidates):
            return

        #当前组合符合条件
        if target == 0:
			#直接append，会被后面修改，需要深拷贝
            all_combination.append(copy.deepcopy(cur_combination))
            return

        #跳过当前数
        self.backtrace(candidates, all_combination, cur_combination, target, index + 1)

        #使用当前数
        if target - candidates[index] >= 0:
            #可以重复使用当前数，故这里索引为index
            cur_combination.append(candidates[index])
            self.backtrace(candidates, all_combination, cur_combination, target - candidates[index], index)
            cur_combination.pop()


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        all_combination = []
        cur_combination = []
        self.backtrace(candidates, all_combination, cur_combination, target, 0)
        return all_combination

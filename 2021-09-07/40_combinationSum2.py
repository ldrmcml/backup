class Solution(object):
    def backtrace(self, candidates, target, index, all_combination, cur_combination):
        if target == 0:
            all_combination.append(copy.deepcopy(cur_combination))
            return

        if index == len(candidates):
            return    
        
        i = index
        while i < len(candidates):
            if target - candidates[i] >= 0:
				#相同的数不需要重复遍历
                if i > index and candidates[i] == candidates[i-1]:
                    i = i + 1
                else:
                    cur_combination.append(candidates[i])
                    self.backtrace(candidates, target-candidates[i], i+1, all_combination, cur_combination)
                    cur_combination.pop()
                    i = i + 1
            else:
                break
            
        

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        all_combination= []
        cur_combination = []
        self.backtrace(candidates, target, 0, all_combination, cur_combination)
        return all_combination

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// 1. 广度优先，队列，层次遍历，最后一层第一个节点
func findBottomLeftValue(root *TreeNode) int {
	// 二叉树的节点个数的范围是 [1,104]，无需判空root

	var q []*TreeNode

	// q just store one level of tree
	q = append(q, root)

	for len(q) > 0 {
		// current level of tree
		var curLevel []*TreeNode
		for _, n := range q {
			if n.Left != nil {
				curLevel = append(curLevel, n.Left)
			}
			if n.Right != nil {
				curLevel = append(curLevel, n.Right)
			}
		}

		if len(curLevel) == 0 {
			return q[0].Val
		}

		q = curLevel
	}

	return -1
}
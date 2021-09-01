/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// 1. 中序遍历的逆序：右中左
// 2. 数组存储遍历结果：cur += pre
func convertBST(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	// will modify root's Val
	sum := 0
	reverseInorder(root, &sum)
	return root
}
func reverseInorder(root *TreeNode, sum *int) {
	if root == nil {
		return
	}
	if root.Right != nil {
		reverseInorder(root.Right, sum)
	}
	*sum += root.Val
	root.Val = *sum
	if root.Left != nil {
		reverseInorder(root.Left, sum)
	}
}
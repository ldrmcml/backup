/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */
// 1. 根节点特点：遍历根节点及其所有子节点，那么根节点只出现一次，而子子节点将出现两次：一次作为父节点，一次作为子节点；而根节点只会作为父节点出现。
// 2. 利用异或特性：两个相等的数字异或为0，那么按照上述顺序遍历异或一遍，最终结果为根节点值；
// space: O(1), time: O(3n-1)~=O(n)
func findRoot(tree []*Node) *Node {
	if tree == nil {
		return nil
	}

	a := 0

	for _, node := range tree {
		a ^= node.Val
		for _, child := range node.Children {
			a ^= child.Val
		}
	}

	for _, node := range tree {
		if node.Val == a {
			return node
		}
	}

	return nil
}
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Random *Node
 * }
 */
// 记忆化dfs
// 1. dfs，并且用map保存，如果已经创建则复用，否则新建。因为random可能指向任意已经创建的节点。
func copyRandomBinaryTree(root *Node) *NodeCopy {
	// if root == nil {
	//     return root
	// }

	m := make(map[*Node]*NodeCopy)

	return dfs(m, root)
}

func dfs(m map[*Node]*NodeCopy, root *Node) *NodeCopy {
	if root == nil {
		return nil
	}

	if _, exists := m[root]; exists {
		return m[root]
	}

	newNode := new(NodeCopy)
	newNode.Val = root.Val
	m[root] = newNode

	newNode.Left = dfs(m, root.Left)
	newNode.Right = dfs(m, root.Right)
	newNode.Random = dfs(m, root.Random)

	return newNode
}
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */
// 1. 借助map: key是子节点, value是出现次数。如果从未出现在某节点的子节点那么肯定就是根节点。
// space:O(n), time:O(3n-1)~=O(n)
func findRoot(tree []*Node) *Node {
	m := make(map[*Node]int)

	for _, node := range tree {
		if _, exists := m[node]; !exists {
			// 这个时候node插入map，那么m将已经包含node
			m[node] = 0
		}
		for _, child := range node.Children {
			m[child]++
		}
	}

	for node, times := range m {
		if times == 0 {
			return node
		}
	}

	return nil
}
/**
 * Definition for Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Parent *Node
 * }
 */
// 1. 遍历p父节点，保存到map；再遍历q父节点并查询map；
func lowestCommonAncestor(p *Node, q *Node) *Node {
	m := make(map[*Node]int)

	for p != nil {
		m[p] = 0
		p = p.Parent
	}

	for q != nil {
		if _, exists := m[q]; exists {
			return q
		}
		q = q.Parent
	}

	return nil
}
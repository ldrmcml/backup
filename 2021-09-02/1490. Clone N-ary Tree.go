/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */
// 1. 双队列：一个队列存原N叉树，另一个队列存目的N叉树；
// 2. 同时对源N叉树和目的N叉树广度优先遍历；
func cloneTree(root *Node) *Node {
	if root == nil {
		return root
	}

	var qs, qd []*Node
	qs = append(qs, root)

	rootD := &Node{Val: root.Val}
	qd = append(qd, rootD)

	for len(qs) > 0 {
		ns := qs[0]
		qs = qs[1:]

		nd := qd[0]
		qd = qd[1:]

		deepClone(ns, nd)
		if ns.Children != nil {
			qs = append(qs, ns.Children...)
			qd = append(qd, nd.Children...)
		}
	}

	return rootD
}

func deepClone(ns, nd *Node) {
	nd.Val = ns.Val

	if ns.Children == nil {
		return
	}

	var destC []*Node
	for _, nc := range ns.Children {
		destC = append(destC, &Node{
			Val: nc.Val,
		})
	}
	nd.Children = destC
}
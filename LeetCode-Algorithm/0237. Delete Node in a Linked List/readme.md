只给了当前节点的引用，没前一个节点，不能用node.next=node.next.next的方法，只能把后节点的数值复制到前一个节点

这题直接在leetcode网页上敲的，CE了一次，没处理好最后的节点wa了一次，随后ac
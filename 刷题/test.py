class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def PrintFromTopToBottom(root):
    # write code here
    outList=[]
    queue=[root]
    while queue!=[] and root:
        outList.append(queue[0].val)
        if queue[0].left!=None:
            queue.append(queue[0].left)
        if queue[0].right!=None:
            queue.append(queue[0].right)
        queue.pop(0)
    return outList

def GetNext(pNode):
    if pNode.right != None:
        nextNode = pNode.right.left
        while nextNode.left:
            nextNode = nextNode.left
        return nextNode.val
    elif pNode == pNode.next.left:
        return pNode.next.val
    else:
        nextNode = pNode.next
        if nextNode == nextNode.next.right:
            nextNode = nextNode.next
        else:
            return nextNode.next.val

def reConstructBinaryTree(pre, tin):
    if len(pre) == 0 or len(tin) == 0:
        return None
    root = TreeNode(pre[0])
    for i in range(len(tin)):
        if tin[i] == root.val:
            break
    root.left = reConstructBinaryTree(pre[1:1+i],tin[0:i])
    root.right = reConstructBinaryTree(pre[1+i:],tin[i+1:])
    return root
if __name__ == '__main__':
    result = reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
    # preOrderTraverse(result)
    print(PrintFromTopToBottom(result))
    print(GetNext(result))
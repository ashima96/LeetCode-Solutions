/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int max_len = 0;
    
    public int diameterOfBinaryTree(TreeNode root) {
        calculateDiameter(root);
        return max_len;
    }
    
    public int calculateDiameter(TreeNode root){
        if (root == null){
            return 0;
        }
        
        int leftTree = calculateDiameter(root.left);
        int rightTree = calculateDiameter(root.right);
        
        max_len = Math.max(max_len, leftTree+rightTree);
        
        return Math.max(leftTree, rightTree) + 1;
    }
}
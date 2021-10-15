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
    int sum = 0;
    
    public int rangeSumBST(TreeNode root, int low, int high) {
        traverse(root, low, high);
        return sum;
    }
    
    public void traverse(TreeNode root, int low, int high){
        if (root != null){
            int value = root.val;
            if(value >= low && value <= high){
                sum += value;
            }
            
            if(value > low){
                traverse(root.left, low, high);
            }
             if(value < high){
                traverse(root.right, low, high);
            }
        }
    }
}
public class Solution {
    public int solution(int[] num_list) {
        int odd=0;
        int even=0;
        for(int n:num_list){
            if (n%2==1)
                odd= odd*10+n;
            else
                even= even*10+n;
        }
        return odd+even;
    }

}

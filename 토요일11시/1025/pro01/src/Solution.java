public class Solution /*extends Object*/{
    //public Solution(){}
    //len(리스트)
    //인스턴스 메서드
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        for(int i=0; i < included.length; i++,a+=d)if(included[i])answer+=a;
        return answer;
    }

}

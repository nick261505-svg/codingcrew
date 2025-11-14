import java.util.HashSet;

public class App {
    public static void main(String[] args) throws Exception {
        //App app=new App();
        App.Solution obj=new App().new Solution();

        int result=obj.solution(2, 6, 1);
        System.out.println(result);
    }

    //멤버를 포함하는 클래스의 객체생서후 접근
    //non-static 멤버로 취급
    //멤버 클래스(inner class)
    class Solution {
        public int solution(int a, int b, int c) {
            int r1=a+b+c;
            int r2=r1*(a*a+b*b+c*c);
            int r3=r2*(a*a*a+b*b*b+c*c*c);
            //중복을 제거해줘
            HashSet<Integer> set=new HashSet<>();
            set.add(a);set.add(b);set.add(c);
            if (set.size()==3)
                return r1;
            else if (set.size()==2)
                return r2;
            return r3;
        }

        /*
        public int solution(int a, int b, int c) {
            
            int r1=a+b+c;
            int r2=r1*(a*a+b*b+c*c);
            int r3=r2*(a*a*a+b*b*b+c*c*c);
            if(a==b && b==c){
                return r3;
            }else if(a!=b && b!=c && a!=c){
                return r1;
            }
            return r2;
        }
             */

    }
}


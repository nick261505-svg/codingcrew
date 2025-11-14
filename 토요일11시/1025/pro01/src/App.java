public class App /*extends Object*/{
    public static void main(String[] args) throws Exception {
        //1. 클래스를 이용해서 객체생성(인스턴스화)
        //Solution obj: stack 메모리에 변수생성
        //new: heap 메모리공간의 새로운객체를 생성
        //Solution(): 기본적으로 필드초기화를 담당한다.
        Solution obj=new Solution();
        //2. 객체변수.메서드() , 객체변수.필드
        int a=3;
        int d=4;
        boolean[] included={true, false, false, true, true};
        int result=obj.solution(a,d,included);
        System.out.println(result);
    }
}

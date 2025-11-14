public class Test01 {
    //멤버필드
    //인스턴스 필드
    int a;
    double b;
    String c;
    boolean d;
    //static 필드
    static int aa=300;
    static final double PI;
    

    //멤버 메서드(
    //인스턴스 메서드
    void disp(){}
    //static 메서드
    static void aaa(){}
    //멤버 생성자
    public Test01(){
        a=10;
        System.out.println("인스턴스필드 초기화");
    }
    //static 초기화블럭
    static{
       aa=100; 
       PI=3.14;
       System.out.println("static 필드 초기화됨");
    }
}

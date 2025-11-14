public class MainTest {

    public static void main(String[] args) {
        //Test클래스의  a를 출력하고 싶어
        //객체를 만든다
        Test01 obj=new Test01();
        System.out.println(obj.a);
        //System.out.println(obj.aa);

        Test01 obj2=new Test01();
        obj2.disp();
        System.out.println(Test01.PI);
      
    }

}

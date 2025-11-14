public class Solution {
    //non-static:인스턴스 멤버
    public int solution(int[] num_list) {
        int odd = 0;//351
        int even=0;//42
        //내장된 자동추출장치로 순서대로 뽑아줘  (구성요소를 저장하는 변수:집합)
        //한개씩 뽑아줘 데이터가 없을때까지
        for(int num :num_list){
            //홀수인지 짝수인지
            if(num%2==1){
                odd=odd*10+num;
            }else{
                even=even*10+num;
            }            
        }
        return odd+even;
    }

}

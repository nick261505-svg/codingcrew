import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class App {
    public static void main(String[] args) throws Exception {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        int[] scarecrows=new int[N+1];//0번 인덱스 사용하지 않으려고

        st = new StringTokenizer(br.readLine());
        for(int i=1; i<=N; i++){
            scarecrows[i]=Integer.parseInt(st.nextToken());
        }

        //System.out.println(Arrays.toString(scarecrows));

        //각 허수아비 위치 마다 화살을 막을수 있는지
        //막을수 없으면 -1
        //막을수 있다면 최소의 허수아비 개수
        //각 위치에 대한 답을 저장 배열
        int[] answer= new int[N+1];

        //각 허수아비 위치에 대해 계산
        for(int i=1; i<=N; i++){
            answer[i]=solve(N, P, scarecrows, i);
        }

        //출력 
        StringBuilder sb=new StringBuilder();
        for(int i=1; i<=N; i++){
            sb.append(answer[i]);
            sb.append(" ");
        }
        System.out.println(sb.toString());

    }

    //허수아비 위치에서 화살을 멈추게하는 최소 허수아비 개수를 리턴
    private static int solve(int N, int P, int[] scarecrows, int target) {
        
        //dp적용: 기록 
        Map<Integer, Integer> current=new HashMap<>();
        Map<Integer, Integer> next=new HashMap<>();

        //초기상태 : 위치 0에서 화살의 힘P, 허수아비 0개 사용
        current.put(P, 0);

        for(int i=1; i <= target; i++){
            //현재 위치
            for(int power :current.keySet()){
                int count=current.get(power);

                //화살이 power <= 0 화살이 멈춘상태
                if(power <=0){
                    continue;
                }
                //현재위치에 허수아비를 설치하지 않는 경우
                updateMinCount(next,power,count);

                //현재위치에 허수아비를 설치 
                if(power > scarecrows[i]){
                    int newPower=power-scarecrows[i];
                    updateMinCount(next, newPower, count+1);
                }else{
                    //화살이 허수아비를 통과하지 못하는 경우
                    updateMinCount(next, 0, count+1);
                }
                
            }
            //다음 단계를 위해 swap
            Map<Integer, Integer> temp=current;
            current=next;
            next= temp;
        }

        Integer result=current.get(0);

        return result!=null ? result: -1;
    }

    private static void updateMinCount(Map<Integer,Integer> next, int power, int count) {
        if(!next.containsKey(power)||next.get(power)>count){
            next.put(power, count);
        }
    }
}

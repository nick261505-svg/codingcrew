public class App {
    public static void main(String[] args) {
        Player player1=new Player("코딩");
        Player player2=new Player("조재청");

        for(int i=0; i<10;i++){
            player1.attackPlayer(player2);
        }
    }

}

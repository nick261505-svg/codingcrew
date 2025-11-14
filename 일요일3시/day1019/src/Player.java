public class Player extends MineCraftEntity{
    private String[] inventory;
    private int experience;
    private int reduct;
    private int attackDamage;
    
    public Player(String name){
        super(name,100);
        reduct=10;
        attackDamage=20;
    }
    //MineCraftEntity() is undefined for default constructor
    
    //상속관계에서 메서드는 오버라이드(재정의)
    public void takeDamage(int damage){
        //방어구 계산
        int reduceDamage=calculaterArmorRuduction(damage);

       super.takeDamage(reduceDamage);
    }

    private int calculaterArmorRuduction(int damage) {
        return damage-reduct;
    }

    public void attackPlayer(Player player) {
        player.takeDamage(attackDamage);
        System.out.println(player.getName() +"attacked!");
    }
}

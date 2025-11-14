public class MineCraftEntity {

    //필드(속성)
    private String name;
    private int health;
    private double x,y,z;

    //생성자가 코드로 존재하지 않은 경우만 생략된걸로 간주한다.
    //MineCraftEntity(){}
    //필드초기화담당
    public MineCraftEntity(String name, int health){
        this.name=name;
        this.health=health;
        this.x=0;//0.0
        this.y=64;//64.0
        this.z=0;//0.0
    }

    public void move(double x, double y, double z){
        this.x +=x;
        this.y +=y;
        this.z +=z;
    }
    public void die(){
        System.out.println(name+" has died!");
    }

    public void takeDamage(int damage){
        health -= damage;
        if(health<=0){
            die();
        }
    }

    public int getHealth(){
        return health;
    }
    public void setHealth(int health){
        this.health=health;
    }
    public String getName() {
        return name;
    }
    
}

public class Bracket {
	int type; //0:( 1: [ 2: {
	int index;
	
    public Bracket(int type, int index) {
        this.type = type;
        this.index = index;
    }
}

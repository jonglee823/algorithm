package STUDY;

public class findString {

	public static void main(String[] args) {
		String a = "pPoooY";
        a = a.toLowerCase();
        int p = 0;
        int y = 0;
        for(int i=0; i<a.length(); i++){
            char spell = a.charAt(i);
            if(spell == 'p'){
                p++;
                continue;
            }
            
            if(spell == 'y'){   
                y++;
                continue;
            }
        }
        
        if(p == y){
            System.out.print("true");
        }else{
        	System.out.print("false");
        }
	}

}

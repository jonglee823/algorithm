package STUDY;
class gcd {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        gcd gcd = new gcd();
        
        if(n > m) {
            int tmp = n;
            n = m;
            m = tmp;
        }
        
        answer[0] = gcd.eucd(n, m);
        answer[1] = (n*m)/answer[0];
        return answer;
    }
    
    public int eucd(int bn, int sn) {
        int r = bn % sn;

        if( r==0) {
            return sn;
        }else {
            return eucd(sn, r);
        }
    }
}
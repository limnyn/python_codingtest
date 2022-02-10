
public class firstProgram {
    
    int findmax(int [] data, int begin, int end){
        if(begin == end)
            return  data[begin];
        else
            return Math.max(data[begin, findMax(data,begin+1, end)]);
    }

    }
    public static void main(String[] args) {
     System.out.println("Welcome to java");
     
 }   
}

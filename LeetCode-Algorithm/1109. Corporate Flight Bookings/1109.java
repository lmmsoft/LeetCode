class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] res =new int[n];
        for(int i =0;i<n;++i){
            res[i]=0;
        }

        for(int a=0;a<bookings.length;++a){
            int i=bookings[a][0];
            int j=bookings[a][1];
            int k=bookings[a][2];
            for(int b=i;b<j+1;++b){
                res[b-1]+=k;
            }
        }
        return res;
    }
}
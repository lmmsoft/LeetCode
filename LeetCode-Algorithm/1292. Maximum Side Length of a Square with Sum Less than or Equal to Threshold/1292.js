/**
 * @param {number[][]} mat
 * @param {number} threshold
 * @return {number}
 */
var maxSideLength = function(mat, threshold) {
    let pre=[];
    let x = mat.length;
    let y =mat[0].length;
    let sz = Math.min(x,y);

    for(let i=0;i<x;++i){
        let s=0;
        let r =[];
        for(let j=0;j<y;++j){
            s +=mat[i][j];
            r.push(s);
        }
        pre.push(r)
    }

    var get_row = function(a,b,l){
        let s = pre[a][b+l-1];
        if(b===0){
            return s;
        }
        return s - pre[a][b-1];
    }

    var get_sum = function(a,b,l){
        let s=0;
        for(let r=0;r<l;++r){
            s += get_row(a+r,b,l);
        }
        return s;
    }

    while(sz>0){
        for(var b=0;b<=y-sz;++b){
            let s = -1;
            for(var a=0;a<=x-sz;++a){
                if(s===-1){
                    s = get_sum(a,b,sz);
                }else{
                    s = s + get_row(a + sz - 1, b, sz) - get_row(a - 1, b, sz)
                }

                if(s<=threshold){
                    return sz;
                }
            }
        }
        sz--;
    }
    return 0;

};


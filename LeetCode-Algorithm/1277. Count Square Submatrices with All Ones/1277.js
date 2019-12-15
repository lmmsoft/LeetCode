/**
 * @param {number[][]} matrix
 * @return {number}
 */
var countSquares = function(matrix) {
    const la = matrix.length;
    const lb = matrix[0].length;
    const l = Math.min(la,lb);
    let c =0;
    //let t=0;
    for(let size=1;size<=l;size++){
        //let st=0;
        for(let a=0;a<=la-size;a++){
            for(let b=0;b<=lb-size;++b){
                t=check(size,a,b,matrix);
                c+=t;
                //st+=t;
            }
        }
        //console.log(st)
    }
    return c;
};

function check(size,a,b,matrix){
    for(let i=0;i<size;++i){
        for(let j=0;j<size;++j){
            if(matrix[a+i][b+j]===0){
                return 0;
            }
        }
    }
    return 1;
}
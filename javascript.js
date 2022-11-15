// 6


let arr = [3, 6, 7, 8, 5, 10];       
var a=[3, 6, 7, 5, 10,8]; 
var S = 12
for (i in a){
    for(j in a){
        if ((a[i]+a[j]==S)&&(a[i]!=a[j])){
            console.log(a[i],a[j])
            a.splice(i,1)

        }

    }
}










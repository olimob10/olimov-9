
function run(){
    let arr = [];
    for(let i=0;i<20;i++){
        arr.push(Math.floor(Math.random()*100));
    }
    document.getElementById("out").innerText =
        "Generated: " + arr.join(", ");
}

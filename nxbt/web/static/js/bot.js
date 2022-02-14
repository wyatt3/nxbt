const macro = `
HOME 0.1s
1s
X 0.1s
0.4s
A 0.1s
1.3s
A 0.1s
0.3s
A 0.1s
24.6s
A 0.1s
0.3s
A 0.1s
0.3s
A 0.1s
0.3s
A 0.1s
2.6s
A 0.1s
0.3s
A 0.1s
13s
A 0.1s
0.3s
A 0.1s
0.3s
A 0.1s
1.0s
A 0.1s
0.3s
A 0.1s
0.1s
` //Put your macro here
async function runMacro() {
    createProController();
    console.log("here");
    setTimeout(() => {
        sendMacro(macro);
        console.log("now here");
        var newEl = document.createElement("div");
        newEl.id = "MacroDone";
        var el = document.getElementById('controller-config');
        el.appendChild(newEl);
    }, 8000);

}

console.log('here first');
runMacro();
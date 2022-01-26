const macro = `
HOME 0.1s
1.5s
HOME 0.1s
0.1s
` //Put your macro here
createProController();
setTimeout(() => {sendMacro(macro)}, 6500);
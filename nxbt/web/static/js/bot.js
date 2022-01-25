const macro = `` //Put your macro here

document.addEventListener("DOMContentLoaded", function(e) {
    restartController();
    setTimeout(sendMacro(macro), 5000);
});
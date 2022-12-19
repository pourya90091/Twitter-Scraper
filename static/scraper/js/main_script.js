const inputs = document.querySelector("div.inputs");
inputs.firstElementChild.focus();

if (inputs) {
    inputs.addEventListener("keydown", function (key_data) {
        let focus = document.getSelection();
        let allInputs = inputs.querySelectorAll(".input:not([type='file'])");
        let index = Math.floor(focus.focusOffset / 2);
        
        if (key_data.key === "Enter") {
            if (focus.focusNode === inputs) {
                if (index + 1 < allInputs.length) {
                    allInputs[index + 1].focus();
                }
                else {
                    document.querySelector("button.btn").click();
                }
            }
        }
        else if (key_data.key === "ArrowDown") {
            try {allInputs[index + 1].focus();} catch {}
        }
        else if (key_data.key === "ArrowUp") {
            try {allInputs[index - 1].focus();} catch {}
        }
    });
}

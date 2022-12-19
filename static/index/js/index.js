function login_request(plain) {
    let url = `${base_url}/login`;

    const r1 = document.getElementById("me").value;
    const r2 = document.getElementById("you").value;
    const r3 = document.getElementById("they").value;

    $.ajax({
        url: url,
        method: "POST",
        data: {
            r1: r1,
            r2: r2,
            r3: r3,
            plain: plain
        },
        success: function (data, status, xhr) {
            set_cookie("access_token", data.code);
            window.location.href = data.url;
        },
        error: function (jqXhr, textStatus, errorMessage) {
            const error = document.getElementById("error");
            alert(jqXhr.responseJSON.error);
            error.innerHTML = jqXhr.responseJSON.error;
        }
    }).then(n => {btn.disabled = false}).catch(n => {btn.disabled = false});
}

function sendEmail(email) {
    let url = `${base_url}/email`;

    $.ajax({
        url: url,
        method: "POST",
        data: {
            email: email
        },
        success: function (data, status, xhr) {
            alert(data.resp);
            document.querySelector(".input[placeholder='Email']").value = "";
        },
        error: function (jqXhr, textStatus, errorMessage) {
            const error = document.getElementById("error");
            alert(jqXhr.responseJSON.error);
            error.innerHTML = jqXhr.responseJSON.error;
        }
    }).then(n => {btn.disabled = false}).catch(n => {btn.disabled = false});
}

function go() {
    btn.disabled = true;

    const email = document.querySelector(".input[placeholder='Email']").value;
    const plain = document.querySelector(".input[placeholder='Secret']").value;

    if (email) {
        sendEmail(email);
    }
    else if (plain) {
        login_request(plain);
    }
}

const btn = document.querySelector(".btn[type='submit']");
btn.onclick = go;

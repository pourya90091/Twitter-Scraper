const Chref = window.location.href;

if (window.location.port) {
    var url = `${window.location.protocol}//${window.location.hostname}:${window.location.port}`;
}
else {
    var url = `${window.location.protocol}//${window.location.hostname}`;
}
const base_url = url;

function set_cookie(name, content) {
    document.cookie = `${name}=${content};expires=;path=/`;
}
function get_cookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return null;
}
function delete_cookie(name) {
    var date = new Date();
    var expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=;${expires};path=/`;
}

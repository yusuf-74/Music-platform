const btn = document.getElementById("login-btn");
const UserName = document.getElementById("user-name");
const pass1 = document.getElementById("password");
const statuz = document.getElementById("status");

btn.addEventListener("click", () => {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const next = urlParams.get("next");
  fetch("http://127.0.0.1:8000/auth/login/", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      userName: UserName.value,
      password: pass1.value,
    }),
  })
    .then((response) => response.json())
    .then((response) => {
      console.log(next)
if (response.status === "OK") {
  if (next)
  window.location.href = "http://127.0.0.1:8000/" + next;
  else 
  {

      statuz.innerHTML = "loged in successfully";
  statuz.style = "color : green;";
  }

} else {
  const key = Object.keys(response.status)[0];
  statuz.innerHTML = response.status[key][0];
  statuz.style = "color : red;";
}
        }
      
    );
});

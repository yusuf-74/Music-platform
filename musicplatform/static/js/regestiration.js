const btn = document.getElementById("register-btn");
const fname = document.getElementById("f-name");
const lname = document.getElementById("l-name");
const UserName = document.getElementById("user-name");
const pass1 = document.getElementById("pass-1");
const pass2 = document.getElementById("pass-2");
const statuz = document.getElementById("status");

btn.addEventListener("click", () => {

    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const next = urlParams.get("next");
  fetch("http://127.0.0.1:8000/auth/register/", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      firstName: fname.value,
      lastName: lname.value,
      userName: UserName.value,
      pass1: pass1.value,
      pass2:pass2.value,
      next:next,
    }),
  })
    .then((response) => response.json())
    .then((response) => {
      if (response.status === "OK") {
        statuz.innerHTML = "created successfully";
        statuz.style = "color : green;";
      } else if (response.status === 'password') {
        statuz.innerHTML = 'passwords are not identical'
        statuz.style = "color : red;";
      }
      else if (response.status === 'exist')
      {
        statuz.innerHTML = "user already exist";
        statuz.style = "color : red;";
      }
      else {
        statuz.innerHTML = "some data are incorrect";
        statuz.style = "color : red;";
      }
    });
});

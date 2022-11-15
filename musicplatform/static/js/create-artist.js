const btn = document.getElementById("create-btn");
const stageName = document.getElementById("stage-name");
const socialLink = document.getElementById("social-link");
const status = document.getElementById("status");
console.log(btn);
btn.addEventListener("click", () => {
  fetch("http://127.0.0.1:8000/artists/create/", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      stageName: stageName.value,
      socialLink: socialLink.value,
    }),
  })
    .then((response) => response.json())
    .then((response) => {
      if (response.status === "OK") {
        status.innerHTML = "created successfully";
        status.style = "color : green;";
      } else if (response.status === "validation error") {
        status.innerHTML = "validation error";
        status.style = "color : red;";
      } else {
        status.innerHTML = "something went wrong";
        status.style = "color : red;";
      }
    });
});

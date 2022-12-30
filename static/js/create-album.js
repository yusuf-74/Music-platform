const btn = document.getElementById("create-btn");
const name = document.getElementById("name");
const cost = document.getElementById("cost");
const artist = document.getElementById("artist");
const releasing = document.getElementById("releasing");
const status = document.getElementById("status");

btn.addEventListener("click", () => {
  console.log("hola");

  fetch("http://127.0.0.1:8000/albums/create/", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: name.value,
      cost: cost.value,
      releaseDateTime: releasing.value,
      stageName: artist.value,
    }),
  })
    .then((response) => response.json())
    .then((response) => {
      if (response.status === "OK") {
        status.innerHTML = "created successfully";
        status.style = "color : green;";
      } else {
        const key = Object.keys(response.status)[0];
        status.innerHTML = "error -> " + key + " : " + response.status[key][0];
        status.style = "color : red;";
      }
    });
});

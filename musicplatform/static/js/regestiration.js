const btn = document.getElementById('create-btn')
const stageName = document.getElementById("stage-name");
const socialLink = document.getElementById("social-link");
console.log(btn)
btn.addEventListener('onClick' , ()=> {

    console.log(stageName.value , 'hola');

    // fetch("http://127.0.0.1:8000/artists/create/", {
    //   method: "POST",
    //   headers: {
    //     Accept: "application/json",
    //     "Content-Type": "application/json",
    //   },
    //   body: JSON.stringify({'stageName':stageName.value , 'socialLink': socialLink.value }),
    // })
    //   .then((response) => response.json())
    //   .then((response) => console.log(JSON.stringify(response)));
})
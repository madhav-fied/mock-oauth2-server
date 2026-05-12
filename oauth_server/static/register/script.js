const submit = document.getElementById("register-btn")
const clientIdInput = document.getElementById("client_name")
const redirectURIInput = document.getElementById("redirect_uri")

submit.addEventListener('click', (event) => {
    event.preventDefault()
    console.log("Button clicked")
    fetch("http://localhost:8000/register/", {
        method: "POST",
        body: JSON.stringify({
            client_id: clientIdInput.value,
            redirect_url: redirectURIInput.value,
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
})

/*
[ X ] Send a post request
Accept it from the backend
Write in the DB
*/

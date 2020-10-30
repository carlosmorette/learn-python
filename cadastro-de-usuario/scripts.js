const newFetch = (url, body, method) => new Promise(async (resolve, reject) => {
    try {
        const request = await fetch(url, {
            body,
            method
        })

        const response = await request.json()
        setTimeout(() => {
            resolve(response)
        }, 3000);

    } catch (error) {
        reject(error)
    }
})
const url = "http://localhost:8888/"

const bodyRequest = {
    name: document.querySelector("input[name=name]").value,
    email: document.querySelector("input[name=email]").value,
    password: document.querySelector("input[name=password]").value
}

function requestApi() {
    document.querySelectorAll("h2")[1].innerText = "Carregando..."
    const request = newFetch(url, JSON.stringify(bodyRequest), "POST")
        .then(response => {
            console.log(response)
            document.querySelectorAll("h2")[1].innerText = ""

        })
        .catch(error => {
            console.log(error)
            document.querySelectorAll("h2")[1].innerText = ""
        })
}
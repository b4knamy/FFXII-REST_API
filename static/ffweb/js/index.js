
let isShowing = false
const navBtnOpen = document.querySelector('.icon-open')
const navBtnClose = document.querySelector('.icon-close')
const navContainer = document.querySelector('.navbar-content-links-mobile')

navBtnOpen.addEventListener('click', (event) => {
    event.target.style.display = 'none'
    navBtnClose.style.display = 'block'
    navContainer.style.display = 'flex'
})
navBtnClose.addEventListener('click', (event) => {
    event.target.style.display = 'none'
    navBtnOpen.style.display = 'block'
    navContainer.style.display = 'none'
})


function showContent() {
    document.getElementById('json').style.display = 'none';
    document.getElementById('content').style.display = 'block';
}
function showJson() {
    document.getElementById('content').style.display = 'none';
    document.getElementById('json').style.display = 'block';
}
 
document.getElementById('submit').addEventListener('click', (event) => {
    event.preventDefault()
    const container = document.querySelector('.content-view-container')
    
    if (isShowing == true) {
        container.classList.add('opacity-animation')

        setTimeout(
            () => {
                container.classList.remove('appear-animation')
            }, 400
        )

        setTimeout(
            () => {
                container.classList.add('appear-animation')
                container.classList.remove('opacity-animation')
                getData()
            }, 1000
        )
        

    } else {

        container.classList.add('appear-animation')
        getData()
        container.style.display = 'block'
        isShowing = true
    }
    
})

async function getData() {
    const url = document.getElementById('url').value
    const precode = document.querySelector('.pre-code')
    
    try {
        await fetch(
            url
        ).then(
            (response) => {
                const status = document.getElementById('request-status')
                status.innerHTML = `Status: ${response.status}`
                status.setAttribute('response', response.status)
                return response.json()
            }
        ).then((data) => {

            const textJson = JSON.stringify(data, null, 4)
            precode.innerHTML = textJson
            
        })
    } catch (error) {
        const status = document.getElementById('request-status').getAttribute('response')
        if (status == 404) {
            precode.innerHTML =  `Error 404 Not found.\nPlease, check your parameters, values or the entire URL. \n${error}`
        } else if (status == 400) {
            precode.innerHTML =  `Error 400 Bad Request.\nPlease, check your parameters, values or the entire URL. \n${error}`
        } else if (status == 411) {
            precode.innerHTML =  `Error 411 Length Required.\nYou can't set a 0 value to limit parameter. \n${error}`
        } else {
            precode.innerHTML =  error
        }
    }
    
}


function getVaanUrl() {
    const url = document.getElementById('url');
    url.value = 'https://ffxiiapi.onrender.com/api/characters/filter?name=vaan'
}
function getAllCharUrl() {
    const url = document.getElementById('url');
    url.value = 'https://ffxiiapi.onrender.com/api/characters/all'
}
function getZodiarkUrl() {
    const url = document.getElementById('url');
    url.value = 'https://ffxiiapi.onrender.com/api/espers/filter?name_esper=zodiark'
}
function getAllEsperUrl() {
    const url = document.getElementById('url');
    url.value = 'https://ffxiiapi.onrender.com/api/espers/all'
}
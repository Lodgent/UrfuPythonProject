let btn = document.querySelector(".toggle-btn");
btn.onclick = function(){OpenMenu()}
let asideBtn = document.querySelector("aside");
function OpenMenu()
{
    if(asideBtn.classList.contains("active"))
    {
        asideBtn.classList.remove("active")
    }
    else
    {
        asideBtn.classList.add("active")
    }


}


function GetCurrentYear() {
    document.getElementById("footer-text-date").innerHTML = new Date().getFullYear();
}

function PageIsInFrame() {
    if (document.getElementsByTagName("frame") !== undefined) {
        
        var sectionBlocks = document.getElementsByClassName("section-block");

        for (let sectionBlock in sectionBlocks) {
            sectionBlock.classList.remove("section-block");
            sectionBlock.classList.add("section-block-framed");
        }
    }
}
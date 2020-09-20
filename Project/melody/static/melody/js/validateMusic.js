function validate(){
    
    if(document.musicForm.songTitle.value = "")
    {
        alert("Please provide the Song Title!");
        document.musicForm.songTitle.focus();
        return false;
    }
}
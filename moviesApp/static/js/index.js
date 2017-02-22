function validateRegistration(){
    var password = document.forms["registration"]["password"].value
    var verifyPassword = document.forms["registration"]["verifyPassword"].value

    /*Check n°2 : verify password and password must be equals*/
    if ((password != verifyPassword)) {
        alert("Check that password and verifyPassword are equals")
        return false;
    }
    return true;
}

/*Function that verify if all field are written*/
function InvalidMsg(textbox) {
    if (textbox.value == '') {
        textbox.setCustomValidity('Field mandatory!');
    }
    else if (textbox.validity.typeMismatch){
        textbox.setCustomValidity('Please enter a valid email address');
    }
    else {
       textbox.setCustomValidity('');
    }
    return true;
}


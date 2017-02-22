function cercaFilm(){
    $.getJSON('cercaFilm/',
        {
            nomeFilm: "ciaooo"
        },
        function(data){
            console.log(data);
    });
}

function validateRegistration(){
    var name = document.forms["registration"]["name"].value
    var surname = document.forms["registration"]["surname"].value
    var email = document.forms["registration"]["email"].value
    var password = document.forms["registration"]["password"].value
    var verifyPassword = document.forms["registration"]["verifyPassword"].value
    var age = document.forms["registration"]["age"].value
    var gender = document.forms["registration"]["gender"].value
    var profession = document.forms["registration"]["profession"].value
    var education = document.forms["registration"]["education"].value

    alert(age)

    /*Check n°1 : all element will be defined*/
    if ((name == "") || (surname == "") || (email == "") ||
        (password == "") || (verifyPassword == "") || (age == "") ||
        (gender == "") || (profession == "") || (education == "")) {

        alert("Compile all!")
        return false;
    }

    return true;

}

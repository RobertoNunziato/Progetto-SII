function validateRegistration() {
    var password = document.forms["registration"]["password"].value
    var verifyPassword = document.forms["registration"]["verifyPassword"].value

    /*Check n°2 : verify password and password must be equals*/
    if ((password != verifyPassword)) {
        alert("Check that password and verifyPassword are equals")
        return false;
    }
    return true;
}

function verifyUser() {
    var email = document.forms["registration"]["email"].value
    $.getJSON('/verifyUser/',
        {
            email: email
        },
        function (result) {
            if (result == true) {
                document.forms["registration"]["email"].value = ""
                alert("Email already used!")
            }
        });

}

/*Function that verify if all field are written*/
function InvalidMsg(textbox) {
    if (textbox.value == '') {
        textbox.setCustomValidity('Field mandatory!');
    }
    else if (textbox.validity.typeMismatch) {
        textbox.setCustomValidity('Please enter a valid email address');
    }
    else {
        textbox.setCustomValidity('');
    }
    return true;
}


function validateSurvey() {
    var survey = ($("#survey").val())
    survey = parseSurvey(survey)

    /*Controllo n° 1: compila tutte le domande*/
    for (key in survey) {
        for (elem in survey[key]) {
            if ((survey[key])[elem] == 0) {
                alert("compile all questions!")
                return false;
            }
        }
    }

    var preferences = [];
    var gender = $("#userGender").val()
    var q1 = survey["1"][0],
        q2 = survey["1"][1],
        q3 = survey["1"][2],
        q4 = survey["1"][3],
        q5 = survey["1"][4],
        q6 = survey["1"][5],
        q7 = survey["1"][6],
        q8 = survey["1"][7],
        q9 = survey["1"][8],
        q10 = survey["1"][9],

        q11 = survey["2"][0],
        q12 = survey["2"][1],
        q13 = survey["2"][2],
        q14 = survey["2"][3],
        q15 = survey["2"][4],
        q16 = survey["2"][5],
        q17 = survey["2"][6],
        q18 = survey["2"][7],
        q19 = survey["2"][8],
        q20 = survey["2"][9],

        q21 = survey["3"][0],
        q22 = survey["3"][1],
        q23 = survey["3"][2],
        q24 = survey["3"][3],
        q25 = survey["3"][4],
        q26 = survey["3"][5],
        q27 = survey["3"][6],
        q28 = survey["3"][7],
        q29 = survey["3"][8],
        q30 = survey["3"][9],

        q31 = survey["4"][0],
        q32 = survey["4"][1],
        q33 = survey["4"][2],
        q34 = survey["4"][3],
        q35 = survey["4"][4],
        q36 = survey["4"][5],
        q37 = survey["4"][6],
        q38 = survey["4"][7],
        q39 = survey["4"][8],
        q40 = survey["4"][9],

        q41 = survey["5"][0],
        q42 = survey["5"][1],
        q43 = survey["5"][2],
        q44 = survey["5"][3],
        q45 = survey["5"][4],
        q46 = survey["5"][5],
        q47 = survey["5"][6],
        q48 = survey["5"][7],
        q49 = survey["5"][8],
        q50 = survey["5"][9];
    var e, a, c, n, o;
    e = (20 + q1 - q6 + q11 - q16 + q21 - q26 + q31 - q36 + q41 - q46) * 5 / 40;
    a = (14 - q2 + q7 - q12 + q17 - q22 + q27 - q32 + q37 + q42 + q47) * 5 / 40;
    c = (14 + q3 - q8 + q13 - q18 + q23 - q28 + q33 - q38 + q43 + q48) * 5 / 40;
    n = (38 - q4 + q9 - q14 + q19 - q24 - q29 - q34 - q39 - q44 - q49) * 5 / 40;
    o = (8 + q5 - q10 + q15 - q20 + q25 - q30 + q35 + q40 + q45 + q50) * 5 / 40;

    /*    alert("Extroversion: " + e +
     "\nAgreeableness: " + a +
     "\nConscientiousness: " + c +
     "\nNeuroticism: " + n +
     "\nOpenness to Experience: " + o);*/

    var cont = 0;
    if ((o > 2 && o <= 4.25) && (e > 2.35 && e <= 5) && (a > 2.52 && a <= 5)) {
        if (!contains(preferences, "comedy")) {
            preferences.push("comedy");
            cont += 1;
        }
    }
    if ((o > 2.8 && o <= 5) && (c > 2 && c <= 4.5) && (a > 2 && a <= 4.52) && (n > 1 && n <= 4)) {
        if (!contains(preferences, "horror")) {
            preferences.push("horror");
            cont += 1;
        }
    }
    if ((o > 2.6 && o <= 5) && (e > 2.62 && e <= 5) && (a > 2 && a <= 5)) {
        if (!contains(preferences, "horror")) {
            preferences.push("horror")
            cont += 1;
        }
    }
    if ((o > 2.6 && o <= 5) && (e > 2 && e <= 5) && (a > 2 && a <= 5) && (n > 1.53 && n <= 4)) {
        if (!contains(preferences, "horror")) {

            preferences.push("horror")
            cont += 1;
        }
    }
    if ((o > 2.6 && o <= 5) && (a > 2 && a <= 4.52) && (n > 1.53 && n <= 3.85)) {
        if (!contains(preferences, "horror")) {

            preferences.push("horror")
            cont += 1;
        }
    }
    if ((o > 2.8 && o <= 5) && (e > 2.62 && e <= 4.89) && (a > 2.52 && a <= 4.85)) {
        if (!contains(preferences, "comedy")) {

            preferences.push("comedy")
            cont += 1;
        }
    }
    if ((e > 1.37 && e <= 3.75) && (n > 2.7 && n <= 5.02)) {
        if (gender == "Female") {
            if (!contains(preferences, "animation")) {

                preferences.push("animation");
                console.log("animation");//woman
                cont += 1;
            }
        }
    }
    if ((o > 3.2 && o <= 5) && (c > 2.25 && c <= 4.6) && (e > 4.8 && e <= 3.2)) {
        if (gender == "Male") {
            if (!contains(preferences, "animation")) {

                preferences.push("animation");
                console.log("animation");//man
                cont += 1;
            }
        }
    }
    if ((c > 2.25 && c <= 4.6) && (n > 0.47 && n <= 2.79)) {
        if (gender == "Male") {
            if (!contains(preferences, "animation")) {

                preferences.push("animation");
                console.log("animation");//man
                cont += 1;
            }
        }
    }
    if ((o > 2.8 && o <= 5) && (e > 2.5 && e <= 4.87) && (n > 1.4 && n <= 3.72)) {
        if (gender == "Female") {
            if (!contains(preferences, "children")) {

                preferences.push("children");
                console.log("children");//woman-cartoon
                cont += 1;
            }
        }
    }
    if ((c > 2.67 && c <= 5) && (a > 2.3 && a <= 4.6) && (n > 1.72 && n <= 4.05)) {
        if (gender == "Female") {
            if (!contains(preferences, "romance")) {

                preferences.push("romance");
                console.log("romance");//woman
                cont += 1;
            }
        }
    }
    if ((o > 3.6 && o <= 5) && (c > 2.25 && c <= 4.6)) {
        if (gender == "Male") {
            if (!contains(preferences, "film-noir")) {

                preferences.push("film-noir");
                console.log("film-noir");//man-neo-noir
                cont += 1;
            }
        }
    }
    if ((o > 3.2 && o <= 5) && (c > 2.6 && c <= 5) && (n > 1.74 && n <= 4)) {
        if (gender == "Male") {
            if (!contains(preferences, "drama")) {

                preferences.push("drama");
                console.log("drama");//man
                cont += 1;
            }
        }
    }
    if ((o > 2.4 && o <= 4.6) && (e > 2.8 && e <= 5)) {
        if (gender == "Male") {
            if (!contains(preferences, "war")) {

                preferences.push("war");
                console.log("war");//man
                cont += 1;
            }
        }
    }
    if ((e > 2 && e <= 4.4) && (n > 1 && n <= 3.42)) {
        if (gender == "Male") {
            if (!contains(preferences, "adventure")) {

                preferences.push("adventure");
                console.log("adventure");//man
                cont += 1;
            }
        }
    }
    if ((o > 2.8 && o <= 5) && (e > 2 && e <= 4.4) && (n > 1.42 && n <= 3.74)) {
        if (gender == "Male") {
            if (!contains(preferences, "comedy")) {

                preferences.push("comedy");
                console.log("comedy");//man
                cont += 1;
            }
        }
    }
    if ((o > 3.2 && o <= 5) && (a > 2.35 && a <= 5) && (n > 0.786 && n <= 3.104)) {
        if (gender == "Male") {
            if (!contains(preferences, "adventure")) {

                preferences.push("adventure");
                console.log("adventure");//man
                cont += 1;
            }
        }
    }
    if ((c > 2.6 && c <= 5) && (e > 2 && e <= 4.4) && (n > 1.74 && n <= 4.06)) {
        if (gender == "Male") {
            if (!contains(preferences, "drama")) {

                preferences.push("drama");
                console.log("drama");//man
                cont += 1;
            }
        }
    }
    if ((o > 2.6 && o <= 5) && (e > 2.4 && e <= 5) && (a > 2.7 && a <= 5) && (n > 1.42 && n <= 3.74)) {
        if (gender == "Male") {
            if (!contains(preferences, "action")) {

                preferences.push("action");
                console.log("action");//man
                cont += 1;
            }
        }
    }
    if ((o > 3 && o <= 5) && (n > 2 && n <= 5)) {
        if (gender == "Male") {
            if (!contains(preferences, "musical")) {

                preferences.push("musical");
                console.log("musical");//man-music video
                cont += 1;
            }
        }
    }
    if ((o > 2.91 && o <= 5) && (c > 2.375 && c <= 4.55) && (a > 2.5 && a <= 5)) {
        if (!contains(preferences, "sci-fi")) {

            preferences.push("sci-fi");
            console.log("sci-fi");//science fiction
            cont += 1;
        }
    }
    if ((o > 2.91 && o <= 5) && (a > 2.5 && a <= 4.65)) {
        if (!contains(preferences, "sci-fi")) {

            preferences.push("sci-fi");
            console.log("sci-fi");//science fiction
            cont += 1;
        }
    }
    if ((o > 2.9 && o <= 5) && (e > 2 && e <= 4.4) && (n > 1.7 && n <= 4)) {
        if (!contains(preferences, "fantasy")) {

            preferences.push("fantasy");
            console.log("fantasy");
            cont += 1;
        }
    }
    if ((o > 2.7 && o <= 5) && (c > 2.4 && c <= 4.6) && (n > 1.6 && n <= 4)) {
        if (!contains(preferences, "thriller")) {

            preferences.push("thriller");
            console.log("thriller");
            cont += 1;
        }
    }
    if ((o > 2.7 && o <= 5) && (n > 1.8 && n <= 4.15)) {
        if (!contains(preferences, "crime")) {

            preferences.push("crime");
            console.log("crime");
            cont += 1;
        }
    }
    if ((o > 2.7 && o <= 5) && (c > 2.4 && c <= 5) && (a > 2.45 && a <= 5)) {
        if (!contains(preferences, "mistery")) {

            preferences.push("mistery");
            console.log("mystery");
            cont += 1;
        }
    }
    if ((o > 3 && o <= 5) && (e > 2 && e <= 5) && (a > 2 && a <= 5)) {
        if (!contains(preferences, "documentary")) {

            preferences.push("documentary");
            console.log("documentary");
            cont += 1;
        }
    }

    if (cont == 0) {
        alert("cont=0")
        preferences.push("comedy")
        preferences.push("horror")
        preferences.push("animation")
        preferences.push("children")
        preferences.push("romance")
        preferences.push("film-noir")
        preferences.push("drama")
        preferences.push("war")
        preferences.push("adventure")
        preferences.push("action")
        preferences.push("musical")
        preferences.push("sci-fi")
        preferences.push("fantasy")
        preferences.push("thriller")
        preferences.push("crime")
        preferences.push("mistery")
        preferences.push("documentary")
        console.log("ambiguous personality");
    }


    document.forms["completeRegistration"]["preferences"].value = preferences
    return true;

}
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

function validateSurvey() {
    var size = $('input[type=radio]:checked').size();
    if (size < 50){
        alert("checked all questions!");
        return false;
    }
    else{
        var preferences = [];
        var q1 = Number($("input[name=q1]:checked").val()),
            q2 = Number($("input[name=q2]:checked").val()),
            q3 = Number($("input[name=q3]:checked").val()),
            q4 = Number($("input[name=q4]:checked").val()),
            q5 = Number($("input[name=q5]:checked").val()),
            q6 = Number($("input[name=q6]:checked").val()),
            q7 = Number($("input[name=q7]:checked").val()),
            q8 = Number($("input[name=q8]:checked").val()),
            q9 = Number($("input[name=q9]:checked").val()),
            q10 = Number($("input[name=q10]:checked").val()),
            q11 = Number($("input[name=q11]:checked").val()),
            q12 = Number($("input[name=q12]:checked").val()),
            q13 = Number($("input[name=q13]:checked").val()),
            q14 = Number($("input[name=q14]:checked").val()),
            q15 = Number($("input[name=q15]:checked").val()),
            q16 = Number($("input[name=q16]:checked").val()),
            q17 = Number($("input[name=q17]:checked").val()),
            q18 = Number($("input[name=q18]:checked").val()),
            q19 = Number($("input[name=q19]:checked").val()),
            q20 = Number($("input[name=q20]:checked").val()),
            q21 = Number($("input[name=q21]:checked").val()),
            q22 = Number($("input[name=q22]:checked").val()),
            q23 = Number($("input[name=q23]:checked").val()),
            q24 = Number($("input[name=q24]:checked").val()),
            q25 = Number($("input[name=q25]:checked").val()),
            q26 = Number($("input[name=q26]:checked").val()),
            q27 = Number($("input[name=q27]:checked").val()),
            q28 = Number($("input[name=q28]:checked").val()),
            q29 = Number($("input[name=q29]:checked").val()),
            q30 = Number($("input[name=q30]:checked").val()),
            q31 = Number($("input[name=q31]:checked").val()),
            q32 = Number($("input[name=q32]:checked").val()),
            q33 = Number($("input[name=q33]:checked").val()),
            q34 = Number($("input[name=q34]:checked").val()),
            q35 = Number($("input[name=q35]:checked").val()),
            q36 = Number($("input[name=q36]:checked").val()),
            q37 = Number($("input[name=q37]:checked").val()),
            q38 = Number($("input[name=q38]:checked").val()),
            q39 = Number($("input[name=q39]:checked").val()),
            q40 = Number($("input[name=q40]:checked").val()),
            q41 = Number($("input[name=q41]:checked").val()),
            q42 = Number($("input[name=q42]:checked").val()),
            q43 = Number($("input[name=q43]:checked").val()),
            q44 = Number($("input[name=q44]:checked").val()),
            q45 = Number($("input[name=q45]:checked").val()),
            q46 = Number($("input[name=q46]:checked").val()),
            q47 = Number($("input[name=q47]:checked").val()),
            q48 = Number($("input[name=q48]:checked").val()),
            q49 = Number($("input[name=q49]:checked").val()),
            q50 = Number($("input[name=q50]:checked").val());
        var e, a, c, n, o;
        e = (20 + q1 - q6 + q11 - q16 + q21 - q26 + q31 - q36 + q41 - q46) * 5 / 40;
        a = (14 - q2 + q7 - q12 + q17 - q22 + q27 - q32 + q37 + q42 + q47) * 5 / 40;
        c = (14 + q3 - q8 + q13 - q18 + q23 - q28 + q33 - q38 + q43 + q48) * 5 / 40;
        n = (38 - q4 + q9 - q14 + q19 - q24 - q29 - q34 - q39 - q44 - q49) * 5 / 40;
        o = (8 + q5 - q10 + q15 - q20 + q25 - q30 + q35 + q40 + q45 + q50) * 5 / 40;
        alert("Extroversion: " + e +
            "\nAgreeableness: " + a +
            "\nConscientiousness: " + c +
            "\nNeuroticism: " + n +
            "\nOpenness to Experience: " + o);
        var cont = 0;
        if ((o > 2 && o <= 4.25) && (e > 2.35 && e <= 5) && (a > 2.52 && a <= 5)) {
            preferences.push("comedy");
            cont += 1;
        }
        if ((o > 2.8 && o <= 5) && (c > 2 && c <= 4.5) && (a > 2 && a <= 4.52) && (n > 1 && n <= 4)) {
            preferences.push("horror");
            cont += 1;
        }
        if ((o > 2.6 && o <= 5) && (e > 2.62 && e <= 5) && (a > 2 && a <= 5)) {
            preferences.push("horror")
            cont += 1;
        }
        if ((o > 2.6 && o <= 5) && (e > 2 && e <= 5) && (a > 2 && a <= 5) && (n > 1.53 && n <= 4)) {
            preferences.push("horror")
            cont += 1;
        }
        if ((o > 2.6 && o <= 5) && (a > 2 && a <= 4.52) && (n > 1.53 && n <= 3.85)) {
            preferences.push("horror")
            cont += 1;
        }
        if ((o > 2.8 && o <= 5) && (e > 2.62 && e <= 4.89) && (a > 2.52 && a <= 4.85)) {
            preferences.push("comedy")
            cont += 1;
        }
        if ((e > 1.37 && e <= 3.75) && (n > 2.7 && n <= 5.02)) {
            preferences.push("animation");
            console.log("animation");//woman
            cont += 1;
        }
        if ((o > 3.2 && o <= 5) && (c > 2.25 && c <= 4.6) && (e > 4.8 && e <= 3.2)) {
            preferences.push("animation");
            console.log("animation");//man
            cont += 1;
        }
        if ((c > 2.25 && c <= 4.6) && (n > 0.47 && n <= 2.79)) {
            preferences.push("animation");
            console.log("animation");//man
            cont += 1;
        }
        if ((o > 2.8 && o <= 5) && (e > 2.5 && e <= 4.87) && (n > 1.4 && n <= 3.72)) {
            preferences.push("children");
            console.log("children");//woman-cartoon
            cont += 1;
        }
        if ((c > 2.67 && c <= 5) && (a > 2.3 && a <= 4.6) && (n > 1.72 && n <= 4.05)) {
            preferences.push("romance");
            console.log("romance");//woman
            cont += 1;
        }
        if ((o > 3.6 && o <= 5) && (c > 2.25 && c <= 4.6)) {
            preferences.push("film-noir");
            console.log("film-noir");//man-neo-noir
            cont += 1;
        }
        if ((o > 3.2 && o <= 5) && (c > 2.6 && c <= 5) && (n > 1.74 && n <= 4)) {
            preferences.push("drama");
            console.log("drama");//man
            cont += 1;
        }
        if ((o > 2.4 && o <= 4.6) && (e > 2.8 && e <= 5)) {
            preferences.push("war");
            console.log("war");//man
            cont += 1;
        }
        if ((e > 2 && e <= 4.4) && (n > 1 && n <= 3.42)) {
            preferences.push("adventure");
            console.log("adventure");//man
            cont += 1;
        }
        if ((o > 2.8 && o <= 5) && (e > 2 && e <= 4.4) && (n > 1.42 && n <= 3.74)) {
            preferences.push("comedy");
            console.log("comedy");//man
            cont += 1;
        }
        if ((o > 3.2 && o <= 5) && (a > 2.35 && a <= 5) && (n > 0.786 && n <= 3.104)) {
            preferences.push("adventure");
            console.log("adventure");//man
            cont += 1;
        }
        if ((c > 2.6 && c <= 5) && (e > 2 && e <= 4.4) && (n > 1.74 && n <= 4.06)) {
            preferences.push("drama");
            console.log("drama");//man
            cont += 1;
        }
        if ((o > 2.6 && o <= 5) && (e > 2.4 && e <= 5) && (a > 2.7 && a <= 5) && (n > 1.42 && n <= 3.74))    {
            preferences.push("action");
            console.log("action");//man
            cont += 1;
        }
        if ((o > 3 && o <= 5) && (n > 2 && n <= 5))    {
            preferences.push("musical");
            console.log("musical");//man-music video
            cont += 1;
        }
        if ((o > 2.91 && o <= 5) && (c > 2.375 && c <= 4.55) && (a > 2.5 && a <= 5))    {
            preferences.push("sci-fi");
            console.log("sci-fi");//science fiction
            cont += 1;
        }
        if ((o > 2.91 && o <= 5) && (a > 2.5 && a <= 4.65))    {
            preferences.push("sci-fi");
            console.log("sci-fi");//science fiction
            cont += 1;
        }
        if ((o > 2.9 && o <= 5) && (e > 2 && e <= 4.4) && (n > 1.7 && n <= 4))    {
            preferences.push("fantasy");
            console.log("fantasy");
            cont += 1;
        }
        if ((o > 2.7 && o <= 5) && (c > 2.4 && c <= 4.6) && (n > 1.6 && n <= 4))    {
            preferences.push("thriller");
            console.log("thriller");
            cont += 1;
        }
        if ((o > 2.7 && o <= 5) && (n > 1.8 && n <= 4.15))    {
            preferences.push("crime");
            console.log("crime");
            cont += 1;
        }
        if ((o > 2.7 && o <= 5) && (c > 2.4 && c <= 5) && (a > 2.45 && a <= 5))    {
            preferences.push("mistery");
            console.log("mystery");
            cont += 1;
        }
        if ((o > 3 && o <= 5) && (e > 2 && e <= 5) && (a > 2 && a <= 5))    {
            preferences.push("documentary");
            console.log("documentary");
            cont += 1;
        }
        if (cont==0){

            console.log("ambiguous personality");
        }
    }
    return true;
}
function parseSurvey(surveyString){
    console.log(surveyString)
    var survey = {};
    var surveySplit = surveyString.split("],");
    var elem1 = surveySplit[0],
        elem2 = surveySplit[1],
        elem3 = surveySplit[2],
        elem4 = surveySplit[3],
        elem5 = surveySplit[4];

    var key1 = elem1.split("\"")[1]
    if(key1 != "5") {
        var value1 = (elem1.split("[")[1]).split(",")
        var preferences = []
        for (var index = 0; index < value1.length; index++) {
            var number = ((value1[index]).split("\""))[1]
            if (isNaN(parseInt(number)))
                preferences.push(0)
            else
                preferences.push(parseInt(number))
        }
        survey[key1] = preferences;
    }
    var key2 = elem2.split("\"")[1]
    if(key2 != "5") {
        var value2 = (elem2.split("[")[1]).split(",")
        var preferences = []
        for (var index = 0; index < value2.length; index++) {
            var number = ((value2[index]).split("\""))[1]
            if (isNaN(parseInt(number)))
                preferences.push(0)
            else
                preferences.push(parseInt(number))
        }
        survey[key2] = preferences;
    }
    var key3 = elem3.split("\"")[1]
    if(key3 != "5") {
        var value3 = (elem3.split("[")[1]).split(",")
        var preferences = []
        for(var index=0; index<value3.length; index++){
            var number = ((value3[index]).split("\""))[1]
            if(isNaN(parseInt(number)))
                preferences.push(0)
            else
                preferences.push(parseInt(number))

        }
        survey[key3]=preferences;

    }
    var key4 = elem4.split("\"")[1]
    if(key4 != "5"){
        var value4 = (elem4.split("[")[1]).split(",")
        var preferences = []
        for(var index=0; index<value4.length; index++){
            var number = ((value4[index]).split("\""))[1]
            if(isNaN(parseInt(number)))
                preferences.push(0)
            else
                preferences.push(parseInt(number))
        }
        survey[key4]=preferences;
    }
    var key5 = elem5.split("\"")[1]
    if(key5 != "5"){
        var value5 = (elem5.split("[")[1]).split(",")
        var preferences = []
        for(var index=0; index<value5.length; index++){
            var number = ((value5[index]).split("\""))[1]
            if(isNaN(parseInt(number)))
                preferences.push(0)
            else
                preferences.push(parseInt(number))
        }
        survey[key5]=preferences;
    }

    var preferences = []
    var q41,q42,q43,q44,q45,q46,q47,q48,q49,q50;
    q41 = Number($("input[name=q41]:checked").val())
    q42 = Number($("input[name=q42]:checked").val())
    q43 = Number($("input[name=q43]:checked").val())
    q44 = Number($("input[name=q44]:checked").val())
    q45 = Number($("input[name=q45]:checked").val())
    q46 = Number($("input[name=q46]:checked").val())
    q47 = Number($("input[name=q47]:checked").val())
    q48 = Number($("input[name=q48]:checked").val())
    q49 = Number($("input[name=q49]:checked").val())
    q50 = Number($("input[name=q50]:checked").val())

    if(isNaN(q41)) preferences.push(0)
    else preferences.push(q41)
    if(isNaN(q42)) preferences.push(0)
    else preferences.push(q42)
    if(isNaN(q43)) preferences.push(0)
    else preferences.push(q43)
    if(isNaN(q44)) preferences.push(0)
    else preferences.push(q44)
    if(isNaN(q45)) preferences.push(0)
    else preferences.push(q45)
    if(isNaN(q46)) preferences.push(0)
    else preferences.push(q46)
    if(isNaN(q47)) preferences.push(0)
    else preferences.push(q47)
    if(isNaN(q48)) preferences.push(0)
    else preferences.push(q48)
    if(isNaN(q49)) preferences.push(0)
    else preferences.push(q49)
    if(isNaN(q50)) preferences.push(0)
    else preferences.push(q50)
    survey["5"]=preferences;

    return survey
}
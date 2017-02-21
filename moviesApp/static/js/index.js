function cercaFilm(){
    $.getJSON('cercaFilm/',
        {
            nomeFilm: "ciaooo"
        },
        function(data){
            console.log(data);
    });
}


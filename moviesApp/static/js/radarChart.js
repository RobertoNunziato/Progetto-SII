//line chart data

//radar chart data
var radarData = {
	labels : ["Extroversion","Agreeableness","Coscientioussness","Neuroticism","OpenessToExperience"],
	datasets : [
		{
			 fillColor: "#ffb135",
			 strokeColor: "#f6ff00",
			pointColor : "#ff4111",
			pointStrokeColor : "#ffffff",
			data : [2,3,1,5,2]
		}
	]
}



//Create Radar chart
var ctx2 = document.getElementById("radarChart").getContext("2d");
var myNewChart = new Chart(ctx2).Radar(radarData);

new Chart(ctx2).Radar(radarData,options);



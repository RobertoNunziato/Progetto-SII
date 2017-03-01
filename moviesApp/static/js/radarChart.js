var scripts = document.getElementsByTagName('script');
var lastScript = scripts[scripts.length-1];
var scriptName = lastScript;
var big5 = scriptName.getAttribute('userBig5');

var data =big5.split(",")
var data2=[]
console.log(big5)

for (i in data){
	data2.push(parseFloat(data[i]))
}
//radar chart data
var radarData = {
    labels: ["Extroversion","Agreeableness","Coscientioussness","Neuroticism","OpenessToExperience"],
    datasets: [
        {
            label: "Big5 values",
            backgroundColor: "rgba(179,181,198,0.2)",
            borderColor: "rgba(179,181,198,1)",
            pointBackgroundColor: "rgba(179,181,198,1)",
            pointBorderColor: "#fff",
            pointHoverBackgroundColor: "#fff",
            pointHoverBorderColor: "rgba(179,181,198,1)",
            data: data2
        }]
};

var option = {
    responsive: true,
    };




//Create Radar chart
var ctx2 = document.getElementById("radarChart").getContext("2d");
var myNewChart = new Chart(ctx2).Radar(radarData,option);


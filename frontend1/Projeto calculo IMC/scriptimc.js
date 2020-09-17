function IMC(){
    var altura = parseInt(document.getElementById("a").value)/100;
    var peso = parseInt(document.getElementById("p").value);
    var imc = peso / (altura*altura)
    var text = "<h1> você esta abaixo do peso</h1>";
    if(imc >18.5 && imc< 25){
			text =  " <h1>seu peso esta normal</h1>";}
	else if (imc > 25 && imc < 30){
			text = " <h1> Você esta acima do peso </h1> ";
	}else if (imc>30) {
			text = " <h1>voce está com Obesidade de fofura</h1> ";
	}
	resultado = document.getElementById("result");
	resultado.innerHTML = text;

fun

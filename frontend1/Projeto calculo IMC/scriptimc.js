var nome = prompt("Digite seu nome");
var altura = prompt("Digite sua altura");
var peso = prompt("Digite seu peso");
    imc=peso/(altura*altura);

		if(imc < 18.5){
			document.write( nome +  "<h1> você esta abaixo do peso</h1>")
		}else if(imc >18.5 && imc< 25){
			document.write( nome +  " <h1>seu peso esta normal</h1>")
		}else if(imc > 25 && imc < 30){
			document.write( nome +  " <h1> Voce esta acima do peso </h1> ");
		}else if (imc>30) {
			document.write( nome +  " <h1>voce está com Obesidade morbida</h1> ");
		}
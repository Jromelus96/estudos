<script type="text/javascript">
		function IMC() {
			var a=document.getElementById('a').value;
			var p=document.getElementById('p').value;
			var bmi=w/(a/100*a/100);
			var bmio=(bmi.toFixed(2));

			document.getElementById("resultado").innerHTML="Your IMC is " + bmio;
}

div>
			<h2>BMI Calculator</h2>
			<p class="text">Altura</p>
			<input type="text" id="h">
			<p class="text">Peso</p>
			<input type="text" id="p">
			<p id="resultado"></p>
			<button id="btn" onClick="IMC()">Calculate</button>
			<p id="info">Por favor insira altura [Cm] e peso [Kg]</p>
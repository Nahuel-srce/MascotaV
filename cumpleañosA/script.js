function mostrarMensaje() {
  const musica = document.getElementById("musica");
  const notas = document.getElementById("notas");

  notas.style.display = "block";

  musica.play();
}

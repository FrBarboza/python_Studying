function teste(){
    alert("Teste...")
}

function mostrar() {
    var produto_nome = document.getElementById("produto").getAttribute("data-nome")
    alert("Produto passado: " + produto_nome)
}

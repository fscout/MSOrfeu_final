window.onload = verifica_acesso()

function verifica_acesso(){
    nivel = document.getElementsByClassName("nivel")
    // alert(nivel[0].innerHTML + " Testes")
    if (nivel[0].innerHTML != "admin") {
        // Definir como será apresentada a mensagem para o usuário que não tem permissão. EX: Modal, Alert, etc...
        alert("Ops! Vc não tem acesso! ")
        window.location.href = "/index";
    }else{
    // alert("Vc tem acesso! ")
    hider = document.getElementsByClassName("hider")
    hider[0].style.display = "block";
}
}

function pega_valor(){
    cod_barras = document.getElementById("cod_barras")
    // alert("Testando" + cod_barras.value)
    cod_barras.value = cod_barras.value
    // alert("Testando" + cod_barras.innerHTML)
}
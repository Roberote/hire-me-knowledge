package edu.robert.segundasemana;
public class MinhaClasse {

public static void main (String [] args) {

    String primeiroNome = "Robert";

    String segundoNome = "Castilho";

    String nomeCompleto = nomeCompleto (primeiroNome,segundoNome);
    System.out.println(nomeCompleto);
}

public static String nomeCompleto (String primeiroNome, String segundoNome){
    return "Resultado do método é " + primeiroNome.concat(" ").concat(segundoNome);


}

}


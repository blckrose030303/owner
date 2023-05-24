def  obtener_colores_bandera ( pais ):
    colores_bandera  = {
        "Argentina" : [ "celeste" , "blanco" ],
        "Brasil" : [ "verde" , "amarillo" ],
        "Canada" : [ "rojo" , "blanco" ],
        "Francia" : [ "azul" , "blanco" , "rojo" ],
        "India" : [ "naranja" , "blanco" , "verde" ],
        "Colombia" : [ "amarillo" , "azul" , "rojo" ],
      # Agrega mas paises y sus colores de bandera aqui
    }

    si  pais  en  colores_bandera :
        colores  =  colores_bandera [ pais ]
        print ( f"Los colores de la bandera de { pais } son: { ', ' . join ( colores ) } " )
    más :
        print ( "No se encontró información sobre la bandera de ese país." )

# Ejemplo de uso
pais  =  input ( "Ingresa el nombre de un pais: " )
obtener_colores_bandera ( pais )
#YulianCastañeda
#Bandera de países
#IEM_ESCUELA_NORMAL_PASTO #11-1

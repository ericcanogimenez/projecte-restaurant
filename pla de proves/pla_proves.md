

| ID      | Descripció de la prova                           | Entrada                                                | Accions                                  | Resultat esperat                                        | Estat    |
| ------- | ------------------------------------------------ | ------------------------------------------------------ | ---------------------------------------- | ------------------------------------------------------- | -------- |
| **P01** | Crear una nova comanda amb un sol producte       | Client: "Eric"; Prod: "Aigua"; Preu: 1.5; Quantitat: 1 | Seleccionar opció 1, introduir dades     | Es genera ticket amb subtotal 1.50 i total amb IVA 1.65 | Correcte |
| **P02** | Crear comanda amb 3 productes                    | Diverses entrades vàlides                              | Crear comanda amb 3 productes            | Es mostra tiquet amb 3 línies i total correcte          | Correcte |
| **P03** | Sortir del menú                                  | Opció 4                                                | Seleccionar 4                            | El programa finalitza amb missatge "Fins la propera"    | Correcte |
| **P04** | Actualitzar comanda sense haver-ne creat cap     | Opció 2                                                | Seleccionar 2                            | Mostra missatge "No hi ha cap comanda enregistrada"     | Correcte |
| **P05** | Visualitzar comanda sense haver-ne creada cap    | Opció 3                                                | Seleccionar 3                            | Mostra missatge "No hi ha cap comanda enregistrada"     | Correcte |
| **P06** | Introducció d’una lletra on s’espera un número   | Preu = "abc" o Quantitat = "x"                         | Crear comanda i donar entrada incorrecta | El programa captura l’error i torna a demanar dades     | Correcte |
| **P07** | Actualitzar comanda afegint un producte          | Comanda prèvia existent                                | Opció 2, afegir producte                 | Nova línia afegida + total recalculat                   | Correcte |
| **P08** | Mostrar últim tiquet després d’una actualització | Comanda creada i actualitzada                          | Opció 3                                  | El tiquet mostra tots els productes (antics + nous)     | Correcte |
| **P09** | Afegir múltiples productes a opció 2             | Productes diversos                                     | Actualitzar fins “n”                     | Cada producte es mostra correctament en línia           | Correcte |
| **P10** | Entrada d’opció del menú incorrecta              | Opció = “hola” o 99                                    | Introduir opció no vàlida                | Mostra “Opció no vàlida” i torna al menú                | Correcte |


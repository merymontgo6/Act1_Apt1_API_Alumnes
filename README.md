# API d'alumnes
## Activitat 1 - Apartat 1
Aquesta API permet gestionar alumnes i les seves dades en una base de dades mitjançant operacions CRUD (crear, llegir, actualitzar, eliminar). 
Els usuaris poden afegir nous alumnes, llistar tots els alumnes, obtenir els detalls d'un alumne específic, actualitzar-ne la informació i eliminar-lo si cal. 
Les dades de cada alumne inclouen el seu nom, cicle, curs, grup i l'aula assignada, que es valida abans d'actualitzar o crear l'alumne. 
Les consultes SQL interactuen amb les taules d'alumnes i aules, garantint la integritat de les dades i retornant missatges d'èxit o error segons el resultat de les operacions.

#### GET "/"
No realitza cap operació de gestió de dades, sinó que simplement indica que el servidor està funcionant correctament.

![image](https://github.com/user-attachments/assets/5388c8c9-6cef-49d9-b8ab-1af11fe9fc51)

#### GET /alumnes/list: 
Llista tots els alumnes de la base de dades, incloent-hi informació com el nom, cicle, curs i grup. Retorna un missatge d'error si no hi ha alumnes enregistrats.

![image](https://github.com/user-attachments/assets/c86ea9bb-d89e-4a78-8c30-04095483fad3)

#### GET /alumne/show/{id}: 
Retorna la informació d'un alumne específic identificat pel seu id. Si l'alumne no existeix, retorna un error 404.

![image](https://github.com/user-attachments/assets/d4494fda-3dff-4abb-a4ea-892d655ed31c)

#### POST /alumne/add: 
Afegeix un nou alumne a la base de dades amb la informació proporcionada (IdAula, nom, cicle, curs, grup). Abans de crear l'alumne, valida que l'aula especificada existeixi. Si l'aula no existeix, es retorna un error.

![image](https://github.com/user-attachments/assets/85cb8c85-7e68-46ad-8161-5d67857f2f2a)

#### PUT /alumne/update/{id}: 
Actualitza la informació d'un alumne existent, identificat pel seu id, amb les noves dades proporcionades (IdAula, nom, cicle, curs, grup). També valida que l'aula existeixi abans d'actualitzar. Si no es troba l'alumne o l'aula, es retorna un error.

![image](https://github.com/user-attachments/assets/976c30bc-f7b7-4b02-8bde-37e101ede3b5)

#### DELETE /alumne/delete/{id}: 
Elimina un alumne de la base de dades pel seu id. Si l'alumne no existeix, es retorna un error 404.

![image](https://github.com/user-attachments/assets/c9a6fe04-72db-4705-a8e6-44367edbddb6)

#### GET /alumne/listAll 
Recupera i retorna una llista completa de tots els alumnes enregistrats a la base de dades, incloent-hi informació addicional sobre l'aula a la qual pertanyen.

![image](https://github.com/user-attachments/assets/2aa3b37c-bd33-4450-9f9e-1d56b60057d3)

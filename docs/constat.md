Structure d'un constat



Un constat est une ligne du rapport. Il décrit une violation trouvée.



fichier : le fichier de données où se trouve la violation.

ligne   : position de la ligne fautive dans le fichier.

colonne : nom de la colonne où se trouve la valeur en violation.

valeur  : la valeur effectivement trouvée dans la cellule.

règle : identifiant de la règle qui n'a pas été respectée. Permet au lecteur de retrouver dans le fichier YAML ce qui était exigé et pourquoi.



Questions non tranchées :

\- Le numéro de ligne est instable. Faut-il une clé métier en plus ?

\- Distingue-t-on la gravité des violations ? Si oui, moteur ou YAML ?


# Sploks
Sploks est un programme de remplacement de Coliks, qui est utilisée depuis 17 ans dans le magasin Sports-Time d'Echallens pour gérer la location de matériel de sports d'hiver.

## Mettre en place l'environnement

### Applications à télecharger
- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) ou un IDE de votre choix.
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) ou un autre outil SQL de votre préference.
- [Python](https://www.python.org/downloads/)
- [QtDesigner](https://build-system.fman.io/qt-designer-download) si vous voulez ouvrir les fichiers _.ui_

### Marche à suivre
Après avoir installé les programmes au dessus:

1. Lancer le script SQL qui se trouve dans _docs/workbench_
2. Dans le dossier SPLoks, dupliquez le fichier _const.py.example_ et effacez lui l'extension _.example_
3. Remplacez les "_..._" par vos propres configs SQL
4. Ensuite, ouvrir le CMD et entrez: _pip install pyqt5_
5. Toujours dans le CMD: _pip install pyqt5-tools_
6. Vous pouvez maintenant fermer le CMD et ouvrir le dossier Sploks avec votre IDE (PyCharm, chez nous).
7. Dans le projet (alt+1 si pas visible), click droit sur _sploks.py_ et clickez sur l'option _run sploks_.
8. Votre projet devrait normalment ce lancer si tout est bien installé.

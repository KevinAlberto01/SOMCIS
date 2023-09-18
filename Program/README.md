Comandos 

catkin_create_pkg (nombre del archivo) rospy(para python) std_msgs ---para crear un archivo con sus atributos usar 
vim nombreArchivo.py --archivo python

Crear un paquete

catkin_create_pkg <package name> [depened1] [depend2] [depende3]

cd ~/catkin_ws/src
catkin_create_pkg somcis std_msgs rospy


Crear un talker (Esta en la carpeta de carpetas)

cd ~/catkin_ws/src/somcis
mkdir scripts
cd scripts 
touch talker.py
sudo chmod +x talker.py




# rolon_pkg

Este proyecto utiliza la secuencia `r2b_robotarm` del [R2B Dataset 2024 de NVIDIA](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/isaac/resources/r2bdataset2024), que contiene datos sensoriales y de control de un brazo robótico. Me interesó esta secuencia porque permite trabajar con percepción visual y control de actuadores en un entorno de simulación cercano a la realidad, lo cual es ideal para empezar a explorar conceptos ROS 2.

## Clonar el repositorio

```console
cd ~/ros2_ws/ 
git clone https://github.com/rolma271/rolon_pkg.git
```

## Descarga del dataset

1. Instalar el cliente de NGC:

```console
wget --content-disposition https://ngc.nvidia.com/downloads/ngccli_linux.zip
unzip ngccli_linux.zip
chmod u+x ngc-cli/ngc
```

2. Descargar el dataset:

```console
./ngc-cli/ngc registry resource download-version "nvidia/isaac/r2bdataset2024:1"
```

3. Ubicar la carpeta ```r2bdataset2024_v1/``` en el mismo nivel que este repositorio (```rolon_pkg/```).


## Construir el workspace

```console
cd ~/ros2_ws
colcon build --packages-select rolon_pkg --symlink-install
source install/setup.bash
```

## Cómo lanzar

Como lanzar el rosbag:

```console
cd rolon_pkg
ros2 launch rolon_pkg rosbag_visualization.launch.py
```

Esto hará lo siguiente:

1. Reproducirá automáticamente el **rosbag**.
2. Abrirá **RViz** con la visualización configurada del entorno del brazo robótico.
3. Iniciará **RQT** con una perspectiva personalizada que muestra los tópicos del sistema.
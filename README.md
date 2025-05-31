# rolon_pkg

Este proyecto utiliza la secuencia `r2b_robotarm` del [R2B Dataset 2024 de NVIDIA](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/isaac/resources/r2bdataset2024), que contiene datos sensoriales y de control de un brazo robótico. Nos interesó esta secuencia porque permite trabajar con percepción visual y control de actuadores en un entorno de simulación cercano a la realidad, lo cual es ideal para probar algoritmos en ROS 2.

## Descarga del dataset

1. Instalar el cliente de NGC:

   ```bash
   wget --content-disposition https://ngc.nvidia.com/downloads/ngccli_linux.zip
   unzip ngccli_linux.zip
   chmod u+x ngc-cli/ngc
   ```
2. Descargar el dataset:

    ```
    ./ngc-cli/ngc registry resource download-version "nvidia/isaac/r2bdataset2024:1"
    ```

3. Ubicar la carpeta r2bdataset2024_v1/ en el mismo nivel que este repositorio (rolon_pkg/).


## Cómo lanzar

    ```bash
    cd rolon_pkg
    ros2 launch rolon_pkg rosbag_visualization.launch.py
    ```
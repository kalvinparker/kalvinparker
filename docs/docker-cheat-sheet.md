<!-- Imported from https://github.com/kalvinparker/docker-cheat-sheet.git
Commit: ea7edbf
Author: JacobLinCool <jacoblincool@gmail.com>
License: 
Imported-on: 2025-11-01T22:17:52.3709944+00:00 -->

# Docker Cheat Sheet

**Â¿Quieres colaborar en este *cheat sheet*? Â¡Revisa la secciÃ³n de [ContribuciÃ³n](#contributing)!**

## Tabla de Contenidos

* [Por quÃ© Docker](#por-quÃ©-Docker)
* [Prerrequisitos](#prerrequisitos)
* [InstalaciÃ³n](#instalaciÃ³n)
* [Contenedores](#contenedores)
* [ImÃ¡genes](#imÃ¡genes)
* [Redes](#redes)
* [Registry y Repositorios](#Registry-y-Repositorios)
* [Dockerfile](#dockerfile)
* [Capas](#capas)
* [Enlaces](#enlaces)
* [VolÃºmenes](#volÃºmenes)
* [Exponiendo Puertos](#Exponiendo-Puertos)
* [Buenas prÃ¡cticas](#buenas-prÃ¡cticas)
* [Docker-Compose](#docker-compose)
* [Seguridad](#seguridad)
* [Consejos](#consejos)
* [ContribuciÃ³n](#contribuciÃ³n)

## Por quÃ© Docker

"Con Docker, los desarrolladores (y desarrolladoras) pueden construir cualquier aplicaciÃ³n en cualquier lenguaje usando cualquier herramienta. Las aplicaciones "Dockerizadas" son totalmente portables y pueden funcionar en cualquier lugar: En portÃ¡tiles con OS X y Windows de compaÃ±eros; servidores de QA con Ubuntu en el cloud; y VMs de los datacenters de producciÃ³n que funcionan con Red Hat.

Los desarrolladores pueden empezar a trabajar rÃ¡pidamente a partir de cualquiera de las mÃ¡s de 13.000 aplicaciones disponibles en Docker Hub. Docker gestiona y guarda los cambios y dependencias, facilitando el trabajo a los Administradores de Sistemas a la hora de entender cÃ³mo funcionan las aplicaciones hechas por los desarrolladores. Y, con Docker Hub, los desarrolladores puedes automatizar el despliegue y compartir el trabajo con colaboradores a travÃ©s de repositorios pÃºblicos o privados.

Docker ayuda a los desarrolladores a trabajar y conseguir aplicaciones de mejor calidad de forma mÃ¡s rÃ¡pida." -- [QuÃ© es docker](https://www.docker.com/what-docker#copy1)

## Prerrequisitos

De forma opcional, se puede hacer utilizar [Oh My Zsh](https://github.com/ohmyzsh/oh-my-zsh) con el [plugin de Docker](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins#docker) para autocompletar los comandos de Docker.

### Linux

[El requisito mÃ­nimo](https://docs.docker.com/engine/installation/binaries/#check-kernel-dependencies) para Docker es utilizar una versiÃ³n de Kernel (nÃºcleo) posterior a la 3.10.x.

### MacOS

Se requiere de la versiÃ³n 10.8 â€œMountain Lionâ€ o posterior.

### Windows 10

Se debe activar Hyper-V en la BIOS.

En caso de estar disponible, tambiÃ©n se debe activar VT-D (Procesadores Intel).

### Windows Server

Como mÃ­nimo se requiere la versiÃ­n de Windows Server 2016 para instalar Docker y Docker Compose. No obstante, existen limitaciones en esta versiÃ³n, como a la hora de utilizar redes virtualizadas y contenedores Linux.

Se recomienda utilizar Windows Server 2019 o posteriores.

## InstalaciÃ³n

### Linux

Ejecuta este comando rÃ¡pido y sencillo proporcionado por Docker:

```sh
curl -sSL https://get.docker.com/ | sh
```

Si no estÃ¡s dispuesto a ejecutar un shell script que no sabes lo que trae, por favor: revisa las instrucciones de [instalaciÃ³n](https://docs.docker.com/engine/installation/linux/) de tu distribuciÃ³n.

Si eres totalmente nuevo en Docker, te recomendamos seguir esta [serie de tutoriales](https://docs.docker.com/engine/getstarted/).

### macOS

Descarga e instala [Docker Community Edition](https://www.docker.com/community-edition). Si tienes Homebrew-Cask, simplemente escribe `brew install --cask docker`. O descarga e instala [Docker Toolbox](https://docs.docker.com/toolbox/overview/). [Docker For Mac](https://docs.docker.com/docker-for-mac/) estÃ¡ bien, pero no estÃ¡ tan pulido como como la instalaciÃ³n de VirtualBox. [Revisa la comparaciÃ³n aquÃ­](https://docs.docker.com/docker-for-mac/docker-toolbox/).

> **NOTA:** Docker Toolbox estÃ¡ deprecado. DeberÃ­as utilizar Docker Community Edition, revisa [Docker Toolbox](https://docs.docker.com/toolbox/overview/).

Una vez hayas instalado Docker Community Edition, haz click en el icono de docker en el Launchpad. Entonces inicia un contenedor:

```sh
docker run hello-world
```

Â¡Y ya estarÃ­a! Ya tienes un contenedor de docker funcionando.

Si eres totalmente nuevo en Docker, te recomendamos seguir esta [serie de tutoriales](https://docs.docker.com/engine/getstarted/).

### Windows 10

Las instrucciones para instalar Docker Desktop para Windows se encuentran [aquÃ­](https://docs.docker.com/desktop/windows/install/)

Una vez instalado, abre Powershell como administrador y ejecuta:

```powershell
# Muestra la versiÃ³n de docker instalada:
docker version

# Descarga, crea, y ejecuta 'hello-world':
docker run hello-world
```

Para continuar con esta chuleta, haz click derecho sobre el icono de Docker en la secciÃ³n de notificaciones (abajo a la derecha), y ves a ajustes. Para montar volÃºmenes, el disco C:/ debe ser habilitado en ajustes para poder pasar la informaciÃ³n a los contenedores (se detalla mÃ¡s adelante en este artÃ­culo).

Para alternar entre contenedores Windows y Linux, haz botÃ³n derecho en el icono de Docker en la secciÃ³n de notificaciones y haz click en el botÃ³n de cambiar el sistema operativo del contenedor. Hacer esto pararÃ¡ los contenedores que estÃ©n funcionando y serÃ¡n inaccesibles hasta que el SO del contenedor vuelva a cambiar.

Adicionalmente, si tienes WSL (Subsitema de Windows para Linux) o WSL2 instalado en tu equipo, quizÃ¡s tambiÃ©n quieras instalar el Kernel de Linux para Windows. Las instrucciones para ello pueden encontrarse [aquÃ­](https://techcommunity.microsoft.com/t5/windows-dev-appconsult/using-wsl2-in-a-docker-linux-container-on-windows-to-run-a/ba-p/1482133). Esto requiere la caracterÃ­stica de Subsistema de Windows para Linux. Esto permitirÃ¡ que los contenedores sean accesibles desde los sistemas operativos WSL, asÃ­ como mejorar la eficiencia ejecutando sistemas operaviso WSL en docker. TambiÃ©n es preferible utilizar la [terminal de Windows](https://docs.microsoft.com/en-us/windows/terminal/get-started) para esto.

### Windows Server 2016 / 2019

Sigue las instrucciones de Microsoft que puedes encontrar [aquÃ­](https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/deploy-containers-on-server#install-docker)

Si haces uso de la Ãºltima versiÃ³n de 2019, prepÃ¡rate para trabajar solo con powershell, dado que es solo una imÃ¡gen del nÃºcleo del servidor (sin interfaz de escritorio). Cuando inicies esta mÃ¡quina, se loguearÃ¡ y mostrarÃ¡ una ventana de powerhell. Se recomienda instalar editores de texto y otras herramientas utilizando [Chocolatey](https://chocolatey.org/install)

Tras instalarlo, funcionarÃ¡n los siguientes comandos:

```powershell
# Muestra la versiÃ³n de docker instalada:
docker version

# Descarga, crea, y ejecuta 'hello-world':
docker run hello-world
```

Windows Server 2016 no puede ejecutar imÃ¡genes de Linux.

Windows Server Build 2004 es capaz de ejecutar contenedores de Linux y Windows simultÃ¡neamente a travÃ©s del aislamiento de Hyper-V. Cuando se ejecuten los contenedores, utiliza el comando ```isolation=hyperv```, el cual lo aislarÃ¡ utilizando distintas instancias de kernel para cada contenedor.

### Revisar la versiÃ³n

Es muy importante que siempre conozcas la versiÃ³n de Docker que estÃ¡s utilizando en cualquier momento. Es muy Ãºtil dado que permite saber las caracterÃ­sticas compatibles con lo que estÃ©s ejecutando. Esto tambiÃ©n es importante para conocer que contenedores puedes ejecutar de la docker store cuando estÃ©s intentando utilizar un contenedor como plantilla. Dicho esto, veamos como recuperar la versiÃ³n de Docker que estÃ¡ ejecutÃ¡ndose actualmente.

* [`docker version`](https://docs.docker.com/engine/reference/commandline/version/) muestra que versiÃ³n de docker estÃ¡ ejecutÃ¡ndose.

Recuperar la versiÃ³n del servidor:

```console
$ docker version --format '{{.Server.Version}}'
1.8.0
```

Puedes volcar la informaciÃ³n en un JSON:

```console
$ docker version --format '{{json .}}'
{"Client":{"Version":"1.8.0","ApiVersion":"1.20","GitCommit":"f5bae0a","GoVersion":"go1.4.2","Os":"linux","Arch":"am"}
```

## Contenedores

[Proceso bÃ¡sico del aislamiento en Docker](http://etherealmind.com/basics-docker-containers-hypervisors-coreos/). Los contenedores son a las mÃ¡quinas virtuales lo que los threads son a los procesos. O puedes verlo como un *chroot* dopado.

### Ciclo de vida

* [`docker create`](https://docs.docker.com/engine/reference/commandline/create) crea un contenedor pero no lo inicia.
* [`docker rename`](https://docs.docker.com/engine/reference/commandline/rename/) permite renombrar el nombre de un contenedor.
* [`docker run`](https://docs.docker.com/engine/reference/commandline/run) crea e inicia un contenedor.
* [`docker rm`](https://docs.docker.com/engine/reference/commandline/rm) elimina un contenedor.
* [`docker update`](https://docs.docker.com/engine/reference/commandline/update/) actualiza los recursos mÃ¡ximos de un contenedor.

Si ejecutas un contenedor sin opciones este se iniciarÃ¡ y detendrÃ¡ automÃ¡ticamente, si quieres mantenerlo funcionando puedes utilizar el comando `docker run -td container_id`, esto utilizarÃ¡ la opciÃ³n `-t`, que habilitarÃ¡ una pseudo-sesiÃ³n de TTY, y `-d`, que separarÃ¡ el contenedor automÃ¡ticamente (lo ejecutarÃ¡ en segundo plano y mostrarÃ¡ la ID del contenedor)

Si quieres un contenedor efÃ­mero, `docker run --rm` eliminarÃ¡ el contenedor en cuanto se detenga.

Si quieres mapear un directorio del host al contenedor de docker, `docker run -v $HOSTDIR:$DOCKERDIR`. Revisa [VolÃºmenes](https://github.com/wsargent/docker-cheat-sheet/#volumes).

Si al eliminar el contenedor tambiÃ©n quieres borrar los volÃºmenes asociados, el borrado deberÃ¡ contener `-v`, por ejemplo: `docker rm -v`.

TambiÃ©n existe un [driver de logs](https://docs.docker.com/engine/admin/logging/overview/) disponible para contenedores individuales en Docker 1.10. Para ejecutar docker con un driver de logs personalizado, ejecuta `docker run --log-driver=syslog`.

Otra opciÃ³nÃºtil es `docker run --name yourname docker_image` donde especificando la opciÃ³n `--name` dentro del comando *run*, esto te permitirÃ¡ iniciar y detener el contenedor utilizando el nombre especificado al crearlo.

### Ejecutando y deteniendo

* [`docker start`](https://docs.docker.com/engine/reference/commandline/start) inicia un contenedor.
* [`docker stop`](https://docs.docker.com/engine/reference/commandline/stop) detiene un contenedor que estÃ© iniciado.
* [`docker restart`](https://docs.docker.com/engine/reference/commandline/restart) detiene y ejecuta un contenedor.
* [`docker pause`](https://docs.docker.com/engine/reference/commandline/pause/) pausa un contenedor que se estÃ¡ ejecutando, congelÃ¡ndolo.
* [`docker unpause`](https://docs.docker.com/engine/reference/commandline/unpause/) reactiva un contenedor.
* [`docker wait`](https://docs.docker.com/engine/reference/commandline/wait) se bloquea hasta que el contenedor se detiene.
* [`docker kill`](https://docs.docker.com/engine/reference/commandline/kill) envÃ­a una SIGKILL a un contenedor.
* [`docker attach`](https://docs.docker.com/engine/reference/commandline/attach) se conecta a un contenedor.

Si quieres despegarte de un contenedor, utiliza `Ctrl + p, Ctrl + q`.

Si quieres integrar un contenedor con un [gestor de procesos](https://docs.docker.com/engine/admin/host_integration/), inicia el daemon con `-r=false`, despuÃ©s utiliza `docker start -a`.

Si quieres exponer un puerto del contenedor a travÃ©s del host, revisa la secciÃ³n [exponiendo puertos](#exposing-ports).

Las polÃ­ticas de reinicio en una instancia bloqueada se [explica aquÃ­](http://container42.com/2014/09/30/docker-restart-policies/).

#### Restricciones de CPU

Puedes limitar la CPU, ya sea especificando el porcentÃ¡ge global de las CPU o definiendo el nÃºmero de nÃºcleos.

Por ejemplo, puedes especificar la configuraciÃ³n de [`cpu-shares`](https://docs.docker.com/engine/reference/run/#/cpu-share-constraint). Este parÃ¡metro es un poco raro -- 1024 significa el 100% de la CPU, por lo que si quieres que el contenedor utilice el 50% de todas las CPU, deberÃ¡s especificar 512. Revisa <https://docs.docker.com/engine/reference/run/#/cpu-share-constraint> para mÃ¡s informaciÃ³n.

```sh
docker run -it -c 512 agileek/cpuset-test
```

TambiÃ©s puedes utilizar Ãºnicamente algunos nÃºcleos de la CPU utilizando [`cpuset-cpus`](https://docs.docker.com/engine/reference/run/#/cpuset-constraint). Revisa <https://agileek.github.io/docker/2014/08/06/docker-cpuset/> para mÃ¡s detalles y algunos vÃ­deos guays:

```sh
docker run -it --cpuset-cpus=0,4,6 agileek/cpuset-test
```

FÃ­jate que Docker puede seguir **viendo** todas las CPU dentro del contenedor -- simplemente no la utiliza entera. Revisa <https://github.com/docker/docker/issues/20770> para mÃ¡s informaciÃ³n.

#### Restricciones de memoria

TambiÃ©n puedes especificar [restricciones de memoria](https://docs.docker.com/engine/reference/run/#/user-memory-constraints) en Docker

```sh
docker run -it -m 300M ubuntu:14.04 /bin/bash
```

#### Capacidades

Las capacidades de linux se pueden establecer utilizando `cap-add` y `cap-drop`. Revisa <https://docs.docker.com/engine/reference/run/#/runtime-privilege-and-linux-capabilities> para mÃ¡s detalles. Debe usarse para una mejor seguridad.

Para montar un sistema de ficheros basado en FUSE, debes combinar --cap-add con --device:

```sh
docker run --rm -it --cap-add SYS_ADMIN --device /dev/fuse sshfs
```

Para dar acceso a un Ãºnico dispositivo:

```sh
docker run -it --device=/dev/ttyUSB0 debian bash
```

Para dar acceso a todos los dispositivos:

```sh
docker run -it --privileged -v /dev/bus/usb:/dev/bus/usb debian bash
```

MÃ¡s informaciÃ³n sobre contenedores con privilegios [aquÃ­](
https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities)

### InformaciÃ³n

* [`docker ps`](https://docs.docker.com/engine/reference/commandline/ps) muestra los contenedores funcionando.
* [`docker logs`](https://docs.docker.com/engine/reference/commandline/logs) recupera los logs del contenedor. (Puedes utilizar un driver personalizado para los logs, pero los logs solo estÃ¡n disponibles para `json-file` y `journald` en la versiÃ³n 1.10).
* [`docker inspect`](https://docs.docker.com/engine/reference/commandline/inspect) revisa toda la informaciÃ³n del contenedor (incluyendo la direcciÃ³n IP).
* [`docker events`](https://docs.docker.com/engine/reference/commandline/events) recupera los eventos del contenedor.
* [`docker port`](https://docs.docker.com/engine/reference/commandline/port) muestra los puertos abiertos al exterior del contenedor.
* [`docker top`](https://docs.docker.com/engine/reference/commandline/top) muestra los procesos que se estÃ¡n ejecutando en el contenedor,
* [`docker stats`](https://docs.docker.com/engine/reference/commandline/stats) Muestra las estadÃ­sticas del uso de recursos del contenedor.
* [`docker diff`](https://docs.docker.com/engine/reference/commandline/diff) Muestra los archivos que han cambiado en el sistema de ficheros del contenedor.

`docker ps -a` muestra todos los contenedores: que estÃ¡n funcionados o parados.

`docker stats --all` lista todos los contenedores, por defecto solo los que estÃ¡n funcionando.

### Import / Export

* [`docker cp`](https://docs.docker.com/engine/reference/commandline/cp) copia los ficheros y carpetas de un contenedor al sistema de ficheros local.
* [`docker export`](https://docs.docker.com/engine/reference/commandline/export) vuelca el sistema de ficheros de un contenedor como fichero .tar en el STDOUT.

### Ejecuntando comandos

* [`docker exec`](https://docs.docker.com/engine/reference/commandline/exec) ejecuta un comando en el contenedor.

Para entrar a un contenedor que estÃ¡ funcionando, acopla un nuevo proceso de terminal al contenedor usando: `docker exec -it <ID/Nombre del contenedor> /bin/bash`.

## ImÃ¡genes


Las imÃ¡genes simplemente son [plantillas para contenedores de docker](https://docs.docker.com/engine/understanding-docker/#how-does-a-docker-image-work).

### Ciclo de vida

* [`docker images`](https://docs.docker.com/engine/reference/commandline/images) muestra todas las imÃ¡genes.
* [`docker import`](https://docs.docker.com/engine/reference/commandline/import) crea una imÃ¡gen a partir de un fichero .tar.
* [`docker build`](https://docs.docker.com/engine/reference/commandline/build) crea una imÃ¡gen a partir de un Dockerfile.
* [`docker commit`](https://docs.docker.com/engine/reference/commandline/commit) crea una imÃ¡gen a partir de un contenedor, deteniÃ©ndolo temporalmente si estÃ¡ funcionando.
* [`docker rmi`](https://docs.docker.com/engine/reference/commandline/rmi) elimina una imÃ¡gen.
* [`docker load`](https://docs.docker.com/engine/reference/commandline/load) carga una imÃ¡gen a partir de un fichero .tar pasado como STDIN, incluyendo imÃ¡genes y etiquetas.
* [`docker save`](https://docs.docker.com/engine/reference/commandline/save) guarda una imÃ¡gen en un fichero .tar pasado como STDOUT con todas las capas superiores, etiquetas y versiones.

### InformaciÃ³n

* [`docker history`](https://docs.docker.com/engine/reference/commandline/history) muestra el historial de una imÃ¡gen.
* [`docker tag`](https://docs.docker.com/engine/reference/commandline/tag) etiqueta una imÃ¡gen (local o *registry*).

### Limpiar

Puedes utilizar el comando `docker rmi` para eliminar una imÃ¡gen especÃ­fica, pero tambiÃ©n existe una herramienta alternativa llamada [docker-gc](https://github.com/spotify/docker-gc) que elimina de forma segura las imÃ¡genes que ya no estÃ¡n siendo utilizadas por ningÃºn contenedor. En la versiÃ³n 1.13 de docker, tambiÃ©n existe el comando `docker image prine`, el cual elimina las imÃ¡genes que no estÃ¡n siendo utilizadas. Revisa [Prune](#prune)

### Cargar/Guardar una imÃ¡gen

Carga una imÃ¡gen a partir de un fichero:

```sh
docker load < my_image.tar.gz
```

Guarda una imÃ¡gen existente:

```sh
docker save my_image:my_tag | gzip > my_image.tar.gz
```

### Importar/Exportar un contenedor

Importa un contenedor como imÃ¡gen a partir de un fichero:

```sh
cat my_container.tar.gz | docker import - my_image:my_tag
```

Exporta un contenedor existente:

```sh
docker export my_container | gzip > my_container.tar.gz
```

### Diferencia entre cargar y guardar una imÃ¡gen e importar y exportar un contenedor como imÃ¡gen

Cargar una imÃ¡gen utilizando el comando `load` crea una nueva imÃ¡gen incluyeno su historial.
Importar un contenedor como imÃ¡gen utilizando el comando `import` crea una nueva imÃ¡gen excluyendo el historial, lo que se traduce en una imÃ¡gen mÃ¡s ligera comparada con cargarla.

## Redes

Docker tiene la caracterÃ­stica de [Redes](https://docs.docker.com/engine/userguide/networking/). Docker automÃ¡ticamente crea tres interficies de red al instalarlo (puente, host, nula). Por defecto, cuando se lanza un nuevo contenedor es aÃ±adido la red puente. Para habilitar la comunicaciÃ³n entre varios contenedores puedes crear una nueva red y lanzar los contenedores en ella. Esto permite a los contenedores comunicarse entre ellos y aislarese de los contenedores que no estÃ¡n conectados a su misma red. AdemÃ¡s, esto permite mapear nombres de contenedores a sus direcciones IP. Revisa *[working with networks](https://docs.docker.com/engine/userguide/networking/work-with-networks/)* para mÃ¡s informaciÃ³n.

### Ciclo de vida

* [`docker network create`](https://docs.docker.com/engine/reference/commandline/network_create/) NAME Crea una nueva red (por defecto de tipo puente).
* [`docker network rm`](https://docs.docker.com/engine/reference/commandline/network_rm/) NAME Elimina una o mÃ¡s redes indicando el nombre o el identificador. No pueden haber contenedores conectados a la red al eliminarla.

### Info

* [`docker network ls`](https://docs.docker.com/engine/reference/commandline/network_ls/) Lista las redes creadas.
* [`docker network inspect`](https://docs.docker.com/engine/reference/commandline/network_inspect/) NAME Muestra informaciÃ³n detallada de una o mÃ¡s redes.

### Connection

* [`docker network connect`](https://docs.docker.com/engine/reference/commandline/network_connect/) NETWORK CONTAINER Conecta un contenedor a una red.
* [`docker network disconnect`](https://docs.docker.com/engine/reference/commandline/network_disconnect/) NETWORK CONTAINER Desconecta un contenedor de una red.

Puedes especificar una [ip especÃ­fica a un contenedor](https://blog.jessfraz.com/post/ips-for-all-the-things/):

```sh
# crea una nueva red puente con la subnet y puerta de enlace especÃ­ficada
docker network create --subnet 203.0.113.0/24 --gateway 203.0.113.254 iptastic

# ejecuta un contenedor de nginx con al ip especificada en la red iptastic
$ docker run --rm -it --net iptastic --ip 203.0.113.2 nginx

# curl hacia la ip desde cualquier otro lugar (dando por hecho que es una ip pÃºblica hehe)
$ curl 203.0.113.2
```

## Registry y Repositorios

(Nota de traducciÃ³n: Registry serÃ­a traducido como Regitro, pero nadie le llama asÃ­ en el mundo real, asÃ­ que...)

Un repositorio es una colecciÃ³n *alojada* de imÃ¡genes enlazadas que unidas crean el sistema de ficheros para un contenedor.

Un Registry es un *alojamiento* -- un servidor que almacena repositorios y provee de una API HTTP para [gestionar la actualizaciÃ³n y descarga de repositorios](https://docs.docker.com/engine/tutorials/dockerrepos/).

Docker.com posee su propio [Ã­ndice](https://hub.docker.com) como un Registry centralizado que contiene un gran nÃºmero de repositorios. Dicho esto, aclarar que el docker Registry [no hace un buen trabajo verificando imÃ¡genes](https://titanous.com/posts/docker-insecurity), por lo que quizÃ¡s deberÃ­as evitarlo si te preocupa la seguridad.

* [`docker login`](https://docs.docker.com/engine/reference/commandline/login) para loguear en un registry.
* [`docker logout`](https://docs.docker.com/engine/reference/commandline/logout) para desloguear de un registry.
* [`docker search`](https://docs.docker.com/engine/reference/commandline/search) busca en el registry por una imÃ¡gen.
* [`docker pull`](https://docs.docker.com/engine/reference/commandline/pull) recupera una imÃ¡gen del registry a local.
* [`docker push`](https://docs.docker.com/engine/reference/commandline/push) sube una imÃ¡gen local al registry.

### Ejecutar un registry local

Puedes ejecutar un registry local utilizando el proyecto [distribuciÃ³n de docker](https://github.com/docker/distribution) y revisando las instrucciones de como realizar el [deploy local](https://github.com/docker/docker.github.io/blob/master/registry/deploying.md)

Adicionalmente revisa la [mailing list](https://groups.google.com/a/dockerproject.org/forum/#!forum/distribution)

## Dockerfile

[El archivo de configuraciÃ³n](https://docs.docker.com/engine/reference/builder/). Configura un contenedor de docker al ejecutar `docker build` en el. Mucho mÃ¡s preferible a `docker commit`.

AquÃ­ tienes varios editores de textos comunes y mÃ³dulos de resaltado de sintaxis que puedes usar para crear Dockerfiles:

* Si utilizas [jEdit](http://jedit.org), puedes hacer uso del mÃ³dulo de resaltado de sintaxis para [Dockerfile](https://github.com/wsargent/jedit-docker-mode).
* [Sublime Text 2](https://packagecontrol.io/packages/Dockerfile%20Syntax%20Highlighting)
* [Atom](https://atom.io/packages/language-docker)
* [Vim](https://github.com/ekalinin/Dockerfile.vim)
* [Emacs](https://github.com/spotify/dockerfile-mode)
* [TextMate](https://github.com/docker/docker/tree/master/contrib/syntax/textmate)
* [VS Code](https://github.com/Microsoft/vscode-docker)
* Revisa [Docker meets the IDE](https://domeide.github.io/)

### Instructions

* [.dockerignore](https://docs.docker.com/engine/reference/builder/#dockerignore-file)
* [FROM](https://docs.docker.com/engine/reference/builder/#from) utiliza una imÃ¡gen de base para las siguientes instrucciones.
* [MAINTAINER (deprecated - use LABEL instead)](https://docs.docker.com/engine/reference/builder/#maintainer-deprecated) especifica el autor que ha generado las imÃ¡genes.
* [RUN](https://docs.docker.com/engine/reference/builder/#run) ejecuta cualquier comando en una nueva capa de la imÃ¡gen y guarda el estado resultante.
* [CMD](https://docs.docker.com/engine/reference/builder/#cmd) proporcionar valores predeterminados para un contenedor en ejecuciÃ³n.
* [EXPOSE](https://docs.docker.com/engine/reference/builder/#expose) informa a Docker que el contenedor estarÃ¡ escuchando los puertos especificados mientras se ejecute. NOTA: no hace que los puertos sean accesibles.
* [ENV](https://docs.docker.com/engine/reference/builder/#env) define una variable de entorno.
* [ADD](https://docs.docker.com/engine/reference/builder/#add) copia nuevos ficheros, directorios o archivos remotos al contenedor. Invalida cachÃ©s. Procura evitar usar `ADD` e intenta utilizar `COPY` en su lugar.
* [COPY](https://docs.docker.com/engine/reference/builder/#copy) copia nuevos ficheros o directorios al contenedor. Por defecto los copia como *root* independientemente de la configuraciÃ³n de USER/WORKDIR. Utiliza `--chown=<user>:<group>` para cambiar el dueÃ±o. (Lo mismo aplica a `ADD`).
* [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint) configura un contenedor que funcionarÃ¡ como ejecutable.
* [VOLUME](https://docs.docker.com/engine/reference/builder/#volume) crea un punto de montaje para volÃºmenes externos u otros contenedores.
* [USER](https://docs.docker.com/engine/reference/builder/#user) especifica el usuario que ejecutarÃ¡ los prÃ³ximos comandos de tipo RUN / CMD / ENTRYPOINTS.
* [WORKDIR](https://docs.docker.com/engine/reference/builder/#workdir) especifica el directorio de trabajo.
* [ARG](https://docs.docker.com/engine/reference/builder/#arg) define una variable que estarÃ¡ disponible durante el build.
* [ONBUILD](https://docs.docker.com/engine/reference/builder/#onbuild) aÃ±ade una instrucciÃ³n que serÃ¡ lanzada cuando la imÃ¡gen sea utilizada como base de otro build.
* [STOPSIGNAL](https://docs.docker.com/engine/reference/builder/#stopsignal) define la seÃ±al que serÃ¡ enviada al contenedor para detenerse.
* [LABEL](https://docs.docker.com/config/labels-custom-metadata/) aplica metadatos de clave/valor para las imÃ¡genes, contenedores o daemons (servicios).
* [SHELL](https://docs.docker.com/engine/reference/builder/#shell) reemplaza la shell por defecto que es utilizada por Docker para ejecutar los comandos.
* [HEALTHCHECK](https://docs.docker.com/engine/reference/builder/#healthcheck) indica a docker como probar el contenedor para revisar que sigue funcionando.

### Tutorial

* [Flux7's Dockerfile Tutorial](https://www.flux7.com/tutorial/docker-tutorial-series-part-3-automation-is-the-word-using-dockerfile/)

### Examples

* [Ejemplos](https://docs.docker.com/engine/reference/builder/#dockerfile-examples)
* [Buenas prÃ¡cticas para escribir Dockerfiles](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)
* [Michael Crosby](http://crosbymichael.com/) tiene mÃ¡s consejos de [buenas prÃ¡cticas para Dockerfile](http://crosbymichael.com/dockerfile-best-practices.html) / [toma 2](http://crosbymichael.com/dockerfile-best-practices-take-2.html).
* [Construyendo buenas imÃ¡genes de Docker](http://jonathan.bergknoff.com/journal/building-good-docker-images) / [Construyendo mejores imÃ¡genes de Docker](http://jonathan.bergknoff.com/journal/building-better-docker-images)
* [Gestionando la configuraciÃ³n de un contenedor utilizando metadatos](https://speakerdeck.com/garethr/managing-container-configuration-with-metadata)
* [CÃ³mo escribir excelentes Dockerfiles](https://rock-it.pl/how-to-write-excellent-dockerfiles/)

## Capas

Las veriones de los sitemas de ficheros en docker se basan en capas. Son similares a los [git commits o conjuntos de cambios para sistemas de ficheros](https://docs.docker.com/engine/userguide/storagedriver/imagesandcontainers/).

## Enlaces

Los enlaces definen como los contenedores de Docker se comunican entre ellos [mediante puertos TCP/IP](https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/). [Atlassian](https://blogs.atlassian.com/2013/11/docker-all-the-things-at-atlassian-automation-and-wiring/) lo explica con ejemplos. TambiÃ©n puedes resolver [enlaces con nombres de equipo](https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/#/updating-the-etchosts-file).

Esto ha sido parcialmente deprecado por [redes definidas por los usuarios](https://docs.docker.com/network/).

NOTA: Si ÃšNICAMENTE quieres que los contenedores se comuniquen mediante enlaces, inicia el servicio de Docker con `-icc=false` para desactivar la comunicaciÃ³n entre procesos.

Si tienes un contenedor con el nombre CONTAINER (especificado vÃ­a `docker run --name CONTAINER`) y, en el Dockerfile, explones un puerto:

```
EXPOSE 1337
```

Y entonces creas otro contenedor llamado LINKED de la forma:

```sh
docker run -d --link CONTAINER:ALIAS --name LINKED user/wordpress
```

Entonces los puertos expuertos y alias de CONTAINER se mostrarÃ¡n en LINKED con las siguientes variables de entorno:
Then the exposed ports and aliases of CONTAINER will show up in LINKED with the following environment variables:

```sh
$ALIAS_PORT_1337_TCP_PORT
$ALIAS_PORT_1337_TCP_ADDR
```

Y te puedes conectar a Ã©l de esta forma.

Para eliminar los enlaces, utiliza `docker rm --link'.

Generalmente, enlazar mediante servicios de docker es un subgrupo de "descrubrimiento de servicios", un gran problema si tienes pensado utilizar Docker para escalar en producciÃ³n. Por favor, lee [The Docker Ecosystem: Service Discovery and Distributed Configuration Stores](https://www.digitalocean.com/community/tutorials/the-docker-ecosystem-service-discovery-and-distributed-configuration-stores) para mÃ¡s informaciÃ³n.

## VolÃºmenes

Los volÃºmenes de Docker son [sitemas de archivos flotantes](https://docs.docker.com/engine/tutorials/dockervolumes/). Estos no se conectan a un contenedor en particular. Puedes utilizar los volÃºmenes montados de [contenedores de Ãºnicamente datos](https://medium.com/@ramangupta/). A partir de Docker 1.9.0, Docker ha nombrado volÃºmenes que reemplazan los contenedores de solo datos. Considere usar volÃºmenes con nombre para implementarlo en lugar de contenedores de datos.


### Ciclo de vida

* [`docker volume create`](https://docs.docker.com/engine/reference/commandline/volume_create/)
* [`docker volume rm`](https://docs.docker.com/engine/reference/commandline/volume_rm/)

### InformaciÃ³n

* [`docker volume ls`](https://docs.docker.com/engine/reference/commandline/volume_ls/)
* [`docker volume inspect`](https://docs.docker.com/engine/reference/commandline/volume_inspect/)

Los volÃºmenes son Ãºtiles en situaciones donde no puedes utilizar enlaces (los cuales son sÃ³lo TCP/IP). Por ejemplo, si necesitases tener dos instancias de docker comunicÃ¡ndose dejando datos en el sistema de ficheros.

Puedes montarlos en distintos contenedores de docker a la vez, utilizando `docker run --volumes-from`.

Dadp que los volÃºmenes estÃ¡n aislados del sistema de ficheros, estos tambiÃ©n son utilizados para almacenar el estado a partir de cÃ¡lculos de contenedores temporales. Exacto, puedes tener un contenedor sin estado y temporal ejecutÃ¡ndose a partir de una receta,  destruÃ­rlo, y entonecs tener otra instancia temporal que pueda recuperar lo que ha dejado atrÃ¡s el primer contenedor.

Revisa [volÃºmenes avanzados](http://crosbymichael.com/advanced-docker-volumes.html) para mÃ¡s informaciÃ³n. [Container42](http://container42.com/2014/11/03/docker-indepth-volumes/) tambiÃ©n es de utilidad.

Puedes [mapear directorios de MacOS como volÃºmenes de Docker](https://docs.docker.com/engine/tutorials/dockervolumes/#mount-a-host-directory-as-a-data-volume):

```sh
docker run -v /Users/wsargent/myapp/src:/src
```

Puedes utilizar un volÃºmen NFS remoto si [eres valiente](https://docs.docker.com/engine/tutorials/dockervolumes/#/mount-a-shared-storage-volume-as-a-data-volume)

TambiÃ©n puedes plantearme utilizar contenedores de solo datos como se describen [aquÃ­](http://container42.com/2013/12/16/persistent-volumes-with-docker-container-as-volume-pattern/) para tener portabilidad de datos.

Ten en cuenta que puedes montar [archivos como volÃºmenes](#volumes-can-be-files).

## Exponiendo puertos

Exponer puertos de entrada a travÃ©s de un contenedor es [complejo pero factible](https://docs.docker.com/engine/reference/run/#expose-incoming-ports).

Puede hacerse a travÃ©s del mapeo de puertos del contenedor hacia el host (utilizando Ãºnicamente la interficie de localhost) mediante el uso de `p`:

```sh
docker run -p 127.0.0.1:$HOSTPORT:$CONTAINERPORT \
  --name CONTAINER \
  -t algunaimÃ¡gen
```
Puedes decirle a docker que el contenedor escucha en el puerto especificado utilizando [EXPOSE](https://docs.docker.com/engine/reference/builder/#expose):

```Dockerfile
EXPOSE <CONTAINERPORT>
```

NÃ³tese que `EXPOSE` no expone el puerto por si mismo - solo `-p` lo hace.

Para exponer el puerto de un contenedor en localhost, ejecuta:

```sh
iptables -t nat -A DOCKER -p tcp --dport <LOCALHOSTPORT> -j DNAT --to-destination <CONTAINERIP>:<PORT>
```

Si estÃ¡s ejecutando Docker en Virtualbox, tambiÃ©n necesitarÃ¡s hacer forward del puerto, utilizando [forwarded_port] (https://docs.vagrantup.com/v2/networking/forwarded_ports.html). Define un rango de puertos en tu Vagrantfile de la siguiente manera para mapearlos dinÃ¡micamente:

```
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  ...

  (49000..49900).each do |port|
    config.vm.network :forwarded_port, :host => port, :guest => port
  end

  ...
end
```

Si te olvidas de los puertos que has mapeado, utiliza `docker port` para mostrarlo:

```sh
docker port CONTAINER $CONTAINERPORT
```

## Buenas prÃ¡cticas

AquÃ­ tienes algunas buenas prÃ¡cticas de Docker y algunas batallitas:

* [The Rabbit Hole of Using Docker in Automated Tests](http://gregoryszorc.com/blog/2014/10/16/the-rabbit-hole-of-using-docker-in-automated-tests/)
* [Bridget Kromhout](https://twitter.com/bridgetkromhout) has a useful blog post on [running Docker in production](http://sysadvent.blogspot.co.uk/2014/12/day-1-docker-in-production-reality-not.html) at Dramafever.
* TambiÃ©n tienes buenas prÃ¡cticas en este [post](http://developers.lyst.com/devops/2014/12/08/docker/) de Lyst.
* [Building a Development Environment With Docker](https://tersesystems.com/2013/11/20/building-a-development-environment-with-docker/)
* [Discourse in a Docker Container](https://samsaffron.com/archive/2013/11/07/discourse-in-a-docker-container)

## Docker-Compose

Compose es una herramienta para definir y ejecutar varias aplicaciones en contenedores de Docker. Con Compose, utilizas un archivo YAML para configurar tus servicios. Entonces, con un Ãºnico comando, creas e inicias todos los servicios desde tus configuraciones. Para aprender mÃ¡s sobre las caracterÃ­sticas de Compose, revisa la [lista de caracterÃ­sticas](https://docs.docker.com/compose/overview/#features).

Utilizando el siguiente comando puedes iniciar tu aplicaciÃ³n:

```sh
docker-compose -f <docker-compose-file> up
```

TambiÃ©n puedes ejecutar docker-compose en segundo plano utilizando el parÃ¡mentro -d, entonces podrÃ¡s detenerlo cuando lo necesitas con el comando:

```sh
docker-compose stop
```

Puedes tirarlo todo, eliminando los contenedores completamente, con el comando down. Utiliza el parÃ¡metro `--volumes` para tambiÃ©n eliminar los volÃºmenes de datos.

## Seguridad

AquÃ­ te dejamos algunso consejos de seguridad sobre como funciona Docker. La pÃ¡gina de Docker de [seguridad]](https://docs.docker.com/engine/security/security/) lo explica en mÃ¡s detalle.

Lo primero: Docker se ejecuta como root. Si estÃ¡s en el grupo `docker`, [tienes acceso root](https://web.archive.org/web/20161226211755/http://reventlov.com/advisories/using-the-docker-command-to-root-the-host). Si expones el socket de unix de docker a un contenedor, le estÃ¡s dando al contenedor acceso [root a la mÃ¡quina host](https://www.lvh.io/posts/dont-expose-the-docker-socket-not-even-to-a-container/).


Docker no deberÃ­a ser tu Ãºnica defensa. DeberÃ­as asegurarlo y protejerlo.

Para entender como se exponen los contenedores, deberÃ­as leer [Entendiendo y endureciendo Contenedores Linux](https://www.nccgroup.trust/globalassets/our-research/us/whitepapers/2016/april/ncc_group_understanding_hardening_linux_containers-1-1.pdf) de [Aaron Grattafiori](https://twitter.com/dyn___). Esta es una guÃ­a completa y entendible sobre los riesgos relacionados con los contenedores, con una gran cantidad de enlaces y notas a piÃ© de pÃ¡gina. Los siguientes consejos de seguridad son Ãºtiles si ya has protejido tus contenedores en el pasado, pero no son substitutos a entenderlo. 

### Consejos de seguridad

Para mayor seguridad, puedes ejecutar Docker dentro de una mÃ¡quina virtual. Esto es un consejo del Jefe del Equipo de Seguridad de Docker -- [diapositivas](http://www.slideshare.net/jpetazzo/linux-containers-lxc-docker-and-security) / [notas](http://www.projectatomic.io/blog/2014/08/is-it-safe-a-look-at-docker-and-security-from-linuxcon/). Entonces, ejecutalo con AppArmor / seccomp / SELinux /grsec etc. para [limitar los permisos del contenedor](http://linux-audit.com/docker-security-best-practices-for-your-vessel-and-containers/). Revisa [las caracterÃ­sticas de seguridad de Docker 1.10](https://blog.docker.com/2016/02/docker-engine-1-10-security/) para mÃ¡s detalles.

Los identificadores de las imÃ¡genes de Docker son [informaciÃ³n sensible](https://medium.com/@quayio/your-docker-image-ids-are-secrets-and-its-time-you-treated-them-that-way-f55e9f14c1a4) y no deberÃ­an exponerse al mundo exterior. TrÃ¡talos como contraseÃ±as.

Revisa la [Chuleta de Seguridad de Docker](https://github.com/konstruktoid/Docker/blob/master/Security/CheatSheet.adoc) de [Thomas SjÃ¶gren](https://github.com/konstruktoid): ahÃ­ podrÃ¡s encontrar buenos consejos sobre como protejerse.

Revisa el [script de seguridad de Docker Bench](https://github.com/docker/docker-bench-security).


[Las 10 Mejores PrÃ¡cticas de Seguridad para ImÃ¡genes de Docker](https://snyk.io/blog/10-docker-image-security-best-practices/) de Snyk

Puedes empezar utilizando un Kernel con parches inestables de *grsecurity* / *pax* compilados, como [Alpine Linux](https://en.wikipedia.org/wiki/Alpine_Linux). Si haces uso de *grsecurity* en producciÃ³n, deberÃ­as buscar [soporte comercial](https://grsecurity.net/business_support.php) para los [parches estables](https://grsecurity.net/announce.php), de la misma forma que deberÃ­as hacer para RedHat. Son unos 200$ al mes, lo cual es insignificante para el presupuesto de devops.

A partir de Docker 1.11, puedes limitar fÃ¡cilmente el nÃºmero de procesos que se ejecutan en un contenedor para evitar *fork bombs*. Esto requiere utilizar un Kernel de Linux >= 4.3 con CGROUP_PIDS=y en la configuraciÃ³n del kernel.

```sb
docker run --pids-limit=64
```

A partir de Docker 1.11 tambiÃ©n estÃ¡ disponible la posibilidad de evitar que los procesos ganen nuevos privilegios. Esta caracterÃ­stica estÃ¡ en el Kernel de Linux desde la versiÃ³n 3.5. Puedes leer mÃ¡s al respecto en [este](http://www.projectatomic.io/blog/2016/03/no-new-privs-docker/) blog.

```sh
docker run --security-opt=no-new-privileges
```

De la [Chuleta de Seguridad de Docker](http://container-solutions.com/content/uploads/2015/06/15.06.15_DockerCheatSheet_A2.pdf) (es un PDF y es un poco complejo de usar, asÃ­ que mejor copia de abajo) de [Container Solutions](http://container-solutions.com/is-docker-safe-for-production/):

Desactiva la comunicaciÃ³n interproceso con:

```sh
docker -d --icc=false --iptables
```

Establece que el contenedor sea solo lectura:

```sh
docker run --read-only
```

Verifica las imÃ¡genes con un *hashsum*:

```sh
docker pull debian@sha256:a25306f3850e1bd44541976aa7b5fd0a29be
```

Establece el volÃºmen como solo lectura:

```sh
docker run -v $(pwd)/secrets:/secrets:ro debian
```

Crea y utiliza un usiario en el Dockerfile para evitar ejecutar como root dentro del contenedor: 

```Dockerfile
RUN groupadd -r user && useradd -r -g user user
USER user
```

### Espacio de Nombres del Usuario (*User Namespaces*)

TambiÃ©n hay que trabajar con los [espacios de nombres de usuario](https://s3hh.wordpress.com/2013/07/19/creating-and-using-containers-without-privilege/) -- disponibles en la 1.10, pero no activados por defecto.

Para activar esta caracterÃ­stica ("reasignar los usuarios") en ubuntu 15.10, [sigue este ejemplo](https://raesene.github.io/blog/2016/02/04/Docker-User-Namespaces/).

### Videos de Seguridad

* [Using Docker Safely](https://youtu.be/04LOuMgNj9U)
* [Securing your applications using Docker](https://youtu.be/KmxOXmPhZbk)
* [Container security: Do containers actually contain?](https://youtu.be/a9lE9Urr6AQ)
* [Linux Containers: Future or Fantasy?](https://www.youtube.com/watch?v=iN6QbszB1R8)

### Ruta de Seguridad

La ruta de Docker habla sobre [el soporte de *seccomp*](https://github.com/docker/docker/blob/master/ROADMAP.md#11-security).

TambiÃ©n hay una polÃ­tica de AppArmor llamada [base](https://github.com/jfrazelle/bane), y estÃ¡n trabajando en [perfiles de seguridad](https://github.com/docker/docker/issues/17142)

## Consejos

Fuentes:

* [15 Docker Tips in 5 minutes](http://sssslide.com/speakerdeck.com/bmorearty/15-docker-tips-in-5-minutes)
* [CodeFresh Everyday Hacks Docker](https://codefresh.io/blog/everyday-hacks-docker/)

### Prune

Los nuevos [Comandos de manejo de datos](https://github.com/docker/docker/pull/26108) llegaron a Docker en la versiÃ³n 1.13

* `docker system prune`
* `docker volume prune`
* `docker network prune`
* `docker container prune`
* `docker image prune`

### df

`docker system df` muestra un resumen del espacio actualmente utilizado por los distintos elementos de Docker.

### Heredoc Docker Container

```sh
docker build -t htop - << EOF
FROM alpine
RUN apk --no-cache add htop
EOF
```

### Ãšltimas IDs

```sh
alias dl='docker ps -l -q'
docker run ubuntu echo hello world
docker commit $(dl) helloworld
```

### Commit con comando (necesita de Dockerfile)

```sh
docker commit -run='{"Cmd":["postgres", "-too -many -opts"]}' $(dl) postgres
```

### Recuperar la direcciÃ³n IP

```sh
docker inspect $(dl) | grep -wm1 IPAddress | cut -d '"' -f 4
```

O, con [jq](https://stedolan.github.io/jq/) instalado:

```sh
docker inspect $(dl) | jq -r '.[0].NetworkSettings.IPAddress'
```

O, utilizando una [plantilla](https://docs.docker.com/engine/reference/commandline/inspect):

```sh
docker inspect -f '{{ .NetworkSettings.IPAddress }}' <container_name>
```

O, al construir la imÃ¡gen desde un Dockerfile, cuando quieres pasar argumentos de compilaciÃ³n:

```sh
DOCKER_HOST_IP=`ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk '{ print $2 }' | cut -f2 -d: | head -n1`
echo DOCKER_HOST_IP = $DOCKER_HOST_IP
docker build \
  --build-arg ARTIFACTORY_ADDRESS=$DOCKER_HOST_IP
  -t sometag \
  some-directory/
```

### Recuperar el mapping de puertos

```sh
docker inspect -f '{{range $p, $conf := .NetworkSettings.Ports}} {{$p}} -> {{(index $conf 0).HostPort}} {{end}}' <nombredecontenedor>
```

### Encontrar contenedores mediante expresiones regulares

```sh
for i in $(docker ps -a | grep "REGEXP_PATTERN" | cut -f1 -d" "); do echo $i; done
```

### Recuperar la configuraciÃ­n del entorno

```sh
docker run --rm ubuntu env
```

### Detener los contenedores en funcionamiento

```sh
docker kill $(docker ps -q)
```

### Eliminar todos los contenedores (Â¡FORZANDO! Los borrarÃ¡ estÃ©n funcionando o parados)

```sh
docker rm -f $(docker ps -qa)
```

### Eliminar los viejos contenedores

```sh
docker ps -a | grep 'weeks ago' | awk '{print $1}' | xargs docker rm
```

### Eliminar los contenedores detenidos

```sh
docker rm -v $(docker ps -a -q -f status=exited)
```

### Eliminar los contenedores despuÃ©s de pararlos

```sh
docker stop $(docker ps -aq) && docker rm -v $(docker ps -aq)
```

### Eliminar las imÃ¡genes colgadas

```sh
docker rmi $(docker images -q -f dangling=true)
```

### Eliminar todas las imÃ¡genes

```sh
docker rmi $(docker images -q)
```

### Eliminar los volÃºmenes colgados

Como en Docker 1.9:

```sh
docker volume rm $(docker volume ls -q -f dangling=true)
```

En 1.90, el filtro `dangling=false` _no_ funciona - es ignorado y mostrarÃ¡ todos los volÃºmenes

### Mostrar las dependencias de las imÃ¡genes

```sh
docker images -viz | dot -Tpng -o docker.png
```

### Reducir el tamaÃ±o de los contenedores Docker

- Limpiar el APT en una capa `RUN` - Esto deberÃ­a hacerse en la misma capa que los otros comandos `apt`. Sino, las capas previas seguirÃ¡n teniendo la informaciÃ³n original y la imÃ¡gen seguirÃ¡ siendo pesada.
    ```Dockerfile
    RUN {apt commands} \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    ```
- Aplanar una imÃ¡gen
    ```sh
    ID=$(docker run -d image-name /bin/bash)
    docker export $ID | docker import â€“ flat-image-name
    ```
- Para las copias de seguridad
    ```sh
    ID=$(docker run -d image-name /bin/bash)
    (docker export $ID | gzip -c > image.tgz)
    gzip -dc image.tgz | docker import - flat-image-name
    ```

### Monitorizar los recursos del sistema utilizados por los contenedores en funcionamiento

Para revisar el uso de CPU, memoria y E/S de red para un solo contenedor, puedes utilizar:

```sh
docker stats <container>
```

Para todos los contenedores listados por ID:

```sh
docker stats $(docker ps -q)
```

Para todos los contenedores listados por nombre:

```sh
docker stats $(docker ps --format '{{.Names}}')
```

Para todos los contenedores listados por imÃ¡gen:

```sh
docker ps -a -f ancestor=ubuntu
```

Eliminar todas las imÃ¡genes sin etiquetas:

```sh
docker rmi $(docker images | grep â€œ^â€ | awk '{split($0,a," "); print a[3]}')
```

Eliminar contenedores mediante una expresiÃ³n regular:

```sh
docker ps -a | grep wildfly | awk '{print $1}' | xargs docker rm -f
```

Elimina todos los contenedores en estado "Exit":

```sh
docker rm -f $(docker ps -a | grep Exit | awk '{ print $1 }')
```

### Los volÃºmenes pueden ser ficheros

Ten encuenta que puedes montar ficheros como volÃºmenes. Por ejemplo, pueden inyectar un archivo de configuraciÃ³n asÃ­:

```sh
# copia el archivo del contenedor
docker run --rm httpd cat /usr/local/apache2/conf/httpd.conf > httpd.conf

# edita el archivo
vim httpd.conf

# inicia el contenedor con la configuracion modificada
docker run --rm -it -v "$PWD/httpd.conf:/usr/local/apache2/conf/httpd.conf:ro" -p "80:80" httpd
```

## ContribuciÃ³n

AquÃ­ tienes como contribuÃ­r a esta chuleta.

### Open README.md

hack click en el [README.md](https://github.com/wsargent/docker-cheat-sheet/blob/master/README.md) <-- este link

![Click](../images/click.png)

### Edit Page

![Edit](../images/edit.png)

### Make Changes and Commit

![Cambios](../images/change.png)

![Commit](../images/commit.png)


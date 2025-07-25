Este es un simulacro de los laboratorios que se implementarán en un futuro

# Reglas del repositorio

Este repositorio es para realizar pruebas de git y github, por lo que se ruega a los participantes a crear su propia rama y no hacer cambios en la rama main.

# Primeras Contribuciones

Leer artículos y ver tutoriales puede ayudar, pero, ¿Qué mejor manera de practicar que hacer las cosas en un entorno de prácticas? Este proyecto se enfoca en guiar a principiantes durante su primera contribución. Si quieres lograr tu primera contribución, sigue los pasos que se muestran a continuación.

#### *Si no estás familiarizado con la consola o terminal, [aquí hay tutoriales usando herramientas con Interfaz Gráfica (GUI)](#Tutoriales-con-otras-herramientas)*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork de este repositorio" />

Si no tienes git en tu equipo, puedes encontrar instrucciones para instalarlo en [este enlace]( https://docs.github.com/es/get-started/quickstart/set-up-git ).

## Bifurca (*Fork*) este repositorio

Haz un *fork* de este repositorio haciendo click en el botón "*Fork*" en la parte superior derecha en esta página.
Esto creará una copia de este repositorio en tu cuenta.

## Clona (*Clone*) el repositorio bifurcado

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clonar este repositorio" />

Ahora clona este repositorio en tu equipo. Dirígete a tu cuenta de GitHub, haz click en el botón "*clone or download*" y luego haz click en el icono para *copiar al portapapeles*.

Abre tu consola o terminal y ejecuta el siguiente comando de git:

```
git clone "url que acabas de copiar"
```

Donde pone "url que acabas de copiar" (sin las comillas dobles) es la *url* a este repositorio (tu *fork* a este proyecto). Mira los pasos previos para obtener la *url*.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copiar URL al portapapeles" />

Por ejemplo:
```
git clone https://github.com/este-eres-tu/first-contributions.git
```
La parte de `este-eres-tu` la reemplazarás con tu usuario de GitHub. Aquí estás copiando los contenidos del repositorio *first-contributions* de GitHub a tu equipo.

## Crea una rama (*Branch*)

Cambia al directorio del repositorio en tu equipo (si es que no estás ahí ya).

```
cd introduccion_test
```

Ahora crea una rama (*branch*) usando el comando `git branch` o `git checkout -b`:
```
git checkout -b <añade tu nombre>
```

Por ejemplo:
```
git checkout -b joel-dev
```

## Haz los cambios necesarios y confirma (*Commit*) esos cambios

Abre el archivo `Contributors.md` en un editor de texto y añade tu nombre. No lo añadas ni al principio ni al final del archivo, hazlo en cualquier otro sitio. Guarda el archivo.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Si vas al directorio del proyecto y ejecutas el comando  `git status`, verás que hay cambios.

Agrega esos cambios a la rama (*branch*) que creaste anteriormente usando el comando `git add`:

```
git add Contributors.md
```

Ahora haz un *commit* sobre estos cambios ejecutando el comando `git commit`:
```
git commit -m "Add <tu-nombre> to Contributors list"
```
cambiando `<tu-nombre>` por tu nombre.

## Sube (*Push*) tus cambios a GitHub

Haz *push* de tus cambios usando el comando `git push`:
```
git push -u origin <añade-el-nombre-de-la-rama>
```
Reemplaza `<añade-el-nombre-de-la-rama>` con el nombre de la rama que creaste anteriormente.

## Envía (*Submit*) tus cambios para ser revisados

Si vas a tu repositorio en GitHub, verás un botón `Compare & pull request`. Haz click sobre el botón.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="crea una pull request" />

Ahora envía la *pull request*.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="enviar la pull request" />

Pronto estaré fusionando tus cambios (haciendo *merge*) con la rama master de este proyecto. Recibirás una notificación por correo electrónico cuando los cambios hayan sido fusionados.

## ¿Cuáles son los siguientes pasos?

¡Enhorabuena! ¡Has completado el flujo de trabajo *_fork -> clone -> edit -> PR_* que encontrarás habitualmente como contribuidor!

Celebra tu contribución y compártela con tus amigos

Creditos totales para el repo de first-contributtions:
https://github.com/firstcontributions/first-contributions
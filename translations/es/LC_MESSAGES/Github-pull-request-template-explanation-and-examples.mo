��    U      �  q   l      0     1  #   3     W     p     �     �  +   �  9   �  #        5     O  +   `     �     �     �     �     �     �  	    	     
	  	   	     #	  [   2	  K   �	  C   �	  �   
  \   �
       +     $   0     U     k     }     �  !   �     �  @   �  7   #  �   [  �   �  E   �  e   �     Z  �   z  �   s  9     8   U  `   �  1   �     !  n   *     �  2   �  (   �  4     k   8  f   �  X     �   d  ;   �  4   ;  �   p  s   D  |   �  �   5  �  �  >   �  h   �  �   a    a  {   g  t   �  i   X  +   �  �   �  i   w  Z   �  �   <  ?   �  K   0  :   |  8   �     �  M  �  l  B!     �"  8   �"  2   �"     #  %   -#  &   S#  ?   z#  K   �#  3   $  $   :$     _$  =   t$     �$     �$     �$      %     %     4%  	   J%     T%  	   n%     x%  y   �%  i   &  ]   v&  �   �&  �   �'     (  :   (  5   H(     ~(     �(     �(     �(  $   �(  (   )  U   +)  4   �)  �   �)  �   =*  U   "+  Y   x+     �+  D  �+  �   0-  N   .  L   a.  t   �.  I   #/     m/  u   v/     �/  C   �/  1   =0  8   o0  �   �0  �   71  V   �1  �   2  8   �2  ?   3    L3  �   _4  �   �4  �   �5  '  B6  H   j8  ~   �8    29  �   ::  �   5;  �   �;  n   u<  A   �<  �   &=     �=  j   B>  �   �>  F   �?  S   �?  :   3@  8   n@     �@  J  �@           B       T      *   F   6   0         U      L                	   +       8   C   5                  -   /          @           K   %          G   &               7   S   <      3       9   "             D                   :   I   ,   #   2   P      O   >                  Q       =   '       (           R       $   J   M              !   
   4          A      E       H   ;   N   ?             )      1   .         # Creating PR's on the NVDA project ## Code Review Checklist ## The template ### Change log entry ### Change log entry: ### Context sensitive help for GUI changes. ### Description of how this pull request fixes the issue: ### Known issues with pull request: ### Link to issue number: ### Manual tests ### Pull Request description is up to date. ### Summary of the issue: ### System tests ### Testing performed: ### Unit tests ### User Documentation * Bug fixes * Changes * New features *Changes* *New features* - Have you considered possible regressions (related features or behaviours that may break)? - Have you ensured testing coverage across all supported operating systems? - How have you tested to ensure that your change works as intended? - If a complicated document is required to test with a 3rd party application, consider attaching it to the PR for others to test with. - If many NVDA settings are required, consider attaching a sample `nvda.ini` file to the PR. > >   - "speak typed characters" is unchecked >   - "speak typed words" is checked > - Keyboard category > 1. Open notepad > 2. Type "hello" > 3. Press space > Expect "hello" to be announced. > In NVDA settings ensure that: A lead developer will update file when merging the pull request. A quick summary of the problem you are trying to solve. After reviewing the checklist the reviewer and author need to use their best judgement on whether they think further changes need to be made. An entry intended to explain changes in NVDA to end users. Your proposed entry will be added to the `changes.t2t` file which is converted to html and used as a whats changed / change log document. Any comments on this can be put under the "testing strategy" heading. Are there any known issues or downsides of this approach. For instance: _Will not work with python 3_ As a reviewer please review it. At the start of the template there is a HTML comment block (starting with `<!--`), which points to this wiki page, it can be left in place and will not appear once the issue is saved. Feel free to delete it, i.e. all text up to and including `-->`. Because the `changes.t2t` file is prone to conflicts, we ask contributors not to edit the file directly, but instead add the entry to the bottom of the PR description. Can the changed code be covered by automated system tests Can the changed code be covered by automated unit tests? Code must be reviewed (via a Pull Request on GitHub) before it can be accepted into the project. Double check that the PR description is accurate. Example: For examples see the [changes.t2t file](https://github.com/nvaccess/nvda/blob/master/user_docs/en/changes.t2t) For instance: Has an appropriate change log entry been supplied. Has the user documentation been updated? Hopefully it helps to prevent items being forgotten. However, in the future, developers may need to come to the PR in search of an explanation for the approach. If the change adds a new GUI option, ensure that the context sensitive help assignment has been added. If the reviewer reaches the same conclusion as the author, no further work is necessary. In some cases, a change will need to be tested by alpha testers and should be described under the "testing strategy" heading of the Pull Request template. Is the described manual testing appropriate for the change? More broadly, try to answer the following questions: Most items in the checklist have a section in the PR template where you can add your thoughts, doing so may preempt questions from the reviewer ensuring you are on the same page, and speed up the review process. Multiple issue numbers can be included, separated by comma. If there is no issue number, you can use the PR number. Not all items will be applicable for all situations, in this case checking the item lets reviewers know its been considered. Note that Github [allows you to automatically close issues using keywords](https://help.github.com/en/articles/closing-issues-using-keywords). For example,  Often in face to face development it's useful to demonstrate a change, quite often bugs are noticed at this point when the new person asks for some variation in testing approach. Since we unlikely to be able to demonstrate a feature in an interactive way, an easy to follow list of steps for a "demo" allows others check themselves without having to work out all the details. It also serves as a starting point for members of the community who are testing the changes that go into NVDA. Often the approach taken can change during the review process. Outline the steps you took to test the change. This should allow someone else to reproduce your testing. Please include a quick discussion of how this change addresses the issue. Please also include any links or external information you may have used in order to address the issue. This helps others to have the same background as you and learn from this work. Please include the issue number here, including information on how this pull request is related to it. This helps us to keep the information linked together. If this is a minor/trivial change an issue does not need to be created. If in doubt, please create one. Please use this section as an opportunity to try to convince us (and yourself) that your proposed change should be merged.  Reviewers are invited to start a conversation about items in the list, to provide guidance on how to improve the PR. See ([`user_docs/en/changes.t2t`](https://github.com/nvaccess/nvda/blob/master/user_docs/en/changes.t2t)) System tests are end to end tests? of NVDA. The Pull Request template (``.github/PULL_REQUEST_TEMPLATE.md``) asks authors (and reviewers) to consider several aspects of the change. The aim of this checklist is to ensure each item has been considered by both the author and the reviewer. These descriptions should be in the format: `"{Description of change}. (#{issue number})"` This page is meant to serve as an explanation for how to fill out [our Github pull request template](https://github.com/nvaccess/nvda/blob/master/.github/PULL_REQUEST_TEMPLATE.md) This should describe in detail the cases checked by the author. You may suggest descriptions for multiple sections. The usual sections are: `Added a command to announce useful thing. (#WXYZ, #ABCD)` `Old command, now also uses new useful command. (#WXYZ)` ``` when writing `closes #7777` or `fixes #4242` in the body of the description, the mentioned issue will automatically be closed when the pull request is merged into the master branch. If your pull request is filed against another branch, such as beta, the particular issue will have to be close manually after merging the pull request. Project-Id-Version: 
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2021-02-23 17:17+0100
Last-Translator: José Manuel Delicado <jmdaweb@hotmail.com>
Language-Team: 
Language: es
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.4.2
Plural-Forms: nplurals=2; plural=(n != 1);
   # Creación de solicitudes de cambio en el proyecto NVDA ## Lista de comprobación de revisión del código ## La plantilla ### Entrada en el registro de cambios ### Entrada en el registro de cambios: ### Ayuda sensible al contexto en cambios de interfaz gráfica. ### Descripción de cómo resuelve la incidencia esta solicitud de cambios: ### Problemas conocidos con la solicitud de cambio: ### Enlace al número de incidencia: ### Pruebas manuales ### La descripción de la solicitud de cambios está al día. ### Resumen de la incidencia: ### Pruebas del sistema ### Pruebas realizadas: ### Pruebas unitarias ### Documentación de usuario * Fallos solucionados * Cambios * Nuevas características *Cambios* *Nuevas características* - ¿Te has planteado que pueda haber posibles regresiones (funciones o comportamientos relacionados que puedan romperse)? - ¿Te has asegurado de que hay una extensa cobertura de pruebas a través de varios sistemas operativos? - ¿Cómo has hecho las pruebas para asegurarte de que tus cambios funcionan como se esperan? - Si se necesita un documento complicado para hacer pruebas con una aplicación de terceros, plantéate adjuntarlo a la solicitud de cambios para que otros hagan pruebas también. - Si es necesario modificar muchos ajustes de NVDA, plantéate adjuntar un archivo `nvda.ini` de muestra a la solicitud de cambio. > >   - "Verbalizar caracteres al escribir" está desmarcada >   - "Verbalizar palabras al escribir" está marcada > - En la categoría teclado > 1. Abre el bloc de notas > 2. Escribe "hola" > 3. Pulsa espacio > Se espera que se verbalice "hola". > En las opciones de NVDA comprueba que: Un desarrollador principal actualizará el archivo al mezclar la solicitud de cambio. Un breve resumen del problema que intentas resolver. Tras revisar la lista de comprobación, el revisor y el autor deben razonar al máximo si piensan que es necesario hacer más cambios. Una entrada destinada a explicar los cambios en NVDA a los usuarios finales. La entrada que propongas se añadirá al archivo `changes.t2t`, que se convierte a HTML y se utiliza como documento de novedades / registro de cambios. Cualquier comentario sobre esto se puede poner bajo el encabezado "testing strategy". ¿Hay problemas o desventajas con este enfoque? Por ejemplo: _No funcionará en Python 3_ Como revisor, revísalo. Al principio de la plantilla hay un bloque de comentarios en HTML (que comienza con `<!--`), que apunta a la versión inglesa de esta página en la wiki, se puede dejar donde está y no aparecerá cuando se guarde la incidencia. Puedes eliminarlo sin problema, borrando todo el texto desde el principio hasta `-->` incluido. Ya que el archivo `changes.t2t` tiende a provocar conflictos, se pide a los colaboradores que no lo editen directamente, y que en su lugar añadan la entrada en la parte inferior de la descripción de la solicitud de cambios. ¿Se puede cubrir el código modificado con pruebas automatizadas del sistema? ¿Se puede cubrir el código modificado con pruebas unitarias automatizadas? El código debe revisarse (mediante una solicitud de cambios en GitHub) antes de que pueda aceptarse en el proyecto. Comprueba bien que la descripción de la solicitud de cambios es precisa. Ejemplo: Por ejemplo, consulta el [archivo changes.t2t](https://github.com/nvaccess/nvda/blob/master/user_docs/en/changes.t2t) Por ejemplo: Se ha proporcionado una entrada adecuada en el registro de cambios. ¿Se ha actualizado la documentación de usuario? Con suerte, ayuda a que no se olviden algunos elementos. Sin embargo, en el futuro, los desarrolladores pueden necesitar volver a la solicitud de cambios en búsqueda de una explicación del enfoque. Si el cambio añade una nueva opción a la interfaz gráfica, asegúrate de que se ha añadido una asignación a la ayuda sensible al contexto. Si el revisor alcanza la misma conclusión que el autor, no es necesario más trabajo. En algunos casos, los evaluadores alpha tendrán que probar el cambio, por lo que hay que describirlo bajo el encabezado "testing strategy" de la plantilla de solicitud de cambios. ¿Es apropiada para el cambio la prueba manual descrita? Vayamos más allá, intenta responder las siguientes preguntas: La mayoría de elementos de la lista de comprobación disponen de una sección en la plantilla de solicitud de cambio donde puedes añadir tus impresiones. Al hacerlo, puedes evitar ciertas preguntas del revisor, y esto asegura que habláis de lo mismo y agiliza el proceso. Se pueden incluir varios números de incidencia separados por comas. Si no hay número de incidencia, puedes usar el número de la solicitud de cambio. No todos los elementos son aplicables a todas las situaciones. En este caso, comprobar el elemento hace saber a los revisores que se ha tenido en cuenta. Ten en cuenta que Github [permite cerrar incidencias automáticamente mediante palabras clave](https://help.github.com/en/articles/closing-issues-using-keywords). Por ejemplo,  A menudo es útil en el desarrollo cara a cara demostrar un cambio, bastantes fallos se descubren en ese momento cuando la otra persona pide una variación en el enfoque de las pruebas. Ya que es bastante improbable que se pueda demostrar una función de manera interactiva, una lista de pasos fácil de seguir para una "demo" permite que otros puedan hacer comprobaciones por sí mismos sin tener que entrar en demasiados detalles. También sirve como punto de partida para los miembros de la comunidad que prueban los cambios que van dentro de NVDA. A veces el enfoque tomado puede cambiar durante el proceso de revisión. Describe los pasos que seguiste para probar tus cambios. Esto debería permitir que alguien más pueda reproducir tus pruebas. Incluye una breve exposición indicando cómo resuelve la incidencia este cambio. Incluye también cualquier enlace o información externa que hayas usado para solucionar el problema. Esto ayuda a que otros tengan la misma base que tú y aprendan de este trabajo. Por favor, incluye aquí el número de la incidencia. Esto ayuda a los desarrolladores a mantener la información relacionada entre sí junta. Si se trata de un cambio menor o trivial, no es necesario crear una incidencia. En caso de dudas, crea una. Emplea esta sección como una oportunidad para intentar convencer a los desarrolladores (y a ti mismo) de que debería mezclarse el cambio que has propuesto.  Se invita a los revisores a que inicien una conversación sobre los elementos de la lista, para proporcionar guiado sobre cómo mejorar la solicitud de cambios. Consulta ([`user_docs/en/changes.t2t`](https://github.com/nvaccess/nvda/blob/master/user_docs/en/changes.t2t)) Las pruebas del sistema son pruebas de extremo a extremo de NVDA. La plantilla de solicitud de cambios (``.github/PULL_REQUEST_TEMPLATE.md``) solicita a los autores (y revisores) que consideren varios aspectos del cambio. El propósito de esta lista de comprobación es asegurar que tanto el autor como el revisor han tenido en cuenta cada elemento. Estas descripciones deberían seguir el formato: `"{Descripción del cambio}. (#{número de incidencia})"` Esta página está creada con la intención de servir como explicación para rellenar [la plantilla de solicitud de cambios de NVDA en GitHub (en inglés)](https://github.com/nvaccess/nvda/blob/master/.github/PULL_REQUEST_TEMPLATE.md) Se deberían describir con detalle los casos comprobados por el autor. Puedes sugerir descripciones para varias secciones. Las secciones más comunes son: `Added a command to announce useful thing. (#WXYZ, #ABCD)` `Old command, now also uses new useful command. (#WXYZ)` ``` si escribes `closes #7777` o `fixes #4242` en el cuerpo de la descripción, la incidencia mencionada se cerrará automáticamente al mezclar la solicitud de cambio en la rama master. Si tu solicitud de cambio se archiva en otra rama, como por ejemplo beta, habrá que cerrar la incidencia manualmente tras mezclar dicha solicitud. 
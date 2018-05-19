��    *      l  ;   �      �     �  &   �     �               ,     <      J     k     �     �     �  �   �  6   U  6   �  7   �  4   �  8   0  �   i  x   �  F  g    �	  �   �
  �  Z  �   7     �  �   �    �    �  V  �      �    �  �    �  "  �  %  �  �  �   $   x"  �   �"  u  N#  �   �$  �  �%     +'  7   G'     '     �'     �'     �'     �'  (   �'  &   (  (   :(  !   c(  "   �(  �   �(  K   1)  R   })  L   �)  L   *  9   j*  �   �*  �   -+  �  �+  z  �.  �   �/  e  �0  �   (3     �3    �3  <  �4  Y  86  �  �7  �  $:    �<  �  ?  �  A  �  �D  �  �G  �  #K  6   #M  �   ZM  �  N  �   �O           *                               	               
          %              !          #   )   (                 '       &                                             $      "                          	if something == False: #code # NVDA Add-on internals: Golden Cursor ## Add-on mechanics ## Conclusion ## Golden Cursor: A History ## Introduction ## References ## Screen coordinates on Windows * 0: Move mouse to the right. * 1: Move mouse to the left. * 2: Move mouse down. * 3: Move mouse up. * GetCursorPos (user32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms648390(v=vs.85).aspx * Mouse moving down: new Y = current Y + movement unit * Mouse moving left: new X = current X - movement unit * Mouse moving right: new X = currnet X + movement unit * Mouse moving up: new Y = current Y - movement unit * Pixel (Wikipedia): https://en.wikipedia.org/wiki/Pixel * SetCursorPos (user32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms648394(v=vs.85).aspx 1. Obtains the current mouse location by calling GetCursorPos function, which returns current X and Y mouse coordinates. 2. Calculates the new mouse location based on direction given and movement unit (movement unit can range from 1 to 100 pixels; a pixel (picture element) is a very small square on displays used to hold display output, such as color, intensity and others, and displays ship with millions of pixels). For example, if Control=Windows+right arrow is pressed, since we're moving to the right, new X coordinate will be current X coordinate plus the movement unit. Similarly, if Contorl+Windows+left arrow is pressed, the new X coordinate will be current coordinate minus the movement unit. 3. If mouse restriction is set (that is, if a mouse is told to stay at the current application), the new locatin will be somewhere inside the restircted application, otherwise mouse will move. Then SetCursorPos function is claled to plce the mouse on the new location. 4. The add-on also includes ability to announce mouse coordinates, and if this is true, new coordinate (at least the new X or Y coordinate) will be announced. A graphical user interface isn't complete without means of moving around the screen and interacting with various elements. For years, a computer mouse was a handy tool for working with graphical elements, with touchscreens and mixed reality replacing functions of the mouse for some people. Even with the introduction of the mouse in the 1970's and move towards touch interaction in the 21st century, one input device has stil remained king of computer interaction: keyboards. Although the add-on had potential, it had numerous coding problems. for example, in early drafts, it used Python's boolean statements like this: Author: Joseph Lee Besides mouse movement commands, the add-on comes with two option flags to announce new mouse coordinate in pixels and to restrict mouse movement to the currently using app. Copyright notice: NVDA is copyright 2006-2018 NV Access Limited. Golden Cursor add-on is copyright 2015-2018 Salah Atair, Wafeeq Taher, Joseph Lee and contributors. Microsoft Windows, Windows API and related technologies are copyright Microsoft Corporation. Eventually some serious issues were resolved, and after working closely with the original add-on developer, Golden Cursor was submitted to the add-ons website for community testing, wihch resulted in positive feedback. Thus in January 2016, Golden Cursor became an official NVDA add-on. For many blind people, the concept of using a mouse (or touch interaction) may sound foreign, especially for people used to textual interfaces. For some people, using the mouse as a blind person was only a dream. Recent advancements in screen reading has bridged the gap somewhat, although there are areas that still need work, including describing cursor colors, more accuracy in mouse cursor shape announcement and so on, as well as ability to move the mouse with a keyboard. Fortunately, the last advancement is now a reality thanks to an add-on we'll be examining in this aricle: Golden Cursor. For people familiar with mathematical representation of a 2D graph or a plane, the ideal starting point (or origin) would be center, or for computer monitors, bottom left. However, on Windows, the starting point is top left. For example, on a 1920 by 1080 pixel display, the top left is (0, 0), and top right is (1920, 0). Using this logic, we can see that bottom left is (0, 1080), and bottom right is (1920, 1080). Note that you need to subtract one from the maximum, so the coordinate for the bottom right corner becomes (1919, 1079). In 2017, I (Joseph Lee) announced an initiative to modernize community add-ons by making them work well under Python 3, and naturally Golden Cursor was one of those add-ons that needed modernization. The problem was that the community lost contact with the original developers of this add-on, thus I volunteered to modernize this add-on. Thus the below notes are based on old add-on releases, as well as results of modernization work done in early 2018. It is said that the simple something is, the better. The Golden Cursor add-on fits this definition perfectly: a simple add-on that is surprisingly powerful and useful. The ability to use the keyboard to move the mouse has been a dream for many, and now, thanks to this add-on, it has become a reality. Time will tell how this add-on will evolve to meet people's needs, and some useful ideas are already being planned by the community. Mouse coordinate tag and jumping to a specific coordinate is a variation of the above mechanism. When one wishes to move mouse to another location, one can invoke mouse jump dialog and type the new coordinate (x, then comma, then y value). Similarly, when one wishes to mark a mouse locatoin with a tag, one can move th mouse to the desired location and open positions dilaog, give it a label nad press Enter, with the tag saved to an ini file named for the app name with the file extension of .gc (for example, outlook.gc for mouse tags for Microsoft Outlook). Then one can invoke positions list dialog, select a tag, and press Enter to move the mouse to the tagged location, with the positoins list dilaog also providing means to rename, delete or clear the tag for the application. Simply put, the add-on serves as a "keyboard wheel" for a computer mouse. This is made more intuitive by the fact that Windows+NvDA+arrow keys (or just arrow keys with mouse arrows layer turned on) were assigned to move the mouse. In addition, hotspot functionality is available where a mouse coordinate (xy) is tagged with a label and jumped to, as well as giving users ability to move to a specific mouse coordinate location. The coordinate tag is then stored in a file that looks like a typical ini file, allowing easy sharing between systems. Simply speaking, Golden Cursor is an add-on that allows NVDA users to manipulate the mouse via keyboard. Although Windows does have mouse keys, a keyboard with a physical numpad is required to take full advantage of this. On the other hand, Golden Cursor does not require a physical numpad, thus making it a bit more universal. Even though the add-on has seen little development activity, it is still an interesting add-on to study, as it showcases the enthusiasm the NVDA community has shown for this add-on, and a chance for the author of this article to improve the add-on and present its inner workings. In "NVDA Add-on Internals: Golden Cursor", we'll learn the history behind this add-on, recent developments, and dive into how this add-on improves mouse usability for blind people around the world. The "wheel" is actually a call to SetCursorPos Windows API function, wrapped inside winUser module (as winUser module wraps user32.dll), ultimately controlled by moveMouse method in the add-on. The moveMouse method takes the mouse direction flag, and based on cursor location, direction given and mouse restriction flag, positions the mouse cursor on the new location. The direction flags are: The moveMouse routine is as follows: To download this add-on, visit https://addons.nvda-project.org/addons/goldenCursor.en.html. The source code repository can be found at https://github.com/josephsl/goldenCursor. Towards end of 2015, an Arabic-speaking NVDA translator contacted NVDA add-ons team and introduced the community to an add-on a friend of the translator was developing. Called "Golden Cursor", the add-on came with keyboard commands to manipulate the mouse. Since the community has shown interest in this add-on, I decided to contact the devleoper and review the new add-on. When we apply this to mouse movement, the X coordinate increases when the mouse moves to the right, while the Y coordinate decreases as the mouse moves up. For sake of completeness, mouse movement expressions are: Project-Id-Version: 
POT-Creation-Date: 2018-05-19 13:10+Hora de verano romance
PO-Revision-Date: 2018-05-19 13:15+0200
Last-Translator: José Manuel Delicado <jmdaweb@hotmail.com>
Language-Team: 
Language: es
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.0.7
Plural-Forms: nplurals=2; plural=(n != 1);
 	if algo == False: #código # Complementos de NVDA vistos por dentro: Golden Cursor ## Mecanismos del complemento ## Conclusión ## Golden Cursor: la historia ## Introducción ## Referencias ## Coordenadas de la pantalla en Windows * 0: mueve el ratón hacia la derecha. * 1: mueve el ratón hacia la izquierda. * 2: mueve el ratón hacia abajo. * 3: mueve el ratón hacia arriba. * Referencia de GetCursorPos (user32.dll) (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms648390(v=vs.85).aspx * Se mueve el ratón hacia abajo: nueva y = y actual + unidad de movimiento * Se mueve el ratón hacia la izquierda: nueva x = x actual - unidad de movimiento * Se mueve el ratón a la derecha: nueva x = x actual + unidad de movimiento * Se mueve el ratón hacia arriba: nueva y = y actual - unidad de movimiento * Píxel (Wikipedia): https://en.wikipedia.org/wiki/Pixel * Referencia de SetCursorPos (user32.dll) (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms648394(v=vs.85).aspx 1. Se obtiene la ubicación actual del cursor llamando a la función GetCursorPos, que devuelve las coordenadas x e y del ratón. 2. Se calcula la nueva ubicación del ratón basada en la dirección dada y la unidad de movimiento (esta unidad tiene un rango que varía entre 1 y 100 píxeles; un píxel (del inglés picture element) es un cuadrado muy pequeño en los monitores usado para procesar la información saliente, como por ejemplo el color, intensidad y demás, y los monitores vienen con millones de píxeles). Por ejemplo, si pulsamos ctrl+windows+flecha derecha ya que nos movemos en esa dirección, la nueva coordenada x será la suma de la coordenada x actual y la unidad de movimiento. De manera similar, si pulsamos ctrl+windows+flecha izquierda, la nueva coordenada x será la resta de la coordenada x actual y la unidad de movimiento. 3. Si se establece una restricción del ratón (por ejemplo, si lo configuramos para que deba permanecer en la aplicación actual), la nueva ubicación estará en algún lugar dentro de la aplicación donde restringimos, en cualquier otro caso el ratón se moverá. A continuación, se llama a la función SetCursorPos para establecer en pantalla la nueva ubicación del ratón. 4. El complemento también incluye la posibilidad de verbalizar las nuevas coordenadas del ratón. Si esta característica está activada, se verbalizará al menos una coordenada (x o y) o ambas. Una interfaz gráfica de usuario no está completa si no da la posibilidad de moverse por la pantalla e interactuar con diversos elementos. Durante años, un ratón de ordenador ha sido una herramienta muy útil para trabajar con elementos gráficos, siendo algunas de sus funciones sustituidas para algunas personas por tecnologías tales como pantallas táctiles o realidad mixta. Incluso con la llegada del ratón en la década de los 70 y el movimiento hacia la interacción táctil en el siglo XXI, un dispositivo de entrada ha permanecido todavía como el rey de la interacción con ordenadores: el teclado. Aunque el complemento tenía potencial, padecía varios problemas de codificación. Por ejemplo, en sus versiones preliminares, usaba sentencias booleanas de Python como estas: Autor: Joseph Lee Además de las órdenes de movimiento del ratón, este complemento viene equipado con dos indicadores que permiten configurar si se verbalizan las nuevas coordenadas del ratón en píxeles, o si se restringe el movimiento del mismo a la aplicación utilizada actualmente. Aviso de derechos de copia: NVDA tiene copyright 2006-2018 por NV Access Limited. El complemento Golden Cursor tiene copyright 2015-2018 por Salah Atair, Wafeeq Taher, Joseph Lee y otros contribuyentes. Microsoft Windows, la api de Windows y otras tecnologías relacionadas tienen copyright de Microsoft Corporation. Eventualmente se resolvieron varias incidencias serias, y después de trabajar mano a mano con el desarrollador del complemento, se envió Golden Cursor a la web de complementos de la comunidad en fase de pruebas, recibiendo una retroalimentación muy positiva. Por tanto, en enero de 2016, Golden Cursor se convirtió en un complemento oficial. Para muchas personas ciegas, el concepto de usar un ratón (o interacción táctil) puede sonar extraño, especialmente para aquellas acostumbradas a interfaces basadas en texto. Para algunos, usar el ratón siendo ciegos era solamente un sueño. Los recientes avances en lectores de pantalla lo han posibilitado un poco, aunque hay áreas que todavía necesitan trabajo: descripción de los colores del cursor, más precisión en el anunciado de sus cambios de forma, así como la posibilidad de mover el ratón con un teclado. Por suerte, el último punto ya se ha hecho realidad gracias a un complemento que examinaremos en este artículo: Golden Cursor. Para la gente familiarizada con la representación matemática de un plano o un gráfico 2D, el punto de inicio ideal (también llamado origen) podría ser el centro, o para monitores de ordenador, la esquina inferior izquierda. Sin embargo, en Windows, el punto de inicio es la esquina superior izquierda. Por ejemplo, en una pantalla con una resolución de 1920x1080 píxeles, la esquina superior izquierda es (0,0), y la esquina superior derecha es (1920,0). Aplicando esta lógica, podemos ver que la esquina inferior izquierda es (0,1080) y la inferior derecha es (1920,1080). Ten en cuenta que es necesario restar una unidad del máximo, por lo que la coordenada de la esquina inferior derecha en realidad es (1919,1079). En 2017, yo (Joseph Lee) anuncié una iniciativa para modernizar los complementos de la comunidad haciéndolos compatibles con Python 3, y naturalmente Golden Cursor era uno de esos complementos que necesitaban modernizarse. El problema vino porque la comunidad perdió el contacto con los desarrolladores originales del complemento, así que me ofrecí voluntario para modernizarlo. Las notas que hay más abajo están basadas en las versiones antiguas del complemento, así como en los trabajos de modernización hechos a principios de 2018. Se suele decir que cuanto más simple es algo, mejor. El complemento Golden Cursor encaja en esta definición perfectamente: un complemento simple que a la vez es sorprendentemente potente y útil. La capacidad para usar el teclado para mover el ratón ha sido un sueño para muchos, y ahora, gracias a este complemento, se ha hecho realidad. El tiempo dirá como evolucionará este complemento para satisfacer las necesidades de la gente, ya se están planteando algunas buenas ideas en la comunidad. El etiquetado de coordenadas y el salto a coordenadas específicas son dos variantes del mecanismo explicado más arriba. Cuando se desea desplazar el ratón a otra ubicación, se puede invocar el diálogo de salto y escribir las nuevas coordenadas (valor de x, una coma, y luego el valor de y). De forma similar, si se desea marcar una ubicación del ratón con una etiqueta, se puede mover el ratón a la ubicación deseada y abrir el diálogo de posiciones, escribir una etiqueta y pulsar intro, guardando esta etiqueta en un fichero ini cuyo nombre es el nombre de la aplicación y la extensión .gc (por ejemplo, outlook.gc para etiquetas del ratón en Microsoft Outlook). A continuación, se puede invocar el diálogo de lista de posiciones, seleccionar una etiqueta, y pulsar intro para mover el ratón a la ubicación etiquetada, con el diálogo de lista de posiciones ofreciendo también opciones para renombrar, eliminar o limpiar las etiquetas para la aplicación. En términos generales, el complemento sirve como una "rueda en el teclado" para el ratón del ordenador. Esto se vuelve más intuitivo con el hecho de que las teclas que se asignan por defecto para mover el ratón son ctrl+windows+flechas (o simplemente flechas al activar la capa de flechas del ratón). Además, hay disponible una función de marcadores que permite etiquetar posiciones del ratón en pantalla (coordenadas x e y) y saltar a ellas, así como saltar simplemente a coordenadas introducidas manualmente. Las coordenadas etiquetadas se almacenan en un fichero que tiene el aspecto de cualquier fichero ini, y que puede compartirse fácilmente con otros usuarios y sistemas. A modo de resumen, Golden Cursor es un complemento que permite a los usuarios de NVDA manipular el ratón utilizando el teclado. Aunque Windows tiene la función de teclas del ratón, es imprescindible disponer de un teclado numérico para aprovechar al máximo esta característica. Por otra parte, Golden Cursor no necesita un teclado numérico físico, haciéndolo por tanto más universal. Incluso aunque el complemento ha tenido poca actividad de desarrollo últimamente, sigue siendo digno de estudio al ser un caso de éxito. La comunidad se ha mostrado entusiasmada con este complemento, y este artículo supone una oportunidad para su autor para mejorar el complemento y exponer los detalles internos de su trabajo. En este artículo conoceremos la historia que hay tras este complemento, los desarrollos recientes, y veremos cómo mejora la usabilidad del ratón para personas ciegas de todo el mundo. Realmente, la "rueda" es una llamada a la función de la api de Windows SetCursorPos, encapsulada dentro del módulo winUser (ya que winUser encapsula las funciones de user32.dll), y controlada en última instancia por el método moveMouse del complemento. El método moveMouse recibe un indicador con la dirección del ratón, y basándose en la posición actual del mismo, su dirección y el indicador de restricciones, posiciona el cursor del ratón en la nueva ubicación. Los indicadores de dirección son: El procedimiento para mover el ratón es el siguiente: Para descargar este complemento, visita la sección de complementos en el menú superior de nuestra web. Su código fuente se encuentra en https://github.com/josephsl/goldenCursor. Hacia finales de 2015, un traductor árabe contactó con el equipo de complementos de NVDA y presentó ante la comunidad un complemento que un amigo suyo estaba desarrollando. Llamado "Golden Cursor", el complemento vino con órdenes de teclado para manipular el ratón. Ya que la comunidad ha mostrado interés en este complemento, decidí contactar con el desarrollador y revisarlo. Cuando aplicamos esto al movimiento del ratón, la coordenada x se incrementa al mover el ratón a la derecha, mientras que la coordenada y disminuye cuando lo subimos hacia arriba. Para dar más completitud, las expresiones de movimiento del ratón son: 
# coding=utf-8
from django.utils.translation import ugettext as _

_TOPIC_CHOICES = (('', _(u'Selecciona una categoria')),
                  ('gobierno_digital_y_modernizacion_de_la_gestion_publica', _(u'Gobierno Digital y Modernización de la Gestión Pública')),
                  ('educacion_salud_seguridad_alimentaria_y_nutricional', _(u'Educación, Salud, Seguridad Alimentaria y Nutricional')),
                  ('gestion_publica_e_inclusion_social', _(u'Inclusión Social y Poblaciones en Condiciones de Vulnerabilidad')),
                  ('medio_ambiente_cambio_climatico_y_gestion_integral_para_la_reduccion_del_riesgo_a_desastres', _(
                      u'Medio Ambiente, Cambio Climático y Gestión Integral del Riesgo de Desastres')),
                  ('reduccion_de_la_pobreza_y_migracion', _(u'Reducción de la Pobreza y Migración')),
                  ('gestion_y_seguimiento_de_iniciativas_tratados_y_convenios_internacionales_en_materia_de_transparencia_anticorrupcion_y_rendicion_de_cuentas', _(
                      u'Gestión y seguimiento de Iniciativas, Tratados y Convenios Internacionales en Materia de Transparencia, Anticorrupción y Rendición de Cuentas')),
                  )

_TOPIC_DESCRIPTIONS = (
    ('gobierno_digital_y_modernizacion_de_la_gestion_publica', _(u'Para modernizar la gestión pública deben cambiar los fines y formas de funcionamiento de la institucionalidad pública para una mejora constante e innovadora. El Gobierno está obligado a desarrollar y hacer uso de nuevas tecnologías de información y comunicación para democratizar y descentralizar los servicios públicos, como base para la consolidación de gobiernos abiertos, garantizando el cumplimiento de los derechos humanos de la población.La inclusión del gobierno digital en el Plan de Acción Nacional de Gobierno Abierto, contribuirá a fortalecer el cumplimiento de los principios de transparencia, participación ciudadana, rendición de cuentas, innovación y tecnología, promoviendo la lucha contra la corrupción, la fiscalización y la auditoría social.Estos dos elementos, el Gobierno Digital y Modernización de la Gestión Pública, se complementan, comprendiendo a la ciudadanía como sujeto de derechos humanos y razón fundamental del aparato burocrático, por lo tanto, es necesario mejorar en la calidad del servicio prestado y formular nuevas formas de acercamiento y facilitando procesos, aprovechando el uso de la tecnología, la cual también genera datos que pueden ser utilizados en ejercicios de fiscalización y auditoría social de la gestión pública, haciendo observancia de la Política Nacional de Datos Abiertos y la Carta Internacional de Datos Abiertos.')),
    ('educacion_salud_seguridad_alimentaria_y_nutricional', _(u'Desde la Constitución Política de la República de Guatemala, en observancia de los derechos inherentes a la persona humana, se garantiza la educación y salud, de carácter universal, siendo elementos fundamentales para el desarrollo y en el marco de la pandemia del COVID-19, es fundamental innovar en la prestación de servicios públicos para atender en un corto plazo los efectos de la misma, además son fundamentales los ejercicios de fiscalización y auditoría social a los planes, programas y proyectos que implementan las instituciones rectoras en materia de salud, seguridad alimentaria y nutricional y educación, según las necesidades de la población, comprendiendo la diversidad de la misma y las necesidades particulares de las aquellas en condiciones vulnerabilidad. En el marco de la educación, se ha limitado su acceso debido a la brecha digital y a la coyuntura por el COVID-19, principalmente, niñez, adolescencia, juventudes, mujeres y personas en condiciones de vulnerabilidad, siendo imperante la implementación de acciones que coadyuven a evitar que se continúe con esta tendencia, con transparencia.El COVID-19 presenta un reto en el área de la salud y seguridad alimentaria y nutricional, siendo importante contener su expansión y promover su inoculación, además, implementar acciones que prevengan la desnutrición aguda y materno infantil, por lo tanto, el monitoreo y auditoría social de estas acciones es fundamental, tanto por la transparencia como por la calidad de los servicios prestados.')),
    ('gestion_publica_e_inclusion_social', _(u'El impulso de acciones orientadas a la materialización de los deberes del Estado requiere que los gobiernos implementen una serie de acciones públicas orientadas a garantizar el desarrollo social y garantizar los derechos humanos de la población. Los gobiernos deben realizar acciones orientadas a la universalización de la prestación de servicios públicos con la finalidad que toda la ciudadanía sea sujeto de la prestación de los mismos que implica la inclusión social a través del ejercicio de la función pública, para una verdadera garantía de los derechos humanos. La atención a las poblaciones en condiciones de vulnerabilidad a través del impulso de acciones gubernamentales y/o programas sociales como paliativo de la profundización de los problemas  que atraviesa el país es imperante para superar sus condiciones  actuales, requiriendo  de administraciones que acerquen cada vez más sus propuestas gubernamentales hacia las poblaciones menos atendidas, ampliando la cobertura de los servicios públicos y beneficios sociales en el marco de la transparencia en el ejercicio de la función pública y administración para el desarrollo. La inclusión social debe entenderse como acciones implementadas para asegurar el derecho al desarrollo de las poblaciones en condiciones de vulnerabilidad, en riesgo de pobreza y exclusión social, en el marco laboral, seguridad, educación, salud, seguridad alimentaria y nutricional, en su diversidad multiétnica, pluricultural y multilingüe, así como de género.')),
    ('medio_ambiente_cambio_climatico_y_gestion_integral_para_la_reduccion_del_riesgo_a_desastres', _(u'Este eje contempla la alteración al medio ambiente y cambio climático como una de las vulnerabilidades que provocan alto riesgo a desastres en el país. La vulnerabilidad ambiental se define como la pérdida de la convivencia armónica del ser humano con la naturaleza por factores socio-culturales, económico-productivos y ambientales. Engloba lo concerniente a: prevención, protección, conservación, mitigación y mejoramiento del ambiente y los recursos naturales, como políticas, acciones y presupuestos gubernamentales con participación multisectorial. Desde esta temática se busca obtener acciones públicas orientadas al derecho humano a un ambiente saludable y ecológicamente equilibrado para la generación de un desarrollo sostenible, en todos los niveles de la gestión pública. Al realizar estas acciones existe un aporte sustancial a reducir el riesgo ante desastres  y con esto, resguardar la seguridad de la persona como un deber del Estado y aportar al desarrollo sustentable del país. ')),
    ('reduccion_de_la_pobreza_y_migracion', _(u'Derivado a factores principalmente de origen económico y sus efectos sociales, los Estados como el guatemalteco afrontan una serie de problemas públicos que deben ser atendidos por parte de los gobiernos, ya que sus efectos producen la emigración de sus habitantes hacia otros territorios en búsqueda de mejores condiciones de vida y desarrollo social, que no han sido garantizadas en sus países de origen. La migración es un derecho humano, no obstante, la migración irregular, produce efectos económicos y sociales en países receptores y de tránsito, volviéndose una problemática humanitaria. Esta situación ha obligado a los Estados a buscar alternativas que permitan reducir la pobreza y desigualdad en los países de origen, implementar acciones humanitarias en los países de tránsito y países receptores para garantizar la vida e integridad de las personas migrantes. La pobreza es un efecto de la creciente desigualdad social sobre la cual los gobiernos deben ejecutar acciones públicas sostenibles, orientadas a minimizar la brecha social, mejorar la calidad de vida de la población, promover empleos dignos con inclusión laboral y monitorear la inversión pública en materia de migración.')),
    ('gestion_y_seguimiento_de_iniciativas_tratados_y_convenios_internacionales_en_materia_de_transparencia_anticorrupcion_y_rendicion_de_cuentas', _(u'Guatemala desde el año 2010 se adhirió de forma voluntaria a diversas iniciativas internacionales que promueven la transparencia, la rendición de cuentas, el libre acceso a la información pública, la participación ciudadana, y el combate a la corrupción, entre las cuales actualmente funciona: La Alianza para el Gobierno Abierto(OGP), Iniciativa Global para la Transparencia Fiscal(GIFT), Iniciativa de Transparencia en Industrias Extractivas(EITI), Iniciativa de Transparencia en Infraestructura(CoST), entre otras. Asimismo, el Estado de Guatemala forma parte de los Mecanismos de Examen de las convenciones internacionales en materia de transparencia y mecanismos contra la corrupción, entre las cuales están: la Convención Interamericana contra la Corrupción y la Convención de Naciones Unidas contra la Corrupción (CNUCC - de Naciones Unidas), y el Mecanismo de Seguimiento de la Implementación de la Convención Interamericana contra la Corrupción(MESICIC de la OEA), entre otras. Estas iniciativas tienen como objetivo realizar recomendaciones y generar herramientas para que los Estados, sus gobiernos locales y la iniciativa privada, mejoren en materia de transparencia y anticorrupción, rendición de cuentas, acceso a la información pública, modernización de la gestión pública, sus marcos jurídicos, calidad en la ejecución del gasto público, compras y contrataciones, la participación de la sociedad civil en el combate contra la corrupción, la tipificación de actos de corrupción tales como el soborno trasnacional y el enriquecimiento ilícito, la protección a quienes los denuncien y la asistencia a los órganos de control superior encargados de prevenir, detectar, investigar y sancionar dichos actos. En ese sentido, es sumamente importante que existan entidades que realicen el monitoreo y seguimiento constante de los principios, prácticas, recomendaciones, acciones propias de cada iniciativa, tratado o convención, para llevar a cabo por parte de la institucionalidad pública, la implementación gradual, en función de la viabilidad legal, técnica, financiera o de cualquier otra naturaleza, de las acciones y procedimientos que se consideren necesarios para cumplir satisfactoriamente cada uno de los estándares y buenas prácticas que permitan alcanzar el fin último del Estado, que lo constituye el bienestar común y mejora continua la calidad de vida de los guatemaltecos.'))
)

import streamlit as st
st.title("Polarización de la luz")
st.write("La polarización es una propiedad de la luz, que describe la geometría interna de una fuente de radiación")
st.subheader("La luz:")
col1, col2, col3 = st.beta_columns([1,6,1])
with col2:
   st.markdown("![Alt Text](http://www.juliohernandezfotografia.cl/wp-content/uploads/2015/10/luz-polarizador.gif)")
st.write("La luz son ondas electromagneticas, visible al ojo humano,estas ondas vibran en diferentes direcciones perpendiculares en forma de propagación hasta que estas son sometidas a la polarizacion")
st.subheader("Luz polarizada:")
st.write("las ondas de luz vibran en un solo plano, esto se produce gracias a la ayuda de un polarizador")
col1, col2, col3 = st.beta_columns([1,6,1])
with col2:
st.markdown("![Alt Text](https://www.baumer.com/medias/sys_master/images-content/images-content/h98/hae/8940792119326/Grafik-Polarisation-2-EN.gif)")
st.subheader("Polarizador:")
col1, col2, col3 = st.beta_columns([1,6,1])
with col2:
st.image("https://w7.pngwing.com/pngs/939/208/png-transparent-polarized-light-polarimeter-optical-rotation-density-matrix-bulbs-angle-experiment-light.png")
st.write ("Los polarizdores son materiales que transmiten de forma selectiva las ondas electromagneticas de la luz, restringiendo las ondas a una sola direccion de propagacion bloqueando el resto de planos de polarizacion")
botones_vector = ['Lineal','Circular','Elíptica']
vectores = st.radio ('Tipo de polarizacion',botones_vector)
if vectores == 'Lineal':
     st.write("El vector E traza sobre el plano perpendicular a la dirección de propagación una linea recta.")
if vectores == 'Circular':
    st.write('Componentes de E misma magnitud, pero una diferencia de fase, puede verse girando a la izquierda o hacia la derecha.')
if vectores == 'Elíptica':
    st.write('Componentes de E son diferentes, abarca cualquier diferencia de magnitud de fase de Ex y Ey, es el estado de polarización más general.') 

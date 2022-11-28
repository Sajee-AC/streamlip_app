
import streamlit
import snowflake.connector
import pandas



streamlit.title('Air Canada Webpage')



streamlit.header('Missing Roles')

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

#my_cur = my_cnx.cursor()

#my_cur.execute("SELECT * FROM SANDBOX.USR_SAJEEVAN_PARAMSOTHY.ROLES_WITH_INVALID_NAMING")
#myresult = my_cur.fetchall()




#streamlit.dataframe(myresult)




#streamlit.header('Check out our Roles:')
#my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.OUR_ROLES")
#myresult = my_cur.fetchall()
#streamlit.multiselect("Pick a user: ", list(my_cur.index))
#streamlit.dataframe(myresult)

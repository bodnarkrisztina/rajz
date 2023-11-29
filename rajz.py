### Usage
```python
import plotly.express as px
import streamlit as st

from streamlit_plotly_events import plotly_events

# Writes a component similar to st.write()
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)

# Can write inside of things using with!
with st.beta_expander('Plot'):
with st.expander('Plot'):
    fig = px.line(x=[1], y=[1])
    selected_points = plotly_events(fig)

@@ -36,7 +38,7 @@ Returns
list of dict
    List of dictionaries containing point details (in case multiple overlapping points have been clicked).
    Details can be found here: 
    Details can be found here:
        https://plotly.com/javascript/plotlyjs-events/#event-data
    Format of dict:

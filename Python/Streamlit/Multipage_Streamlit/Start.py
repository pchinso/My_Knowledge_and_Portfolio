import streamlit as st
import streamlit_extras

from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Main",
    page_icon="🏁",
)

st.markdown("# This is the main Page! 🏁")

st.sidebar.success("List of pages:")

st.markdown(
    """
# Sport

## Gym Plan Week 

|  To Do   | Monday |  Tuesday  | Wednesday | Thursday  | Friday | Saturday | Sunday |
|:--------:|:------:|:---------:|:---------:|:---------:|:------:|:--------:|:------:|
|   WOD    |        |   🏋️‍♂️   |           |   🏋️‍♂️   |        |  🏋️‍♂️   |        |
|   Swim   | 🏊‍♀️  |           |   🏊‍♀️   |           | 🏊‍♀️  |  🏊‍♀️   |        |
|   Bike   | 🚴‍♂️  |           |   🚴‍♂️   |           | 🚴‍♂️  |  🚴‍♂️   | 🚴‍♂️  |
| Kid Swim |        | 🏊‍♀️👼👼 |           | 🏊‍♀️👼👼 |        |          |        |

- [ ] Gym
	- [ ] WOD
	- [ ] Other
- [ ] Bike 
	- [ ] Commute
	- [ ] Train
- [ ] Run
	- [ ] Outdoors
	- [ ] Indoors
- [ ] Swim 

"""
)
from motion_detector import df
from bokeh.plotting import figure,output_file,show
from bokeh.models import HoverTool,ColumnDataSource

df["Start_str"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")

df["End_str"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)
f=figure(width=1000,height=600,x_axis_type='datetime',title="Motion Graph")

hovertool=HoverTool(tooltips=[("Start","@Start_str"),("End","@End_str")])
f.add_tools(hovertool)
p=f.quad(left="Start",right="End",top=1,bottom=0,color="green",source=cds)

f.yaxis.minor_tick_line_color=None
#f.ygrid[0].ticker.desired_num_ticks=1
output_file("Graph.html")

show(f)

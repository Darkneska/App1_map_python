import pandas
import folium



data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[50.01287326163686, 16.68242205527992], zoom_start=10, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lat, lon, elev, name in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location=(lat, lon), radius=6, popup=str(elev) + " m", tooltip=str(name),
                                      fill_color=color_producer(elev), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'). read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")

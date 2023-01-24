import geocoder
import folium

ip = input("Enter the ip: ")
g = geocoder.ip(ip)

Address = g.latlng
print(Address)

my_map1 = folium.Map(location=Address,
                     zoom_start=12)

folium.CircleMarker(location=Address,
                    radius=50, popup="Found").add_to(my_map1)

folium.Marker(Address,
              popup="Found").add_to(my_map1)

my_map1.save("my_map.html")

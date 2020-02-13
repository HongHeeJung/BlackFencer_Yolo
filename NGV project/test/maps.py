import folium
import base64
import os
from math import radians, cos, sin, asin, sqrt
from datetime import datetime
from PIL import Image

class datamap():
	def __init__(self):
		pass

	def create_map(self):
		templist = os.listdir(os.getcwd()+"/temp/")
		loc_filename = ""
		for name in templist:
			if ".txt" in name:
				loc_filename = name
		print(loc_filename)
		loc_data = open("temp/"+loc_filename, 'r')
		print("loc data open success")
		detected_data = open("detection_result.txt", "r")
		print("detected data open success")

		detected_idx_list = list()
		try:
			for d in detected_data:
				detected_idx_list.append(int(d.replace('\n','').split('.')[0]))
		except:
			pass

		print(detected_idx_list)

		idx_list = list()
		loc_list = list()
		for l in loc_data:
			idx_list.append(l.replace('\n','').split(':')[0])
			loc_list.append(l.replace('\n','').split(':')[1].split(','))

		for index in detected_idx_list:
			try:
				m = folium.Map(location=[float(loc_list[index][0]), float(loc_list[index][1])],
								zoom_start=17)
				break
			except:
				continue

		markerList = list()
		skipFlag = 0
		for loc in detected_idx_list:
			try:
				if ((loc_list[loc][0] == "NaN") | (loc_list[loc][1] == "NaN")):
					continue
				loc_list[loc][0]
				for marker in markerList:
					distance = datamap.calcDistance(marker[1],marker[0],float(loc_list[loc][1]),float(loc_list[loc][0]))
					if distance < 6.0:
						skipFlag = 1
						break
				if skipFlag == 1:
					skipFlag = 0
					continue
				tooltip = loc_list[loc][0] + ',' + loc_list[loc][1]
				image_name = 'slice/' + str(loc) + '.jpg'
				image = Image.open(image_name).resize((280,280)).save("temp.jpg")
				pic = base64.b64encode(open("temp.jpg",'rb').read()).decode()
				image_tag = '<img src="data:image/jpeg;base64,{}">'.format(pic)
				iframe = folium.IFrame(image_tag, width=300, height=300)
				popup = folium.Popup(iframe, max_width=1200)

				folium.Marker([float(loc_list[loc][0]), float(loc_list[loc][1])],
								popup=popup,
								tooltip=tooltip).add_to(m)

				markerList.append([float(loc_list[loc][0]), float(loc_list[loc][1])])
			except:
				continue

		savename = "DBResult/"+datamap.date()+".html"
		m.save(savename)
		os.remove("temp.jpg")

	def calcDistance(lon1, lat1, lon2, lat2):
	    """
	    Calculate the great circle distance between two points
	    on the earth (specified in decimal degrees)
	    """
	    # convert decimal degrees to radians
	    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	    # haversine formula
	    dlon = lon2 - lon1
	    dlat = lat2 - lat1
	    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	    c = 2 * asin(sqrt(a))
	    km = 6367 * c
	    m = km * 1000
	    return m

	def date():
		now = datetime.now()
		day = "%s-%s-%s_%s:%s:%s" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
		return day
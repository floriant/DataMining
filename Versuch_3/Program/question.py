import pylast as fm

network=fm.get_lastfm_network()

dict = {}
dict['dictA'] = {}
dict['dictB'] = {}
dict['dictA']['dictAA'] = {}
dict['dictA']['dictAB'] = {}
dict['dictA']['dictAA']['key1'] = 'value1'
dict['dictA']['dictAB']['key2'] = 'value2'
dict['dictB']['dictBA'] = {}
dict['dictB']['dictBB'] = {}
dict['dictB']['dictBA']['key3'] = 'value3'
dict['dictB']['dictBB']['key4'] = 'value4'

print dict

madonna = network.get_artist("Madonna")
albums = madonna.get_top_albums()
bio = madonna.get_bio_content()
biosum = madonna.get_bio_summary()


print madonna
print albums
for album in albums:
    print album

print bio
